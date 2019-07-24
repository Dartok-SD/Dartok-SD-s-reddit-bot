import SetupPraw
raw = SetupPraw.setUp()
sub = raw.subreddit('Megaten')
for submission in sub.top(limit=5):
	print (submission.title)