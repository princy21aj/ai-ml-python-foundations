
#stores student name in data.txt

name = input("Enter your Name:")

with open("data.txt","w") as f:
    f.write(f"{name}")

print(f"Hello {name},your name has been saved\n")


