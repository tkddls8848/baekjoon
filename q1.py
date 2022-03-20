char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
question = ['b','w','z','z','h','','','','','','','','','','','']
arr = []
for q in question:
    if q == '':
        continue
    arr.append(char.index(q))

for i in range(0, 26):
    for a in range(len(arr)):
        arr[a] += 1
        if arr[a] > 25:
            arr[a] -= 26
    for p in arr:
        print(char[p], end='')
    print()
