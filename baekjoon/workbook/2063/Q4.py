n = int(input())
attends = list(map(int, input().split(" ")))
main_capa, sub_capa = list(map(int, input().split(" ")))

total = 0
for attend in attends:
    capa = attend
    capa -= main_capa
    total += 1
    if capa%sub_capa != 0:
        total += (int(capa/sub_capa) + 1)
    else:
        total += (int(capa/sub_capa))

print(total)

