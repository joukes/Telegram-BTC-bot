### Telegram BTC bot

## Installation

### 1. Clone the GitHub repository
```sh
git clone https://github.com/joukes/Telegram-BTC-bot.git
```

### 2. Install all needed requirements

```sh
pip install -r requirements.txt
```

## Create a Telegram Bot using <a href="t.me/BotFather">BotFather</a> on Telegram and get other credentials

### 1. Create the bot and it's token using the <a href="t.me/BotFather"> @BotFather</a> telegram account.

- Open a new chat with <a href="t.me/BotFather">BotFather</a> and click "start".
- Send the command: `/newbot` and follow all instructions from BotFather.

#### If you have any questions or the Bot creation fails, please watch the Video Tutorial.

⚠️ After the setup the bot will give you a token. Store is secure, if anyone else has acess to it the person can delete your bot! ⚠️

### 2. Get your API_ID and API_HASH from Telegram

- Open the <a href="my.telegram.org/"> Telegram Developer dashboard</a> and enter your phone number.
- After the official telegram account sent a verification Code to your Account verify the web login.
- Create a new "App" with random credentials and store the API_ID and API_HASH to the <a href="https://github.com/joukes/Telegram-BTC-bot/blob/main/credentials.txt"> credentials file</a> (Replace them with your values!).

#### If you have any questions or the app creation fails, please watch the Video Tutorial.

⚠️ After the setup store both values secure. If a other person gets the credentials, the person will be able to manage your Telegram account! ⚠️

## Setup and run the bot

#### Ater you inserted all credentials in the right way, make sure to run the script. For this open a command prompt in your foler and run the following commands.

`python main.py`- On windows
`sudo python main.py` - On Linux

