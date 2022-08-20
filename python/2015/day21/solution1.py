import re

def hitsTillDeath(damage,armor,health):
    damagePerHit = damage - armor if damage - armor > 0 else 1
    return round((health/damagePerHit)+0.49999)

def readInput():
    input = open("input.txt").read().split("\n\n\n")

    enemyStatsRaw = input[0]
    enemyStats = [x.strip() for x in enemyStatsRaw.split("\n")]

    enemyHealth = int(enemyStats[0].split(": ")[-1])
    enemyDamage = int(enemyStats[1].split(": ")[-1])
    enemyArmor = int(enemyStats[2].split(": ")[-1])

    shopRaw = input[-1]
    pattern = re.compile("\s\d+")

    shop = []

    for i in range(3):
        allEquipments = []
        allEquipmentsRaw = shopRaw.split("\n\n")[i].split("\n")[1:]
        for equipmentRaw in allEquipmentsRaw:
            matches = pattern.findall(equipmentRaw)
            allEquipments.append([int(matches[0][1:]),int(matches[1][1:]),int(matches[2][1:])])

        shop.append(allEquipments)

    return shop, enemyHealth, enemyDamage, enemyArmor

def assembleKits(shop):
    #kit = (price, damage, armor)
    kits = []
    for possibleWeapon in shop[0]:
        for possibleArmor in shop[1]+[[0,0,0]]:
            for possibleRing1 in shop[2]+[[0,0,0]]:
                for possibleRing2 in shop[2]+[[0,0,0]]:
                    if possibleRing1 != possibleRing2:
                        newKit = [0,0,0]

                        newKit[0] += possibleWeapon[0]
                        newKit[1] += possibleWeapon[1]
                        newKit[2] += possibleWeapon[2]

                        newKit[0] += possibleArmor[0]
                        newKit[1] += possibleArmor[1]
                        newKit[2] += possibleArmor[2]

                        newKit[0] += possibleRing1[0]
                        newKit[1] += possibleRing1[1]
                        newKit[2] += possibleRing1[2]

                        newKit[0] += possibleRing2[0]
                        newKit[1] += possibleRing2[1]
                        newKit[2] += possibleRing2[2]

                        kits.append(newKit)
    
    return kits

shop, enemyHealth, enemyDamage, enemyArmor = readInput()

allKits = assembleKits(shop)

#kit = (price, damage, armor)

lowestKitWonPrice = 9999

for kit in allKits:
    ownResistance = hitsTillDeath(enemyDamage,kit[2],100)
    bossResistance = hitsTillDeath(kit[1],enemyArmor,enemyHealth)
    if ownResistance >= bossResistance and lowestKitWonPrice > kit[0]:
        lowestKitWonPrice = kit[0]

print(lowestKitWonPrice)

