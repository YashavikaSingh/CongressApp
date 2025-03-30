from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from database import save_bills, save_members
from congress_api import fetch_recent_bills, fetch_members
import asyncio

scheduler = AsyncIOScheduler()

async def update_data():
    bills = fetch_recent_bills()
    members = fetch_members()
    await save_bills(bills)
    await save_members(members)

def start_scheduler():
    # Schedule the update function to run every day at midnight
    scheduler.add_job(update_data, CronTrigger(hour=0, minute=0))
    # Start the scheduler
    scheduler.start()
