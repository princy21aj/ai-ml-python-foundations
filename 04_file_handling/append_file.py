
# appends user input to data.txt

line = input("Tell about yourself:")

with open("data.txt","a") as f:
    f.write(f"{line}\n")
