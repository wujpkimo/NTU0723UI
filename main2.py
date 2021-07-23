x = 5
print("x=", x, "x id=", hex(id(x)))
x = 6
print("x=", x, "x id=", hex(id(x)))
l1 = [5]
print("l1=", l1, "l1 id=", hex(id(l1)))
print("l1=[0] id=", hex(id(l1[0])))
l1[0] = 6
print("l1=", l1, "l1 id=", hex(id(l1)))
print("l1=[0] id=", hex(id(l1[0])))
print(x == l1[0], x is l1[0])