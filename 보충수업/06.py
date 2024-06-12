'''
    두 개의 리스트를 만듭니다.
    하나의 리스트에는 반복문을 이용하여 1~5까지 저장합니다.
    또 다른 리스트에는 사용자로부터 좋아하는 과일을 5개 입력 받아 저장합니다.
    각 리스트의 이름은 'list1_본인학번', 'list2_본인학번'으로 생성합니다.
    두 리스트의 조합으로 아래와 같이 출력하시오.
    
    [결과]
    1번 과일을 입력하세요 : 딸기
    2번 과일을 입력하세요 : 바나나
    3번 과일을 입력하세요 : 포도
    4번 과일을 입력하세요 : 수박
    5번 과일을 입력하세요 : 망고
    
    list1_학번 : [1, 2, 3, 4, 5]
    list2_학번 : ['딸기', '바나나', '포도', '수박', '망고']
    1. 딸기
    2. 바나나
    3. 포도
    4. 수박
    5. 망고
'''
list1 = []
list2 = []

for i in range(1,6) :
    list1.append(i)
    
for j in range(1,6) :
    fruit = input(str(j) + "번 과일을 입력하세요 : ")
    list2.append(fruit)
    
print('list1_학번 : ', list1)
print('list2_학번 : ', list2)
print('리스트 결합 결과')
for i in list1 :
    print('{}. {}'.format(i, list2[i-1]))