import logging
from fastapi import FastAPI
from cron_job import start_scheduler, update_data
from database import bills_collection, members_collection
import asyncio
from dotenv import load_dotenv  # Add this line
from contextlib import asynccontextmanager
from bson import ObjectId # Add this line


load_dotenv() # Add this line
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting the app")
    asyncio.create_task(update_data())  # Run update_data() concurrently
    start_scheduler()
    yield
    # Shutdown
    logger.info("Shutting down...")  # Replace with any shutdown logic

app = FastAPI(lifespan=lifespan)

def convert_object_id(item):
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, ObjectId):
                item[key] = str(value)
            elif isinstance(value, (dict, list)):
                convert_object_id(value)
    elif isinstance(item, list):
        for element in item:
            convert_object_id(element)

@app.get("/bills")
async def get_bills():
    bills = await bills_collection.find().to_list(100)
    convert_object_id(bills)
    return bills

@app.get("/members")
async def get_members():
    members = await members_collection.find().to_list(100)
    convert_object_id(members)
    return members
