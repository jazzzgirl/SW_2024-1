'''
    작성일 : 2024년 4월 12일
    작성자 : 학과 학번 이름
    설명 : 단을 입력받아 구구단을 출력하는 프로그램
    
    [문제분석]
        사용자로부터 단을 입력받는다. => 정수
        단은 고정이다.
        곱하는 수는 1부터 9까지 1씩 증가한다.
        곱하는 결과는 단 * 수 이다.
        해당 구구단은 곱하기 하면서 바로바로 출력된다.
            => 합계처럼 한번에 결과가 출력되면 안된다.
            => 구구단 과정이 하나씩 출력되어야 한다.
                3 * 1 = 3
                3 * 2 = 6
                 :
                3 * 9 = 27
    
    [알고리즘]
        1. 단을 입력 받는다.
        2. 곱하는 수는 1부터 (초기값)
        3. 곱하는 수는 9까지 반복하면서 (조건식)
            3-1. 구구단을 출력한다.   3 * 1 = 3
            3-2. 곱하는 수는 1씩 증가한다. (증감식)
'''
dan = int(input("알고 싶은 단 입력 : "))
print(f"= {dan}단 출력 =")

su = 1  # 초기값
while su <= 9 :  # 조건식    
    print(dan, "*", su, "=", (dan*su))
    #print(f"{dan} * {su-1} = {dan*(su-1)}")
    su = su + 1   # 증감식  
    
    