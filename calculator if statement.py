
#   An example of using if-statement
def calculator():


    #input the 1st number, 2nd number, and the opreation
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    op = input("Enter what opreation do you want to do: ")
    #If-statement example
    if op == "+":
        return(num1 + num3)
    elif op == "-":
        return(num1 - num2)
    elif op == "/":
        return(num1 / num3)
    elif op == "*":
        return(num1 * num2)
    else:
        print("You entered an invlid value!")
