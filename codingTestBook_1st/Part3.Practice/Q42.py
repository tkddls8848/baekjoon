'''
4
3
4
1
1

4
6
2
2
3
3
4
4

'''
gate_num = int(input())
plane_num = int(input())
plane_gate = []
gate_occupy = [False]* (gate_num+1)
for i in range(plane_num):
    plane_gate.append(int(input()))
count = 0
for i in range(len(plane_gate)):
    flag = False
    for j in range(plane_gate[i]):
        a = plane_gate[i]-j
        if not gate_occupy[a]:
            gate_occupy[a] = True
            flag = True
            break
    if flag:
        count += 1
        print(count)
    else:
        break


print(gate_occupy)







