s = 'Hello World!' # string
print(s[0]) # character at index 0 -> H
print(s[2:5]) # substring from index 2 to 4 -> llo
print(s[3:]) # substring from index 3 to the end -> lo World!
print(s*2) # repeating twice -> Hello World!Hello World!
print(s+' Everyone!') # string concatenation -> Hello World!Everyone!
print(s.lower()) # lowercase -> hello world! ( <-> upper() )
print(s.replace('l','s')) # replace character(s) -> Hesso Worsd!
print(len(s)) # length of a string -> 12
print(s.strip()) # remove leading/trailing whitespaces
print(s.split(' ')) # split into substrings list -> ['Hello', 'World!']
