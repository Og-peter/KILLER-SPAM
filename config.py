# ©️ @SACHIN_OWNER || @V_VIP_OWNER
import logging
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Direct API Credentials
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"

CMD_HNDLR = "!"
HEROKU_APP_NAME = None
HEROKU_API_KEY = None

# Direct Bot Tokens
BOT_TOKENS = [
    "7335799800:AAEqEIH_FqVnSJB8C6Czcx6btuchVFvMuVQ",
    "7456960988:AAF2qtGunhDGWzwLRX7Izq4GON_2kS_uxPw"
]

# Direct SUDO Users & Owner ID
OWNER_ID = 6236734355
SUDO_USERS = [OWNER_ID]

# ------------- CLIENTS -------------
clients = []

for i, token in enumerate(BOT_TOKENS, start=1):
    client = TelegramClient(f'❖ | sᴀɴᴀᴛᴀɴɪ ꭙ ʙᴏᴛ | ❖ {i}', API_ID, API_HASH).start(bot_token=token)
    clients.append(client)
