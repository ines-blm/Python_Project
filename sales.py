
order = {"tomato":30, "thyme":4.5, "garlic":7.5, "rice":10, "onions":4, "fish":9.99}
def grocery_cart_total(price):
    try:
        total = 0
        for item in order:
          total+= order[item] 
         
    except Exception as error:
       return("Item not in the list")
    return total
        
total_cart = grocery_cart_total(order)
       
print(f"the grocery cart total is:{total_cart}")