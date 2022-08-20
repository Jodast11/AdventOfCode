with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

earlyest_departure_time  = int(lines[0])    
buslines=lines[1].split(",")
buslinesvalid = []
#print(buslines)
for i in buslines:
    if i != "x":
        buslinesvalid.append(int(i))
buslinesvalid.sort()
buslinesvalid_departure_times = []
  
print(buslinesvalid)

for i in buslinesvalid:
    time = 0
    while time < earlyest_departure_time:
        time += i
    buslinesvalid_departure_times.append(time)
    
print(buslinesvalid_departure_times)

lowest_time = 1000000000
lowest_index = 0

for i in range(len(buslinesvalid_departure_times)):
    if buslinesvalid_departure_times[i] < lowest_time:
        lowest_time = buslinesvalid_departure_times[i]
        lowest_index = i
      
print(lowest_time)
print(buslinesvalid[i-1])
print((lowest_time-earlyest_departure_time)*buslinesvalid[i-1])
     



