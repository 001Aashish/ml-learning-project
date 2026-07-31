import sys

from dsproject.exception import CustomException
from dsproject.logger import logging

from dsproject.components.data_ingestion import DataIngestion
from dsproject.components.data_transformation import DataTransformation
from dsproject.components.model_trainer import ModelTrainer


class TrainPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("========== Training Pipeline Started ==========")

            # Step 1: Data Ingestion
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            # Step 2: Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
                train_path,
                test_path,
            )

            # Step 3: Model Training
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(
                train_arr,
                test_arr,
            )

            logging.info(f"Training completed successfully.")
            logging.info(f"Final R2 Score : {r2_score}")

            return r2_score

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    pipeline = TrainPipeline()
    score = pipeline.run_pipeline()
    print(f"Training completed successfully.")
    print(f"R2 Score: {score}")

        