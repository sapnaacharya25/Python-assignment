def count_digit_one(n):
    count = 0
    factor = 1

    while factor <= n:
        divisor = factor * 10
        count += (n // divisor) * factor + min(max(n % divisor - factor + 1, 0), factor)
        factor *= 10

    return count

# Example usage:
n1 = 13
output1 = count_digit_one(n1)
print(output1)

n2 = 0
output2 = count_digit_one(n2)
print(output2)
