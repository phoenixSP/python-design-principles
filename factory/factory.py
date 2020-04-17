# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:51:04 2020

@author: shrey
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:57:36 2020

@author: shrey
"""

from abc import ABCMeta, abstractmethod

#you can also use ABC, the difference is that you can use ABC using simple inheritance while ABCMeta needs to be specified using the metaclass tag
class Pizza(metaclass = ABCMeta):

    def __init__(self):
        pass
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []
     
    def prepare(self):
        print("Preparing " + self.name)
#        print("Preparing ")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        
        for topping in self.toppings:
            print("    " + topping)
            
    def bake(self): 
        print("Bake for 25 minutes at 350")
        
    def cut(self):
        print("Cutting the pizza into diagonal slices")
        
    def box(self):
        print("Place pizza in official PizzaStore box")
        
    def getName(self):
        return self.name
    
class NYCheesePizza(Pizza):
    def __init__(self):
        super().__init__()       #you can skip this part since you are not 
        #reusing any info from the parent class (just dont use append in toppings)
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        
class NYPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Pepperoni Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Sliced Pepperoni")
        
class NYClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Clam Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Fresh Clams")
        
class ChicagoCheesePizza(Pizza):
    def __init__(self):
        super().__init__()        
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Mozzarella Cheese")
        
class ChicagoPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Pepperoni")
        
class ChicagoClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Clam Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Frozen Clams")
        
    
class PizzaStore(metaclass = ABCMeta):
        
    def orderPizza(self, pizza_type):
        
        pizza = self.createPizza(pizza_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    @abstractmethod
    def createPizza(self, pizza_type):
        pass
    
class NYPizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYCheesePizza()
        elif pizza_type == "pepperoni":
            return NYPepperoniPizza()
        elif pizza_type == "clam":
            return NYClamPizza()

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoCheesePizza()
        elif pizza_type == "pepperoni":
            return ChicagoPepperoniPizza()
        elif pizza_type == "clam":
            return ChicagoClamPizza()       

    
    

if __name__ == '__main__':
    ny_pizza = NYPizzaStore()
    chicago_pizza = ChicagoPizzaStore()
    
    pizza_type = input("Enter the type of pizza you want:")
    ny_pizza.orderPizza(pizza_type)
    
    pizza_type = input("Enter the type of pizza you want:")
    chicago_pizza.orderPizza(pizza_type)
    
      
    

    