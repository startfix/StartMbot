import asyncio
import sys
import logging as log
from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from KyyRobot import MONGO_DB_URI
from KyyRobot.confing import get_int_key, get_str_key




MONGO_DB = "Nasty"


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
db = motor[MONGO_DB]
db = client["Nasty"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
