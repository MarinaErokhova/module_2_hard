# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911

import random
random_number = random.randint(3, 20)
print(random_number)
password = []
divider = []
for i in range(3, random_number + 1): #делители рандомного числа
    if random_number % i == 0:
        divider.append(i)
print(divider)

for j in range(1, random_number):
    for k in divider:
        if j < k // 2 + 1 and j != k - j:
            password += f'{j}{k-j}'


print(*password)