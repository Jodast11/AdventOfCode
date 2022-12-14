import copy

containers = [(y, int(x.strip())) for y, x in enumerate(open("input.txt"))]

def getAllCombinations(remainingContainers, target, maxContainerId):
    #print(f"Target: {target}, remaining containers: {remainingContainers}, max ID: {maxContainerId}")
    combinations = []
    for container in remainingContainers:
        if container[0] <= maxContainerId:
            if container[1] <= target:
                if target - container[1] == 0:
                    combinations.append([container])
                else:
                    newRemainingContainers = copy.deepcopy(remainingContainers)
                    newRemainingContainers.pop(newRemainingContainers.index(container))
                    for combination in getAllCombinations(newRemainingContainers, target - container[1], container[0]):
                        combinations.append([container]+combination)
    return combinations

print(len(getAllCombinations(containers, 150, max([x[0] for x in containers]))))