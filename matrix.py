j = int(input("Enter number of rows (j): "))
i = int(input("Enter number of columns (i): "))

matrix = []

print("\nEnter the elements row by row:")
for row in range(j):
    current_row = []
    for col in range(i):
        value = int(input(f"Enter value for position [{row}][{col}]: "))
        current_row.append(value)
    matrix.append(current_row)

print("\nYour matrix is:")
for row in matrix:
    print(row)
