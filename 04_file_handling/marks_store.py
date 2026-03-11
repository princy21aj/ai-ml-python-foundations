# store students name and marks to file

name = input("Enter your name:")
mark1 = int(input("Enter your mark1:"))
mark2 = int(input("enter your mark2:"))
mark3 = int(input("Enter your mark3:"))
marks = (f"{mark1},{mark2},{mark3}")


with open("marks.txt","w") as f:
    f.write(f"{name},{marks}\n")
    

print("marks saved successfully!")
