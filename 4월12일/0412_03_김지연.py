'''
    작성일 : 2024년 4월 12일
    작성자 : 학과 학번 이름
    설명 : 단을 입력받아 구구단을 출력하는 프로그램
           반복문 for
'''
dan = int(input("알고 싶은 단 입력 : "))
print(f"= {dan}단 출력 =")

for su in range(1, 10, 1) :
    print(dan, "*", su, "=", (dan*su))