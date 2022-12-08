import pandas as pd
import os 
import pandas as pd
from sensor.config import mongo_client 
from sensor.logger import logging
from sensor.exception import SensorException

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame():
    """ 

    Parameters : Database_name , Collection_Name

    Returns DataFrame 
    
    
    """

    try:
        df=pd.Dataframe(mongo_client[database_name][collection_name].find())
        logging.info(f"Found columns :{df.columns}")

        if "_id" in df.columns:
            logging.info(f"Dropping column : _id")
            df.df.drop("_id",axis=1)
        
        logging.info(f"Row and Columns in df : {df.shape}")
    except Exception as e:
        raise SensorException(e, sys)


