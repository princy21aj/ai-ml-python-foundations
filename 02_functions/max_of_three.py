# max of the three numbers

def maxofthree(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z 

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c : "))

largest = maxofthree(a,b,c)

print(f"The largest Number of the Given numbers is : {largest}")



    