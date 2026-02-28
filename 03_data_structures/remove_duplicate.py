# remove duplicate from a list

def remove(value):
    result = []
    for j in value:
        if j not in result:
            result.append(j)
    return result


lst = []
print("If you done entering numbers type 'done'")

while True:
    nums = input("Enter the numbers : ")
    if nums == "done":
        break
    lst.append(int(nums))
print(lst)

duplicate = remove(lst)
print(f"{duplicate}")

