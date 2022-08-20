knownAllergens = []
knownIngredients = []
allAllergens = []
allFoods = []

safeFoods = []
dangerusFoods = []

food_map = {}

with open("Input.txt") as f:
    foods = f.read().split("\n")

for food in foods:
    parts = food.split(" (")
    ingredients = parts[0].split(" ")
    allergens = parts[1].replace(")","").replace("contains ","").split(", ")
    knownAllergens.append(allergens)
    knownIngredients.append(ingredients)
    for allergen in allergens:
        if allergen not in allAllergens:
            allAllergens.append(allergen)
    for ingredient in ingredients:
        if ingredient not in allFoods:
            allFoods.append(ingredient)

def findIdsOfFoddsContainingAllergen(ingredient):
    output = []
    for counter,content in enumerate(knownAllergens):
        if ingredient in content:
            output.append(counter)
    return output

def canIngredientBeAllergen(ingredient, allergen):
    foodsWithAllergen = findIdsOfFoddsContainingAllergen(allergen)    
    for food_id in foodsWithAllergen:
        if ingredient not in knownIngredients[food_id]:
            return False
    return True

def addIfSafe(ingredient):
    possibleAllergen = False
    for allergen in allAllergens:
        if canIngredientBeAllergen(ingredient,allergen):
            #print("Carefull! Possible Alleregen")
            possibleAllergen = True
    if not possibleAllergen:
        safeFoods.append(ingredient)
    else:
        dangerusFoods.append(ingredient)
        
def countOccurances(ingredientToSearch, arrayToSarchIn):
    counter = 0
    for ingredients in arrayToSarchIn:
        for ingredient in ingredients:
            if ingredientToSearch == ingredient:
                counter += 1
    return counter

for ingredient in allFoods:
    addIfSafe(ingredient)
    
#print(safeFoods)

counter = 0

for food in safeFoods:
    counter += countOccurances(food, knownIngredients)
    
#print(counter)

allAllergens.sort()
print(allAllergens)
print(dangerusFoods)

for allergen in allAllergens:
    for food in dangerusFoods:
        if canIngredientBeAllergen(food, allergen):
            food_map.update({food : allergen})
            print(food+" could be "+allergen)
            
#print(food_map)
    




    
    
    
