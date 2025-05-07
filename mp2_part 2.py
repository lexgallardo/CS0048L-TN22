import math

def to_fahrenheit(x):
    return (9/5 * x) + 32

def to_celcius(x):
    return (x - 32) * 5/9


def main():
    
    while True:
        print("MENU:")
        print("Convert Celsius to Fahrenheit")
        print("Convert Fahrenheit to Celsius")
        print("EXIT")
        menu = int(input("Enter your choice (1-3): "))
        
        if menu == 3:
            print("Exiting the program, GOODBYE!")
            break
    
    
        elif menu == 1:
            x = float(input("Enter temperature in Celsius: "))
            print("Result: ", to_fahrenheit(x))
    
        elif menu == 2:
            x = float(input("Enter temperature in Fahrenheit: "))
            print("Result: ", to_celcius(x))
            
        else:
            print("Invalid input!")
       
if __name__ == "__main__":
    main()













