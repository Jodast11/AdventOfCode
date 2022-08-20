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
            

        
    def remap(self,active_cup_node, destination_cup_node):
    
        
        start_three_node = active_cup_node.next
        end_three_node = start_three_node.next.next
        after_three_node = end_three_node.next
        
        after_destination_node = destination_cup_node.next
        

        active_cup_node.next = after_three_node
        destination_cup_node.next = start_three_node
        end_three_node.next = after_destination_node
        
        

def getDestinationCup(active_cup_node):
    first_node = active_cup_node.next
    second_node = first_node.next
    third_node = second_node.next
    
    value_to_search = active_cup_node.data
    while True:
        value_to_search -= 1
        
        if value_to_search < 1:
            value_to_search = my_list.max()
        
        if value_to_search != first_node.data and value_to_search != second_node.data and value_to_search != third_node.data:
            destination_cup_node = cup_node_map[value_to_search]
            return destination_cup_node
        
    



cup_node_map = {}

with open("Input.txt") as f:
    cups_str = f.read()

my_list = linked_list()
for cup in cups_str:
    my_list.append(int(cup))

my_list.appendFromTo(10,1000001)

my_list.mapNodesToLibrary()

start_time = time.time()
active_cup_node = my_list.head
for i in range(10000000):
    active_cup_node = active_cup_node.next    
    destination_cup_node = getDestinationCup(active_cup_node)
    my_list.remap(active_cup_node, destination_cup_node)   
    
print(time.time()-start_time)
    
print(cup_node_map[1].next.data * cup_node_map[1].next.next.data)
    
# my_list.display()   

print("Done")


    



    