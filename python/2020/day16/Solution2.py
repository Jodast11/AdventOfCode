with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

valid_lines = []
valid = []
possible_fields = []
final_corelations = {}

def findValid():
    global valid
    valid_raw = []
    for counter, content in enumerate(lines):
        if counter<20:
            start1 = int(content[content.index(":")+1:content.index("-")])
            end1 = int(content[content.index("-")+1:content.index(" ",content.index("-"))])
            start2 = int(content[content.index(" or ")+4:content.index("-",content.index(" or "))])
            end2 = int(content[content.index("-",content.index(" or "))+1:])
            for i in range(start1,end1+1):
                valid_raw.append(i)
            for i in range(start2,end2+1):
                valid_raw.append(i)
    valid = list(set(valid_raw))
    valid.sort()
    #print(valid)
    
def removeInvalid():
    for i in range(25,len(lines)):
        line = lines[i].split(",")
        isValid = True
        for a in line:
            if int(a) not in valid:
                isValid = False
        if isValid:
            valid_lines.append(lines[i].split(","))        
    #print(valid_lines)
    
def validValuesForField(field_nr):
    valid_raw = []
    start1 = int(lines[field_nr][lines[field_nr].index(":")+1:lines[field_nr].index("-")])
    end1 = int(lines[field_nr][lines[field_nr].index("-")+1:lines[field_nr].index(" ",lines[field_nr].index("-"))])
    start2 = int(lines[field_nr][lines[field_nr].index(" or ")+4:lines[field_nr].index("-",lines[field_nr].index(" or "))])
    end2 = int(lines[field_nr][lines[field_nr].index("-",lines[field_nr].index(" or "))+1:])
    for i in range(start1,end1+1):
        valid_raw.append(i)
    for i in range(start2,end2+1):
        valid_raw.append(i)
    return valid_raw
    
def checkIfValuesWork(values,valid_values):
    for value in values:
        if int(value) not in valid_values:
            return False
    return True

def getFieldOfNearbyTickets(field):
    fields = []
    for i in valid_lines:
        fields.append(i[field])
    return fields
    
def getCorelations():
    global possible_fields
    for a in range(20):
        possible_fields_in_processing = []
        for i in range(20):
            if checkIfValuesWork(getFieldOfNearbyTickets(i),validValuesForField(a)):
                print(str(a)+":"+str(i))
                possible_fields_in_processing.append(i)
        possible_fields.append(possible_fields_in_processing)
                
def removeNumberFromCorelations(nr):
    for a in range(len(possible_fields)):
        try:
            possible_fields[a].remove(nr)
        except:
            pass
            
                
                
    
findValid()
removeInvalid()
getCorelations()

print(possible_fields)
for a in range(20):
    for i in range(len(possible_fields)):
        if len(possible_fields[i]) == 1:
            final_corelations.update({i:possible_fields[i][0]})
            removeNumberFromCorelations(possible_fields[i][0])

print(final_corelations)
awnser = 1
my_ticket = lines[22].split(",")
for i in range(6):
    awnser *= int(my_ticket[final_corelations[i]])
    
print(awnser)






            

    