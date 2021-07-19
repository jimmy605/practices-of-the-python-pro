import unittest

from collections import defaultdict
from product import Product


class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))
    
    def add_product(self, product, quantity=1):
        self.products[product.generate_sku()]['quantity'] += quantity
    
    def remove_product(self, product, quantity=1):
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] == 0:
            del self.products[sku]

class ShoppingCartTestCase(unittest.TestCase):
    def test_cart_initially_empty(self):
        cart = ShoppingCart()
        self.assertDictEqual({}, cart.products)
    
    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')
        
        cart.add_product(product)
        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 1}}, cart.products)
    
    def test_add_two_of_a_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')
        cart.add_product(product, quantity=2)
        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 2}}, cart.products)
    
    def test_add_two_different_products(self):
        cart = ShoppingCart()
        product_one = Product('shoes', 'S', 'blue')
        product_two = Product('shirt', 'M', 'gray')
        
        cart.add_product(product_one)
        cart.add_product(product_two)
        
        self.assertDictEqual({
            'SHOES-S-BLUE': {'quantity': 1},
            'SHIRT-M-GRAY': {'quantity': 1}
        }, cart.products)
    
    def test_remove_too_many_products(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')
        
        cart.add_product(product)
        cart.remove_product(product, quantity=2)
        
        self.assertDictEqual({}, cart.products)
    
    # def test_add_and_remove_product(self):
    #     cart = ShoppingCart()
    #     product = Product('shoes', 'S', 'blue')
        
    #     cart.add_product(product)
    #     cart.remove_product(product)
        
    #     self.assertDictEqual({}, cart.products)
