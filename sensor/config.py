from dataclasses import dataclass
import pymongo
import os


@dataclass


class EnvironmentVariable:
    mongodb_url : str = os.getenv("MONGO_DB_URL")  ## reads from .env file



env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongodb_url)