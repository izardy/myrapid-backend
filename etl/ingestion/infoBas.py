import pandas as pd
import numpy as np
import os

infoDepot=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoDEPOT.csv',low_memory=False)[['depot_id','depot_name']].drop_duplicates()

infoTRIP=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/trip_departure/processed/td_agg.csv',low_memory=False)
infoTRIP['ope_date']=pd.to_datetime(infoTRIP['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

infoTRIP['point_a']=infoTRIP['point_a'].str.upper()#.str.replace('\/|\.','-')
infoTRIP['point_b']=infoTRIP['point_b'].str.upper()#.str.replace('\/|\.','-')

infoBas=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoBAS.csv',low_memory=False)

infoBas['ope_date']=pd.to_datetime(infoBas['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date']=pd.to_datetime(infoBas['br_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date_entry']=pd.to_datetime(infoBas['br_date_entry']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_target_completed']=pd.to_datetime(infoBas['br_target_completed']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['rtd_date']=pd.to_datetime(infoBas['rtd_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['date_issues']=pd.to_datetime(infoBas['date_issues']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['acc_date']=pd.to_datetime(infoBas['acc_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

#infoBas=infoBas.drop(columns=['label_1','label_2','label_3'])

infoBas=pd.merge(infoBas,infoTRIP,how='left',on=['ope_date','depot_id','line_id','bus_no']).drop_duplicates()
infoBas=pd.merge(infoBas,infoDepot,how='left',on=['depot_id']).drop_duplicates()

infoBas=infoBas[['ope_date', 'depot_id', 'line_id', 'bus_no', 'point_a', 'point_b',
       'br_id', 'br_repair_status', 'br_entry_status', 'br_date',
       'br_date_entry', 'br_target_completed', 'br_ttl_days', 'label_2',
       'rtd_id', 'rtd_date', 'route_id', 'bus_model_id', 'driver_id',
       'rtd_cause', 'cause_remark', 'fc_remark', 'label_3', 'date_issues',
       'capt_id', 'bcc_acc_id', 'acc_date', 'bus_damage', 'eng_find',
       'label_1', 'label', 'depot_name']]

infoBas['label_1']=infoBas['label_1'].str.upper()
infoBas['label_2']=infoBas['label_2'].str.upper()
infoBas['label_3']=infoBas['label_3'].str.upper()
infoBas['label']=infoBas['label'].str.upper()

infoBas['point_a']=infoBas['point_a'].str.upper()
infoBas['point_b']=infoBas['point_b'].str.upper()

infoBas=infoBas.rename(columns={'point_a':'point_A','point_b':'point_B'})

infoBas=infoBas.to_json(orient = "records")

with open('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoBas.json', 'w') as f:
    f.write(infoBas)

# run once to create solr collection infoBas /home/hadoop/solr-9.3.0/bin/solr create -c infoBas
# os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoBAS')

# run once to post data into infoBas collection /home/hadoop/solr-9.3.0/bin/post -c infoDepot /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoBas.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoBAS /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoBas.json')

#/home/hadoop/MyRapidHack2023-BackEnd/
