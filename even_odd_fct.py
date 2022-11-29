# even and odd number using function
number1 = int(input("enter your number:\n"))

def even_odd_fct(number):
    if number % 2 == 0: 
        print(f'{number} is even')

    else: 
        print(f'{number} is odd')

even_odd_fct(number1)

