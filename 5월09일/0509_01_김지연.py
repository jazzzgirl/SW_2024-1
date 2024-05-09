'''
    작성일 : 2024년 5월 9일
    작성자 : 학과 학번 이름
    설명 : 시퀀스 자료형 - 문자열
'''
# 문자열 생성.
text1 = '안녕하세요.'

# 빈 문자열 생성.
text2 = ''
text3 = str()   # str()함수를 사용하여 빈 문자열 생성.

text4 = "오늘은 '목요일'입니다."
print(text4)

'''
    str()함수를 사용하여 다른 자료형(숫자, 리스트, 튜플)을 
    문자열로 변환하여 새로운 문자열 생성.
'''
# 정수를 문자열로 생성.
text5 = str(12345)
print("text5 = ", text5)
print("text5의 자료형 : ", type(text5))

# 리스트[]를 문자열로 생성.
text6 = str([1,2,3])    # 리스트 자체를 문자열로 인식한다.
print("text6 = ", text6)
print("text6의 자료형 : ", type(text6))

print("text6[0] = ", text6[0])  # 결과 [
    
# 튜플()을 문자열로 생성.
text7 = str((1,2,3))    # 튜플 자체를 문자열로 인식
print("text7 = ", text7)

# text7에서 문자열의 세 번째 문자 출력 (1,2,3)
print("text7[2] = ", text7[2])  # 결과 ,

'''
    대소문자 변환.
'''
text8 = 'i like python language'
print(text8)

print("첫 문자만 대문자로 변환 : ", text8.capitalize())
print("모든 단어의 첫 문자를 대문자로 변환 : ", text8.title())

text9 = text8.upper()  # 모두 대문자로 변환.
print("모두 대문자로 변환 : ", text9)

text10 = text9.lower()  # 모두 소문자로 변환.
print("모두 소문자로 변환 : ", text10)

'''
    문자열 찾기
'''
print(text10)
print("문자열에 'a'가 몇 개 있나요? ", text10.count('a'))
print("문자열 인덱스 0번지부터 12번지 사이에 'a'가 몇 개? ", text10.count('a', 0, 12))
print("문자열 인덱스 12번지 이후에 'a'가 몇 개? ", text10.count('a', 12))

print("문자열 내의 'l'의 인덱스(위치)는? ", text10.index('l'))
print("문자열 내의 'l'의 인덱스(위치)는? ", text10.find('l'))

print("문자열 내의 'l'을 오른쪽부터 검색하면? ", text10.rindex('l'))
print("문자열 내의 'l'을 오른쪽부터 검색하면? ", text10.rfind('l'))

print("문자열 내의 'python'의 위치는? ", text10.index('python'))

# 대문자 Python이 없으므로 오류 발생.
#print("문자열 내의 'Python'의 위치는? ", text10.index('Python'))

# find 사용하면 문자열이 없으면 -1을 출력한다.
print("문자열 내의 'Python'의 위치는? ", text10.find('Python'))

print("문장이 'i like'로 시작하는가? ", text10.startswith('i like'))
print("문장이 'title'로 끝나는가? ", text10.endswith('title'))

'''
    문자열 결합
'''
# 문자열 리스트 생성.
list1 = ['1', '2', '3', '4']
print("list1 = ", list1)

# 리스트에 있는 문자열을 '-'와 결합
join1 = '-'.join(list1)
print("'-'와 결합 : ", join1)

# 정수 리스트 생성.
list2 = [1, 2, 3, 4]
print("list2 = ", list2)

# 리스트에 있는 정수를 '-'와 결합
# join이 되는 대상은 반드시 문자열이어야 한다.
# 정수와 문자열의 결합은 오류가 발생한다.
# join2 = '-'.join(list2)
# print("'-'와 결합 : ", join2)

'''
    문자열 분리
'''
text10 = 'i like python language'
print("text10 = ", text10)

# 문자열을 스페이스로 구분하여 리스트로 반환.
list3 = text10.split()  # 스페이스로 구분
print("문자열 분리(스페이스로 분리) : ", list3)

text11 = 'i-like-python-language'
print("text11 = ", text11)

# 문자열을 '-'로 분리하여 리스트로 반환.
list4 = text11.split('-')
print("문자열 분리(-로 분리) : ", list4)

'''
    문자열 변환.
'''
# 'python'을 기준으로 문자열을 나누어 튜플로 반환.
tuple1 = text10.partition('python')
print("문자 변환 : ", tuple1)

print("'like'를 'love'로 대체 : ", text10.replace('like', 'love'))

'''
    문자열 검사
'''
text12 = 'I Like Python Language'
print("모든 단어의 첫 문자가 대문자인가? ", text12.istitle())

text13 = 'abc123'
print("문자열이 숫자와 문자로 구성되어 있나? ", text13.isalnum())

text14 = '1234567890'
print("문자열이 숫자로만 구성되어 있나? ", text14.isdigit())
print("문자열이 문자로만 구성되어 있나? ", text14.isalpha())

print("모든 문자가 대문자인가? ", text14.isupper())
print("모든 문자가 소문자인가? ", text14.islower())