'''
    작성일 : 2024년 3월 28일
    작성자 : 학과 학번 이름
    설명 : 정수를 입력받아 양수인지 음수인지 판단하시오.
            
    [문제분석]
        필요한 변수는 무엇? num
    
        양수는 0보다 큰 수
        음수는 0보다 작은 수
        정수를 입력 받는다.
        입력 받은 정수가 0보다 큰가요?
        (입력받은 정수가 양수인가요?)
        
        입력 받은 정수가 0보다 작은가요?
        (입력받은 정수가 음수인가요?)
        
        입력 받은 정수가 양수이면 "00은 양수입니다."
        입력 받은 정수가 음수이면 "00은 음수입니다."
        
    [알고리즘]
        1. 정수를 입력 받는다.
        2. 만약에 정수가 0보다 크면 (양수인가?)
            2-1. "00은 양수입니다."
        3. 아니면
            3-1. "00은 음수입니다."
        4. "감사합니다." 출력한다. 
              => 조건과 상관없이 무조건 출력
'''
# 1. 정수를 입력 받는다.
num = int(input("정수 입력 : "))

# 2. 만약에 정수가 0보다 크면 (양수인가?)
if num > 0 :
    print(f"{num}은 양수입니다.")
    
# 3. 아니면 => else 에는 조건식을 작성하지 않는다.
else :
    print(f"{num}은 음수입니다.")
 
# 3. "프로그램 종료" 출력
print("프로그램 종료")