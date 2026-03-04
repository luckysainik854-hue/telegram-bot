import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot 24/7 running bro 😎🔥")

async def main():
    print("Bot started...")
    await app.start()
    await idle()

from pyrogram import idle

if __name__ == "__main__":
    asyncio.run(main())
