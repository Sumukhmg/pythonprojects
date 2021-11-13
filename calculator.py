def addition(a,b):
    print("Addition of",a ,b,"is",a+b)

def subtraction(num1,num2):
    print("subtraction of ",a ,b,"is",a-b)

def multiplication(num1,num2):
    print("multiplication of",a ,b,"is",a*b)

def division(num1,num2):
    print("division of",a ,b,"is",a/b)

def remainder(num1,num2):
    print("remainder of",a ,b,"is",a%b)

def quotient(num1,num2):
    print("quotient of",a ,b,"is",a//b)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division") 
    print("5. remainder") 
    print("6. quotient")    
    print("7. Exit")
    choice=int(input("Enter your choice(1-7):"))

    if choice==1:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        addition(a,b)


    elif choice==2:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        subtraction(a,b)
    
    elif choice==3:
        a=int(input("Enter First Number:"))
        b=int(input("Enter SecondNumber:"))
        multiplication(a,b)
    
    elif choice==4:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        if b == 0:
            print('Infinity')
        else:
            division(a,b)

    elif choice==5:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        remainder(a,b)

    elif choice==6:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        quotient(a,b)

    elif choice==7:
        break
      
    else:
        print("Wrong Choice")

