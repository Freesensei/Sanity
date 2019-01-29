from sys import exit
import time
Running = False 
i = 0, 1, 2, 3, 4, 5, 6 
##################
class NPC:

    raise_amt = 1.05
    num_npc_amount = 0
    
    def __init__(self, first, last, pay, position):
        self.first = first
        self.last = last
        self.pay = pay
        self.position = position
        self.email = first + '.' + last + '@company.com'
        
        NPC.num_npc_amount += 1     
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        return int(self.pay)
    def Full_name(self):
        print("My name is ", end="")
        return str(self.first + ' ' + self.last)
    def pay_amount(self):
        return int(self.pay)
    def num_npc_amount_(self):
        print("Npc Count", end=": ")
        return int(self.num_npc_amount)
    def npc_position(self):
        print("My position is", end=" ") 
        return int(self.position)
    def EMAIL(self):
        self.email = self.first + '.' + self.last + '@company.com'
        return str(self.email) 
  
npc = []
npc.append(NPC("Karen", "lee", 50000, 0))   # npc[0]
npc.append(NPC("Tea", "cli", 60000, 1))     # npc[1]
npc.append(NPC("James", "Jin", 50000, 2))   # npc[2]
npc.append(NPC("Kasper", "test", 60000, 3)) # npc[3]
npc.append(NPC("Isak", "test", 70000, 4))   # npc[4]
npc.append(NPC("Glenn", "Clint", 50000, 5)) # npc[5]
npc.append(NPC("Joe", "test", 50000, 6))    # npc[6]

for i in (npc):
    print(NPC.Full_name(i))
    print(NPC.EMAIL(i))
    print(NPC.pay_amount(i))
    print(NPC.pay_raise(i))
    print(NPC.num_npc_amount_(i))
    print(NPC.npc_position(i))
       
for i in (npc):
    print(NPC.pay_raise(i))
for i in (npc):
    print(NPC.pay_amount(i)) 
for i in (npc):
    print(NPC.pay_raise(i))
for i in (npc):
    print(NPC.pay_amount(i))
for i in (npc):
    print(NPC.pay_raise(i))
for i in (npc):
    print(NPC.pay_amount(i))
##################
items_list = []
class items:
    
    def __init__(self, name, worth, currency):
        self.name = name
        self.worth = worth
        self.currency = currency
    
    def item_name(self):
        return str(self.name)
    def item_worth(self):
        print("Market worth of", end=" ")
        return int(self.worth) 
    def full_description(self):
        print("This " + str(self.name) + " has a market worth of", end=" ")
        return int(self.worth)
    def Currency(self):
        return str(self.currency)
            
items_list.append(items("Cookie", 10, "kr")) #1
items_list.append(items("Bottled mineral water", 20, "kr")) #2
items_list.append(items("Coke", 30, "kr")) #3
items_list.append(items("Med-kit", 100, "kr")) #4

# full description of items and Currency
for i in (items_list):
    print(items.full_description(i), end=" ")
    print(items.Currency(i))

###################  

def start_narrative():
    print("A long time ago there was a village stunning and beautiful at sight which flourished throughout time, until that one faithful day...")
def Player_Talk_little_girl():
    print("Hello")
    print("...")
    print("hi...")
    do_what = input("> ")
    if "shoot" in do_what:
        print("How could you! My body feels cold....")
        exit()    
    elif "buy" in do_what or "trade" in do_what:
        print("What would you like?")
    elif "ask directions" in do_what:
        time.sleep(0.8)
        print("There is a town..., Olive Town to be exact, is North-east from here")
def Merchant():
    print("Hello!")
    do_what = input("> ")
    if "Buy" in do_what:
        print("What would you like?")
    if "Trade" in do_what:
        print("Let's trade then, shall we?")
    if "Rob" in do_what:
        time.sleep(0.8)
        print("Please you don't need to do this!")
        time.sleep(0.8)
        print("Do you want to continue?")
        choice = input("press 1 to continue or 0 to stop: ")
        choice = int(choice)
        if choice == 1:
            print("Oh god! what a cruel world...")
        elif choice == 0:
            Merchant()
        
        

def dead():
    print("Wrong move friend. You shall be lost forever into the infinite abyss of nothingness.")
    exit()

def exit():
    Running = False

start_narrative()
Player_Talk_little_girl()
Merchant()
##################
