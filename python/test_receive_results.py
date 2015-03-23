
# python proof of concept of remote relevance using REST APIs

#prevent *.pyc creation:   http://stackoverflow.com/questions/154443/how-to-avoid-pyc-files
import sys
sys.dont_write_bytecode = True


from flask import Flask
import requests
import urllib
import json
# http://stackoverflow.com/questions/1761744/python-read-password-from-stdin
import getpass

# config file where BES_ROOT_SERVER_DNS and similar are set
from BES_CONFIG import *

BES_API_URL = "https://" + BES_ROOT_SERVER_DNS + ":" + BES_ROOT_SERVER_PORT + "/api/"
BES_PASSWORD = getpass.getpass()


# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Computer%20Group
# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Relevance
# computergroup/{site type}/{site name}/{id}/computers
# http://docs.python-requests.org/en/latest/user/advanced/
# http://www.saltycrane.com/blog/2008/10/how-escape-percent-encode-url-python/
def get_computergroup_resource_url(bes_computer_group_id):
    relevance = 'concatenations "/" of ( ( if operator site flag of it then "operator" else if custom site flag of it then "custom" else if master site flag of it then "actionsite" else "external" ) of site of it; name of site of it; (it as string) of id of it) of bes computer groups whose(id of it = '+ bes_computer_group_id +')'
    r = requests.get(BES_API_URL + 'query?relevance=' + urllib.quote_plus(relevance), auth=(BES_USER_NAME, BES_PASSWORD), verify=False)
    print r.text
    return "Work in Progress: " + BES_API_URL + 'working_on_this'

def get_computerids_from_computergroup(bes_computer_group_id):
    return "Work in Progress: " + bes_computer_group_id


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
    return "<b>result:</b> " + bes_result + " <br/><b>base64decode:</b> " + result


# http://isbullsh.it/2012/06/Rest-api-in-python/
# https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/RESTAPI%20Action
# http://www-01.ibm.com/support/knowledgecenter/SS63NW_9.1.0/com.ibm.tem.doc_9.1/Platform/Config/c_actions.html
# http://bigfix.me/relevance/details/3000069
@app.route('/remote/query/<path:bes_query>')
def rest_bes_query_submit(bes_query):
    print BES_API_URL
    return bes_query + " "


if __name__ == '__main__':
    print get_computergroup_resource_url(BES_COMPUTER_GROUP)
    #app.run(host='0.0.0.0', port=8080)
    #print "doing nothing, just testing  " + BES_API_URL
else:
    app.run(host='0.0.0.0', port=80)
