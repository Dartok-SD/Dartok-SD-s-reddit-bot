import SetUpPraw
raw = SetUpPraw.setUp()
sub = raw.subreddit('manga')
for submission in sub.new():
	print (submission.title)