import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '0')
    API_ID = int(os.environ.get("API_ID", '25129557'))
    API_HASH = os.environ.get("API_HASH", '83c9546cfdee154fd2d16759c4d0582a')
    AUTH_USER = os.environ.get('AUTH_USERS', '1923238241').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ᴊᴏʜɴ✰ᴡɪᴄᴋ࿐"#Here You Can Change with Your Name  or any custom name or title you prefer
