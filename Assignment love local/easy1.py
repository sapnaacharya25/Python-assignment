def length_of_last_word(s):
  
    s = s.strip()
    
 
    last_word = s.split()[-1]
    return len(last_word)

# Example usage:
print(length_of_last_word("Hello World"))  # Output: 5
print(length_of_last_word("   fly me   to   the moon  "))  # Output: 4
print(length_of_last_word("luffy is still joyboy"))  # Output: 6
