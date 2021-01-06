# "items" 
#         id
#         name
#         cond

class Item:
    def __init__(self, item_id, name, condition):
        self.item_id = item_id
        self.name = name
        self.condition = condition
        

    def __str__(self):
    
        return f"Id:{self.item_id}\tName:{self.name}\tCondition:{self.conditions}"

if __item_one = Item(0, "book", "used")
item_two = Item(0, "water bottle", "naw")

print(item_one)
print(item_two)