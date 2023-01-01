fhand = input("Enter file name ") #Ask user for file name
if len(fhand) < 1 :
    fhand = "mbox.txt" # If file name is not entered pull up mbox
file  = open(fhand) #open file
counts = dict() #make dictionary
for line in file: # for each line in the file
    words = line.split() #split the words in file by spaces
    for word in words: #for each word in the file
        counts[word] = counts.get(word, 0 ) + 1 # check if word is in dict, increment +1

lst = list() #create list for ordering
for key, val in counts.items(): # for each key and value in the dict
    newtup = (val, key) #assign val key to new variable
    lst.append(newtup) #add val, key to dict

lst = sorted(lst, reverse = True)

for val, key in lst[:10] :
    print(key, val)
