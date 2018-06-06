# Twitterbot
Twitter Bot that Tweets messages from a text file but also follows, favorites and retweets stuff.

## Usage

1. Add your Twitter API credentials to your **credentials.py**.

2. Modify **yourtextfile.txt** with your own material that you want to tweet. *One line* equals to *one tweet*.

3. Modify **twitterbot_tweeter.py** and **twitterbot_retweeter.py** to fit your own demand. It is now set to Tweet once in a week. 

4. Edit your Retweetable tag in **twitterbot_retweeter.py**. If it is a popular tag, modify the sleep time. If you do not do that your bot will spam every tweet with the hashtag. Your Bot ***WILL*** be blacklisted, so please take good care of the values. 

