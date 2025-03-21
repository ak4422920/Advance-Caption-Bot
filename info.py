from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7251898668"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "29171167"))
API_HASH = str(getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002442422204") 
MONGO_DB = str(getenv("MONGO_DB", "=mongodb+srv://akfile:akfile@cluster0.coguvzb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
