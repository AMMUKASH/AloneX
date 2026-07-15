# ALONE-CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "38138069"))
        self.API_HASH = getenv("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8997247669:AAEhcPwhbtRwR3SxvVKsZU3bSnnS3RPO5xg")
        self.MONGO_URL = getenv("MONGO_URL", " mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003947649552"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8724182918"))
        
        self.SESSION1 = getenv("SESSION", "AQJF8NUAGQeFi5yiBZDNr6Hj8ldBLHyZNxe6aCY4iznu5GCaSvhIJKYnYv219DQY52VtZ0q8pjTOk1VsrqkA8ZZXkJZGlxazx9Ekn8dS9AgHQQhKkhxxvGzwr6LlZhSB4LX31wKM-uXfQjL3Hh7NwlocBhxHq2dTWeC8ZCpw60Q_f0ppnRyWoY2jClVE3C-xa6yhxMh84mLP9YwAm99UWCNi-RPAFF1q1J8PjvV74e0y69k8OO2ucyfVgMu3SHWKinSS7a5m2zvbCrjglZHZsMVQJwy0Q6Ywpn1HdgA7WsAdJBTXcdJoccgN80bPjlbPVwpvQqhZnBD0uiSbPCbis8pesLJcDAAAAAH_hA2LAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NovaBot_Support")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NovaBot_Support")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
