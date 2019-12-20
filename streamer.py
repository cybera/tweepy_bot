import tweepy
import json
import pandas as pd
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime
import datetime as dt
from swift_upload import upload_file
# you'll need a login.py script with all these things. Also note you'll need
# to enable insecure login of 3rd party apps... so don't use this with an 
# email you care about. This is mostly to set yourself notifications if something 
# has crashed or not 
from login import me, you, password, tweepy_oauth1, tweepy_oauth2, tweepy_token1, tweepy_token2

auth = tweepy.OAuthHandler(tweepy_oauth1, 
                           tweepy_oauth2)
auth.set_access_token(tweepy_token1, 
                      tweepy_token2)

api = tweepy.API(auth, wait_on_rate_limit=True)

#This is a basic listener that just prints received tweets to stdout.
import pandas as pd
import time

class StdOutListener(StreamListener):

    def __init__(self, filename):
        self.file = filename
    def on_status(self, status):
        try:
            jsonData = status._json
            tweetID = jsonData.get("id_str")
            tweetData = api.get_status(tweetID)

            #check if tweet is valid (not a retweet)
            if ( (hasattr(tweetData, 'retweeted_status')) ):
                pass
            else:
                with open("alberta_tweets_nov_2019", 'a') as f:
                    f.write(str(jsonData))
                    print(jsonData['text'])
                    f.write('\n')
                
        except (tweepy.error.RateLimitError):
            print("rate limiting?, waiting for one minute")
            time.sleep(60)

        except Exception as e:
            print("something went wrong")
            print(e)
            pass


    def on_error(self, status):
        #error number 503, servers down
        #print('Error #:', status)
        pass

def send_email(file):
    with open(file) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
    msg['Subject'] = "Your Tweepy Bot at %s" % datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg['to'] = you
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    msg['From'] = me
    s.login(me, password)
    s.send_message(msg)
    s.quit()

alberta = [-121.000000, 48.000000,-109.000000, 61.000000]

filename = str(dt.datetime.now().date())+ "_start.txt"
twitterStream = Stream(auth, 
                StdOutListener(filename), 
                tweet_mode='extended')
oh_no = 0 
start = time.time()
time_since_failure = time.time()
diff_fail = 0

start = dt.datetime().minute
while True:
    try:
        # failed too many times, something funky is up 
        if diff_fail < 4000:
            if oh_no > 2:
                end = time.time()
                print("I was running for", (end - start)/60/60, 'hours')
                break 
        if diff_fail > 4000: 
            oh_no = 0 
        if (dt.datetime().now() - start) >= 5:
            upload_file("alberta_twitter_data", filename, filename):
            filename = str(dt.datetime.now().now())+ "_start.txt"
            twitterStream.disconnect()
             twitterStream = Stream(auth, 
                StdOutListener(filename), 
                tweet_mode='extended')

        send_email("started_email.txt")
        twitterStream.filter(languages=["en"], locations=alberta)

    except:
        # if something broke, let's wait an hour
        diff_fail = time.time() - time_since_failure
        time_since_failure = time.time()
        oh_no += 1
        send_email("broke_email.txt")
        time.sleep(3600)



# USE THIS TO READ THE DATA
# data = []
# with open("testtweets.txt") as inputData:
#     for line in inputData:
#         json_acceptable_string = line.rstrip('\n').replace("'", "\"")
#         print(json_acceptable_string)
#         data.append(json_acceptable_string)
        
        
        
# json.dumps(data)        
     
            
