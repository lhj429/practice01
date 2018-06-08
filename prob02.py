try:
    n = int(input("수를 입력하세요:"))
    if n%2==0:
        print("짝수")
    else:
        print("홀수")
except ValueError:
    print("정수가 아닙니다.")