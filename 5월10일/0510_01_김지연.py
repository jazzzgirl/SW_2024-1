'''
    작성일 : 2024년 5월 10일
    작성자 : 학과 학번 이름
    설명 : 리스트 => 추가, 삭제, 삽입이 가능한 자료형
'''
# 과일 리스트 생성.
fruits = ['딸기','사과','바나나']
print("과일 목록 : ", fruits)

# 수박 추가 => append()메소드 사용 (마지막에 추가)
fruits.append('수박')
print("과일 목록(수박 추가) : ", fruits)
# 망고 추가
fruits.append('망고')
print("과일 목록(망고 추가) : ", fruits)

# 포도 추가 => + 연산자 사용(연결 연산자)
fruits = fruits + ['포도']   # 포도를 연결하여 fruits에 저장
print("과일 목록(포도 추가) : ", fruits)

# 리스트에서 + 는 연결의 의미이다.
num = [1,2,3] + [4,5,6]
print("숫자 리스트 : ", num)

# * 연산자는 리스트를 n번 반복한다.
num = [1,2,3] * 3
print("숫자 리스트 * 3 : ", num)

# in 연산자는 포함되는가?(안에 있는가?)
print("과일 목록에 '망고'가 있나요? ", '망고' in fruits)

'''
    리스트는 순서가 있다.
    인덱스(주소)를 가지고 있다.
    인덱스를 사용하여 리스트의 항목에 접근 가능하다.
'''
# 과일 리스트에 있는 과일의 개수는? => 리스트의 전체 길이
print("과일 리스트에 있는 과일의 개수는? ", len(fruits), "개")

# 과일 리스트 중에서 제일 첫번째 과일은?
print("과일 리스트 중에서 제일 첫번째 과일은? ", fruits[0])

print("과일 리스트 중에서 제일 마지막 과일은? ", fruits[-1])

fruits.append('두리안')
print("과일 목록 : ", fruits)

print("과일 중 가장 큰 과일은(사전식 순서)? ", max(fruits))

print("과일 중 가장 작은 과일은(사전식 순서)? ", min(fruits))

# 오름차순 정렬
fruits.sort()
print("오름차순 정렬 : ", fruits)
# 내림 차순 정렬
fruits.sort(reverse=True)
print("내림차순 정렬 : ", fruits)


''''
    리스트를 원하는 모양으로자르는 슬라이싱
'''
print("과일 리스트 중 2,3,4번 과일은? ", fruits[1:4])  # 1번지 ~ 4번지 앞까지
print("과일 리스트 중 1~3번 과일은? ", fruits[0:3])
print("과일 리스트 중 1~3번 과일은? ", fruits[:3])   # 처음부터 2번지까지.

print("과일 리스트 중 3번부터 마지막까지 과일은? ", fruits[2:])

print("과일 리스트 중 1,3,5번 과일은? ", fruits[::2])

print("과일을 거꾸로 출력 : ", fruits[::-1])

''''
    리스트의 원소값 조작.
'''
print()
print("과일 목록 : ", fruits)

# 원하는 위치에 '사과' 삽입하기 => insert()메소드
# 3번지에 '사과' 삽입
fruits.insert(3, '사과')
print("과일 목록(3번지에 사과 삽입) : ", fruits)

# 위치 찾기(index) => index()메소드
print("사과의 위치는? ", fruits.index('사과'))

# 개수 => count()메소드
print("사과의 개수는? ", fruits.count('사과'))

'''
    리스트 항목 삭제
'''
print()

# 사과 삭제 => remove()메소드 => 삭제할 항목 지정.
fruits.remove('사과')   # 처음 만나는 사과만 삭제
print("과일 목록(사과 삭제) : ", fruits)

# pop()메소드 => 마지막 항목 삭제
fruits.pop()
print("과일 목록(마지막 항목 삭제) : ", fruits)

# del() 키워드
del fruits[0]  # 번지 지정하여 삭제
print("과일 목록(0번지 삭제) : ", fruits)