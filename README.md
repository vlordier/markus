# markus
Markus is a simple Telegram bot running on AWS Lambda 
https://aws.amazon.com/lambda/

The goal of this little bot is to play around with serverless architecture.

It's scraping a stoic quote, asking for mood status, runs through a bunch of questions, done.
Not storing data anywhere as you can see in the code, respecting privacy.
If you were to store data, you could then run stats on completion, sentiment analysis, check fequent words (tf-idf) or much other fun little things to track your mood and progress.
~~ Use it daily, and your life will become amazing (c) ~~

You can easily modify the questions.

## Setup  : 
1- ### Get a Telegram token ##
Visit the botfather, https://t.me/botfather
Type /newbot and follow his instructions to set up a new bot.
=> you get your TG token

2- ### Get AWS lambda credentials 
Going to AWS Console / IAM / Create user, search for Lambda, add a user 
=> you get a key/secret pair, a .pem file, check with AWS CLI how to handle credentials and other variables 
https://docs.aws.amazon.com/cli/latest/topic/config-vars.html

3- ### deploy your bot to AWS Lambda  using Zappa https://github.com/Miserlou/Zappa
```
mkdir whateverdir && cd whateverdir
virtualenv venv (python 3.6+)
source bin/activate
pip install -r requirements.txt
zappa init (will ask for key/secret pair)
zappa deploy dev
```
You could just the same use 
=> you get a webhook 'my-custom-url'

4- ### connect the webhook to TG  
with your token and 'my-custom-url'
```
curl --request POST --url https://api.telegram.org/bot<Your Telegram TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "my-custom-url"}'
```

boom done, you can reach out to your bot 

There most certainly are millions of other ways to build such thing, but that's one which works.
