import os,sys
from datetime import datetime
from sensor.exception import SensorException



TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")



class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name="aps"
        self.collection_name="sensor"
        self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
        self.feature_store_dir:str =os.path.join(self.data_ingestion_dir,"feature_store")
        self.train_file_path:str=os.path.join(self.data_ingestion_dir,"data_set",TRAIN_FILE_NAME)
        self.test_file_path:str=os.path.join(self.data_ingestion_dir,"data_Set",TEST_FILE_NAME)

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise SensorException(e,sys)    