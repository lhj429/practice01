from random import *

while True:
    randomNum = randint(1, 100)
    print("수를 결정하였습니다. 맞추어 보세요")
    print("1-100")

    cnt = 1
    while True:
        n = int(input("{}>".format(cnt)))
        if n > randomNum:
            cnt += 1
            print("더 낮게")
        elif n < randomNum:
            cnt += 1
            print("더 높게")
        else:
            print("맞았습니다.")
            break

    retry = input("다시 하시겠습니까(y/n)>>")
    if (retry == 'y'):
        continue
    else:
        break