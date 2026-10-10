# ============================================================
# RS MIRROR LEECH BOT — CONFIGURATION
# All settings are managed in this file. No .env required.
# ============================================================


# ============================================================
# REQUIRED CONFIG — BOT STARTUP
# ============================================================

BOT_TOKEN = "8963100948:AAFUSKmosVS_eochlzcJqhKrN3ga1oohq-E"
# REQUIRED
# GET: Telegram -> @BotFather -> /newbot -> Copy the bot token.

OWNER_ID = 6621572366
# REQUIRED
# GET: Telegram -> @userinfobot -> Send /start -> Copy your numeric user ID.

TELEGRAM_API = 25976192
# REQUIRED
# GET: https://my.telegram.org -> API development tools -> api_id.

TELEGRAM_HASH = "8ba23141980539b4896e5adbc4ffd2e2"
# REQUIRED
# GET: https://my.telegram.org -> API development tools -> api_hash.

DATABASE_URL = "mongodb+srv://RAHAT1132:RAHAT11a@rahat.txn4lkk.mongodb.net/?appName=Rahat"
# REQUIRED
# GET: MongoDB Atlas -> Database -> Connect -> Drivers -> Copy the connection URI.
# Replace the username, password and database details with your own values.
# IMPORTANT: Keep database credentials private.


# ============================================================
# OPTIONAL CONFIG — GENERAL
# ============================================================

DEFAULT_LANG = "en"  # OPTIONAL: Default language.
TG_PROXY = None
# OPTIONAL: Proxy settings, if needed.
# Example: {"scheme": "socks5", "hostname": "127.0.0.1", "port": 1080,
#           "username": "", "password": ""}

USER_SESSION_STRING = ""  # OPTIONAL: User session, only if a feature requires it.
CMD_SUFFIX = ""  # OPTIONAL: Custom command suffix.
AUTHORIZED_CHATS = "-1004366562744"  # OPTIONAL: Authorized chat IDs; format depends on the bot.
SUDO_USERS = "6621572366"  # OPTIONAL: Additional privileged user IDs.
STATUS_LIMIT = 10  # OPTIONAL: Maximum status entries.
DEFAULT_UPLOAD = "rc"  # REQUIRED FOR RCLONE UPLOAD; otherwise choose a supported destination.
STATUS_UPDATE_INTERVAL = 15  # OPTIONAL: Status refresh interval, in seconds.


# ============================================================
# OPTIONAL EXTERNAL UPLOAD SERVICES
# ============================================================

FILELION_API = ""  # OPTIONAL: Get from your FileLions account/API dashboard.
STREAMWISH_API = ""  # OPTIONAL: Get from your StreamWish account/API dashboard.
ALLDEBRID_API_KEY = ""  # OPTIONAL: Get from your AllDebrid account.
ALLDEBRID_NO_SEED_TIMEOUT = 180  # OPTIONAL: Torrent seed timeout.

EXCLUDED_EXTENSIONS = ""  # OPTIONAL: Extensions excluded from processing.
INC_TASK_NOTIFY = False  # OPTIONAL: Incremental task notifications.
YT_DLP_OPTIONS = ""  # OPTIONAL: Extra yt-dlp options.
USE_SERVICE_ACCOUNTS = False  # OPTIONAL: Google Drive service accounts.
NAME_SWAP = ""  # OPTIONAL: Rename/swap rules.
FFMPEG_CMDS = {}  # OPTIONAL: Custom FFmpeg commands.
UPLOAD_PATHS = {}  # OPTIONAL: Destination-specific upload paths.
WEB_ACCESS_PASSWORD = ""  # OPTIONAL: Secret for web-access password derivation.


# ============================================================
# HYPER TG DOWNLOADER
# ============================================================

HELPER_TOKENS = ""  # OPTIONAL: Helper bot tokens, if Hyper requires them.
STREAM_TOKENS = ""  # OPTIONAL: Stream tokens, if Hyper requires them.
USE_HYPER = True  # OPTIONAL: Enable Hyper downloader support.


# ============================================================
# MEGA API
# ============================================================

MEGA_EMAIL = ""  # OPTIONAL: Mega account email.
MEGA_PASSWORD = ""  # OPTIONAL: Mega account password.
DISABLE_MEGA = False  # OPTIONAL: Disable Mega support.


