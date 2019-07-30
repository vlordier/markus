# markus
Markus is a simple Telegram bot running on AWS Lambda
https://aws.amazon.com/lambda/

It's scraping a stoic quote, asking for mood status, runs through a bunch of questions, done.
Not storing data anywhere as you can see in the code.

You can easily modify the questions, never hardcode your AWS credentials.

Steps: 
1- Get a Telegram token
Visit the botfather, https://t.me/botfather
Type /newbot and follow his instructions to set up a new bot.
=> you get your TG token

2- Get AWS lambda credentials by going to Console / IAM / Create user, search for Lambda, add a user 
=> you get a key/secret pair

3- deploy your bot to AWS Lambda
mkdir whateverdir && cd whateverdir
virtualenv venv (python 3.6+)
source bin/activate
pip install -r requirements.txt
zappa init (will ask for key/secret pair)
zappa deploy dev

=> you get a webhook 'my-custom-url'

4- now connect the webhook to TG with your token and 'my-custom-url'
curl --request POST --url https://api.telegram.org/bot<Your Telegram TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "my-custom-url"}'

boom done.

There most certainly are millions of other ways to build such thing, but that's one which works.
