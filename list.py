# new_list=[]
# for i in range(1,10):
#     new_list.append(i)
# print(new_list)
# b = new_list
# b.insert(6,23)
# print(b)

# a = ['hi','hello',1,'ratnakumar','monika','vuchilli',65,89]
# b = a[::-1]
# print(b)

# li = []
# for i in range(1,10):
#     li.append(i)
# li.append("hey")
# li.append([x*2 for x in range(1,10)])
# print(li)
# print(len(li))


# li = [1,2,3,4]
# li.append(89)
# li.extend(['hey'])
# li.remove(li[1])
# li.pop()
# print(li)
# clear(li)

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

b = [2,4,6]
def sq(s):
    return s*2
a = list(map(sq,b))
print(a)

