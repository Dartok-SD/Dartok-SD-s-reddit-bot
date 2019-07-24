import SetUpPraw
import sqlite3
fileName = 'TestTracking.txt'
subreddit = 'AskReddit'
raw = SetUpPraw.setUp()
sub = raw.subreddit(subreddit)
lineList = [line.rstrip('\n') for line in open(fileName)]
for submission in sub.stream.submissions(skip_existing = True):
	# print(submission.title)
	if any(word in submission.title for word in lineList):
		print(submission.title)