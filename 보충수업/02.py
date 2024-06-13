'''
    함수에 여러 개의 값을 넘겨주는 고급 기능
    두 수를 입력받아 함수를 호출한다.
    전달받은 두 수 사이의 합을 계산하여 결과를 돌려준다.
'''
print(":: 매개변수가 2개인 함수(두 수 사이의 합 구하기) ::")

# 함수 선언
def get_sum(start, end):     # start, end를 매개변수로하여 인자를 받는다
    sum = 0
    for i in range(start, end + 1):     # start부터 end까지 정수의 합을 구함
        sum += i
    return sum     # start부터 end까지 수의 합을 반환한다

start = int(input("시작 수 입력 : "))
end = int(input("종료 수 입력 : "))
result = get_sum(start, end)

# result에 저장된 값 출력
print(f"{start}부터 {end}까지의 합은 {result}입니다.") 
# 두 값을 가지고 함수 호출하여 돌려받은 값을 바로 출력
print(f"{start}부터 {end}까지의 합은 {get_sum(start, end)}입니다.")
