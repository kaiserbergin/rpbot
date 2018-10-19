import random


diceValuesNumeric = (-1, 0, 0, 1, 2, 3)


class RollResult:
    def __init__(self, dice=[], hits=0):
        self.dice = dice
        self.hits = hits


def rollDie() -> int:
    return diceValuesNumeric[random.randint(0, 5)]


def rollDice(x: int) -> int:
    dice = []
    for x in range(0, x):
        dice.append(rollDie())
    return dice


def getHits(dice: [int]) -> int:
    hits = 0
    tempDice = sorted(dice)
    lastIndex = len(tempDice)
    index = 0
    while index < lastIndex:
        if tempDice[index] < 0 and tempDice[-index - 1] > 0:
            lastIndex = lastIndex - 1
        else:
            hits += tempDice[index]
        index += 1
    return hits


def removeMisses(dice: [int], removals: int) -> [int]:
    for x in range(0, len(dice)):
        if dice[x] < 0:
            dice[x] = 0
            removals -= 1
        if removals < 1:
            break
    return dice


def rerollDiceByCount(dice: [int], rerolls: int) -> [int]:
    tempDice = sorted(dice)
    for x in range(0, len(tempDice)):
        if tempDice[x] > -1:
            dice[dice.index(tempDice[x])] = rollDie()
            rerolls -= 1
        if rerolls < 1:
            break
    return dice


def formatDice(dice: [int]) -> [str]:
    formattedDice = []
    for x in dice:
        if x == -1:
            dieStr = "X"
        else:
            dieStr = str(x)
        formattedDice.append(dieStr)
    return formattedDice


def standardRoll(dieCount: int) -> {}:
    result = RollResult()
    result.dice = rollDice(dieCount)
    if len(result.dice) > 0:
        result.hits = getHits(result.dice)
    return result


"""def fixRoll(dice: [int], skillPoints: int) -> {}:
    result = {
        "dice":}"""
