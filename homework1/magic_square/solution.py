def magic_square(matrix):
    diag1 = diag2 = 0
    for i in range(len(matrix)):
        diag1 += matrix[i][i]
        rows = columns = 0
        for j in range(len(matrix)):
            rows += matrix[i][j]
            columns += matrix[j][i]
    result = []
    lqlq = (range(len(matrix)))[::-1]
    for i in lqlq:
        result.append(i)
    for i in result:
        diag2 += matrix[i][i]
    return diag1 == diag2 == rows == columns

