import pandas as pd
import numpy as np
import os
import json
import logging
from sensor.config import mongo_client


## dumping sensor.csv file to mongodb

def dump_csv_file_to_mongodb_collection(file_path:str,database_name:str,collection_name:str)->None:
    
    try:
        df = pd.read_csv(file_path)
        df.reset_index(drop=True,inplace=True)
        json_record = list(json.loads(df.T.to_json()).values())

        mongo_client[database_name][collection_name].insert_many(json_record)

    except Exception as e:
        print(e)