import time

class node:
    def __init__(self,data=None,first_node=None):
        self.data=data
        self.next=first_node
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        cur = self.head
        start_node = cur.next
        runs = 0
        try:
            while runs < 2:
                while cur.next != start_node:
                    cur = cur.next
                cur_prev = cur
                cur = cur.next
                runs += 1
            new_node = node(data,self.head.next) 
            cur_prev.next = new_node
            #print("Normal")
        except:
            #print("Expecting")
            new_node = node(data) 
            self.head.next = new_node
            new_node.next = new_node
        
        
        
    def length(self):   
        # cur = self.head
        # start_node = cur.next
        # runs = 0
        # counter = 0
        # try:
            # while runs < 2:
                # while cur.next != start_node:
                    # cur = cur.next
                    # counter += 1
                # cur = cur.next
                # runs += 1
            # print("Normal")
            # return counter
        # except:
            # print("Expecting")
            # return counter
        return(len(cup_node_map))

        
    def display(self):
        elems = []
        cur_node = self.head
        start_node = cur_node.next
        runs = 0
        while runs < 2:
            while cur_node.next != start_node:
                cur_node=cur_node.next
                elems.append(cur_node.data)
            runs += 1
            cur_node = cur_node.next
            elems.append(cur_node.data)
        del elems[-1]
        print(elems)
        
    def get(self,index):
        cur_idx = 0
        cur_node=self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx+=1
            
    def erase(self,index):
        cur_idx = 0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx += 1
            
    def index(self,searchtearm):
        cur_idx = 0
        cur_node = self.head
        start_node = cur_node.next
        runs = 0
        while runs < 2:
            while cur_node.next != start_node:
                cur_node=cur_node.next
                if cur_node.data == searchtearm:
                    return cur_idx
                cur_idx += 1
            runs += 1
            cur_node = cur_node.next
            if cur_node.data == searchtearm:
                return cur_idx
            cur_idx += 1
        return -1
        
    def max(self):
        return(max(cup_node_map))
        
    def appendFromTo(self,from_value,to_value):
        cur = self.head
        start_node = cur.next
        runs = 0
        while runs < 2:
            while cur.next != start_node:
                cur = cur.next
            cur_prev = cur
            cur = cur.next
            runs += 1
        prev_new_node = cur_prev
        for i in range(from_value,to_value):
            new_node = node(i,self.head.next) 
            prev_new_node.next = new_node
            prev_new_node = new_node
            #print(i)

    def mapNodesToLibrary(self):
        cur_node = self.head
        start_node = cur_node.next
        runs = 0
        while runs < 2:
            while cur_node.next != start_node:
                cur_node=cur_node.next
                cup_node_map.update({int(cur_node.data) : cur_node})
            runs += 1
            cur_node = cur_node.next
            cup_node_map.update({int(cur_node.data) : cur_node})
            

        
    def remap(self,active_cup, destination_cup):
    
        
        active_cup_node = cup_node_map[active_cup]
        start_three_node = active_cup_node.next
        end_three_node = start_three_node.next.next
        after_three_node = end_three_node.next
        
        destination_cup_node = cup_node_map[destination_cup]
        after_destination_node = destination_cup_node.next
        

        active_cup_node.next = after_three_node
        destination_cup_node.next = start_three_node
        end_three_node.next = after_destination_node
        
        

def getDestinationCup(active_cup_value):
    list_max_value = my_list.max()
    value_to_search = active_cup_value - 1
    while True:
        if my_list.index(value_to_search) != -1:
            if isNumberPossible(active_cup_value, value_to_search): 
                return value_to_search
            else:
                value_to_search -= 1
                if value_to_search < 1:
                    value_to_search = list_max_value   
        else:
            value_to_search -= 1
            if value_to_search < 1:
                value_to_search = list_max_value
 

def isNumberPossible(active_cup_value, value):
    index_active_cup_value = my_list.index(active_cup_value)
    index_value = my_list.index(value)
    list_length = my_list.length()
    if index_active_cup_value == index_value:
        return False
    if index_active_cup_value+1 == index_value:
        return False
    if index_active_cup_value+2 == index_value:
        return False
    if index_active_cup_value+3 == index_value:
        return False
    if index_active_cup_value+2 >= list_length:
        list_0 = my_list.get(0)
        list_1 = my_list.get(1)
        overflow_length = index_active_cup_value+2 - list_length + 1
        if overflow_length == 1:
            if list_0 == value:
                return False
        if overflow_length == 2:
            if list_0 == value or list_1 == value:
                return False
        if overflow_length == 3:
            if list_0 == value or list_1 == value or my_list.get(2) == value:
                return False
        
    return True



cup_node_map = {}

with open("Input.txt") as f:
    cups_str = f.read()

my_list = linked_list()
for cup in cups_str:
    my_list.append(int(cup))

my_list.appendFromTo(10,1000001)
#my_list.display()
print()

my_list.mapNodesToLibrary()


# active_cup_index = 0
# for i in range(100):
    # start_time = time.time()
    # active_cup_value = my_list.get(active_cup_index)
    # print("1: "+str(time.time()-start_time))
    # start_time = time.time()
    # destination_cup = getDestinationCup(active_cup_value)
    # print("2: "+str(time.time()-start_time))
    # start_time = time.time()
    # my_list.remap(active_cup_value, destination_cup)   
    # print("3: "+str(time.time()-start_time))
    # start_time = time.time()
    # active_cup_index = my_list.index(active_cup_value)+1
    # print("4: "+str(time.time()-start_time))
    # print()

    

# print("Done")

start_time = time.time()
for i in range(10000):
    # my_list.index(i)
    isNumberPossible(i,8)
    
print(time.time()-start_time)
    






    