infoCaptain=pd.read_csv('../data/captain_schedule/processed/infoCAPTAIN.csv')
infoCaptain['cs_date']=pd.to_datetime(infoCaptain['cs_date'])
infoCaptain['ope_date']=pd.to_datetime(infoCaptain['ope_date'])
infoCaptain=infoCaptain.rename(columns={'dt_gps_max':'dt_endduty','dt_gps_min':'dt_startduty'})

infoCaptain=infoCaptain.to_json(orient = "records")

with open('../data/processed/json/infoCaptain.json', 'w') as f:
    f.write(infoCaptain)

# run once to create solr collection infoCaptain /home/hadoop/solr-9.3.0/bin/solr create -c infoCaptain
os.system('/home/hadoop/solr-9.3.0/bin/solr create -c infoCaptain')

# run once to post data into infoCaptain collection /home/hadoop/solr-9.3.0/bin/post -c infoCaptain /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoCaptain.json
os.system('/home/hadoop/solr-9.3.0/bin/post -c infoCaptain /home/hadoop/MyRapidHack2023-BackEnd/data/processed/json/infoCaptain.json')