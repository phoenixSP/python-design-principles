# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:23:04 2020

@author: shrey
"""

from abc import ABCMeta, abstractmethod

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
    
    def __init__(self):
    
        self.ingredient_factory = NYPizzaIngredientFactory()
    
    def createPizza(self, pizza_type):
        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.setName("NY Cheese Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.setName("NY Pepperoni Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(self.ingredient_factory)
            pizza.setName("NY Clam Pizza")
            
        return pizza
    
class ChicagoPizzaStore(PizzaStore):
    
    def __init__(self):
        #why instance creation cant happen outside init
    
        self.ingredient_factory = ChicagoPizzaIngredientFactory()
    
    def createPizza(self, pizza_type):
        if pizza_type == "cheese":
            pizza = CheesePizza(self.ingredient_factory)
            pizza.setName("Chicago Cheese Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(self.ingredient_factory)
            pizza.setName("Chicago Pepperoni Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(self.ingredient_factory)
            pizza.setName("Chicago Clam Pizza")
            
        return pizza
    
    
class PizzaIngredientFactory(metaclass = ABCMeta):
    
    @abstractmethod
    def createDough(self):
        pass
    
    @abstractmethod
    def createSauce(self):
        pass
    
    @abstractmethod
    def createCheese(self):
        pass
    
    @abstractmethod
    def createClam(self):
        pass
    
    @abstractmethod
    def createPepperoni(self):
        pass
    
    
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    
    def createDough(self):
        return "ThinCrustDough"
    
    def createSauce(self):
        return "MarinaraSauce"
    
    def createCheese(self):
        return "ReggianoCheese"
    
    def createClam(self):
        return "FreshClams"
    
    def createPepperoni(self):
        return "SlicedPepperoni"
    

    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    
    def createDough(self):
        return "ThickCrustDough"
    
    def createSauce(self):
        return "PlumTomatoSauce"
    
    def createCheese(self):
        return "MozzarellaCheese"
    
    def createClam(self):
        return "FrozenClams"
    
    def createPepperoni(self):
        return "SlicedPepperoni"
    

class Pizza(metaclass = ABCMeta):

    def __init__(self):

        self.name = None 
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.pepperoni = None
        self.clam = None
        
    @abstractmethod 
    def prepare(self):
        pass
            
    def bake(self): 
        print("Bake for 25 minutes at 350")
        
    def cut(self):
        print("Cutting the pizza into diagonal slices")
        
    def box(self):
        print("Place pizza in official PizzaStore box")
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
class CheesePizza(Pizza):
    
    def __init__(self, pizza_ingredient_factory):
        super().__init__()
        self.ingredient_factory = pizza_ingredient_factory
        
    def prepare(self):
        print("Preparing", self.name) #check this part
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createCheese()
        
class ClamPizza(Pizza):
    def __init__(self, pizza_ingredient_factory):
        super().__init__()
        self.ingredient_factory = pizza_ingredient_factory
        
    def prepare(self):
        print("Preparing", self.name) #check this part
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createClam()
     
        
class PepperoniPizza(Pizza):
    def __init__(self, pizza_ingredient_factory):
        super().__init__()
        self.ingredient_factory = pizza_ingredient_factory
        
    def prepare(self):
        print("Preparing", self.name) #check this part
        self.dough = self.ingredient_factory.createDough()
        self.sauce = self.ingredient_factory.createSauce()
        self.cheese = self.ingredient_factory.createPepperoni()
        


if __name__ == '__main__':
    ny_pizza = NYPizzaStore()
    chicago_pizza = ChicagoPizzaStore()
    
    pizza_type = input("Enter the type of pizza you want:")
    ny_pizza.orderPizza(pizza_type)
    
    pizza_type = input("Enter the type of pizza you want:")
    chicago_pizza.orderPizza(pizza_type)
        

    
    
    
    
    

