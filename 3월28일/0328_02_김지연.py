'''
    작성일 : 2024년 3월 28일
    작성자 : 학과 학번 이름
    설명 : 점수를 입력받아 80점 이상이면 
            "합격입니다."를 출력하고,
            아니면 "불합격입니다."를
            출력하는 프로그램을 작성하시오.
            
    [문제분석]
        필요한 변수는 무엇? 점수 저장 변수 : score / jumsu
        점수는 80점 이상이어야 한다.
        
        입력 받은 점수가 80점 이상인가?
        아닌가?
        
        80점 이상이면 "합격" 출력한다.
        아니면 "불합격" 출력한다.
        
        점수를 입력 받는다. -> 정수로 변환 -> 변수에 저장.
    
    [알고리즘]
        1. 점수를 입력받는다.
        2. 점수가 80점 이상이면
            2-1. "합격입니다."
        3. 아니면
            3-1. "불합격입니다."
        4. "감사합니다." 출력한다. 
              => 조건과 상관없이 무조건 출력
'''
score = int(input("점수를 입력하시오 : "))

if score >= 80 :
    print("합격입니다.")
else :
    print("불합격입니다.")

print("감사합니다.")

# num을 2로 나눈 나머지가 0이다.
num % 2 == 0

# num을 2로 나눈 나머지가 0이 아니다.
num % 2 != 0

# num을 2로 나눈 나머지가 1이다.
num % 2 == 1