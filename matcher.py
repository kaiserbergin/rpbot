import re


def isMatch(pattern, string) -> bool:
    matchObj = re.match(pattern, string, re.IGNORECASE)
    if matchObj:
        return True
    else:
        return False


def getMatch(pattern, string):
    matchObj = re.match(pattern, string, re.IGNORECASE)
    if matchObj:
        return matchObj.group()
    else:
        return None


def isSimpleRoll(string) -> bool:
    pattern = r'^!roll \d+$'
    return isMatch(pattern, string)


def getFirstNum(string) -> int:
    return int(string.split(' ')[1])
