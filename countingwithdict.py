name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counter = dict()
for line in handle: #For each line in file
    line = line.rstrip() #Strips right side white space from each line
    if line.startswith("From: "): # Checks if line starts with From:
        words = line.split() # Splits line into words
        #get value associated with word adds 1 if not there return 0
        counter[words[1]] = counter.get(words[1],0) + 1

lkey = None # declares variables for most prolific committer
lvalue = None
for key,val in counter.items(): # For each key/value in dict
    if lvalue is None: # Sets variables for first iteration
        lvalue = val
        lkey = key
    elif val > lvalue: # Sets most prolific committer
        lvalue = val
        lkey = key
print(lkey, lvalue)
