# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:57:36 2020

@author: shrey
"""

from abc import ABCMeta, abstractmethod

#you can also use ABC, the difference is that you can use ABC using simple inheritance while ABCMeta needs to be specified using the metaclass tag
class Pizza(metaclass = ABCMeta):
    
    def __init__(self):
        self.name = None
#        self.dough = None
#        self.sauce = None
#        self.toppings = []
        
    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
#        print("Adding toppings:")
#        
#        for topping in toppings;:
#            print("    " + topping)
            
    def bake(self): 
        print("Bake for 25 minutes at 350")
        
    def cut(self):
        print("Cutting the pizza into diagonal slices")
        
    def box(self):
        print("Place pizza in official PizzaStore box")
        
    def getName(self):
        return self.name
    
class CheesePizza(Pizza):
    def __init__(self):
        self.name = "Cheese Pizza"
        
class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni Pizza"
        
class ClamPizza(Pizza):
    def __init__(self):
        self.name = "Clam Pizza"
    
class SimplePizzaFactory:
    
    
    def createPizza(self, pizza_type):
        #in case of smaller names, you can always use eval(object_type)() to get the specific class 
        
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        elif pizza_type == "clam":
            return ClamPizza()
        
    
class PizzaStore:
    
    def __init__(self, factory):
        self.factory = factory
        
    def orderPizza(self, pizza_type):
        
        pizza = self.factory.createPizza(pizza_type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

if __name__ == '__main__':
    pf = SimplePizzaFactory()
    pizza_type = input("Enter the type of pizza you want:")
    PizzaStore(pf).orderPizza(pizza_type)
    