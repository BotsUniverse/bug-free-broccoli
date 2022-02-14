from pyrogram import Client, filters
from pyrogram.types import Message
import os
import time
import json
import asyncio
import requests
import datetime
import _thread
import logging
# logging.base

with open('main.json') as f:
    data = json.load(f)


env = lambda x=None, y=None: data.get(x, y)
mins = lambda x: x * 60
hours = lambda x: x * 60 * 60


client = Client(
    "bot_checker_bot",
    api_id = env('api_id'),
    api_hash = env('api_hash'),
    phone_number = env('phone_number')
)

started = False
statuses = len(env("bots"))
newMessageText = "Working Status\n"
usernames = []

async def check_status(_from="thread"):
    global statuses
    global newMessageText
    global client
    bot = client
    print(_from)
    username = usernames.pop()
    print(username)
    if username.startswith('@'):
        username = username[1:]
        myMessage = await bot.send_message(username, "/start")
        print("start", username)
        await asyncio.sleep(20)
        print("stop", username)
        lastMessage = (await bot.get_history(username, 1))
        res = (myMessage.message_id != lastMessage[0].message_id)
        username = '@' + username
    else:
        link = requests.get(username, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "cookies": ""
        }, timeout=30)

        res = link.status_code in [200]

    if res:
        newMessageText += f"💛 {username} **WORKING**\n"
        print(f"💛 {username} **WORKING**\n")
    else:
        newMessageText += f"💔 {username} **NOT WORKING**\n"
        print(f"💔 {username} **NOT WORKING**\n")
        

    statuses -= 1

        

    


@client.on_message(filters.private)
async def on_start(bot:Client, message:Message):
    global statuses
    global started
    global newMessageText

    if started:
        return False

    started = True    
    while True:
        await message.reply("Check Started")
        if env("userId"):
            await bot.send_message(env("userId"), "Check Started")
        for username in data['bots']:
            usernames.append(username)
        
        await asyncio.gather(
            *[check_status() for i in range(statuses)],
        )

            
        while statuses != 0: # wait till all the bots are checked
            print(statuses)
            time.sleep(3)
            pass

        newMessageText += f"\n`Last Checked At {str(datetime.datetime.utcnow())}`\n"
        newMessageText += f"Will check after {env('sleep_time', hours(4))} seconds"

        if env("channelId") and env("editMessageId"):
            await bot.edit_message_text(env("channelId"), env("editMessageId"), newMessageText)
        

        await message.reply(newMessageText)
        if env("userId"):
            await bot.send_message(env("userId"), newMessageText)
        time.sleep(hours(4))


if __name__ == "__main__":
    client.run()
