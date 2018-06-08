n = int(input("금액: "))

money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
money_dict = {}

for i in money_list:
    cnt = n //i
    money_dict[i] = cnt
    n -= i*cnt

for key, value in money_dict.items():
    print("{}원 : {}개".format(key, value))