def celsius(temp):
    return (temp-32)*5/9 

def fahrenheat(temp):
    return (temp*9/5)+32 

print("Temperature converter")
print("choose 1 : to covert celsius to fahrenheat")
print("choose 2 : to convert fahrenheat to celsius")


choice = int(input("Enter your choice :"))
value = int(input("Enter the value : "))

if choice == 1:
    celsius = celsius(value)
    print(f"Result : {celsius:.2f} ")
elif choice == 2:
    fahrenheat = fahrenheat(value)
    print(f"Result : {fahrenheat:.2f} ")
else :
    print("Invalid value")
