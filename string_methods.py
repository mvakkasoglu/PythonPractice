string = "Hello World!"

print(string.isalnum())
print(string.isalpha())
print(string.startswith("H"))
print(string.rfind("d"))
print(string.find("d"))
print(string, 2) # Hello World! 2


# isalnum()
# isalpha()
# isdigit()
# islower()
# isupper()
# isspace()
# endswith(s)
# startswith(s)
# count(s)
# find(s)
# rfind(s)
# capitalize()
# lower()
# upper()
# title()
# swapcase()
# replace(old,new)
# strip()
# split(',')
# Returns True if the string is alphanumeric. if there is space it will return false.
# Returns True if the string contains only alphabets. if there is space it will return false.
# Returns True if the string contains only digits.
# Returns True if the string is in lowercase.
# Returns True if the string is in uppercase.
# Returns True if the string contains only whitespace.
# Returns True if the string ends with substring s.
# Returns True if the string starts with substring s.
# Returns number of occurrences of substring s in the string.
# Returns lowest index from where s starts in the string, if not found returns -1.
# Returns the string with only the first character capitalized.
# Returns the string by converting every character to lowercase.
# Returns the string by converting every character to uppercase.
# Returns the string by capitalizing first letter of every word in the string.
# Removes whitespace
# splits by commas into a list
