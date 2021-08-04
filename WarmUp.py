#This is practice



colors = ['red', 'green', 'blue']
print(colors)

print(colors[2])

colors[0] = 'pink'

print(colors)

del colors[2]

print(colors)

colors.append('purple')

print(colors)

colors.insert(0, 'yellow')

print(colors)

#New Warm Up

a = [3, 10, -1]

print(a)
a.append(1)
print(a)

a.append([1, 2])
print(a)

# pop deletes the last item on list EX:
a.pop()

print(a)

print(a[0])

a[0] = '1milly'

print(a)

# temp allows you to switch the values inside a variable EX:
b = ["banana", "apple", "microsoft"]

temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

# To swap back

b[0], b[2] = b[2], b[0]
print(b)



#Warmup 3




a = [1, 3, 5, 7, 9, 11]
# [2, 6, 10, 14, 18, 22]

c = []
for x in a:
	c.append(x * 2)
	print(c)
d = [x * 4 for x in a]
print(d)

e1 = []
for x in range(1, 7):
	e1.append(x ** 2)
print(e1)


box1 = ['chips', 'candy', 'soda', 'bacon', 'egg', 'cheese']
#         0         1        2        3       4       5

print(box1)

temp = box1[0]
box1[0] = box1[5]
box1[5] = temp

print(box1)

box1.append('sausage')

print(box1)

box1.insert(0, 'phone')
print(box1)

del box1[4]

print(box1)

box1.pop()
print(box1)