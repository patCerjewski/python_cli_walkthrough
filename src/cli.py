"""
work wants inventory app that:
stores data in file
uses command line to add/ update/ delete:
    "items" 
        id
        name
        cond
        checkedIn
"""
import models.item import Item
next_id = 0
items = []
#tood make a menu print out showing options
#make file s
def menu():
    print("""hello
1. List All Items
2. Add New Items
3. Update Existing Item
4. Delete Item(by item id)
5. Exit
""")#  can be used as a meny

# 1. List All Items
def list_items():
    
    for item in items:
        print(item)
       
    
# 2. Add New Items
def new_item():
    global next_id
    name = input("name:")
    cond = input("Condition: ")
    item_id = next_id
    next_id += 1
    
    tmp = Item(item_id, name, cond)
    items.append(tmp)
    pass
# 3. Update Existing Item
def update_existing(itemId):
    pass
# 4. Delete Item(by item id)
def delete_item(itemId):
    pass
# 5. Exit
while True:
    menu()
    choice = input("> ")
    
    if choice =="1":
        list_items()
    elif choice == "2":
        new_item()
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":

        exit()
    else:
        input("Invalid Input\n(Press Enter to try again)")