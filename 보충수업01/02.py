'''
1.정수를 입력받아 정사각형의 넓이를 계산하여 출력하는 프로그램을 작성하시오.
'''
length = int(input("정사각형의 한 변의 길이를 입력하세요: "))
area = length ** 2
print("정사각형의 넓이는", area, "입니다.")


'''
2. 사용자로부터 시작 값과 끝 값을 입력 받아 두 수 사이의 전체 합계와 짝수의 합계, 홀수의 합계를 출력하시오.
'''
start = int(input("시작 값 입력: "))
end = int(input("끝 값 입력: "))

total_sum = 0
even_sum = 0
odd_sum = 0

for num in range(start, end + 1):
    total_sum += num
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("두 수 사이의 전체 합계:", total_sum)
print("짝수의 합계:", even_sum)
print("홀수의 합계:", odd_sum)


start = int(input("시작 값 입력: "))
end = int(input("끝 값 입력: "))

if start > end:
    start, end = end, start

total_sum = 0
even_sum = 0
odd_sum = 0

for num in range(start, end + 1):
    total_sum += num
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("두 수 사이의 전체 합계:", total_sum)
print("짝수의 합계:", even_sum)
print("홀수의 합계:", odd_sum)


'''
3. 두 개의 정수를 입력 받아 첫 번째 정수가 두 번째 정수의 배수이면 
   “00은 00의 배수이다.”를 출력하고, 
   아니면 “00은 00의 배수가 아니다.”를 출력하는 프로그램을 작성 하시오. 
   (단, 두 번째 숫자가 0인 경우에는 “0으로 나눌 수 없음”을 출력)
'''
'''
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

if num2 == 0:
    print("0으로 나눌 수 없음")
else:
    if num1 % num2 == 0:
        print("{}은(는) {}의 배수이다.".format(num1, num2))
    else:
        print("{}은(는) {}의 배수가 아니다.".format(num1, num2))
'''

'''
4. 커피 자판기
'''
'''
print("주문을 시작합니다.")
print("1. 아이스 아메리카노 - 1,500원")
print("2. 카페 라떼 - 2,500원")
print("3. 레몬 에이드 - 2,000원")
print("0. 주문 종료")

total_price = 0

while True:       
    choice = int(input("주문할 음료의 번호를 입력하세요 (0 입력 시 주문 종료): "))
    if choice == 0:
        print("주문이 종료되었습니다.")
        break
    else:
        cup = int(input("주문할 잔 수를 입력하세요: "))
        if choice == 1:
            total_price += 1500 * cup
        elif choice == 2:
            total_price += 2500 * cup
        elif choice == 3:
            total_price += 2000 * cup

if total_price == 0 :
    print("감사합니다.")
else :        
    print("총 주문 금액은 {}원 입니다.".format(total_price))

    pay = int(input("지불할 금액을 입력하세요: "))
    change = pay - total_price
    print("거스름돈은 {}원 입니다.".format(change))
'''

'''
while True:
    print("주문을 시작합니다.")
    print("1. 아이스 아메리카노 - 1,500원")
    print("2. 카페 라떼 - 2,500원")
    print("3. 레몬 에이드 - 2,000원")
    print("0. 주문 종료")
    
    total_price = 0
    
    while True:
        choice = int(input("주문할 음료의 번호를 입력하세요 (0 입력 시 주문 종료): "))
        if choice == 0:
            break
        elif choice < 0 or choice > 3:
            print("올바른 번호를 입력하세요.")
            continue
        else:
            cup = int(input("주문할 잔 수를 입력하세요: "))
            if choice == 1:
                total_price += 1500 * cup
            elif choice == 2:
                total_price += 2500 * cup
            elif choice == 3:
                total_price += 2000 * cup
    
    if total_price == 0:
        print("주문이 종료되었습니다.")
        break
    
    print("총 주문 금액은 {}원 입니다.".format(total_price))
    
    while True:
        pay = int(input("지불할 금액을 입력하세요: "))
        if pay < total_price:
            print("금액이 부족합니다. 다시 입력해주세요.")
        else:
            change = pay - total_price
            print("거스름돈은 {}원 입니다.".format(change))
            break
'''