# ============================================================
# FEATURE DISABLE OPTIONS
# Set True to disable a feature.
# ============================================================

DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_MIRROR = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False
DISABLE_JD = False
DISABLE_NZB = False
DISABLE_SEEDR = False
DISABLE_RSS = False
DISABLE_SEARCH = False
DISABLE_STREAM = False
DISABLE_YTDLP = False
DISABLE_PLUGINS = True


# ============================================================
# PLUGINS AND MEMORY
# ============================================================

PLUGIN_INDEXES = []  # OPTIONAL: Plugin source/index configuration.
MEM_BUDGET = 0  # OPTIONAL: Memory budget, if supported.
MEM_DEEP_STATS = False  # OPTIONAL: Detailed memory statistics.


# ============================================================
# TELEGRAPH
# ============================================================

AUTHOR_NAME = "RS Mirror Leech Bot"
AUTHOR_URL = "https://rsanime03.lovable.app/"


# ============================================================
# TASK LIMITS
# Zero commonly means no explicit limit, depending on the module.
# ============================================================

DIRECT_LIMIT = 0
MEGA_LIMIT = 0
TORRENT_LIMIT = 0
GD_DL_LIMIT = 0
RC_DL_LIMIT = 0
CLONE_LIMIT = 0
JD_LIMIT = 0
NZB_LIMIT = 0
SEEDR_LIMIT = 0
YTDLP_LIMIT = 0
PLAYLIST_LIMIT = 0
LEECH_LIMIT = 0
EXTRACT_LIMIT = 0
ARCHIVE_LIMIT = 0
STORAGE_LIMIT = 0


# ============================================================
# CPU AND FFMPEG
# ============================================================

CPU_LIMIT = 20
FFMPEG_CORES = "auto"
THROTTLE_SERVICES = "auto"


# ============================================================
# IMAGE SEARCH
# ============================================================

USE_IMAGES = False
IMG_SEARCH = ""
IMG_PAGE = 1
IMG_SOURCES = ["wallpaperflare"]


# ============================================================
# INSTAGRAM VIDEO DOWNLOADER API
# ============================================================

INSTADL_API = ""  # OPTIONAL: Get from the selected API provider.


# ============================================================
# NZB SEARCH
# ============================================================

HYDRA_IP = ""  # OPTIONAL: Your Hydra service address.
HYDRA_API_KEY = ""  # OPTIONAL: Get from your Hydra service.


# ============================================================
# MEDIA SEARCH
# ============================================================

IMDB_TEMPLATE = ""  # OPTIONAL: Custom IMDb message template.


# ============================================================
# TASK TOOLS
# ============================================================

FORCE_SUB_IDS = ""  # OPTIONAL: Force-subscribe channel IDs.
MEDIA_STORE = True
DELETE_LINKS = False


# ============================================================
# LIMITERS AND LOGIN
# ============================================================

BOT_MAX_TASKS = 5
USER_MAX_TASKS = 5
USER_TIME_INTERVAL = 30
VERIFY_TIMEOUT = 30
LOGIN_PASS = "RS"  # OPTIONAL: Web login password, if the feature is enabled.


# ============================================================
# CRASH REPORTING
# ============================================================

ENABLE_TELEMETRY = False  # OPTIONAL: Disabled by default for privacy.


# ============================================================
# BOT SETTINGS
# ============================================================

BOT_PM = False
SET_COMMANDS = True
TIMEZONE = "Asia/Dhaka"


# ============================================================
# GOOGLE DRIVE
# Configure only if using Google Drive as a mirror destination.
# ============================================================

GDRIVE_ID = ""
# REQUIRED FOR GOOGLE DRIVE MIRROR
# GET: Google Drive -> Select the destination folder -> Copy folder ID from its URL.

GD_DESP = "Uploaded with RS Mirror Leech Bot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""  # OPTIONAL: Public Google Drive index URL.


# ============================================================
# YOUTUBE TOOLS
# ============================================================

YT_DESP = "Uploaded with RS Mirror Leech Bot"
YT_TAGS = ["telegram", "bot", "youtube"]
YT_CATEGORY_ID = 22
YT_PRIVACY_STATUS = "unlisted"


