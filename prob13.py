n = int(input("숫자를 입력하세요: "))

if n%2==0:
    startNum = 2
else:
    startNum = 1

total = 0
for i in range(startNum, n+1, 2):
    total += i

print("결과 값 : {}".format(total))