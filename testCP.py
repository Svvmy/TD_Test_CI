import unittest
from CartePizzeria import CartePizzeria
from mock import Mock

class Test_CartePizzeria(unittest.TestCase):
    def setUp(self):
        pizza = Mock()
        self.empty_pizza = CartePizzeria()
        self.not_empty_pizza = CartePizzeria()
        self.not_empty_pizza.pizzas = [pizza]
        
    def test_add_pizza(self):
        pizza = Mock()
        self.empty_pizza.add_pizza(pizza)
        self.assertEqual(self.empty_pizza.pizzas, [pizza])
        
    def test_nb_pizzas_on_empty(self):
        assert self.empty_pizza.nb_pizzas() == 0
        

if __name__ == "__main__":
    unittest.main()