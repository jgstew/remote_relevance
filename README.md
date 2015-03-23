NOTE: This does not actually work yet. Still in initial development.

# remote-relevance
Evaluate relevance on remote systems using BigFix actions.

#### Concept:

- user enters relevance query into webapp
- webapp creates a BigFix action using REST API targeting a "testing" computer group
- action uses relevance substitution to return the result to the webapp using CURL(or similar) on the endpoint
- target computers specifically (computer_ids for client mailboxing) based upon group membership. (dynamically get the list)

##### Inputs:

##### Relevance Substitution on Client:

    concatenations "~" of (base64 encode it) of unique values of (it as string) of ( THE_RELEVANCE_QUERY_GOES_HERE )
    
##### Example:

    concatenations "~" of (base64 encode it) of unique values of (it as string) of ( names of regapps )

#### Models?

- computers
  - /api/computer/{computer id}
- computergroups
  - /api/computergroup/{site type}/{site name}/{id}/computers

- computergroups
  - queries
    - computers
      - results

#### frameworks

Not sure yet: 
- Node.js
- WebSockets?
- Express or Loopback?

#### References:

[ IBM DevWorks BigFix REST API Doc ](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli+Endpoint+Manager/page/REST+API)

http://stackoverflow.com/questions/695438/safe-characters-for-friendly-url

https://en.wikipedia.org/wiki/Base64

http://bigfix.me/relevance/details/2163

http://software.bigfix.com/download/bes/misc/BESImport-ExportReference71_080906.pdf

http://www-01.ibm.com/support/knowledgecenter/SS63NW_9.1.0/com.ibm.tem.doc_9.1/Platform/Config/c_actions.html

http://bigfix.me/relevance/details/3000069

https://forum.bigfix.com/t/what-does-isurgent-do-to-an-action/12836

[BES XSD - XML Schema for BES content](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/BES.xsd)

[BESAPI XSD - XML Schema for BESAPI results](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli%20Endpoint%20Manager/page/BESAPI.xsd)

