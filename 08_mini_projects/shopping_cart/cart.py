# shopping cart

product_item_name=(input("Enter the item u bought:"))
price=int(input("Enter the price of the item:"))
quantity=int(input("Enter the quantity of the item:"))

total=price*quantity

print(f"You like to have {product_item_name}")
print(f"this is the price of this item ${price}")
print(f"You ordered {quantity} x {product_item_name}")
print(f"your total price is {total}")
