# Dartok-SD's reddit bot
 Creating a bot just for fun

If you want to run this, then you should replace: 

```
raw = SetupPraw.setUp()
```

in RedditBot.py with:

```
clientId = 'Your Client ID'
clientSecret = 'Your Client Secret'
raw = praw.Reddit(user_agent='User Agent Name', client_id=clientId, client_secret=clientSecret)
```

