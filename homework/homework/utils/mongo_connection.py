from pymongo import MongoClient
import configparser

from ..settings import BASE_DIR

# connect to cluster on AtlasDB
def connect_mongo() -> MongoClient:
    """
    This function will create and return a MongoDB client.
    """
    file_config = BASE_DIR / "secrets" / "mongo_config.ini"
    config = configparser.ConfigParser()
    config.read(file_config)
    
    mongo_user = config.get('DB', 'USER')
    mongodb_pass = config.get('DB', 'PASS')
    db_name = config.get('DB', 'DB_NAME')
    domain = config.get('DB', 'DOMAIN')
    uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"

    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        return client.task1
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
