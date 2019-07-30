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

	
	
# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to"))