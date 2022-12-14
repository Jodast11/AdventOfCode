class Monkey:
    def __init__(self, id, items, opperationType, opperationAmount, devisibleCheck, targetMonkeys) -> None:
        self.id = id
        self.items = items
        self.opperationType = opperationType
        self.opperationAmount = opperationAmount
        self.devisibleCheck = devisibleCheck
        self.targetMonkeys = targetMonkeys
        self.itemsInspected = 0

    def throwItems(self):
        global monkeys
        global kgv

        while len(self.items) > 0:
            self.itemsInspected += 1
            currentItem = self.items.pop(0)

            #Apply opperation
            if not self.opperationType:
                currentItem += self.opperationAmount
            elif self.opperationType == 1:
                currentItem *= self.opperationAmount
            else:
                currentItem = currentItem*currentItem

            currentItem %= kgv

            #Test divisibility
            testPassed = not (currentItem % self.devisibleCheck)

            monkeys[self.targetMonkeys[testPassed]].items.append(currentItem)

monkeysRaw = open("input.txt").read().split("\n\n")

monkeys = []

kgv = 1

for monkeyRaw in monkeysRaw:
    monkeyRawInfo = monkeyRaw.split("\n")
    monkeyId = monkeyRawInfo[0].replace(":","").split(" ")[-1]
    items = [int(x) for x in monkeyRawInfo[1].replace("  Starting items: ","").replace(",","").split(" ")]
    worryLevelAffektType, worryLevelAffektAmount = monkeyRawInfo[2].replace("  Operation: new = old ","").split(" ")
    worryLevelAffektType = 2 if worryLevelAffektAmount == "old" else (1 if "*" == worryLevelAffektType else 0)
    worryLevelAffektAmount = int(worryLevelAffektAmount) if worryLevelAffektType < 2 else -1
    testCondition = int(monkeyRawInfo[3].replace("  Test: divisible by ",""))
    kgv *= testCondition
    nextMonkeys = (int(monkeyRawInfo[5].split(" ")[-1]), int(monkeyRawInfo[4].split(" ")[-1]))

    newMonkey = Monkey(monkeyId, items, worryLevelAffektType, worryLevelAffektAmount, testCondition, nextMonkeys)
    monkeys.append(newMonkey)

print(kgv)

for i in range(10000):
    for monkey in monkeys:
        monkey.throwItems()

activity = [x.itemsInspected for x in monkeys]
activity.sort()

print(activity[-1]*activity[-2])