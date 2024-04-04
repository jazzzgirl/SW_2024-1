'''
    작성일 : 2024년 3월 22일
    작성자 : 학과 학번 이름
    설명 : 5과목의 점수를 입력받아 
           합계와 평균을 출력하는 프로그램을 작성하시오.
            
    [문제분석]
        총점 = 5과목의 합
        평균 = 합계 / 5 
        과목 5개 점수를 입력 받는다.
        점수는 정수로 입력 받는다.
        필요한 변수 : kor, eng, math, com, sci, total, avg
    
    [알고리즘]
        1. 5과목의 점수를 입력받는다.
        2. 합계를 계산한다.
        3. 평균을 계산한다.
        4. 합계와 평균을 출력한다. 
'''

# 1. 5과목 점수 입력받아 정수로 변환하여 변수에 저장.
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
com = int(input("컴퓨터 점수 입력 : "))
sci = int(input("과학 점수 입력 : "))

# 2. 합계 계산
total = kor + eng + math + com + sci

# 3. 평균 계산
avg = total / 5

# 4. 합계와 평균 출력
print("국어 점수 : ", kor)
print("영어 점수 : ", eng)
print("수학 점수 : ", math)
print("컴퓨터 점수 : ", com)
print("과학 점수 : ", sci)

print("5과목의 총점 : ", total)

print("5과목의 평균 : ", avg)
print("5과목의 평균 : {:.2f}" .format(avg))
print(f"5과목의 평균 : {avg:.2f}")
