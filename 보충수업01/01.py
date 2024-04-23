### 3장

'''
    3분에 2100자를 입력할 수 있는 사람이 
    45분 동안 몇 자를 입력할 수 있는지를 구하는 프로그램을 작성하시오.
'''
# 【코드 1】
typing = 2100 / 3 * 45
print("45분동안 입력할 수 있는 글자 수 : ",typing)
print(f"45분동안 입력할 수 있는 글자 수 : {typing:.0f}자")


'''
    지난 해 남부 대리점의 TV 판매 금액은 3,500,000원이다. 
    판매에서 25%의 이익률이 발생했다면 총 판매 이익금을 구하는 프로그램을 작성하시오.
'''
# 【코드 1】
money = 35000000 * 0.25
print("총 판매 이익금 : ",money)

# 【코드 2】
price = 3500000
profit_ratio = 0.25

total = price * profit_ratio
print(f"총 판매 이익금은 {total:.0f}원 입니다.")


'''
    홍길동의 본봉은 300만원이다. 
    이번 달 수당으로 30만원을 받았으며, 세금으로 총액 20%를 냈다. 
    홍길동이 이번 달 월급으로 수령해 간 수령액을 구하는 프로그램을 작성하시오.
    
    수령액 = 본봉 + 수당 - 세금
    세금 = 총액 * 20%
'''
# 【코드 1】
money = 3000000 + 300000 - ((3000000 + 300000) * 0.2)
print("이번달 수령액 : ", money, "원")


'''
    패밀리 레스토랑에서 저녁 식사 후 음식 요금이 56000원 나왔다. 
    10%의 부가세를 포함한다면 지불해야 할 식사 금액이 얼마인지를 구하는 프로그램을 작성하시오.
    
    지불 식사 금액 = 음식 요금 + ( 음식 요금 * 부가세 )
'''
# 【코드 1】
pay = 56000 + 56000 * 0.1
print("총 식사 금액 : ",pay)

# 【코드 2】
price = 56000
surtax = 0.1
total_price = price + (price * surtax)
print(f"음식요금이 {price}원 10%부가세를 포함한다면 지불해야할 식사 금액은 {total_price}원입니다.")



### 4장
 
'''
    두 개의 숫자를 입력받아 두 숫자 사이의 홀수값을 모두 더하여 출력하는 프로그램을 작성하시오.
'''
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 큰 수와 작은 수를 비교하여 변수에 할당
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

# 홀수값을 더할 변수 초기화
sum_of_odds = 0

# 두 숫자 사이의 홀수값 더하기
for num in range(num1, num2 + 1):
    if num % 2 != 0:
        sum_of_odds += num

# 결과 출력
print(f"{num1}와 {num2} 사이의 홀수값의 합은 {sum_of_odds}입니다.")


'''
    두 개의 숫자를 입력받아 
    두 번째 수가 첫 번째 수의 약수인지 아닌지 구분하는 프로그램을 작성하시오.
'''
# 사용자로부터 숫자 입력 받기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 두 번째 숫자가 첫 번째 숫자의 약수인지 확인
if num1 % num2 == 0:
    print(f"{num2}는 {num1}의 약수입니다.")
else:
    print(f"{num2}는 {num1}의 약수가 아닙니다.")


'''
    두 개의 숫자를 입력 받아 두 개의 수가 모두 짝수이면 두 수를 더한 결과를 출력하고, 
    그렇지 않고 둘 중 하나가 홀수이면 몇 번 째 입력한 수를 짝수로 입력해야 하는지 출력하시오. 
'''
# 사용자로부터 정수 입력 받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 두 정수가 모두 짝수일 때
if (num1 % 2 == 0) and (num2 % 2 == 0):
    print(f"{num1} + {num2} = {num1 + num2}")

elif (num1 % 2 == 1) and (num2 % 2 == 0):   # 첫 번째 정수만 홀수일 때
    print("첫 번째 정수를 짝수로 입력하세요.")

elif (num1 % 2 == 0) and (num2 % 2 == 1):   # 두 번째 정수만 홀수일 때
    print("두 번째 정수를 짝수로 입력하세요.")

else:   # 두 정수가 모두 홀수일 때
    print("두 숫자 모두를 짝수로 입력하세요.")

    
    
### 5장

'''
    10개의 숫자를 입력 받아, 
    0보다 큰 수에 대해서만 전체 합과 평균을 출력하는 프로그램을 
    while문을 사용하여 작성하시오.
    
    【풀이 1】
    (1) 조건 추출 - 10개의 숫자를 입력 (for num in range(10)) 
                  - 0보다 큰 수에 대해서만 합과 평균 출력 (if(num > 0))
    (2) 연계된 논리 결정 - 10개의 숫자를 입력 : 반복논리
                        - 0보다 큰 수에 대해서만 : 선택논리
    (3) 논리구조도- 반복논리 안에 선택논리가 포함되어 있는 구조.
'''
sum = 0

# 10번 반복하는 루프
for num in range(10):
    input_num = int(input("숫자 입력: "))

    # 입력받은 숫자가 양수인 경우에만 합산
    if(input_num > 0):
        sum += input_num

# 전체 합과 평균 계산 후 출력
avg = sum / 10
print("합계:", sum)
print("평균:", avg)


'''
    (1) 조건 추출 - 숫자 입력 반복 : 무한반복 ( while True )
                 - 10개 까지만 숫자 입력 받기 : if ( count >10: break )
                 - 0보다 큰 숫자들의 합계 평균 구하기 : if ( num > 0 )
    (2) 연계된 논리 결정 - 10개의 숫자 입력 : 반복 논리, 조건 논리
                        - 0보다 큰 숫자 구하기 : 조건 논리 
    (3) 논리구조도- 반복 논리 내에 조건 논리 포함 
'''
sum = 0
count = 1

