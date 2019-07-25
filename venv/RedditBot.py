import SetUpPraw
import NameDifference
import sqlite3
import time
import threading

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        conn.close()
    return conn

def create_table(cursor):
	cursor.execute('''CREATE TABLE submissions
             (real submitted, Title text, Link text, TextBody text)''')

def insert_table(cursor,submission):
	# submission.title
	# submission.selftext
	# submission.url
	currentTime = time.time()
	insertTable = [currentTime,submission.title,submission.url,submission.selftext]
	cursor.execute('INSERT INTO submissions VALUES(?,?,?,?)',insertTable)

def empty_db_thread(cursor):
	currentTime = time.time()
	# There are 86400 seconds in a day
	passedTime = currentTime - 86400
	cursor.execute("DELETE FROM submissions WHERE submitted>?",passedTime)
	
if __name__ == '__main__':
	fileName = 'TestTracking.txt'
	subreddit = 'manga'
	raw = SetUpPraw.setUp()
	sub = raw.subreddit(subreddit)
	lineList = [line.rstrip('\n') for line in open(fileName)]
	
	conn = create_connection("SubmissionDatabase.db")
	c = conn.cursor()
	# create_table(c)

	for submission in sub.stream.submissions(skip_existing = True):
		# print(submission.title)
		if any(word in submission.title for word in lineList):
			insert_table(c, submission)
			conn.commit()
			print(submission.title)