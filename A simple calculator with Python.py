
def calculate(option):
    result = eval(option)
    print(result)

    continuee = input("if you continue calculate[Y|N]: ")
    if continuee.capitalize() == "Y":
        again(result)
    else:
        quit()
    
def again(result):
    number = float(input("Enter the Number: "))

    action = input("Enter the Action [+|-|*|/]: ")

    result = f"{result} {action} {number}"
    calculate(result)


number1 = float(input("Enter the First Number: "))

action = input("Enter the Action [+|-|*|/]: ")

number2 = float(input("Enter the Second Number: "))

if type(number1) == float and type(number2) == float:
    if action == "+" or action == "-" or action == "*" or action == "/":
        calculation = f"{number1} {action} {number2}"
        calculate(calculation)
    else:
        print("please enter [+|-|*|/]!")
else:
    print("please enter the number!")
        


