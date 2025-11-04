from Matrix_Body import create_matrix, print_matrix, sum_below_main_diagonal 
matrix = create_matrix()
print_matrix(matrix)

sum_below = sum_below_main_diagonal(matrix)
print(f"\nSum of elements below the main diagonal: {sum_below}")
