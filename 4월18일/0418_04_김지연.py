'''
    작성일 : 2024년 4월 18일
    작성자 : 학과 학번 이름
    설명 : 두 수를 입력받아 두 수 사이의 모든 수의 합을 계산하시오.
            입력받은 두 수를 포함하여 계산합니다.
    
    [문제분석]
        두 수를 입력 받는다.
        첫번째 수가 1이고, 두번째 수가 10이면 1부터 10까지의 합을 계산.
        만약에 사용자가
        첫번째 수가 10이고, 두번째 수가 1이면 
            두 수를 교환한다.
                
        sum = sum + num
        
        반복의 조건 : 두번째 수까지        
        
        첫번째 수 > 두번째 수
            두 값을 교환한다.
                
    [알고리즘]
        1. 두 수를 입력 받는다.
        2. sum = 0 초기화
        3. num1 > num2
            3-1. 두 값을 교환한다.
        4. 첫번째 수부터 두번째 수까지 1씩 증가하면서
            4-1. 합계를 계산한다.
        5. 합계를 출력한다.
'''
num1 = int(input("첫번째 수 입력 : "))
num2 = int(input("두번째 수 입력 : "))

sum = 0  # 합계 계산을 위해 반드시 sum에 초기값 지정해야 함.

if num1 > num2 :   # 두 값을 교환한다.
    temp = num1
    num1 = num2
    num2 = temp

# 작은 수부터 큰 수까지 1씩 증가하면서 반복한다.
for num in range(num1, num2+1, 1) :
    sum = sum + num

print(f"{num1}부터 {num2}까지 합은 {sum}입니다.")