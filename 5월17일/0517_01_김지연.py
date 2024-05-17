'''
    작성일 : 2024년 5월 17일
    작성자 : 학과 학번 이름
    설명 : 키와 값을 가지는 딕셔너리

    문자열 = " "    튜플 = ()   리스트 =  []   => 순서가 있다.
    세트 = {}   딕셔너리 = { key : value }   => 순서가 없다.  
'''
# 빈 딕셔너리 생성.
phone_book1 = {}    # 빈 세트 생성과 동일.

# 딕셔너리에 값 저장  -> 1) key, value  =>  [key] = value
phone_book1['김지연'] = '010-1234-5678'
print("phone_book1 : ", phone_book1)

# 딕셔너리에 값 저장 -> 2) {key : value}
phone_book2 = {'김지연' : '010-1234-5678', '홍길동' : '010-2345-6789'}
print("phone_book2 : ", phone_book2)

# 빈 딕셔너리 생성.
phone_book3 = {}

# 5명의 이름과 전화번호 저장.
phone_book3['김지연'] = '010-1234-5678'
phone_book3['홍길동'] = '010-3434-1278'
phone_book3['김길동'] = '010-5634-3478'
phone_book3['박길동'] = '010-6734-6778'
phone_book3['정길동'] = '010-7834-9078'

print("phone_book3 : ", phone_book3)

print("phone_book3의 모든 key 출력 : ", phone_book3.keys())

print("phone_book3의 모든 value 출력 : ", phone_book3.values())

print("phone_book3의 모든 key와 value 출력 : ", phone_book3.items())

print("전화번호부의 모든 내용 출력")
for name, phone_num in phone_book3.items() : 
    print(name, ":", phone_num)
    
print()

print("전화번호의 key로 접근하여 출력")
for key in phone_book3.keys() : 
    print(key, ":", phone_book3[key])  # 해당 key의 value를 찾아 줌.
    
print()

person_dict = {'name':'김지연', 'age':20, 'class':'1학년'}

# 딕셔너리의 'name' 키(key)로 값(value)을 조회하여 출력
print("name : ", person_dict['name'])

# 딕셔너리의 'age' 키로 값을 출력하시오,
print("age : ", person_dict['age'],"세")

print()

# 딕셔너리의 키를 기준으로 정렬 = phone_book3
print("phone_book3 정렬")
print(sorted(phone_book3))

print("키를 기준으로 전체 정렬")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])  # key 기준.
print(sort_phone_book3)

print("값를 기준으로 전체 정렬")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])  # value 기준.
print(sort_phone_book3)

print()

print("항목 삭제")
del phone_book3['김지연']
print(phone_book3)

print("전체 삭제")
phone_book3.clear()
print(phone_book3)

print()

dict1 = {1:'one', 2:'two', 3:'three'}
print("사전 1 : ", dict1)

print("사전의 모든 키")
for num in dict1.keys() :
    print(num, end=' ')
    
print()

print("사전의 모든 값")
for alpanum in dict1.values() :
    print(alpanum, end=' ')
    
print()

# 1은(는) 영어로 one
# 2은(는) 영어로 two
# 3은(는) 영어로 three
for num, alpanum in dict1.items() : 
    print(num, "은 영어로 ", alpanum)