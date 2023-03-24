class Cart():
    def __init__(self):
        self.cart = dict()
        self.welcome()
        self.commands()
        return
    
    def welcome(self):
        txt = "..................\n" + \
              "Welcome to TyMart!\n" + \
              "..................\n"
        print(txt)
        return
    
    def commands(self):
        """
        Prints a list of valid methods.
        """
        print("Here is the list of valid methods")
        print()
        print(".show()")
        print("Shows you your current shopping cart")
        print()
        print(".add(item:str,quantity:int)")
        print("Add item(s) to cart")
        print()
        print(".subtract(item:str,quantity:int)")
        print("Subtract item(s) from cart")
        print()
        print(".clear()")
        print("Empties cart")
        print()
        print(".commands()")
        print(" Lists the methods you can run")
        print()

    def show(self):
        """
        Method to show the current contents of the cart
        """
        if not self.cart:
            print("You don't have anything in your cart\n")
            return
        
        longest_item = max(max(len(key) for key in self.cart),4)
        # Demos format of how cart will be printed
        print(f"{'Item'.ljust(longest_item,' ')} --- Quantity in cart")
        print()

        for item,quantity in self.cart.items():
            print(f"{item.ljust(longest_item,' ')} --- {quantity}")
        print()
        return
    
    def add(self,item:str,quantity:int):
        """
        Method to add items to cart. "item" is the item to add. "quantity"
        is the amount to add. "quantity must be a non-negative integer"
        """
        
        if not item:
            print("Item can't be empty string, add unsuccessful\n")
            return
        
        if not isinstance(item,str):
            print("Must be a str, add unsuccessful\n")
            return

        item = item.strip().lower()
        
        if not isinstance(quantity,int) or isinstance(quantity,bool):
            print("Quantity must be non-negative integer, add unsuccessful\n")
            return
        
        if quantity < 0:
            print("Quantity must be non-negative integer, add unsuccessful\n")
            return

        self.cart[item] = self.cart.get(item,0) + quantity
        if self.cart[item] == 0:
            del self.cart[item]
        
        print(f"Succefully added:\n {item} ---- {quantity}\n")
        return
    
    def subtract(self,item:str,quantity:int):
        """
        Method to subtract items from cart. "item" is the item to subtract. 
        "quantity" is the amount to subtract. "quantity must be a non-negative integer"
        """

        if not self.cart:
            print("There is nothing in your cart to subtract!\n")

        if not isinstance(item,str):
            print("Must be a str, subtract unsuccessful\n")
            return
        
        item = item.strip().lower()

        if not item:
            print("Item can't be empty string, subtract unsuccessful")
            print("Call show() method to see what is in your cart\n")
            return
        
        if item not in self.cart:
            print("This item isn't in cart, you can't remove it")
            print("Call show() method to see what is in your cart\n")
            return
        
        if not isinstance(quantity,int) or isinstance(quantity,bool):
            print("Quantity must be non-negative integer, subtract unsuccessful\n")
            return
        
        if quantity < 0:
            print("Quantity must be non-negative integer, subtract unsuccessful\n")
            return
        
        if quantity > self.cart[item]:
            print("You are trying to subtract more than you have in your cart")
            print(f"You currently only have {self.cart[item]} item(s)")
            return
        
        if quantity == self.cart[item]:
            del self.cart[item]
        else:
            self.cart[item] -= quantity
        print(f"Succefully removed:\n {item} ---- {quantity}\n")
        return

    def clear(self):
        self.cart.clear()
        print("All items have been removed from the cart")
        return