
*NOTE:* See a similar project here:  
- https://relevance.io/
- https://developer.bigfix.com/
- https://github.com/bigfix/developer.bigfix.com/tree/master/site/api/relevance-evaluate


*NOTE:* Right now the proof of concept in the python folder is working
TODO: write a web app that uses websockets to push the responses to a browser page.

# remote-relevance
Evaluate relevance on remote systems using BigFix actions.

Action expiration: PT15M (15 min in the future)

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
- https://www.meteor.com/
- https://www.meteor.com/ddp
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

https://github.com/CLCMacTeam/besapi

https://www.npmjs.com/package/hljs-bigfix-relevance

#### Related:

https://forum.bigfix.com/t/request-for-remote-fixlet-debugger/11651

https://groups.google.com/forum/#!topic/iem-remote-qna/7F16oPdWnh8

https://www.ibm.com/developerworks/community/forums/html/topic?id=77777777-0000-0000-0000-000014766146

https://www.ibm.com/developerworks/community/forums/html/topic?id=eec5097b-4636-4281-b444-8eb023814dfb#578f271e-b26a-4d5b-a687-f7e638768670

http://bigfix.me/blog/post/2013/12/9/iem-remote-qna
