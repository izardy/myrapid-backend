import pandas as pd
import numpy as np
import os

infoDepot=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoDEPOT.csv',low_memory=False)[['depot_id','depot_name']].drop_duplicates()

infoTRIP=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/trip_departure/processed/td_agg.csv',low_memory=False)
infoTRIP['ope_date']=pd.to_datetime(infoTRIP['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

infoTRIP['point_a']=infoTRIP['point_a'].str.upper().str.replace('\/|\.','-')
infoTRIP['point_b']=infoTRIP['point_b'].str.upper().str.replace('\/|\.','-')

infoBas=pd.read_csv('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/InfoBAS.csv',low_memory=False)

infoBas['ope_date']=pd.to_datetime(infoBas['ope_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date']=pd.to_datetime(infoBas['br_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_date_entry']=pd.to_datetime(infoBas['br_date_entry']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['br_target_completed']=pd.to_datetime(infoBas['br_target_completed']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['rtd_date']=pd.to_datetime(infoBas['rtd_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['date_issues']=pd.to_datetime(infoBas['date_issues']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')
infoBas['acc_date']=pd.to_datetime(infoBas['acc_date']+ ' 00:00:00').dt.strftime('%Y-%m-%d %H:%M:%S')

#infoBas=infoBas.drop(columns=['label_1','label_2','label_3'])

infoTRIP=pd.merge(infoTRIP,infoBas,how='left',on=['ope_date','depot_id','line_id','bus_no']).drop_duplicates()
infoTRIP=pd.merge(infoTRIP,infoDepot,how='left',on=['depot_id']).drop_duplicates()

infoTRIP=infoTRIP[['ope_date', 'depot_id', 'line_id', 'bus_no', 'point_a', 'point_b',
       'ttl_td_id', 'ttl_captain_id', 'ttl_point_a', 'ttl_point_b',
       'max_diff_minutes_from_point_a', 'max_diff_minutes_idle_mode',
       'max_diff_minutes_to_point_a', 'min_diff_minutes_from_point_a',
       'min_diff_minutes_idle_mode', 'min_diff_minutes_to_point_a',
       'avg_diff_minutes_from_point_a', 'avg_diff_minutes_idle_mode',
       'avg_diff_minutes_to_point_a', 'med_diff_minutes_from_point_a',
       'med_diff_minutes_idle_mode', 'med_diff_minutes_to_point_a',
       'max_speed', 'min_speed', 'avg_speed', 'med_speed', 'ttl_td_completed',
       'br_id', 'br_repair_status', 'br_entry_status', 'br_date',
       'br_date_entry', 'br_target_completed', 'br_ttl_days', 'rtd_id',
       'rtd_date', 'route_id', 'bus_model_id', 'driver_id', 'rtd_cause',
       'cause_remark', 'fc_remark', 'date_issues', 'capt_id', 'bcc_acc_id',
       'acc_date', 'bus_damage', 'eng_find', 'label']]

infoTRIP=infoTRIP.rename(columns={'point_a':'point_A','point_b':'point_B','ttl_point_a':'ttl_point_A','ttl_point_b':'ttl_point_B'})

infoTRIP=infoTRIP.to_json(orient = "records")

with open('/home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoTrip.json', 'w') as f:
    f.write(infoTRIP)

# run once to create solr collection infoBas /home/hadoop/solr-9.3.0/bin/solr create -c infoTRIP
# os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoTRIP')

# run once to post data into infoTRIP collection /home/hadoop/solr-9.3.0/bin/post -c infoTRIP /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoTrip.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoTRIP /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoTrip.json')

#/home/hadoop/MyRapidHack2023-BackEnd/

