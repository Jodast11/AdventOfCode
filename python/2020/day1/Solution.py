#Read File into List
Data = []
with open('Input.txt') as data_file:
    for line in data_file:
        Data.append(line.strip())


for i in range(len(Data)):
    rest = 2020 - int(Data[i]) #get the nth value in the input and subtract it from 2020
    if(str(rest) in Data):  #check if the calculated vale exists in the report.
        index = Data.index(str(rest))
        print(int(Data[i])*int(Data[index]))  #multiply the found values to get the solution
        break