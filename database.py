from motor.motor_asyncio import AsyncIOMotorClient
import os
from typing import List
from models import Bill, Member

# MongoDB URI for local or remote MongoDB instance (adjust as necessary)
MONGODB_URI="mongodb+srv://ys6668:4WgoSk7IbibK4A9U@cluster0.4c63zqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(f"MONGODB_URI from environment: {MONGODB_URI}")  # Add this line

DATABASE_NAME = "congress_api_db"

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]

# MongoDB collections for bills and members
bills_collection = db["bills"]
members_collection = db["members"]

async def save_bills(bills: List[Bill]):
    for bill in bills:
        await bills_collection.update_one(
            {"id": bill.id}, {"$set": bill.dict()}, upsert=True
        )

async def save_members(members: List[Member]):
    for member in members:
        await members_collection.update_one(
            {"id": member.id}, {"$set": member.dict()}, upsert=True
        )
