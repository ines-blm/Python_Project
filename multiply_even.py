#this program multiply_even using except.
num_list =[]
list_lenght = 4
for num in range(list_lenght):
    num = int(input("Enter an number:"))
     
    num_list.append(num)

def multiply_even_fct(number):
    total = 1
    try:
        for num in num_list:
            if num % 2 == 0:
                total = total * num
    except TypeError:
       return('please enter even number') 
      
    return total

total  = multiply_even_fct(num_list)
print(f"The total is : {total}")

