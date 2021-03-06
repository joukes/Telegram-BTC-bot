# Telegram BTC bot

A simple Telegram bot to track, buy and alert the BTC prices easily. You can run it on any masine. Easy to set up commads and more! It was made by me using <a href="https://www.python.org">Python</a>, <a href="https://www.telethon.dev"> Telethon</a> and a lot of love.

⚠️ The bot is not totally accurate if any values change or coinbase has a error. Please do not change the code, otherwise you are able to let your Bot/Telegram Account and the Coinbase API crash! ⚠️

## Commands

`/help`- Get the help menu displayed with all commands.

`/get_btc_price`- See the latest BTC Price in Euro.

`/set_btc_alert`- Set a alert to get notified if BTC hits a defined value.

`/get_btc_Wallet`- See your BTC-Wallet Adress (For setup see <a href="more setup">).

## Installation

### 1. Clone the GitHub repository
```sh
git clone https://github.com/joukes/Telegram-BTC-bot.git
```

### 2. Install all needed requirements

```sh
pip install -r requirements.txt
```

## Create a Telegram Bot using <a href="https://www.t.me/BotFather">BotFather</a> on Telegram and get other credentials

### 1. Create the bot and it's token using the <a href="https://www.t.me/BotFather"> @BotFather</a> telegram account.

- Open a new chat with <a href="https://www.t.me/BotFather">BotFather</a> and click "start".
- Send the command: `/newbot` and follow all instructions from BotFather.

#### If you have any questions or the Bot creation fails, please watch the Video Tutorial.

⚠️ After the setup the bot will give you a token. Store is secure, if anyone else has acess to it the person can delete your bot! ⚠️

### 2. Get your API_ID and API_HASH from Telegram

- Open the <a href="https://www.my.telegram.org/"> Telegram Developer dashboard</a> and enter your phone number.
- After the official telegram account sent a verification Code to your Account verify the web login.
- Create a new "App" with random credentials and store the API_ID and API_HASH to the <a href="https://github.com/joukes/Telegram-BTC-bot/blob/main/credentials.txt"> credentials file</a> (Replace them with your values!).

#### If you have any questions or the app creation fails, please watch the Video Tutorial.

⚠️ Please store both values secure. If a other person gets the credentials, the person will be able to manage your Telegram account! ⚠️

## Setup and run the bot

#### Ater you inserted all credentials in the right way, make sure to run the script. For this open a command prompt in your foler and run the following commands.

#### Windows

```python main.py```

#### Linux

```sudo python main.py```

#### Server/ Hosting

If you want to host the bot on a 24/7 server you are hosting, please run theese Commands.

`screen` - This will open the 24/7 console, wich will continue running the script, if you disconnect to your server. After you run thew command it will ask you to ascespt the EULA. To accept simply press Enter/Space.

`sudo python main.py` - Run the bot.

#### After you run the script you will need to enter your phone number and the code telegram will send you. After you did this you can message and start the bot you just created. Congratulations 🥳. You will find the bot like every normal user by searching it in the searchbar or clikc the link in the BotFather message.

## Errors/Bugs

If you entered the values wrong or changed the code, please retry the creation and re-clone the Code how i mentioned it before. If this does not help please contact me or create an issue using this github repository.

## More setups

To setup coinbase commands to do this features: buy, sell, trade, wallet access you will need to some more setups to make the bot run.

1. Generate a API_KEY and API_SECRET on the Coinbase API_Dashboard. To do it, just open the <a href="https://www.coinbase.com/settings/api">Coinbase API-Dashboard</a> and login. Then click "create API-Key" like shown on the Screenshot below (ibb.com link). This will give you the values for the api_key and api_secret. You can add theese also to your credentials.txt file.


      <a href="https://ibb.co/9srwyFw"><img src="https://i.ibb.co/9srwyFw/Screenshot-2021-01-05-193415.png" alt="Screenshot-2021-01-05-193415" border="0"></a>

2. After your added the credentials restart the Bot like usual.

## Contact

You can conatct me on different ways listed below. Make sure to don't spam or send not allowed content, otherwise it will reullt a block.

- Telegram: t.me/lxnnard
- Discord: lxnnard#9580
