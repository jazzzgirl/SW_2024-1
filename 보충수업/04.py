'''
    함수는 튜플을 돌려줄 수 있다.
'''
import math # 파이값 가져오기.

# 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수 (area, circum)
def calCircle(r):    
    area = math.pi * r * r       # 넓이 계산
    circum = 2 * math.pi * r     # 둘레 계산
    return (area, circum)        # 넓이와 둘레의 값을 튜플로 반환 함
    
radius = float(input("원의 반지름을 입력하시오: ")) 
(area, circum) = calCircle(radius) 

print(f"반지름이 {radius}인 원의 넓이는 {area:.2f}이고, 원의 둘레는 {circum:.2f}이다.")