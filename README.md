# Dartok-SD's reddit bot
Creating a bot just for fun

Right now all it does is it constantly checks the new section of a subreddit, and if a post contains 
a word in the list of words then it will add it to the database and notify a user.



If you want to run this, then you should replace: 

```
raw = SetupPraw.setUp()
```

in RedditBot.py with:

```
clientId = 'Your Client ID'
clientSecret = 'Your Client Secret'
raw = praw.Reddit(user_agent='User Agent Name', 
                  client_id=clientId,
                  client_secret=clientSecret
                  password = 'account password',
                  username = 'account username')
```

