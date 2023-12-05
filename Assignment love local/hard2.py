def shortest_palindrome(s):
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1
    
    if i == len(s):
        return s
    
    suffix = s[i:]
    prefix = suffix[::-1]
    return prefix + shortest_palindrome(s[:i]) + suffix

# Example usage:
s1 = "aacecaaa"
output1 = shortest_palindrome(s1)
print(output1)

s2 = "abcd"
output2 = shortest_palindrome(s2)
print(output2)
