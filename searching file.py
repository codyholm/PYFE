# Searching file for X
fname = input("Enter file name: ")
fh = open(fname)
lines = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        lines = lines + 1
        atpos = line.find("0")
        value = float(line[atpos: ])
        total = total + value
print("Average spam confidence:", total / lines)
