import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    if y == 0:
        return "Syntax Error"
    return x / y


def main():
    
    while True:
        print("MENU:")
        print("ADD")
        print("SUBTRACT")
        print("MULTIPLY")
        print("DIVIDE")
        print("EXIT")
        menu = int(input("Enter your choice (1-5): "))
        
        if menu == 5:
            print("Exiting the program, GOODBYE!")
            break
    
    
        elif menu == 1:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result: ", add(x, y))
    
        elif menu == 2:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result: ", subtract(x, y))
            
        elif menu == 3:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result: ", multiply(x, y))
            
        elif menu == 4:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result: ",divide(x, y))
    
        else:
            print("Invalid input!")
       
if __name__ == "__main__":
    main()













