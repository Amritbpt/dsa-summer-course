def row_sums(matrix):
    sums = []

    for row in matrix:
        total = 0
        for n in row:
            total += n
        sums.append(total)

    return sums


matrix = [
    [1, 2, 9],
    [4, 5, 6],
    [7, 8, 3]
]

print(row_sums(matrix))
for column in matrix:
    column.sort()
print(matrix)