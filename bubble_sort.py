def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

v = [54,26,93,17,77,31,44,55,20]
bubble_sort(v)
print(v)