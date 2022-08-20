def analyseRule(rule):
    result = []
    options = rule.split("|")
    for option in options:
        parts = option.split(" ")
        while "" in parts:
            parts.remove("")
        result.append(parts)
    return result

def getRule(rules, rule):
    finalRuleList = []
    for subRule in rules[rule]:
        newRule = []
        for part in subRule:
            if part == "a" or part == "b":
                newRule.append(part)
            else:
                newRule.append(getRule(rules, part))
        finalRuleList.append(newRule if len(newRule) > 1 else newRule[-1])
    return finalRuleList if len(finalRuleList) > 1 else finalRuleList[-1]

def createValidTree(rule):
    for part in rule:
        

     
input = open("Input.txt").read().split("\n\n")

rules = {rule.split(":")[0].replace('"', ""):analyseRule(rule.split(":")[1][1:].replace('"', "")) for rule in input[0].split("\n")}

print(getRule(rules, "0"))