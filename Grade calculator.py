def computegrade(grade):
    if grade < 0 or grade > 1.0:
        print ("Please enter a valid score")
        quit()
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    elif grade < 0.6:
        return "F"


score = input("Enter Score: ")
try:
    grade = float(score)
except:
    print ("Please enter a valid score")
    quit()

sgrade = computegrade(grade)
print (sgrade)





