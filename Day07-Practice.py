#lambda function
numbers: list[int] = [1, 2, 3, 4, 5]
doubled_list: list[int] = list(num*2 for num in numbers)
print(f"Doubled list: {doubled_list}")

#remove element from list
list1: list[int] = [1, 2, 3, 4, 5]
list1.remove(3)
list1 = [num for num in list1 if num != 5]

#matrix transpose
import numpy
matrix: list[list[int]] = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transposed_matrix: list[list[int]] = matrix.T
print(f"Transposed matrix:\n{transposed_matrix}")