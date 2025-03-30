import requests
from typing import List
from models import Bill, Member
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


CONGRESS_API_KEY="5GsoTS3BNzeRbaRZyDcE56BduJayddfbfMS9Qfia"
CONGRESS_API_URL="https://api.congress.gov/v3"

def fetch_recent_bills() -> List[Bill]:
    logger.info("Starting fetch_recent_bills()")
    headers = {}
    if CONGRESS_API_KEY:
        headers["X-API-Key"] = CONGRESS_API_KEY
    try:
        url = f"{CONGRESS_API_URL}/bill?api_key={CONGRESS_API_KEY}"
        logger.info(f"Fetching bills from: {url}")
        response = requests.get(url, headers=headers)
        logger.info(f"Response status code: {response.status_code}")
        response.raise_for_status()  # Raise an exception for bad status codes
        bills_data = response.json()["bills"]
        bills = []
        for bill_data in bills_data:
            bill = Bill(
                id=f"{bill_data['type']}{bill_data['number']}",  # Corrected: type + number
                title=bill_data["title"],
                status=bill_data["latestAction"]["actionDate"],
                introduced_date=datetime.fromisoformat(bill_data["updateDate"][:10]),  # Corrected: updateDate
                summary=bill_data["latestAction"]["text"], # Corrected: latestAction.text
            )
            bills.append(bill)
        logger.info(f"Finished fetch_recent_bills()")
        return bills
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching bills: {e}")
        return []

def fetch_members() -> List[Member]:
    logger.info("Starting fetch_members()")
    headers = {}
    if CONGRESS_API_KEY:
        headers["X-API-Key"] = CONGRESS_API_KEY
    try:
        url = f"{CONGRESS_API_URL}/member?api_key={CONGRESS_API_KEY}"
        logger.info(f"Fetching members from: {url}")
        response = requests.get(url, headers=headers)
        logger.info(f"Response status code: {response.status_code}")
        response.raise_for_status()
        members_data = response.json()["members"]
        members = []
        for member_data in members_data:
            member = Member(
                id=member_data["bioguideId"],  # Corrected: bioguideId
                name=member_data["name"],  # Corrected: name
                party=member_data["partyName"],  # Corrected: partyName
                state=member_data["state"],
                title=member_data["terms"]["item"][0]["chamber"], # Corrected: terms.item[0].chamber
                bill_sponsorship=[], # There is no bill_sponsorship in the response
            )
            members.append(member)
        logger.info(f"Finished fetch_members()")
        return members
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching members: {e}")
        return []
