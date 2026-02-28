# student average program

def avg(mark):
    sum = 0
    for i in mark:
        sum+=i
    avg = sum/len(mark)
    return avg


scores = []

while True:
    marks = input("Enter your mark : ")
    if marks == "done":
        break
    scores.append(int(marks))


average = avg(scores)
print(f"The Average of the Marks is {average}")