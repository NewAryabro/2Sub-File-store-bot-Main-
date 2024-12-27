#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6401414916:AAHx2_MGbexWEMecwIXXBzz42t2dHXKmTX4")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7515868"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002091553156"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Arya_Bro")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6081617163"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "aryabro")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", " -1001798300759"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001713521586"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/97bdc7009062e5d9ef867-2f4e47d5efdcf6038b.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/0338e5f9959b111abc01b.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Telugu_Movies_999\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Telugu_Movies_999>Telugu Movies 999 💓</a></b>"
ABOUT_TXT = "<b>💓 Owner (Arya) : <a href=https://t.me/Arya_Bro>Arya Bro❤‍🔥</a>\n🫡 ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Telugu_movies_999>Telugu Movies 999</a>\n🥵 L€@k$: <a href=https://t.me/+4QSB2tPk-ME2NDdl>clg girl and luvrs 😛</a>\n 🔞 ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+aph6xGmeXgU2NzFl>Adult Movies</a>\n🫰 ғɪʟᴛᴇʀ ʙᴏᴛ : <a href=https://Aryas_Movies_Finder_bot>ғɪʟᴛᴇʀ ʙᴏᴛ 🫶</a></b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "7179779107 2085067057 2066626554 1676717784").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {first}\n\n<b>You are not in our channels given below so you don't get the movie file..\n\n If you want the movie file, click on the '🍿ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs 🍿' button below and join our Two channels, then click on the '🔄 Try Again' button below...\n\nThen you will get the movie files...</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "sorry ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ owner!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
