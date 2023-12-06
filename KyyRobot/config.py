# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/KyyRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
   LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

   API_ID = 15107029  # integer value, dont use ""
   API_HASH = "b7b9b7530025c02442bfcbe409abcb9e"
   TOKEN = "2129034376:AAG-J8HNi2YctuE0EAkyLMzmeTRudeB9Og8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
   OWNER_ID = 955903284  # If you dont know, run the bot and do /id in your private chat with it, also an integer
   OWNER_USERNAME = "IDnyaKosong"
   SUPPORT_CHAT = "nastysupportt"  # Your own group for support, do not add the @
   JOIN_LOGGER = (
        -1001380293847
    )  # Prints any new group the bot is added to, prints just the name and ID.
   EVENT_LOGS = (
        -1001380293847
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
   ERROR_LOGS = -1001723570304
    # RECOMMENDED
   SQLALCHEMY_DATABASE_URI = "postgresql://spkwlwnc:lXkcxvieVABU5inLk1oaLj5iiGVhxUeW@castor.db.elephantsql.com/spkwlwnc"  # needed for any database modules
   LOAD = []
   NO_LOAD = ["rss", "cleaner", "connection", "math"]
   WEBHOOK = False
   INFOPIC = True
   URL = None
   SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
   SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
   MONGO_DB_URI = "mongodb+srv://Nasty:AsampeZ12@cluster0.bsvada0.mongodb.net/?retryWrites=true&w=majority"
   MONGO_DB = "Nasty"
   MONGO_PORT = "27017"
   ARQ_API = "LVAQYQ-CKKOPZ-OMHTDS-ARNKOX-ARQ"
   ARQ_API_KEY = "LVAQYQ-CKKOPZ-OMHTDS-ARNKOX-ARQ"
   ARQ_API_URL = "https://arq.hamker.in"
   BOT_NAME = "Nasty"
   BOT_USERNAME = "Nastymusiicbot"
   BOT_ID = "2129034376"
   OPENWEATHERMAP_ID = "22322"
   REDIS_URL = "redis://Kyy:AsampeZ12_@redis-19390.c85.us-east-1-2.ec2.cloud.redislabs.com:19390/"
   DRAGONS= "955903284, 1960665051, 1368575158, 1883126074"
   DEVS_USER= "1663258664"
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
   DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
   DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
   DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
   TIGERS = get_user_list("elevated_users.json", "tigers")
   WOLVES = get_user_list("elevated_users.json", "whitelists")
   DONATION_LINK = None  # EG, paypal
   CERT_PATH = None
   PORT = 5000
   DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
   STRICT_GBAN = True
   WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
   BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
   ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
   CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
   TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
   WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
   AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
   HEROKU_API_KEY = "YES"
   REM_BG_API_KEY = "yahoo"
   LASTFM_API_KEY = "yeah"
   CF_API_KEY = "jk"
   HEROKU_APP_NAME = "siap"
   BL_CHATS = []  # List of groups that you want blacklisted.
   SPAMMERS = None
   ALLOW_CHATS = None
   MONGO_DB = "Nasty"
   TEMP_DOWNLOAD_DIRECTORY = "./"
   STRING_SESSION = "1BVtsOL8Bu6iKt5R6ZhEf8HtxPscGus00dQCVLaDt-qJZCHt98F2mC8MdjRlV6wkkoiDpUd6xqQcfkGcVYdD_Ug4CweK6I3aykqPyz_t1KXzSkgd1-2PF6BTOBJmmliAw43D_oPQaEL9jI7fam9nqK2xoSoHfVQ96kI_5N2QPD19-zMBPURP0A2Y7wGmwE4OVEYlIERSXFDTPjbbJPgO4kwAd21TlcmrLtG0P-z03S-NcJq1uq6-pfXRRphlgRmQt2pEEGkHtU62RC5ZTnoixaCOm5FHkKcT1uQP3mJnX4BXn3Kwe8i61KJk9SBPU6tlI4CqLUSiETiT336-3jyHf9d6RZixms68="


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True