"""Create a function that will check a given string to determine if it is palindrome."""

# Test String
s = "cat"
s = "".join([i for i in s if i.isalpha()]).replace(" ", "").lower()


def palindrome(s):
    print(s == s[::-1])
    pass


palindrome(s)
