import dice

rollHistories = {}


class RollHistory:
    def __init__(self):
        self.standardRolls = []
        self.lastRoll = dice.RollResult()


def standardRoll(userId: str, dieCount: int) -> {}:
    roll = dice.standardRoll(dieCount)
    if userId not in rollHistories:
        rollHistories[userId] = RollHistory()
    rollHistories[userId].standardRolls.append(roll)
    rollHistories[userId].lastRoll = roll
    return roll
