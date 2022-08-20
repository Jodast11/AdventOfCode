with open("Input.txt") as f:
    cups_str = f.read()

cups = []

for cup in cups_str:
    cups.append(int(cup))
    
for i in range(max(cups)+1,1000001):
    cups.append(i)
    
#print(cups)

def round():
    cups_zw = []
    cups_new = []
    cups_res = []
    active_cup = cups[0]
    next_cups = []
    dest_cup = -1
    dest_cup_ind = -1
    
    for counter, cup in enumerate(cups):
        if counter != 1 and counter != 2 and counter != 3:
            cups_new.append(cup)
        else:
            next_cups.append(cup)
           
    dest_cup = pickDestinationCup(active_cup, cups_new)
    dest_cup_ind = cups_new.index(dest_cup)
    
    for i in range(dest_cup_ind+1):
        cups_zw.append(cups_new[i])
        
    for i in range(3):
        cups_zw.append(next_cups[i])        
       
    for i in range(dest_cup_ind+1,len(cups_new)):
        cups_zw.append(cups_new[i])
    
    for i in range(1,len(cups_zw)):
        cups_res.append(cups_zw[i])

    cups_res.append(cups_zw[0])

    return cups_res
 
def pickDestinationCup(active_cup, cups_new):
    dest_cup = active_cup - 1
    while True:
        if dest_cup in cups_new:
            return dest_cup
        else:
            dest_cup -= 1
            if dest_cup < 1:
                dest_cup = max(cups_new)
        
    

for i in range(100):
    cups = round()
    #print(cups)
    
# solution = ""

# for i in range(cups.index(1)+1,len(cups)):
    # solution = solution + str(cups[i])
    
# for i in range(cups.index(1)):
    # solution = solution + str(cups[i])
    
print("The solution is: "+str((cups[0]*cups[1])))