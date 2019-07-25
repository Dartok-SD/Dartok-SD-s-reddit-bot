import nltk
def differenceBetweenStrings(word1,word2):
	distance = nltk.edit_distance(word1,word2)
	total_length = len(word1)+len(word2)
	different_length = total_length-distance
	return float(different_length/total_length)

# print(differenceBetweenStrings("Kaguya Wants to be Confessed to","Kagya Wants to be Confesed to"))