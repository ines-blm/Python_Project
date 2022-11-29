#this program make a simple calculator using function

n1 = int(input("enter the firstnumber:\n"))
n2 = int(input('enter the secondnumber:\n'))

print("select operation. \n 1 for add \n 2 for subtract \n 3 for multiply \n 4 for divide")

def add(n1, n2):
   return (n1+n2)

def substract(n1, n2):
   return (n1-n2)

def multiply(n1, n2):
   return (n1*n2)

def divede(n1, n2):
   return (n1/n2)

while True:
    #take input from the user
    Choice = input("enter Choice(1\2\3\4):")
    #check if choice is one of the four option
    if Choice in ('1', '2', '3', '4'): 
        n1 = int(input("enter the firstnumber:\n"))
        n2 = int(input('enter the secondnumber:\n'))
        
        if Choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))

        elif Choice == '2':
           print(n1, "_", n2, "=", substract(n1, n2)) 

        elif Choice == '3':
           print(n1, "*", n2, "=", multiply(n1, n2))

        elif Choice == '4':    
           print(n1, "/", n2, "=", divede(n1, n2))

        #if user wants another calculator
        #break the while loop if answer is no
        next_calculator = input("let's do next calculation? (yes/no):") 
        if next_calculator == "no":
         break
    else:
       print("Invalid Input")  








      
       


      

    
    