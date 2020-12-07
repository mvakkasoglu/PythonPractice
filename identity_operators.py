# Identity operators are used to compare the objects, not if they are equal, but if they are actually the
# same object, with the same memory location:
x = 1
y = 1
if x is y:  # same object
    print("same object")
else:
    print("not same object")

x = ["apple", "banana", "cherry"]

y = ["apple", "banana", "cherry"]

print(x is y)  # false
print(x == y)  # true

print(x[1] is y[1])  #true
print(x[1] == y[1])  #true
