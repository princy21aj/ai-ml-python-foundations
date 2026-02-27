# calculator - basic operations
# functions : add,subtract,multiply,divide

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

addition = add(num1,num2)
subtraction = sub(num1,num2)
multiplication = mul(num1,num2)
division  = div(num1,num2)

print(f"The addition of {num1} and {num2} is {addition} ")
print(f"The subtraction of {num1} and {num2} is {subtraction} ")
print(f"The Multiplication of {num1} and {num2} is {multiplication} ")
print(f"The Division of {num1} and {num2} is {division:.2f} ")

