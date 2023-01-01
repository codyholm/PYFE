text = "X-DSPAM-Confidence:    0.8475"
atpos = text.find("0")
value = text[atpos: ]
fvalue = float(value)
print(fvalue)



