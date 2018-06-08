data = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]

cnt = 0
total = 0

for i in data:
    if i%3==0:
        cnt += 1
        total += i

print("주어진 리스트에서 3의 배수의 개수=>", cnt)
print("주어진 리스트에서 3의 배수의 합=>", total)