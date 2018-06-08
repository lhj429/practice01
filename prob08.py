list = []
total = 0

for i in range(0, 5):
    n = int(input("> "))
    list.append(n)
    total += n

print("평균: {}".format(total/5))