# 무한 반복
while True:
    # 사용자로부터 숫자 입력 받기
    input_num = int(input(str(count) + "번째 숫자를 입력하세요: "))

    # 입력받은 숫자가 양수인 경우에만 합산하고 카운트 증가
    if input_num > 0:
        sum = sum + input_num
        count = count + 1
    
    # 카운트가 10을 초과하면 반복문 종료
    if count > 10:
        break

# 전체 합과 평균 계산 후 출력
avg = sum / (count - 1)
print("전체 합:", sum)
print(f"전체 평균: {avg:.1f}")


'''
    10개의 정수를 입력받아 합을 구하는 프로그램을 파이썬 for와 while문을 사용하여 각각 작성하시오. 
    단, 짝수 번째에 입력되는 숫자는 양수는 음수로 음수는 양수로 바꾸어 합을 구하시오.
'''
sum = 0

# 10번 반복하는 루프
for i in range(1, 11):
    num = int(input(f"{i}번째 숫자를 입력하세요: "))

    # 짝수 번째인 경우 부호 변경하여 합산
    if i % 2 == 0:
        num = num * -1

    sum = sum + num

# 결과 출력
print("합:", sum)

#-----------------------
sum = 0
count = 1

# 10번 반복하는 루프
while count <= 10:
    num = int(input(f"{count}번째 숫자를 입력하세요: "))

    # 짝수 번째인 경우 부호 변경하여 합산
    if count % 2 == 0:
        num = num * -1

    sum = sum + num
    count = count + 1

# 결과 출력
print("합:", sum)


'''
    사용자로부터 가장 좋아하는 월을 입력 받아 
    그 월에 해당되는 계절을 출력하는 프로그램을 메뉴형태로 while 문을 사용하여 작성하시오.
    
    (1) 조건 추출 - 0을 입력받으면 종료 (while (choose != 0))
                 - 12 ~ 2월 : 겨울 (if(choose <= 2 or choose == 12))
                 - 3 ~ 5월 : 봄 (elif(choose <= 5))
                 - 6 ~ 8월 : 여름 elif(choose <= 8)
                 - 9 ~ 11월 : 가을 elif(choose <= 11)
    (2) 연계된 논리 결정 
            - 0을 입력 받을 때 까지 실행 : 반복논리
            - 입력 받은 월에 대한 계절 선택 : 선택논리
    (3) 논리구조도
            - 반복논리 안에 선택논리가 포함된 구조, 선택구조의 순차구조를 이용
'''
while True :
    month = int(input("가장 좋아하는 월은?(종료 : 0) : "))

    if month == 3 or month == 4 or month == 5 :
        print("******", month, "월 *******")
        print(month, "월은 봄에 해당됩니다")        
    elif month == 6 or month == 7 or month == 8 :
        print("******", month, "월 *******")
        print(month, "월은 여름에 해당됩니다")
    elif month == 9 or month == 10 or month == 11 :
        print("******", month, "월 *******")
        print(month, "월은 가을에 해당됩니다")
    elif month == 12 or month == 1 or month == 2 :
        print("******", month, "월 *******")
        print(month, "월은 겨울에 해당됩니다")
    if month == 0 :
        break
    
    
'''
    사용자로부터 하나의 숫자를 입력받아 
    1부터 입력받은 숫자 사이의 소수를 구하여 출력하는 프로그램을 작성하시오.
    
    소수 : 1과 자신의 수 이외에는 나뉘지 않는 수(1 제외)
    
    (1) 조건 추출
        - 1부터 입력받은 수까지 반복 : for i in range(2,num+1)
        - 1부터 입력받은 수까지의 약수를 찾기 위한 반복 : for j in range(1,i+1)
        - 약수를 찾기 위한 선택논리 : if(i % j == 0)
        - 소수를 찾기 위한 선택논리 (약수가 2개인 경우) : if(count == 2)

    (2) 연계된 논리 결정 
        - 1부터 입력받은 수까지 반복 : 반복 논리
        - 1부터 입력받은 수까지의 약수를 찾기 위한 반복 : 반복 논리
        - 약수 찾기 (나누었을 때 나머지가 0인 경우) : 선택 논리
        - 소수 찾기 (약수가 2개인 경우) : 선택 논리
    (3) 논리구조도
        - 반복논리 내에 반복논리가 내포되고, 중첩 반복논리 안에 선택논리가 존재하며, 
          내포된 반복논리가 종료된 시점에 선택논리가 포함 된 구조.

'''
# 사용자로부터 숫자 입력 받기
num = int(input("숫자 입력: "))

# 소수를 판별할 숫자의 범위를 2부터 입력받은 숫자까지로 설정하여 반복
for i in range(2, num + 1):
    count = 0
    
    # 현재 숫자를 1부터 자기 자신까지 나누어 떨어지는지 확인하여 소수인지 판별
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    
    # 약수의 개수가 2개인 경우 소수이므로 출력
    if count == 2:
        print(i)

    
# ----------------------
# 사용자로부터 숫자 입력 받기
num = int(input("숫자를 입력하세요: "))

# 2부터 입력받은 숫자까지 반복하여 소수를 찾음
for i in range(2, num + 1):
    # i가 소수인지 확인하기 위해 2부터 자기 자신까지 반복
    for j in range(2, i + 1):
        # i를 j로 나눴을 때 나머지가 0이면 j는 i의 약수이므로 소수가 아님
        if i % j == 0:
            break
    # 소수인 경우 출력
    if i == j:
        print(i, end=" ")
