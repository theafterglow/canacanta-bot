# register.py
from hydrobot import types
from database import data, save_data
from utils import is_youtube, is_vote_time_reached
from config import CONFIG

async def register_country(bot, message):
    if not is_vote_time_reached(CONFIG["vote_time"]):
        await message.reply(f"Ülke seçimi için zaman gelmedi! Oylama zamanı: {CONFIG['vote_time']}")
        return

    user_id = str(message.from_user.id)
    country = message.text.strip()
    data["users"].setdefault(user_id, {})["country"] = country
    save_data()
    await message.reply(f"Ülkeniz kaydedildi: {country}")

async def register_song(bot, message):
    if not is_vote_time_reached(CONFIG["vote_time"]):
        await message.reply(f"Şarkı ekleme için zaman gelmedi! Oylama zamanı: {CONFIG['vote_time']}")
        return

    user_id = str(message.from_user.id)
    song = message.text.strip()
    if not is_youtube(song):
        await message.reply("Geçersiz link! Lütfen YouTube linki girin.")
        return
    data["users"].setdefault(user_id, {})["song"] = song
    save_data()
    await message.reply("Şarkınız kaydedildi!")
