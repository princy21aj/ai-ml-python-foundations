
# read and display the user data

try:
    with open("data.txt","r") as f:
        data = f.read()
        print(f"{data}\n")

except FileNotFoundError:
    print("the file was not found")
