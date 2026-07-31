import os
import sys
from dsproject.exception import CustomException
from dsproject.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from dsproject.components.data_transformation import DataTransformation
from dsproject.components.data_transformation import DataTransformationConfig

from dsproject.components.model_trainer import ModelTrainerConfig
from dsproject.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebooks/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

#     modeltrainer=ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
# Note:
#
# Earlier, this file also executed the complete ML workflow:
#
#     DataIngestion
#          ↓
#     DataTransformation
#          ↓
#      ModelTrainer
#
# That orchestration has now been moved to:
#
#     src/dsproject/pipeline/train_pipeline.py
#
# The TrainPipeline class is responsible for coordinating the complete
# training workflow:
#
#     TrainPipeline
#          ↓
#     DataIngestion
#          ↓
#     DataTransformation
#          ↓
#      ModelTrainer
#          ↓
#        R² Score
#
# Since each component should have a single responsibility, data_ingestion.py
# is now responsible only for reading the dataset and creating the train/test
# splits.
# -------------
    
if __name__ == "__main__":
    # Test only the Data Ingestion component.
    # This is useful for verifying that:
    # - the dataset is read successfully,
    # - train.csv and test.csv are created,
    # - the returned file paths are correct.

    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    print(train_path)
    print(test_path)

