'''
    1~100 사이의 10개의 랜덤수로 리스트를 생성합니다.
    리스트에 저장된 수 중에서 홀수만 리스트에 저장합니다.
    랜덤 생성된 리스트와 홀수 리스트는 오름차순으로 정렬하여 출력하시오.
    랜덤수 저장 변수 : num1
    홀수 저장 변수 : num2
    
    [출력 결과]
    10개의 랜덤 수 리스트 : [20, 21, 25, 28, 34, 34, 44, 56, 88, 98]
    홀수 리스트 : [21, 25]
    홀수는 2개 입니다.
'''
import random
num1 = []
num2 = []

for i in range(10) :
    num1.append(random.randint(1,100))

num1.sort()    

print('10개의 랜덤 수 리스트 :', num1)
for i in range(10) :
    if num1[i] % 2 == 1 :
        num2.append(num1[i])
        
num2.sort()
print('홀수 리스트 : ', num2)
print(f"홀수는 {len(num2)}개 입니다.")