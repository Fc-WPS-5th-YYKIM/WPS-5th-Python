import random

li = [ x for x in range(1,10)]
random.shuffle(li)

print(li)

li_index = len(li) - 1

for i in range(li_index):
    for j in range(li_index - i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]


print(li)