#list data type
L1 = [1,2,3,4,5]
print(type(L1))



My_list = []
print(type(My_list),'List is')
print('Before',My_list)
My_list.append(1)
print('After is',My_list)
My_list.append(2)  #ထပ်ထည်တာ
print(My_list)

l2 = list(range(0,8,2)) # range (start,stop-1,jump)
print(l2,'This is l2 list')
print(l2[1])  #index output

str1 = 'Naing'
print(str1[2])

num = [10,20,30,40,50,60,70,80,90,100]
print(num[2:6:2])
print(num[5::2])
print(num[3:7])
print(num[9:2:-1])

s1 = [1,2,3,4]  # pop
# print(s1.pop(1))

# print('after pop')
# print(s1)

# s1.append(2)
s2 = s1.reverse()
print(s2)

l2 =[1,2,3,4,5,6]
for i in l2:
    if i >= 2:
        print(i)


# tuple
t1 = (1,2,3)
print(type(t1))  
#print(t1.insert(5))
# list mu
# #data type change 
l1 = list(t1)
print(l1)
print(type(l1))
print(l1.append(6))
print(l1)
t1 = tuple(l1)
print(t1)


#set data type   ထပ်ထည်.လို့ရ
s = {1,2,3,4,5,4}
print(type(s))
print(s)
s.add(7)
print(s)
# without duplicate

#dictionary

my_dict = {
    "brand" : 'Ford',
    'model': '2024'
}
print(my_dict)
my_dict['colour'] = 'Yellow'
print(my_dict)
del my_dict["colour"]
print(my_dict)