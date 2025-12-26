import re
from os import getenv, environ
import logging
from Script import script 

# --- LOGGING CONFIGURATION ---
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if isinstance(value, bool):
        return value
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# --- BOT INFORMATION ---
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '22321078'))
API_HASH = environ.get('API_HASH', '9960806d290cf4170e43355fcc3687ac')
BOT_TOKEN = environ.get('BOT_TOKEN', '8200587392:AAGOoy6_fjH3BkI4jfYH6XbSJdbNyc8qfHQ')

# --- BOT SETTINGS ---
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "False"), False)
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg')).split()
PRIME_LOGO = (environ.get('PRIME_LOGO', 'https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg'))

# --- ADMINS, CHANNELS & USERS ---
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7219461396 6226520145').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003303429005').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# --- MONGODB INFORMATION ---
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://xeviw38487_db_user:UAjmxkdslpJC5LPP@cluster0.werptta.mongodb.net/?appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# --- LOG CHANNELS ---
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003474072380'))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', '0'))
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', LOG_CHANNEL))
PRIME_MEMBERS_LOGS = int(environ.get('PRIME_MEMBERS_LOGS', LOG_CHANNEL))

# --- PREMIUM ACCESS ---
lazydownloaders = [int(ld) if id_pattern.search(ld) else ld for ld in environ.get('PRIME_DOWNLOADERS', '').split()]
PRIME_USERS = (lazydownloaders) if lazydownloaders else []
LZURL_PRIME_USERS = [int(lu) if id_pattern.search(lu) else lu for lu in environ.get('LZURL_PRIME_USERS', '5965340120').split()]

QR_CODE_IMG = environ.get('QR_CODE_IMG','https://telegra.ph/file/ca18e2c794f4ea1c3135b.jpg')
UPI_ID = environ.get('UPI_ID', 'lazydeveloper@ybl')

# --- OTHERS ---
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/real_MoviesAdda3/186')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', "True"), True)
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'LazyDeveloper')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "False"), False)

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File Name:</b> {file_caption} \n <b>Size: </b>{file_size}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 Title: <a href={url}>{title}</a>\n🌟 Rating: {rating}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1003303429005')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "False"), False)

# --- LAZYRENAMER CONFIGS ---
FLOOD = int(environ.get("FLOOD", "10"))
LAZY_MODE = is_enabled(environ.get("LAZY_MODE", "False"), False)

# --- URL SHORTENER ---
URL_MODE = is_enabled(environ.get("URL_MODE","False"), False)
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'atglinks.com')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '72a7f0131e5e657e37cf7e2a9e928a616b671cf5')

# --- ONLINE STREAM AND DOWNLOAD ---
PORT = int(environ.get('PORT', 8080))
NO_PORT = is_enabled(environ.get('NO_PORT', "False"), False)
APP_NAME = environ.get('APP_NAME')
ON_HEROKU = 'DYNO' in environ

BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or not getenv('FQDN') else f"{APP_NAME}.herokuapp.com"

HAS_SSL = is_enabled(getenv('HAS_SSL', "False"), False)
if HAS_SSL:
    URL = f"https://{FQDN}/"
else:
    URL = f"http://{FQDN}:{PORT}/"

# --- AUTO DELETE SETTINGS ---
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = is_enabled(environ.get('SELF_DELETE', "True"), True)

# --- LANGUAGES & QUALITIES ---
LANGUAGES = ["hindi", "english", "korean", "tamil", "telugu"]
QUALITIES = ["360P", "480P", "720P", "1080P", "2160P"]

# --- FINAL LOG STRING ---
LOG_STR = "Bot is starting with customized configurations..."

# Credit @LazyDeveloper
