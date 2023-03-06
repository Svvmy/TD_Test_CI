class CartePizzeria:
    
    def __init__(self):
        
        self.pizzas = []
         
    def is_empty(self):
            if(len(self.pizzas) == 0):
                print("la liste de pizza est vide")
                return True
            return False
        
    def nb_pizzas(self):
            #print("nb pizza")
            #print(len(self.pizzas))
            return len(self.pizzas)
        
    def add_pizza(self, pizza):
            #print("add pizza")
            self.pizzas.append(pizza)
            
    def remove_pizza(self, name):
        print("remove pizza")
        for pizza in self.pizzas:
            if (pizza == name):
                self.pizzas.remove(pizza)
            return
        raise Exception(f"La Pizza n'existe pas dans la carte.")




    
    

    
        