class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color 
    
    def transform_name_for_sku(self):
        return self.name.upper()
    
    def transform_color_for_sku(self):
        return self.color.upper()
    
    def generate_sku(self):
        """
        Generates a SKU for this product.
        
        Example:
        >>> small_black_shoes = Product('shoes', 'S', 'black')
        >>> small_black_shoes.generate_sku()
        'SHOES-S-BLACK'
        """
        name = self.transform_name_for_sku()
        color = self.transform_color_for_sku()
        return f'{name}-{self.size}-{color}'

# test = Product('Dean', 'medium', 'white')
# print(test.generate_sku())