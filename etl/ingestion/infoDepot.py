import pandas as pd
import numpy as np
import os

infoDepot=pd.read_csv('../data/processed/InfoDEPOT.csv')
infoDepot=infoDepot.to_json(orient = "records")

with open('../data/processed/json/infoDepot.json', 'w') as f:
    f.write(infoDepot)

# run once to create solr collection infoDepot /home/hadoop/solr-9.3.0/bin/solr create -c infoDepot
os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoDepot')

# run once to post data into infoDepot collection /home/hadoop/solr-9.3.0/bin/post -c infoDepot /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoDepot.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoDepot /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoDepot.json')