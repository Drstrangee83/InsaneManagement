class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 25843527
    API_HASH = "436bed5c2775d426f4eea4166bc1fc8f"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = ""  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = ""

    SUPPORT_CHAT = "ThePokedex_Support"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6100138510:AAHvVLdpKQjZFJkoB2dUxb4q5xTax7QM9gE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "QA72C7APM0OQ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6159220593
   
    QUOTE_API_URI = ""
    
    ARQ_API_KEY = "RPBYOZ-BAMEXC-LNDTEN-INSJDI-ARQ" #get it form @ARQRobot
    
    ARQ_API_URL = "https://arq.hamker.in" # dont change
  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
