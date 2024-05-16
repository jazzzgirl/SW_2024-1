'''
    작성일 : 2024년 5월 16일
    작성자 : 학과 학번 이름
    설명 : 로또번호 만들기
    
    1 ~ 45 사이의 6개 번호
    로또 번호를 생성하고, 오름차순으로 정렬하시오.
'''
import random

print("로또 번호 생성")
lotto = list()  # 빈 리스트 생성.

i = 0   # 랜덤 수 발생 횟수 저장.
while True :  # 무한 반복
    lotto.append(random.randint(1, 45))   # 랜덤 수 생성하여 리스트에 추가
    i = i + 1
    if len(lotto) == 6 :   # 랜덤 수가 6개가 되면
        break              # 반복을 종료한다.
    
print("이번 주 로또번호 : ", sorted(lotto))


print("세트로 생성")
lotto = set()   # 빈 세트 생성.

i = 0
while True :
    lotto.add(random.randint(1, 45))   # 랜덤 수를 세트에 추가
    i = i + 1
    if len(lotto) == 6 :
        break

print("이번 주 로또번호 : ", sorted(lotto))