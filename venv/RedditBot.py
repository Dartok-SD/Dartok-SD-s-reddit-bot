import SetUpPraw
import praw
import NameDifference
import sqlite3
import time
# import threading
import re

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
        conn.close()
    return conn

def create_table(cursor):
	cursor.execute('''CREATE TABLE submissions
             (real submitted, Title text, Link text, TextBody text)''')

def insert_table(cursor,submission,conn):
	# submission.title
	# submission.selftext
	# submission.url
	try:
		currentTime = time.time()
		editedSubmissionUrl = submission.url
		if(editedSubmissionUrl[-2:] == '/1'):
			editedSubmissionUrl = editedSubmissionUrl[:-2]
		insertTable = [currentTime,submission.title,editedSubmissionUrl,submission.selftext]
		cursor.execute('INSERT INTO submissions VALUES(?,?,?,?)',insertTable)
		conn.commit()
		return True
	except Exception as e:
		print(e)
		print("REPOSTED CHAPTER")
		return False
	
def message_person(reddit,person,content, link):
	redditor = reddit.redditor(name=person)
	redditor.message('New Manga Chapter', content + ' has just been released: ' + link)

# Do I really need to remove from the database?
def empty_db_thread(cursor):
	currentTime = time.time()
	# There are 86400 seconds in a day
	passedTime = currentTime - 86400
	cursor.execute("DELETE FROM submissions WHERE submitted>?",passedTime)
	
if __name__ == '__main__':
	fileName = 'TestTracking.txt'
	myFile = 'TrackingManga.txt'
	subreddit = 'manga'
	reddit = SetUpPraw.setUp()
	sub = reddit.subreddit(subreddit)
	lineList = [line.rstrip('\n') for line in open(fileName)]
	myList = [line.rstrip('\n') for line in open(myFile)]
	conn = create_connection("SubmissionDatabase.db")
	c = conn.cursor()
	# create_table(c)

	for submission in sub.stream.submissions(skip_existing = True):
		# print(submission.title)
		# r = re.compile()
		# list(filter(r.match()))
		for txt in myFile:
			my_regex = r"([^.]*?" + txt + "[^.]*\.)"
			found = re.findall(my_regex, submission.title, re.IGNORECASE)
			if(found is not None):
				print(found)
		if any(word in submission.title for word in lineList):
			if(insert_table(c, submission,conn)):
				print(submission.title)
				# message_person(reddit, "Dartok_sd",submission.title,submission.url)
			# if any(word in submission.title for word in myFile):
				# message_person(reddit, "Dartok_sd", submission.title, submission.url)
		# if any((word in submission.title for word in myFile)):
		# 	if(insert_table(c, submission, conn)):
		# 		print(submission.title)
		# 		message_person(reddit, "Dartok_sd", submission.title, submission.url)
		#
