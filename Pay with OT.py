def computepay(h, r):
    if h <= 40:
        pay = h * r
    if h > 40:
        pay = (h - 5) * r + (h - 40) * (1.5 * r)
        return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter a numeric value")
    quit()

p = computepay(h, r)

print ("Pay", p)




