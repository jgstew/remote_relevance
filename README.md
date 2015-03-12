# remote-relevance
Evaluate relevance on remote systems using BigFix actions.

#### Concept:

- user enters relevance query into webapp
- webapp creates a BigFix action using REST API targeting a "testing" computer group
- action uses relevance substitution to return the result to the webapp using CURL(or similar) on the endpoint

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

- Node.js
- Express or Loopback ?

#### References:

[ IBM DevWorks BigFix REST API Doc ](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Tivoli+Endpoint+Manager/page/REST+API)
http://stackoverflow.com/questions/695438/safe-characters-for-friendly-url
https://en.wikipedia.org/wiki/Base64
http://bigfix.me/relevance/details/2163