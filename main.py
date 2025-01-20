from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging


# from  sensor.utils2 import dump_csv_file_to_mongodb_collection
# from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import read_yaml_file
from sensor.utils.main_utils import load_object
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.constant.training_pipeline import SAVED_MODEL_DIR

from fastapi import FastAPI
# from uvicorn import app as app_run
import uvicorn
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from sensor.constant.application import APP_HOST, APP_PORT
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Response



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## connection
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

## training
@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()

        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    
    except Exception as e:
        return Response(f"Error Occurred! {e}")


## prediction
@app.get("/predict")
async def predict_route():
    try:
        #get data from user csv file
        #conver csv file to dataframe

        df=None
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)
        
        #decide how to return file to user.
        
    except Exception as e:
        raise Response(f"Error Occured! {e}")


def main():
    try:

        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()

    except Exception as e:
        print(e)
        logging.exception(e)




if __name__ == "__main__":



    # file_path=r"C:\projects_endtoend\sensorfault_prediction\aps_failure_training_set1.csv"
    # database_name="project1"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    # app_run(app,host=APP_HOST,port=APP_PORT)
    
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)



    





    

    # try:
    #     logging.info("zero division error")
    #     test_exception()
    # except Exception as e:
    #     print(e)