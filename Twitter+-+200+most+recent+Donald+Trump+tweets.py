
# coding: utf-8

# In[1]:

# General:
import tweepy           # To consume Twitter's API


# In[2]:

# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'nn6hQqSoo57dSDxXCr9QgEbGI'
CONSUMER_SECRET = 'aOjcx63ND4DAskmJC93Bi0IvhKNPf56bIhkgeSrM43WDzDbU9j'

# Access:
ACCESS_TOKEN  = '1676154792-5WNbJWy0SxpvddHrMOR6yIOIZoXNRF4axvmrxCy'
ACCESS_SECRET = 'sxG9vmQSfpPjH2RZwM7HhgiQV9wrjvIdCMZBm8FSKnDCK'


# In[3]:

# We import our access keys:
# This will allow us to use the keys as variables

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


# In[6]:

# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="realDonaldTrump", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))
    
print("Recent tweets:\n")
for tweet in tweets:
    print(tweet.text)
    print()


# In[ ]:



