import pymongo
import os 
from dataclasses import dataclass
import json 

@dataclass()
class ENVIRONMENTAL_VARIABLE:
    mongo_db_url:str=os.getenv("MONGO_DB_URL")
    aws_access_key_id: str=os.getenv("AWS_ACCESS_KEY_id")
    aws_access_secret_key:str=os.getenv("AWS_SECRET_ACCESS_KEY")

env_var=ENVIRONMENTAL_VARIABLE()

mongo_client=pymongo.MongoClient(env_var.mongo_db_url)