for i in range(1, 100):
    a = str(i).count('3')
    b = str(i).count('6')
    c = str(i).count('9')
    if a+b+c>0:
        print("{} {}".format(i, "짝"*(a+b+c)))