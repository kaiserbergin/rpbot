import re

msg = "Hello World"
print(msg)


def reMatch(pattern, string):
    matchObj = re.match(pattern, string, re.IGNORECASE)
    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.groups() : ", matchObj.groups())
    else:
        print("No match!!")


reMatch(r'\d+:\d+', "24:2 45")
reMatch(r'!roll', "!roll something")
reMatch(r'!roll', "!rolL something")
reMatch(r'!roll \d+:\d+', "!rolL 2:6")
