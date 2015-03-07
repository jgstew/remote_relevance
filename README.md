# remote-relevance
Evaluate relevance on remote systems using BigFix actions.

### Concept:
- user enters relevance query into webapp
- webapp creates a BigFix action using REST API targeting a "testing" computer group
- action uses relevance substitution to return the result to the webapp using CURL(or similar) on the endpoint

### Models?
- computers
- computergroups
- queries
- results

### frameworks
- Node.js
- Express or Loopback ?
