def create_matrix():
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

    return matrix


def print_matrix(matrix):
    print("\nYour matrix is:")
    for row in matrix:
        print(row)


def sum_below_main_diagonal(matrix):
    total = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if row > col:
                total += matrix[row][col]

    return total