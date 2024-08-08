# ©️ @SACHIN_OWNER || @V_VIP_OWNER
from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_OP = [
    [
        Button.url("⏤͟͟͞͞ 𝐊ɪʟʟᴇʀ", "https://t.me/OFFICIAL_KILLER01"),
        Button.url("ʀᴇᴘᴏ 🕸️", "https://t.me/B_2dlj9uilNhZDg1")
    ],
    [
        Button.inline("🥀 ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 🥀", data="help_back")
    ],
    [
        Button.url("✨ ᴜᴘᴅᴀᴛᴇ", "https://t.me/B_2dlj9uilNhZDg1"),
        Button.url("sᴜᴘᴘᴏʀᴛ ❄️", "https://t.me/+cwqbZHOjMzRmZmZl")
    ],
    [
        Button.url("🌸 ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ 🌸", "https://t.me/+cwqbZHOjMzRmZmZl")
    ],
]

@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        KEX = await event.client.get_me()
        bot_name = KEX.first_name
        bot_id = KEX.id
        TEXT = f"**╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ⏤͟͟͞͞‌‌‌‌★**\n**┆**\n**┊◍ ʜᴇʏ : [{event.sender.first_name}] **\n**┆◍ ɪ ᴀᴍ : [{bot_name}](tg://user?id={bot_id}) **\n**┊**\n**┆● sᴀɴᴀᴛᴀɴɪ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `0.2`\n**┊● ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `8.2.5.1.01`\n**╰─────────────────────────**\n**──────────────────────────**\n**⦿ Oᴡɴᴇʀ - ⏤͟͟͞͞ 𝐊ɪʟʟᴇʀ [ ~ 𝗡𝗫𝗧 ~](https://t.me/+B_2dlj9uilNhZDg1) **\n**──────────────────────────**\n**    ❖ Uᴘᴅᴀᴛᴇ's ⏤͟͟͞͞‌‌‌‌ [❖ ∣ Kɪʟʟᴇʀ Mᴏᴅs ∣ ❖](https://t.me/+B_2dlj9uilNhZDg1) **\n**──────────────────────────**"
        await event.client.send_file(
                    event.chat_id,  
                    "https://telegra.ph/file/a665072ef8e822a7a14f1.mp4",
                    caption=TEXT, 
                    buttons=START_OP
                )
