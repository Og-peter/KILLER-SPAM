# ©️ @SACHIN_OWNER || @V_VIP_OWNER
from telethon import TelegramClient
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# API Credentials
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"

# Command Handler
CMD_HNDLR = "!"  # Yahan apna prefix dal sakte ho

# Direct Bot Tokens (Ensure at least 3 valid tokens)
BOT_TOKENS = [
    "7335799800:AAEqEIH_FqVnSJB8C6Czcx6btuchVFvMuVQ",  # X1
    "7456960988:AAF2qtGunhDGWzwLRX7Izq4GON_2kS_uxPw",  # X2
    "7633665603:AAENUnc3jrABhg8GOzCeSegW1DUlBjUPViQ",  # X3 (Yeh zaroori hai, warna error aayega)
    None, None, None, None, None, None, None  # Extra slots for future bots
]

# Owner & Sudo Users
OWNER_ID = 6236734355
SUDO_USERS = [OWNER_ID]

# Initialize Clients
clients = []
for i, token in enumerate(BOT_TOKENS):
    if token:  # Token available hai tabhi initialize karein
        client = TelegramClient(f'X{i+1}', API_ID, API_HASH).start(bot_token=token)
        clients.append(client)

# Assign variables dynamically
clients += [None] * (10 - len(clients))  # Ensure 10 elements (None if missing)
X1, X2, X3, X4, X5, X6, X7, X8, X9, X10 = clients
