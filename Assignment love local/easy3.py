def generate_pascals_triangle(numRows):
    triangle = []
    
    for i in range(numRows):
        row = [1] * (i + 1)
        
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    return triangle

# Example usage:
numRows1 = 5
output1 = generate_pascals_triangle(numRows1)
print(output1)

numRows2 = 1
output2 = generate_pascals_triangle(numRows2)
print(output2)
