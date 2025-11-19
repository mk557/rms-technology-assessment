import numpy as np

def count_combinations(grid, n):
    # Calculates possible runs horizontally, vertically, and diagonally in the grid
    rows, cols = grid.shape
    total = 0
    total += (cols - n + 1) * rows      # Horizontal
    total += (rows - n + 1) * cols      # Vertical
    total += (rows - n + 1) * (cols - n + 1) * 2  # Both diagonals
    return total

def greatest_product_of_contiguous_integers(grid, n):
    # Finds the highest product of n consecutive numbers
    rows, cols = grid.shape
    max_found = 0
    for i in range(rows):
        for j in range(cols):
            # Check right
            if j + n <= cols:
                prod = np.prod(grid[i, j:j+n])
                max_found = max(prod, max_found)
            # Check down
            if i + n <= rows:
                prod = np.prod(grid[i:i+n, j])
                max_found = max(prod, max_found)
            # Check Down-right diagonal
            if i + n <= rows and j + n <= cols:
                prod = np.prod([grid[i+k, j+k] for k in range(n)])
                max_found = max(prod, max_found)
            # Check Up-right diagonal
            if i - n + 1 >= 0 and j + n <= cols:
                prod = np.prod([grid[i-k, j+k] for k in range(n)])
                max_found = max(prod, max_found)
    return max_found


if __name__ == "__main__":
    # Grid 10x10 example
    grid = [
        [8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45],
    ]
    grid = np.array(grid)
    
    # function which accepts a grid of size n x m and finds the greatest product of x adjacent numbers in the same direction. 
    n = 3
    combo_count = count_combinations(grid, n)
    max_prod = greatest_product_of_contiguous_integers(grid, n)

    print(f"Combinations of 3 adjacent numbers: {combo_count}")
    print(f"Greatest product of 3 adjacent numbers: {max_prod}")
