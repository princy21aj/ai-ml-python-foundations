
# reads marks and calculate student averages

try:
    with open("marks.txt","r") as f:
        data = f.readlines()

    for i in data:
        i = i.strip()
        parts = i.split(",")
        name = parts[0]
        marks = parts[1:]
        try:
            total = 0
            for mark in marks:
                total = total + int(mark)
            avg = total / len(marks)
            print(f"{name}:average={avg:.2f}")
        except ValueError:
            print(f"Skipping {name} - bad data")

except FileNotFoundError:
    print("Error:marks.txt not found")