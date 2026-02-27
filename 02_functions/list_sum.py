# function to calculate sum of a list

def list_sum(value):

    sum = 0
    for i in value:
        sum+=i
    return sum

# function to calculate average of a list

def list_avg(value):
    avg = list_sum(value)/len(value)
    return avg


print("Enter numbers one by one.if you done,type 'done'.")

numbers = []
while True:
    num =input("Enter the value : ")
    if num == "done":
        break
    numbers.append(int(num))

sum = list_sum(numbers)
avg = list_avg(numbers)

print(f"The Given numbers are {numbers}")
print(f"The sum of the given numbers is : {sum}")
print(f"The average of the given number is : {avg:.2f}")

