try:
    n = int(input("수를 입력하세요:"))
    if n%3==0:
        print("3의 배수 입니다.")
    elif n%3!=0:
        print("3의 배수가 아닙니다.")
except ValueError:
    print("정수가 아닙니다.")