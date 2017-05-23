li = [5,1,3,7,2,9]

i = 0

for x in range(len(li)):

    for y in range(len(li)):
        print(li[i])
        if x < li[i]:
            li[i] = x
        i += 1


print(li)
