from pickletools import stringnl


def count(string, letter):
    word = string
    count = 0
    for check in string:
        if check == letter:
            count = count + 1
    print(count)
