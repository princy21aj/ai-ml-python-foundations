# function to check if a number is prime  

def primecheck(num):
    if num < 2:
        return "Not a prime number"
    for i in range(2,num):
        if num % i == 0:
            return "it is not a prime number"
    return "it is a prime number"
        
        

value = int(input("Enter the value : "))
check = primecheck(value)
print(check)
    