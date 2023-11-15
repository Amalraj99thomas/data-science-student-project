import os
import sys
from src.studperform.exception.exception import CustomException
from src.studperform.logging.logger import logger

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.studperform.components.data_transformation import DataTransformation
from src.studperform.components.data_transformation import DataTransformationConfig

from src.studperform.components.model_trainer import ModelTrainerConfig
from src.studperform.components.model_trainer import ModelTrainer

# Decorator 
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")  # Path as a string
    test_data_path: str=os.path.join('artifacts',"test.csv")    # Path constructed with 
    raw_data_path: str=os.path.join('artifacts',"data.csv")     # correct separator

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info("Entered into the data ingestion method or component")
        try:
            #Can add MongoDb or mySQL
            df=pd.read_csv('src/studperform/data/student-performance.csv')
            logger.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logger.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info("Ingestion of data completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))