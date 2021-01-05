import json
import logging
import multiprocessing
import time
from pathlib import Path
from datetime import datetime

import requests
from telethon import TelegramClient, events

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = Path('credentials.txt')

with path.open() as f: 
    apiid = next(f)
    apihash = next(f)
    token = next(f)

api_id = ''.join(apiid).rstrip()
api_hash = ''.join(apihash).rstrip()
token_real = ''.join(token)

client = TelegramClient(None, api_id, api_hash).start(bot_token=token_real)


@client.on(events.NewMessage(pattern=r'(?i)\/help'))
async def help(event):
    await client.send_message(event.chat_id, "**Help menu**\n\n/help - Open this menu.\n/get_btc_price - Get the current BTC price.\n/set_btc_alert <value> - Get notified when BTC hits the value.")


@client.on(events.NewMessage(pattern=r'(?i)\/set_btc_alert'))
async def set_btc_alert (event):
    alert = str(event.text[14:])
    
    now = datetime.now()
    triggertime = now.strftime("%d/%m/%Y %H:%M:%S")

    if alert == "":
        await client.send_message(event.chat_id, f'**Error**\n\n Please enter a value to change the BTC alert!')
    else:
        await client.send_message(event.chat_id, f'**Alert settings changed**\n\nYour BTC alert has been set up on `{triggertime}`.The new price alert is going to be triggered at a price of `{alert}`.')
    p = multiprocessing.Process(target=start_check)
    p.start()

async def check_if_triggered(triggertime, alert, event):
    while True :
        response = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/spot")
        data = response.json()
        price = data["data"]["amount"]

        if(price == alert):
            await client.send_message(event.chat_id, f'**Alert triggered**\n\nYour Bitcoin alert has been triggered on ```{triggertime}```.\n\nCurrent price: ```{price}```\n\nLive chart: https://de.tradingview.com/symbols/BTCEUR/')

async def start_check():
    p = multiprocessing.Process(target=check_if_triggered)
    p.start()

@client.on(events.NewMessage(pattern=r'(?i)\/Start'))
async def main(event):
    await client.send_message("@lxnnard", "Bot got started.")
    await client.send_message(event.chat_id, "**Welcome **\n\nThis Bot was made by @lxnnard to improve the daily trading. You can view all commadns with /help. If you have ideas to improve the bot or found a bot, feel free to contact me here: t.me/lxnnard.")

@client.on(events.NewMessage(pattern=r'(?i)\/get_btc_price'))
async def get_btc_price(event):
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/spot")
    data = response.json()
    #price_before = data["data"]["amount"]
    price_after = data["data"]["amount"]

    await client.send_message(event.chat_id, f'**Bitcoin Price**\n\n**Currency**: Euro\n**Price/BTC**: {price_after}\n\nLive chart: https://de.tradingview.com/symbols/BTCEUR/')


# Run telethon

with client:
    client.run_until_disconnected()
