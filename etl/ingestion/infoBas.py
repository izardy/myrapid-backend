import pandas as pd
import numpy as np
import os

infoTRIP=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/trip_departure/processed/td_agg.csv')
infoTRIP['ope_date']=pd.to_datetime(infoTRIP['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

infoBas=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoBAS.csv')

infoBas['ope_date']=pd.to_datetime(infoBas['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date']=pd.to_datetime(infoBas['br_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date_entry']=pd.to_datetime(infoBas['br_date_entry']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_target_completed']=pd.to_datetime(infoBas['br_target_completed']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['rtd_date']=pd.to_datetime(infoBas['rtd_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['date_issues']=pd.to_datetime(infoBas['date_issues']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['acc_date']=pd.to_datetime(infoBas['acc_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

infoBas=infoBas.drop(columns=['label_1','label_2','label_3'])

infoBas=pd.merge(infoTRIP,infoBas,how='left',on=['ope_date','depot_id','line_id','bus_no']).drop_duplicates()

infoBas=infoBas.to_json(orient = "records")

with open('../data/processed/json/infoBas.json', 'w') as f:
    f.write(infoBas)

# run once to create solr collection infoBas /home/hadoop/solr-9.3.0/bin/solr create -c infoBas
#os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoBAS')

# run once to post data into infoBas collection /home/hadoop/solr-9.3.0/bin/post -c infoDepot /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoBas.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoDepot /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoBAS.json')