def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x


v = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(v)
print(v)
