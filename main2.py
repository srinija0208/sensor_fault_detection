from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging


from  sensor.utils2 import dump_csv_file_to_mongodb_collection
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline



# def test_exception():
#     try:
#         logging.info("ki yaha p bhaiaa ek error ayegi diveision by zero wali error ")
#         a=1/0
#     except Exception as e:
#        raise SensorException(e,sys) 



# if __name__ == "__main__":
#     try:
#         pass
        

#         # file_path = r"C:\projects_endtoend\sensorfault_prediction\aps_failure_training_set1.csv"
#         # database_name = "project1"
#         # collection_name = "sensor"   
#         # dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)

#     except Exception as e:
#         logging.error(f"An error occurred in the main execution: {e}")



if __name__ == "__main__":



    # file_path=r"C:\projects_endtoend\sensorfault_prediction\aps_failure_training_set1.csv"
    # database_name="project1"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()





    

    # try:
    #     logging.info("zero division error")
    #     test_exception()
    # except Exception as e:
    #     print(e)