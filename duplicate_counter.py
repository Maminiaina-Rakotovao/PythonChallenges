word = 'aabbcdedfhjdiigewer'
word = word.lower()

# Convert the string into list
word_list = []
for i in word:
	word_list.append(i)

duplicates_item = [duplicate for duplicate in word_list if  word_list.count(duplicate)>1]
duplicate_list = list(set(duplicates_item))

print(len(duplicate_list))

