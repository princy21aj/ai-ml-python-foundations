# finds largest from a list

def largest(value):

    high = 0
    for check in value:
        if check>high:
            high = check
    return high
lst = []
print("if your done entering type 'done'")


while True:
    num = (input("Enter the numbers : "))
    if num=="done":
        break
    lst.append(int(num))
print(f"{lst}")

large = largest(lst)
print(f"the largest number of the number is : {large}")