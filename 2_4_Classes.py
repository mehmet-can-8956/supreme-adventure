amount=int(input("Enter the amount please:"))

class item:
    def __init__(self, itemName, price):
        self.itemName = itemName
        self.price = price

class customer:
    def __init__(self, customer_id, phone_number):
        self.customer_id = customer_id
        self.phone_number = phone_number        

    def purchase(self, amount, price):
        print("Total Price:", amount * price)

first_item=item('apple',5)
first_customer=customer('123','5551234')
first_customer.purchase(amount, first_item.price)