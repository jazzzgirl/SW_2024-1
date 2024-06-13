'''
    여러 개의 값을 넘겨주고 여러 개의 값을 돌려받자.
    두 수를 전달하여 사칙연산의 결과 값을 돌려준다..
'''
print(":: 사칙연산 결과 출력 ::") 

# 함수 선언
def calc1(n1, n2):
    sum = n1 + n2
    minus = n1 - n2
    mul = n1 * n2
    div = n1 / n2
    rest = n1 % n2    
    return sum, minus, mul, div, rest     # 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지 결과를 반환

num1 = int(input("첫 번째 수 입력 : "))
num2 = int(input("두 번째 수 입력 : "))

# 네 개의 값을 반환받기 위해 4개의 변수를 사용함
sum, minus, mul, div, rest = calc1(num1, num2)    

print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}")
print(f"{num1} x {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {rest}")
