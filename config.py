# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23288918"))
API_HASH = getenv("API_HASH", "fd2b1b2e0e6b2addf6e8031f15e511f2")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6400973182").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002208536233")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002204606355"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", None)
AD_API = getenv("AD_API", None)
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
