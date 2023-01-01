name = input("Enter file:") # Asks user for file name
if len(name) < 1: #Automatically loads mbox if none entered
    name = "mbox.txt"
handle = open(name)
hours = dict() #Creates dictionary to store the hours distribution
for line in handle: # For each line in the file
    words = line.split() # Split the line into words
    if line.startswith("From "): # Checks if line starts with "From "
        time = words[5].split(':') # Finds time by splitting again using ":"
        hours[time[0]] = hours.get(time[0], 0) + 1 # Checks if current hour is in dict, incr +1

lst = list() #Creates list to sort and print hours
for key, val in list(hours.items()): #For each key, val in dict list add to list
    lst.append((key,val))

lst.sort() # Sorts list

for key, val in lst:
    print(key, val) #For each key, val in list prints the key, val
