'''
    작성일 : 2024년 5월 3일
    작성자 : 학과 학번 이름
    설명 : 시퀀스 자료형    
'''
# 문자열
name = '김지연'  # 문자열을 변수에 저장.

# 리스트
city = ['서울시', 800, '부산시', 400]   # 리스트 생성.

# 튜플
num = (100, 200, 300, 400)  # 튜플 생성.

'''
1. 인덱싱(indexing) : 순차적인 자료구조에 인덱스(첨자) 값을
                     가지고 접근할 수 있는 기능.
    [i]  => i번째 값.
'''
surName = name[0]   # name 문자열에서 첫 번째 문자를 변수에 저장.
print("name[0] : ", surName)

print("city[-2] : ", city[-2])  # 리스트 city에서 마지막에서 두번째 요소 출력

# 리스트의 마지막에서 네 번째 요소의 값을 변경.
city[-4] = '서울특별시'
print("city : ", city)
#print("city[5] : ", city[5])   # 리스트의 6번째 요소 값 출력 -> 오류 발생.
                               # IndexError: list index out of range
                               
'''
2. 슬라이싱(slicing) : 시퀀스 자료형에서 일부를 잘라내어 
                      동일한 자료형으로 반환하는 기능.
[start : stop : step]  => start에서 시작해서 stop 이전까지 step 간격으로 추출
'''
#문자열의 1번지부터 2번지까지 잘라서 변수에 저장.
giveName = name[1:3]
print("name[1:3] : ", giveName) # 성 빼고 이름만 출력

# 리스트의 세 번째 요소부터 끝까지 출력.
print("city[2:] : ", city[2:])

# 튜플의 두 번째 요소부터 세 번째 요소까지 출력.
# num = (100, 200, 300, 400)
print("num[1:3] : ", num[1:3])

# 튜플의 처음부터 끝까지 2씩 증가하면서 슬라이싱
print("num[::2] : ", num[::2])

# 인덱스 범위가 벗어났다.  하지만 가능한 값들만 자동 슬라이싱 한다.
print("num[-10:10] : ", num[-10:10])

'''
3. 연결 : + 연산자를 사용하여 두 개의 자료를 연결한다.
         새로운 시퀀스 자료형을 만든다.
자료형 + 자료형
'''
text1 = 'I Like '
text2 = text1 + 'Python Language'   # 문자열 + 문자열
print("text1 + 문자열 = ", text2)

num1 = (1,2,3,4,5)
num2 = (6,7,8,9)
num = num1 + num2       # 튜플 + 튜플
print("num1 + num2 = ", num)

# city(리스트) + num1(튜플)
#result = city + num1  # 오류 발생. 서로 다른 자료형은 합칠 수 없다.
#print("city + num1 = ", result)

'''
4. 반복 : * 연산자 사용한다.
        시퀀스 자료형을 원하는 만큼 반복시킬 수 있는 기능.
자료형 * 반복횟수
'''
# 튜플 생성.
language = ('C', 'JAVA', 'Python')
# language를 3번 반복하여 변수에 저장.
languages = language * 3
print("languages : ", languages)

feel = 'happy. ' * 10   # 문자열 10번 반복
print("feel : ", feel)

contury = ['대한민국']  * 10
print("contury : ", contury)

'''
5. 멤버 유무 검사 : 시퀀스 자료형에 특정 자료가 있는지 알려주는 기능
자료 in 자료형
'''
color = ['red', 'green', 'blue', 'yellow']
print("리스트에 'black'이 있나요? ", 'black' in color)
print("리스트에 'red'가 있나요? ", 'red' in color)

text3 = 'Python'
print("t가 문자열에 있나요? ", 't' in text3)
print("p가 문자열에 있나요? ", 'p' in text3)
print("P가 문자열에 있나요? ", 'P' in text3)

# in 연산자는 for 반복문에 효율적으로 사용.
for i in text3 :  # text3 안에 있는 문자를 하나씩 i 변수에 넣어서 반복
    print(i)

'''
6. 길이 정보 : 내장함수 len() 함수 사용한다.
              시퀀스 자료형의 길이를 알 수있다.
len(자료형)
'''
# 문자열 text2의 길이
print("text2의 길이 : ", len(text2))   # 22 => 띄어쓰기도 포함.
# 리스트 city의 길이
print("city의 길이 : ", len(city))