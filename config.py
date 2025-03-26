import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7534434615:AAEl3tOZzi54kJekygJJKpaTrKWTUIYBjto')
    API_ID = int(os.environ.get("API_ID", '21567814'))
    API_HASH = os.environ.get("API_HASH", 'cd7dc5431d449fd795683c550d7bfb7e')
    AUTH_USER = os.environ.get('AUTH_USERS', '6126688051', '7231497471').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ᴊᴏʜɴ✰ᴡɪᴄᴋ࿐"#Here You Can Change with Your Name  or any custom name or title you prefer
