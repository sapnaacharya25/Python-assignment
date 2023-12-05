def maximalSquare(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side

# Example usage:
matrix1 = [["0"]]
output1 = maximalSquare(matrix1)
print(output1)

matrix2 = [["0", "1"], ["1", "0"]]
output2 = maximalSquare(matrix2)
print(output2)
