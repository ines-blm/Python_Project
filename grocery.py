# this program display total price of item in the receipt.

order = {"tomato":30, "thyme":4.5, "garlic":7.5, "rice":10, "onions":4, "fish":9.99}
def grocery_cart_total(price):
    total = 0
    for item in order:
        total+= order[item]
    print(f"the grocery cart total is:{total}")
grocery_cart_total(order)