import nltk
def differenceBetweenStrings(word1,word2):
	distance = nltk.edit_distance(word1,word2)
	total_length = len(word1)+len(word2)
	different_length = total_length-distance
	return float(different_length/total_length)

def isSimilar(word1,word2):
	distance = nltk.edit_distance(word1,word2)
	total_length = len(word1) + len(word2)
	if distance == 1 and total_length > 5:
		return True
	different_length = total_length - distance
	percentage = float(different_length/total_length)
	if(percentage > .8):
		return True
	return False

def calculateRange(title):
	similar_title = "[DISC] " + title + " Ch.1"
	different_title =  " [DISC] " + title + "- Chapter 1111"
	most_similar = differenceBetweenStrings(title,similar_title)
	most_different = differenceBetweenStrings(title,different_title)
	return [most_similar,most_different]
	
def noDISCRange(title):
	similar_title = title + " Ch.1"
	different_title = title + "- Chapter 1111"
	most_similar = differenceBetweenStrings(title, similar_title)
	most_different = differenceBetweenStrings(title, different_title)
	return [most_similar, most_different]

def onlyHyphen(title):
	different_title = title + "-"
	most_different = differenceBetweenStrings(title, different_title)
	return most_different

# Stupid brute force way of parse the manga title and removing unnecessary things
# Probably could've been better but it doesn't really matter
def parseTitle(title):
	returnTitle = ""
	if(title[:6].lower() == "[DISC]".lower()):
		if(title[6] is not " "):
			returnTitle = title[6:]
		else:
			returnTitle = title[7:]
	if(title[1:7].lower() == "[DISC]".lower()):
		if(title[7] is not " "):
			returnTitle = title[7:]
		else:
			returnTitle = title[8:]
	i = 0;
	found = False
	wordcount = 0
	whatwasfound = ""
	for word in returnTitle.split():
		if(word.lower() == "chapter".lower()):
			found = True
			whatwasfound = "Chapter"
			break
		if(word.lower() == "Ch.".lower() ):
			found = True
			whatwasfound = "Ch."
			break
		if(word.lower() == "Ch".lower()):
			found = True
			whatwasfound = "Ch"
			break
		i+=1
		wordcount += len(word) + 1
	if(found):
		returnTitle = returnTitle[:wordcount]
	# if(returnTitle[len(returnTitle)-1] == " " or returnTitle[len(returnTitle)-1] == "-"):
	# 	returnTitle = returnTitle[:len(returnTitle)-1]
	tempTitle = returnTitle
	try:
		while (returnTitle[len(returnTitle) - 1] == " " or returnTitle[len(returnTitle)-1] == "-"):
			returnTitle = returnTitle[:len(returnTitle) - 1]
	except Exception as e:
		# print (e)
		return tempTitle
	return returnTitle

# print(parseTitle("[DISC] Bleach Chapter 1"))
# print(parseTitle("[DISC]Bleach Chapter 1"))
# print(parseTitle(" [DISC] Bleach Chapter 1"))
# print(parseTitle(" [DISC]Bleach Chapter 1"))
# print(parseTitle("[DISC] Bleach Ch. 1"))
# print(parseTitle("[DISC] Bleach Ch. 1"))
# print(parseTitle(" [DISC] Bleach - Chapter 1"))
# print(parseTitle("[DISC] Bleach - Ch. 1"))
# print(parseTitle("[DISC] Bleach - Ch. 1"))
# print(differenceBetweenStrings(parseTitle("[DISC] Bleach - Ch. 1"), "Bleach"))
#
# print(parseTitle("[DISC]"))
#
#
# # print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to"))
# print("Correct Title")
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kaguya Wants to be Confessed to Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kaguya Wants to be Confessed to Chapter 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kaguya Wants to be Confessed to - Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kaguya Wants to be Confessed to - Chapter 1"))
# print("With [DISC]")
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kaguya Wants to be Confessed to Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kaguya Wants to be Confessed to Chapter 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kaguya Wants to be Confessed to - Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kaguya Wants to be Confessed to - Chapter 1"))
#
# print("Misspelled Title")
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to Chapter 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to - Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to - Chapter 1"))
# print("With [DISC]")
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kagya Wants to be Confesed to Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kagya Wants to be Confesed to Chapter 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kagya Wants to be Confesed to - Ch. 1"))
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","[DISC] Kagya Wants to be Confesed to - Chapter 1"))
#
# # print(isSimilar("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to"))
# # print(isSimilar("Hi","No"))
# print("Difference Range: ")
# print(calculateRange("Kaguya Wants to be Confessed to"))
# print("No [DISC] Range:")
# print(noDISCRange("Kaguya Wants to be Confessed to"))
# print("Difference Range Short Title: ")
# print(calculateRange("Bleach"))
# print("No [DISC] Range Short Title:")
# print(noDISCRange("Bleach"))
# print("Only Hyphen Short Title:")
# print(onlyHyphen("Bleach"))
# print(differenceBetweenStrings("Bleach", "Blech -"))
# print(differenceBetweenStrings("Bleach", "Blech"))