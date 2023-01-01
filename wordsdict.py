# Write your code here :-)
count = 0
dict_words = dict()  #Creates dictionary
handle = open('words.txt') #Opens file words.txt
for line in handle: # Iterates over each line in the file
    words = line.split()
    for word in words:
        count = count + 1
        if word in dict_words:
            continue
        dict_words[word] = count

if 'the' in dict_words:
    print('true')
else:
    print('false')
