def calculator(num1,num2,operator):
    if operator == '+':
        result = num1 + num2
        return result
    elif operator == '-':
        result = num1 - num2
        return result
    elif operator == '*':
        result = num1 * num2
        return result
    elif operator == '/':
        result = num1 / num2
        return result
    else :
        print("Wrong Operator")

num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
operator = input("Select the operator '+','-','*','/':")

print(calculator(num1,num2,operator))
