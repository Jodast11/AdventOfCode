Data = [] 
with open('Input.txt') as data_file: #read the input data
    for line in data_file:
        Data.append(line.strip()) 

for i in range(len(Data)):
    rest = 2020 - int(Data[i]) #subtract the nth value from 2020 
    for a in range(rest): #make a counter from 0 to the calculated value
        if(str(a) in Data and str(rest-a) in Data): #check if the counter is in the input and also the other required awnser
            print(int(Data[i])*a*(rest-a))
            exit()
        
print("Done")