# ============================================================
# RCLONE
# Configure only if using Rclone as the mirror destination.
# ============================================================

RCLONE_PATH = ""
# REQUIRED FOR RCLONE UPLOAD
# GET: Run `rclone config` on the server and configure your remote.
# Set this to the remote/path expected by the bot, for example `remote:folder`.

RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
SHOW_CLOUD_LINK = True
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""


# ============================================================
# JDOWNLOADER
# ============================================================

JD_EMAIL = ""  # OPTIONAL: Your JDownloader account email.
JD_PASS = ""  # OPTIONAL: Your JDownloader account password.


# ============================================================
# SABNZBD / USENET
# ============================================================

USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]


# ============================================================
# UPSTREAM / UPDATE
# ============================================================

UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "main"


# ============================================================
# LEECH SETTINGS
# ============================================================

LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
TRANSMISSION_MODE = "both"
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""
TMDB_ACCESS_TOKEN = ""  # OPTIONAL: Get from https://www.themoviedb.org/
AUTO_THUMBNAIL = False


# ============================================================
# LOG CHANNELS AND GROUPS
# ============================================================

LEECH_LOG_CHAT = ""  # OPTIONAL: Dedicated Leech log/dump chat ID.
LEECH_DUMP_CHATS = {}
LINKS_LOG_ID = ""  # OPTIONAL: Links log chat ID.
MIRROR_LOG_ID = ""  # OPTIONAL: Mirror log chat ID.


# ============================================================
# TORRENT / ARIA2 / WEB UI
# ============================================================

TORRENT_TIMEOUT = 0
BASE_URL = ""
WEB_PINCODE = True


# ============================================================
# QUEUEING SYSTEM
# ============================================================

QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0


# ============================================================
# RSS
# ============================================================

RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0


# ============================================================
# TORRENT SEARCH
# ============================================================

SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbtSearchScripts/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]


# ============================================================
# SEEDR
# ============================================================

SEEDR_EMAIL = ""
SEEDR_PASSWORD = ""
SEEDR_DELETE_FOLDER = False


# ============================================================
# RS MIRROR LEECH BOT — PRIMARY CONFIG
# ============================================================

API_ID = TELEGRAM_API
# REQUIRED ALIAS — Same value as TELEGRAM_API.

API_HASH = TELEGRAM_HASH
# REQUIRED ALIAS — Same value as TELEGRAM_HASH.

LOG_CHANNEL = ""
# OPTIONAL: Get the numeric channel ID from your Telegram channel.
# Add the bot as an administrator if it needs to post there.

LOG_GROUP = ""
# OPTIONAL: Get the numeric group ID from Telegram or an ID bot.

AUTHORIZED_CHANNEL = ""
# OPTIONAL: Channel ID allowed to use the bot.

AUTHORIZED_GROUP = ""
# OPTIONAL: Group ID allowed to use the bot.

ADMIN_ID = OWNER_ID
# REQUIRED ALIAS — Same value as OWNER_ID.


# ============================================================
# COMPATIBILITY ALIASES
# Keep these for the original configuration loader.
# ============================================================

if API_ID:
    TELEGRAM_API = API_ID

if API_HASH:
    TELEGRAM_HASH = API_HASH

if LOG_CHANNEL:
    MIRROR_LOG_ID = LOG_CHANNEL
    LEECH_LOG_CHAT = LOG_CHANNEL

if LOG_GROUP:
    LINKS_LOG_ID = LOG_GROUP

if ADMIN_ID:
    OWNER_ID = ADMIN_ID

_auth_items = [
    str(x).strip()
    for x in (AUTHORIZED_CHANNEL, AUTHORIZED_GROUP)
    if str(x).strip()
]

if _auth_items:
    AUTHORIZED_CHATS = ",".join(
        filter(None, [AUTHORIZED_CHATS, *_auth_items])
    )


# ============================================================
# FINAL BRANDING
# ============================================================

AUTHOR_NAME = "RS Mirror Leech Bot"
AUTHOR_URL = "https://rsanime03.lovable.app/"
GD_DESP = "Uploaded with RS Mirror Leech Bot"
YT_DESP = "Uploaded with RS Mirror Leech Bot"
UPSTREAM_REPO = ""