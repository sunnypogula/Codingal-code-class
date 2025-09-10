lst = ['apple','guava','mango','banana','kiwi']

print("length of list:",len(lst))
print("First element:",lst[0])
print("last element:",lst[-1])

lst.append('papaya')
print("updated list:",lst)

lst.remove('guava')
print("updated list:",lst)

lst.sort()
print("sorted list:",lst)

lst.pop(1)
print("updated list:",lst)

lst.reverse()
print("reversed list:",lst)

lst = lst*2
print("multiplication on list:",lst)

lst = lst[2:5]
print("sliced list:",lst)

lst.clear
print("updated list:",lst)