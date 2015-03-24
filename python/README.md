
This is a proof of concept written in python for remote relevance evaulation

You must set the variables in BES_CONFIG.py

Currently the results are only available on the remote server console, but eventually the idea is to use websockets to deliver them to a web app.

You can test this right now using Nitrious.IO by clicking the following button, changing the config file, pip installing the depedancies, and running:
  python workspace\remote-relevance\python\test_receive_results.py
  
[![Hack jgstew/remote-relevance on Nitrous](https://d3o0mnbgv6k92a.cloudfront.net/assets/hack-l-v1-d464cf470a5da050619f6f247a1017ec.png)](https://www.nitrous.io/hack_button?source=embed&runtime=django&repo=jgstew%2Fremote-relevance&file_to_open=python%2FBES_CONFIG.py)
