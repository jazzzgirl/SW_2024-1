'''
    작성일 : 2024년 5월 2일
    작성자 : 학과 학번 이름
    설명 : 4. 커피 자판기.
    
    [문제분석]
        0을 입력하기 전까지는 주문을 할 수 있다.
        1. 아메이카노를 선택하면 수량을 입력할 수 있다.
        아메리카노 1500원 * 수량 계산.
        각 메뉴에 대한 총 가격을 계산한다.
        
        계속 메뉴를 선택 할 수 있다.
        0을 입력하면
        총 금액을 알려준다.
        지불할 금액을 입력 받아 거스름돈을 알려준다.
        
    [알고리즘]
        1. 메뉴 보여주기
        2. 총 금액 변수 초기화.
        3. 계속 반복하면서
            3-1. 주문할 음료 번호를 입력 받는다.
            3-2. 0이 입력되면
                3-2-1. 주문을 종료한다. break
            3-3. 아니면
                3-3-1. 주문할 잔 수를 입력 받는다.
                3-3-2. 만약 1번 아메리카노이면
                    3-3-2-1. 총 금액 = 1500 * 잔 수 계산한다.
                3-3-3. 아니고 만약 2번 카페라떼이면
                    3-3-3-1. 총 금액 = 2500 * 잔 수
                3-3-4. 아니고 만약 3번 레몬에이드이면
                    3-3-4-1. 총 금액 = 2000 * 잔 수
        4. 만약에 총 금액이 0이면
            4-1. 감사합니다.
        5. 아니면
            5-1. 총 금액 출력한다.
            5-2. 지불할 금액 입력 받는다.
            5-3. 거스름돈 계산.
            5-4. 거스름돈 알려준다.(출력한다.)
'''
# 위 알고리즘에 대한 코드
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
    
    
#----------------------------------------------------
# 주문을 무한반복한다.  0을 입력하기 전까지
while True:
    print("주문을 시작합니다.")
    print("1. 아이스 아메리카노 - 1,500원")
    print("2. 카페 라떼 - 2,500원")
    print("3. 레몬 에이드 - 2,000원")
    print("0. 주문 종료")
    
    total_price = 0 # 총 금액 초기화
    
    # 음로 주문을 반복한다.
    while True:
        choice = int(input("주문할 음료의 번호를 입력하세요 (0 입력 시 주문 종료): "))
        if choice == 0:     # 주문 번호가 0이면 음료주 문을 종료한다.
            break
        elif choice < 0 or choice > 3:  # 잘못 된 주문 번호 입력하면
            print("올바른 번호를 입력하세요.")
            continue    # 음료 주문 처음으로 돌아간다.
        else:
            cup = int(input("주문할 잔 수를 입력하세요: "))
            if choice == 1:     # 아메이카노
                total_price += 1500 * cup
            elif choice == 2:   # 카페라떼
                total_price += 2500 * cup
            elif choice == 3:   # 레몬에이드
                total_price += 2000 * cup
    
    if total_price == 0:    # 메뉴에서 0을 입력 했을 때는 주문 금액이 없다.
        print("주문이 종료되었습니다.")
        break   # 프로그램을 완전히 종료한다.
    
    print("총 주문 금액은 {}원 입니다.".format(total_price))
    
    # 지불할 금액이 부족할 경우를 대비하여 
    # 계속 반복하면서 지불 할 금액을 입력 받는다.
    while True:     
        pay = int(input("지불할 금액을 입력하세요: "))
        if pay < total_price:   # 금액이 부족 할 경우
            print("금액이 부족합니다. 다시 입력해주세요.")
        else:   # 금액이 충분 할 경우
            change = pay - total_price  # 거스름돈 계산
            print("거스름돈은 {}원 입니다.".format(change))
            break   # 금액 입력 반복을 종료.
