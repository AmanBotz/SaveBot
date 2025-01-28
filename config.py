# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23288918"))
API_HASH = getenv("API_HASH", "fd2b1b2e0e6b2addf6e8031f15e511f2")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6400973182"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002208536233"))
FORCESUB = getenv("FORCESUB", "amanbots")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", None) # this is jkust to help if you dont want to force your bot user to login or if they not interested
