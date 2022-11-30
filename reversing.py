#this code split and reverse the word

word = input("enter a world:\n")
word_list = word.split(",")
print(word[::-1])
word_list = list(reversed(word))
print(word_list)
print(" ".join(word_list[::-1]))

#print(word_reverse)
