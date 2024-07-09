
import math

def sqrt(num1):
    x=math.sqrt(num1)
    print("The sqrt is: ", x)
    return x

def div(numerator, denominator):
    q= (numerator / denominator)
    print("The answer is: ", q)
    return q

def mul(val1, val2):
    P= (val1 * val2)
    print("The answer is: ", P)
    return P

def run():
    print("Welcome to Aneesh Kannans super duper maybe not super duper calculator")
    print("This calculator does square root (press1) , division (press 2), and multiplication(press 3).")
    a = float(input("What do you want to find out?"))

    if a == 1:
        print('ok let us do sq root')
        num1=int(input('Enter the number to find the sqrt!: '))
        sqrt(num1)

    elif a==2:
        print('ok let us do division')
        numerator = int(input('Enter the numerator!: '))
        denominator = int(input('Enter the denominator!: '))
        div(numerator,denominator)

    elif a == 3:
        print('ok let us do multiplication')
        num_to_multiply = input("please give us a list of numbers that you want to multiply( Please seperate with commas ) : ")
        num_to_multiply = num_to_multiply.split(',')
        print("Let us solve this for you!")
        print("You have...")
        product=1
        for element in num_to_multiply:
            product=int(element)*product
        print(f"The product of multiplying these numbers {num_to_multiply} is..{product}")

run()

yes_no=input("Would you like to do more calculations?Y/N: ")
if yes_no =='Y':
    print("OK")
    run()

elif yes_no == 'N':
    print("OK, Thanks for using our calculator! =D")

else:
    print("Are you ok silly? That was not an option!!! Now hand over thy service to the EMPIRE! ")
    print("Your shuttle will be arriving for pick up, good bye now! MWHAHAHAAHHA!")
