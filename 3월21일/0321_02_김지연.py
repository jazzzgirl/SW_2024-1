'''
    작성일 : 2024년 3월 21일
    작성자 : 학과 학번 이름
    설명 : 밑변 12, 높이 23인 삼각형의 넓이를 계산하는
            프로그램을 작성하시오.
            
    [문제분석]
        삼각형의 넓이 = (밑변 * 높이) / 2
        밑변 = 12
        높이 = 23
        
        필요한 변수 => bottom(밑변), height(높이), area(넓이)
    
    [알고리즘]
        1. 밑변 변수에 값을 지정한다.  12
        2. 높이 변수에 값을 지정한다.  23
        3. 삼각형의 넓이를 계산한다.
        4. 삼각형의 넓이를 출력한다.
'''
# 1. 밑변 변수에 12를 저장한다.
bottom = 13
# 2. 높이 변수에 23을 저장한다.
height = 23

# 3. 넓이를 계산하여 변수(area)에 저장한다.
area = (bottom * height) / 2

# 4. 넓이를 출력한다.
# 밑변 12, 높이 23인 삼각형의 넓이는 00입니다.
print("밑변", bottom, "높이", height, "인 삼각형의 넓이는 ", area, "입니다.")

print("밑변 {}, 높이 {}인 삼각형의 넓이는 {:.2f}입니다." .format(bottom, height, area))

print(f"밑변 {bottom}, 높이 {height}인 삼각형의 넓이는 {area:.0f} 입니다.")