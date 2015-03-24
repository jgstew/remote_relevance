
# python proof of concept of remote relevance using REST APIs

#prevent *.pyc creation:   http://stackoverflow.com/questions/154443/how-to-avoid-pyc-files
import sys
sys.dont_write_bytecode = True


from flask import Flask
import os
import requests

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

import urllib
import json
import lxml
import lxml.etree
import xml.dom.minidom
import StringIO
#import socket

# ntpath used to split URL
import ntpath
# http://stackoverflow.com/questions/1761744/python-read-password-from-stdin
import getpass

# https://github.com/CLCMacTeam/besapi
# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
#os.system('pip install -U -e git+https://github.com/CLCMacTeam/besapi.git#egg=besapi')
#import besapi

# config file where BES_ROOT_SERVER_DNS and similar are set
from BES_CONFIG import *

BES_API_URL = "https://" + BES_ROOT_SERVER_DNS + ":" + BES_ROOT_SERVER_PORT + "/api/"
BES_PASSWORD = getpass.getpass()
bes_computer_target_list = list()

# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Computer%20Group
# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Relevance
# computergroup/{site type}/{site name}/{id}/computers
# http://docs.python-requests.org/en/latest/user/advanced/
# http://www.saltycrane.com/blog/2008/10/how-escape-percent-encode-url-python/
def get_session_relevance(relevance):
    result = requests.get(BES_API_URL + 'query?relevance=' + urllib.quote_plus(relevance), auth=(BES_USER_NAME, BES_PASSWORD), verify=False)
    return ';'.join( get_xpath_from_xml( result.text, '/BESAPI/Query/Result/Answer/text()' ) )

def get_xpath_from_xml(xmlString, xpath):
    # http://lxml.de/xpathxslt.html
    
    # the following turns the string into a IO file type object, which lxml.etree.parse requires
    ioResult = StringIO.StringIO(xmlString)
    # https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
    # the following line skips the XML decleration at the beginning of the result which trips up lxml.etree.parse
    ioResult.next()
    # http://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
    return ( lxml.etree.parse( ioResult ) ).xpath( xpath )

def get_computergroup_resource_url(bes_computer_group_id):
    relevance = 'concatenations "/" of ( ( if operator site flag of it then "operator" else if custom site flag of it then "custom" else if master site flag of it then "actionsite" else "external" ) of site of it; name of site of it; (it as string) of id of it) of bes computer groups whose(id of it = '+ bes_computer_group_id +')'
    result = get_session_relevance(relevance)
    return BES_API_URL + 'computergroup/' + result

# http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
def get_computerids_from_computergroup(bes_computer_group_id):
    global bes_computer_target_list
    # http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
    # http://stackoverflow.com/questions/3289601/null-object-in-python
    if (bes_computer_target_list is None) or ( 0 == len(bes_computer_target_list) ):
        result = requests.get( get_computergroup_resource_url(bes_computer_group_id) + "/computers" , auth=(BES_USER_NAME, BES_PASSWORD), verify=False)
        # http://stackoverflow.com/questions/4835891/how-to-extract-attribute-s-value-through-xpath
        computer_url_list = get_xpath_from_xml( result.text, '/BESAPI/Computer/@Resource' )
        computer_list = list()
        for strURL in computer_url_list:
            head, tail = ntpath.split(strURL)
            computer_list.append(tail)
    
        bes_computer_target_list = computer_list
    return bes_computer_target_list

# http://stackoverflow.com/questions/1591579/how-to-update-modify-a-xml-file-in-python
# http://stackoverflow.com/questions/14568605/modify-xml-values-file-using-python
# http://stackoverflow.com/questions/2502758/update-element-values-using-xml-dom-minidom
# https://wiki.python.org/moin/MiniDom
def get_action_xml_query(relevance_query):
    #action_xml_file = open('../Remote_Relevance_Action_TEMPLATE.bes.xml')
    xml_dom_action = xml.dom.minidom.parse('../Remote_Relevance_Action_TEMPLATE.bes.xml')
    
    # https://wiki.python.org/moin/MiniDom
    # set the server parameter for the action
    xml_dom_action.getElementsByTagName('Parameter')[0].childNodes[0].nodeValue = REMOTE_RELEVANCE_SERVER + '/remote/results'
    
    # set the query   http://www.tutorialspoint.com/python/string_replace.htm
    xml_dom_action.getElementsByTagName('ActionScript')[0].childNodes[0].nodeValue = xml_dom_action.getElementsByTagName('ActionScript')[0].childNodes[0].nodeValue.replace('REPLACE_WITH_DESIRED_REMOTE_RELEVANCE_QUERY', relevance_query)
    
    # append computer_ids of target group to action xml
    append_computer_ids_to_xml(xml_dom_action)
    
    return xml_dom_action.toxml()

def append_computer_ids_to_xml(xml_dom_action):
    target_elem = xml_dom_action.getElementsByTagName('Target')[0]
    
    # https://wiki.python.org/moin/MiniDom
    for computer_id in get_computerids_from_computergroup(BES_COMPUTER_GROUP):
        computer_id_elem = xml_dom_action.createElement("ComputerID")
        # http://stackoverflow.com/questions/961632/converting-integer-to-string-in-python
        computer_id_elem.appendChild( xml_dom_action.createTextNode( str(computer_id) ) )
        target_elem.appendChild( computer_id_elem )
    return " appended computer ids to target xml element "

def submit_action_xml_rest(relevance_query):
    action_xml = get_action_xml_query(relevance_query)
    # http://docs.python-requests.org/en/latest/user/advanced/
    result = requests.post( BES_API_URL + "actions" , data=action_xml, auth=(BES_USER_NAME, BES_PASSWORD), verify=False)
    return result.text

# define Flask app
app = Flask(__name__)

# http://stackoverflow.com/questions/19995/is-there-some-way-to-push-data-from-web-server-to-browser
# https://flask-socketio.readthedocs.org/en/latest/
# http://software.bigfix.com/download/bes/misc/BESImport-ExportReference71_080906.pdf


# https://en.wikipedia.org/wiki/Base64
# http://stackoverflow.com/questions/3470546/python-base64-data-decode
#  concatenations "~" of (base64 encode it) of unique values of (it as string) of (names of regapps)
@app.route('/remote/results/<path:bes_result>')
def rest_bes_query_result(bes_result):
    result = ""
    for string in bes_result.split("~"):
        result = result + "<br/>" + string.decode('base64')
    print result
    #return "thanks!"
    return "<b>result:</b> " + result


# http://isbullsh.it/2012/06/Rest-api-in-python/
# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Action
# http://www-01.ibm.com/support/knowledgecenter/SS63NW_9.1.0/com.ibm.tem.doc_9.1/Platform/Config/c_actions.html
# http://bigfix.me/relevance/details/3000069
# http://stackoverflow.com/questions/21498694/flask-get-current-route
@app.route('/remote/query/<path:bes_query>')
def rest_bes_query_submit(bes_query):
    print bes_query + ": " + ( bes_query.decode('base64') )
    result = submit_action_xml_rest( bes_query.decode('base64') )
    return bes_query + " :::   " + ( bes_query.decode('base64') ) + "<br/><br/>" + result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
else:
    app.run(host='0.0.0.0', port=80)
