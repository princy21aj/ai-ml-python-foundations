# 1) for loop
for i in range(1, 11):
    print(i)

# 2) while loop
count = 5
while count > 0:
    print(count)
    count -= 1

# 3) range() usage
for i in range(0, 11, 2):
    print(i)

# 4) break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 5) continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 6) Sum of numbers
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)

# 7) Multiplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
