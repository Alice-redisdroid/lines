example = 'жирафы едят кости'
print(example[0])
print(example[-1])
length = len(example)
middle = length // 2
if length % 2 == 0:
    print(example[middle-1:])
else:
    print(example[middle:])
print(example[::-1])
print(example[::2])
