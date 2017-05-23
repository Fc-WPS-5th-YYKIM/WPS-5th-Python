import random

li = [ x for x in range(1,10) ]

random.shuffle(li)

print(li)


def bubble_sort(x):
    length = len(x)-1

    for i in range(length):
        for j in range(length-1):
            if x[i] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]


#selection(li)


def selection1(x):
    length = len(x)

    for i in range(length):
        change_index = i

        for j in range(i + 1, length):
            if x[change_index] > x[j]:
                change_index = j

        x[i], x[change_index] = x[change_index], x[i]

print('--------------------')
selection1(li)
print(li)