import os

class Config(object):
    # 🔐 Bot Token (Telegram BotFather से लिया हुआ)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047785902:AAE59KTfmhRvF8sUSYIzl9wcGnm4FLXiWDk")

    # 📲 Telegram API credentials (my.telegram.org से)
    API_ID = int(os.environ.get("API_ID", 26741932))
    API_HASH = os.environ.get("API_HASH", "d9037cbe01f292eb440468c39c3dc41d")

    # 👑 Admin IDs (bot पर full access वाले user IDs)
    ADMIN_ID = [7047543426]   # अपनी Telegram user ID डालो

    # 🗄️ MongoDB Database Config
    DB_URL = os.environ.get(
        "DB_URL",
        "mongodb+srv://navedmohammad2516:zu02cmOW6medghcJ@cluster0.cq1x5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    DB_NAME = os.environ.get("DB_NAME", "botdb")   # ✅ default "botdb"

    # 📢 Log Channel / Group ID (Bot को admin बनाना ज़रूरी)
    TXT_LOG = int(os.environ.get("TXT_LOG", -1002322908140))

    # 🌍 API Host
    HOST = os.environ.get("HOST", "https://www.masterapi.tech")
