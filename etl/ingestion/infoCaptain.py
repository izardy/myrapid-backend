import pandas as pd
import numpy as np
import os

infoCaptain=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/captain_schedule/processed/infoCAPTAIN.csv')
infoCaptain['cs_date']=pd.to_datetime(infoCaptain['cs_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoCaptain['ope_date']=pd.to_datetime(infoCaptain['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoCaptain=infoCaptain.rename(columns={'dt_gps_max':'dt_endduty','dt_gps_min':'dt_startduty'})

infoCaptain=infoCaptain.to_json(orient = "records")

with open('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoCAPTAIN.json', 'w') as f:
    f.write(infoCaptain)

# run once to create solr collection infoCaptain /home/hadoop/solr-9.3.0/bin/solr create -c infoCaptain
os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoCAPTAIN')

# run once to post data into infoCaptain collection /home/hadoop/solr-9.3.0/bin/post -c infoCaptain /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoCaptain.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoCAPTAIN /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoCAPTAIN.json')
