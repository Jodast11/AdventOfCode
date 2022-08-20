counter = 0
with open("Input.txt") as f:
    data = f.readlines()  #read the Input Data
    data_cleaned = []
    for line in data:   #remove the formating characters
        data_cleaned.append(line.strip())

def get_num_bags(color):
    lines = []
    for line in data_cleaned:  #see if color is in line, and isnt the first color
        if color in line:
            if line.index(color) > line.index("contain"):
                lines.append(line)       
    allColors = []    
    if len(lines) == 0:  #see if there are entrys in lines
        return []        
    else:
        colors = []
        for line in lines: #add the color found in the line to colors
            colors.append(line[:line.index(" bags contain")])
            
        for color in colors:  
            if color in allColors:
                colors.append(color)
  
        for color in colors:
            allColors.append(color)
            bags = get_num_bags(color)
            
            allColors += bags
        
        uniqueColors = []
        for color in allColors:
            if color not in uniqueColors:
                uniqueColors.append(color)
                
        return uniqueColors
            
    
    
#colors = get_num_bags("shiny gold")
#print(len(colors))


    
    
   


def find_amount_of_bags(color, multiplier):
    global counter
    lines_containing_color = []  
    for line in data_cleaned:  #find line containing color
        if color in line:
            if line.index(color) < line.index("contain"):
                lines_containing_color.append(line)
    
    #print(lines_containing_color)
    
    for line in lines_containing_color:  #iterate through lines_containing_color
        multi = line[line.index("contain")+8]  #get multiplier from string
        col = line[line.index("contain")+10:line.index("bag", line.index("contain"))-1] #get color from string
        if multi != "n":                   
            counter += int(multi)*int(multiplier) 
            print(col+multi)
            find_amount_of_bags(col, int(multi)*int(multiplier) )
        else:
            print("")
        index = 0
        
        while True: 
            try:
                multi = line[line.index(",",index)+2]
                col = line[line.index(",",index)+4:line.index("bag",line.index(",",index))]
                index = line.index("bag",line.index(",",index))+1
                counter += int(multi)*int(multiplier)
                find_amount_of_bags(col, int(multi)*int(multiplier))
            except:
                break
   
    
find_amount_of_bags("shiny gold", 1)
print(counter)

# string = "bright silver bags contain 4 dotted indigo bags, 1 drab tomato bag, 1 muted salmon bag."
# for a in range(5):
    # index = 0
    # for i in range(10):
        # try:
            # print(string[string.index(",",index)+4:string.index("bag",string.index(",",index))])
            # index = string.index("bag",string.index(",",index))+1
        # except:
            # break
    

