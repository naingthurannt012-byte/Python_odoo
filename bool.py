# a =  True  #data type is bool
# print(a)
# print(type(a))
# b = False
# print(b)
# print(type(b))


# s = 'vimal'
# print(s[1:10])
# print(s[1:])
# print(s[:3])
# print(s[:])
# print(s*4)
# print(len(s))

# s = 'vijay'
# print(s[0])
# print(s[2])
# print(s[-1])
# print(s[10])

# print(int(12.44))
# print(int(True))
# print(int(False))
# print(int('15'))
# #print(int('15.6)) #invalid literal for int() with base 10: '15.6'

# print(complex(50, -2))
# print(complex(True, False))

print(bool(0))
print(bool(1))
print(bool(15))
print(bool(15.6))
print(bool(0.33))
print(bool(0.0))
print(bool(15-6j))
print(bool(0+2.8j))
print(bool(0+0j))
print(bool('True'))
print(bool('False'))
print(bool(""))

x = 15
y = 15
print(x is y)
print(id(x))
print(id(y))

x1 = [3,6,8,10]
x2 = bytes(x1)
print(type(x2))
print(x2[0])
print(x2[-1])
for i in x2:
    print(i)           


x = [2,4,5,7]
for i in x:
    if i % 2 == 0:
        print(i)
