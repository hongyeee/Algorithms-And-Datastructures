from unicodedata import name


class ItemType:
    def __init__(self, name):
        
        self.name = name


class HashTable:
    def __init__(self):
        self.max_items = 10
        self.table = [None for _ in range(self.max_items)]
        self.num_items = 0

    def retrieve_item(self, item):
        hash_value = self.hash(item)

        return self.table[hash_value]

    def hash(self, item):
        
        sum = 0
        for char in item.name:
            sum += ord(char)
        
        return sum % self.max_items

    def insert_item(self, item):
        hash_value = self.hash(item)
        
        flag = False
        
        while flag is False and self.is_full() is False:
            if self.table[hash_value] is None:
                self.table[hash_value] = item  
                self.num_items += 1
                flag = True
            else:
                hash_value += 1
                hash_value %= self.max_items
    
    def delete_item(self, item):
        hash_value = self.hash(item)
        find = False
        while find is False:
            if self.table[hash_value].name == item.name:
                self.table[hash_value] = None
                find = True
                self.num_items -= 1
            else:
                hash_value += 1
                hash_value %= self.max_items

        for i in range(0, self.max_items):
            if self.table[i] != None:
                temp = self.table[i]
                loc = self.hash(temp)
                if self.table[loc] != temp:
                    for j in range(0, i):
                        if self.table[loc] is None:
                            self.table[loc] = temp
                            self.table[i] = None
                        else:
                            loc += 1
                            loc %= self.max_items


    def is_full(self):
        return self.num_items == self.max_items
    
    def is_empty(self):
        return self.num_items == 0

    def __str__(self):
        
        table = ""    
        for idx, item in enumerate(self.table):
            if item is not None:
                table += f"{idx} : {item.name}\n"
            else:
                table += f"{idx} : None\n"
        
        return table

if __name__ == "__main__":

    table = HashTable()

    a = ItemType("5") 
    b = ItemType("6") 
    c = ItemType("24")
    d = ItemType("2") 
    e = ItemType("1") 
    f = ItemType("67")
    g = ItemType("3") 
    h = ItemType("4") 

    table.insert_item(a)
    table.insert_item(b)
    table.insert_item(c)
    table.insert_item(d)
    table.insert_item(e)
    table.insert_item(f)
    table.insert_item(g)
    table.insert_item(h)

    print(table)

    print("Delete \"1\"")
    table.delete_item(ItemType("1"))
    print(table)

    print("Delete \"24\"")
    table.delete_item(ItemType("24"))

    print(table)
