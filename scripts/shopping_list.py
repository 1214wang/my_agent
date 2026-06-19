class ShoppingList:
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list

    def get_item_count(self):
        return len(self.shopping_list)

    def get_total_price(self):
        price =0
        for i in self.shopping_list:
            price+=self.shopping_list[i]
        return price
    
# s=ShoppingList({'milk':10,'bread':20,'rice':30})
# print(s.get_item_count())
# print(s.get_total_price())
