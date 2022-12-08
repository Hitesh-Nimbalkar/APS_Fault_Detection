import pymongo
import pandas as pd
import json
# Provide the mongoDB localhost URL to conect python to MongoDB 

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":

    # Convert CSV to Data_frame 
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {df.shape}")

    # COnvert data_frame to Jason to dump to Mongo_DB
    df.reset_index(drop=True,inplace=True)
    json_record=json.loads(df.T.to_json().values())
    print(json_records[0])

    # Insert converted jason to MOngo_DB
    client[DATABASE_NAME][COLLECTION_NAME].Insert_many(jason_record)



