class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
        
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
            
        print(elems)
        
    def get(self,index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node=self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx+=1
            
    def erase(self,index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return None
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
        cur_node=self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            if cur_node.data == searchtearm:
                return cur_idx
            cur_idx += 1
        return -1
        
    def max(self):
        max_value = -1
        cur_idx = 0
        cur_node=self.head
        while cur_node.next != None:
            cur_node=cur_node.next  
            if cur_node.data > max_value:
                max_value = cur_node.data
            cur_idx += 1
        return max_value
        
            
        
        
           

active_cup_index=0

def round():
    global active_cup_index
    active_cup_value = my_list.get(active_cup_index)
    dst_Idx = getDestinationCupIndex(active_cup_value)
    my_list.remap(active_cup_index,dst_Idx)
    active_cup_index += 1
    
def getDestinationCupIndex(active_cup_value):
    value_to_search = active_cup_value - 1
    while True:
        if my_list.index(value_to_search) != -1:
            if my_list.index(value_to_search) != my_list.index(active_cup_value)+1 and my_list.index(value_to_search) != my_list.index(active_cup_value)+2 and my_list.index(value_to_search) != my_list.index(active_cup_value)+3:
                print(my_list.index(value_to_search))
                return my_list.index(value_to_search)
            else:
                value_to_search -= 1
                if value_to_search < 1:
                    value_to_search = my_list.max()    
        else:
            value_to_search -= 1
            if value_to_search < 1:
                value_to_search = my_list.max()
                
    
    

with open("Input.txt") as f:
    cups_str = f.read()

my_list = linked_list()
for cup in cups_str:
    my_list.append(int(cup))
my_list.display()

round()

my_list.display()




    