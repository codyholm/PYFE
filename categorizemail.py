name = input("File name: ")
if len(name) < 1:
    name = "mbox.txt"
file = open(name)
mail = dict()
for line in file:
    if line.startswith("From "):
        words = line.split() # Splits line into words
        mail[words[2]] = mail.get(words[2],0) + 1

print(mail)
