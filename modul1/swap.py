#varianta 1
x = 9
y = 7
a = x
x = y
y = a
print(x, y)
#varianta 2
x, y = y, x
print (x, y)
#varianta 3
x = x + y
y = x - y
x = x - y
print(x, y)



