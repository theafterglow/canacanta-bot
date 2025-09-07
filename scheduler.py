# scheduler.py
from hydrobot import filters
from config import CONFIG
from utils import time_valid
import asyncio

async def set_time(bot, message):
    args = message.text.split()
    if len(args) != 2 or not time_valid(args[1]):
        await message.reply("Lütfen zamanı HH:MM formatında girin, örnek: /settime 20:00")
        return
    CONFIG["vote_time"] = args[1]
    await message.reply(f"Oylama zamanı ayarlandı: {CONFIG['vote_time']}")

async def wait_for_vote_time(bot, vote_callback):
    """vote_callback: oylama başlatma fonksiyonu"""
    import datetime
    while True:
        if CONFIG["vote_time"]:
            now = datetime.datetime.now()
            current_time = f"{now.hour:02d}:{now.minute:02d}"
            if current_time == CONFIG["vote_time"]:
                await vote_callback(bot)
                await asyncio.sleep(60)  # 1 dakika bekle, tekrar tetiklememek için
        await asyncio.sleep(10)
