

list1 = [1, 2.2, '3', (1, 2, 3), 5, 1, 3]
print(list1)

unique = set(list1)

print(type(unique))
print(unique)

list2 = list(set(list1))
print(type(list2))
print(list2)

my_tuple = (1, 2, 3, 4, 5, 6)

dictionary = {'one': 1, 'two': 2}
print(dictionary['one'])

print(list1[3])

my_list = []
my_list2 = list()
my_string = "Any string value"
my_list3 = list(my_string)
print(type(my_list3))
print(my_list3)

s = [sym for sym in range(5)]
print(s)

lst = []
for i in range(5):
    lst.append(i)

print(lst)

lst1 = [0, 1, 2, 3, 4, 5]
lst2 = []

print(lst1)
print(lst2)

for el in lst1:
    x = lst1.pop(0)
    lst2.append(x)

print(lst1)
print(lst2)

lst3 = [2, 3, 4]
print(lst3)

lst3.remove(3)

print(lst3)

lst4 = [1, 2, 3, 4, 'str', [1, 2, 3]]
print(lst4.index('str'))

lst5 = [1, 2, 5, 3, 4, 1, 2]
print(lst5.count(0))
print(lst5)
lst5.sort()
print(lst5)

print(reversed(sorted(lst5)))


my_word = "ibdjewbkdj"
x = list(reversed(sorted(my_word)))
y = ''.join(list(reversed(sorted(my_word))))
print(y)

g = [1, 2, 3]
f = g.copy()
f[0] = 5

print(g)
print(f)

lst11 = [1, 2, 3]
lst12 = lst11.copy()

print(lst11)
print(lst12)

lst13 = [[[1, 1], [2, 2]], [3, 4], [5, 6]]
lst14 = lst13.copy()
print(lst14)

#SET
string = 'djxklsnmjdwiq'
x11 = {1, 2, 3}
y11 = set(string)

print(y11)

a = {}
print(type(a))
a['one'] = 1
print(a)


lst22 = [1, 2, 3, 4, 5]
lst23 = [5, 4, 5, 2, 1]

print(set(lst22) == set(lst23))
print(len(set(lst22)))


lst33 = [1, 2, 3, 4]
print(5 in lst33)

s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 0}
s3 = s1.copy()


print(s1.isdisjoint(s2))
print(s1 == s3)
print(s1.union(s2))
print(s1.difference(s2))
s1.remove(5)
print(s1)
s1.discard(6)
print(s1)
s1.clear()
print(s1)


s22 = frozenset(s2)
print(s22)

#dictionary

a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

dc = {'one': 1, 'two': 2, 'three': 3}
print(dc.values())
print(dc.keys())
print(dc.items())

for pair in dc.items():
    print(pair)

for key, value in dc.items():
    dc[key] = value + 1

print(dc)

d1 = dict()
print(d1)

keys = ['one', 'two', 'three']
values = [1, 2, 3]

x33 = dict(zip(keys, values))
print(x33)

x33['four'] = 4
print(x33)

y33 = x33.pop('three')
print(x33)
print(y33)

another_dict = {'five': 5, 'six': 6}
x33.update(another_dict)
print(x33)

for i in range(10):
    print(i)


words = ['one', 'two', 'three']
for word in words:
    print(word)