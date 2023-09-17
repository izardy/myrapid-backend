import pandas as pd
import numpy as np
import os

infoDepot=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoDEPOT.csv')
infoDepot=infoDepot.to_json(orient = "records")

with open('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoDEPOT.json', 'w') as f:
    f.write(infoDepot)

# run once to create solr collection infoDepot /home/hadoop/solr-9.3.0/bin/solr create -c infoDEPOT
# os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoDEPOT')

# run once to post data into infoDepot collection /home/hadoop/solr-9.3.0/bin/post -c infoDEPOT /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoDEPOT.json
# os.system('/home/hadoop/solr-9.3.0/bin/post -c infoDEPOT /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoDEPOT.json')
