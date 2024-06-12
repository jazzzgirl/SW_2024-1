'''
    리스트에 도시의 인구를 저장해보자, 177쪽
    서울, 부산, 인천의 인구를 가지고 리스트를 생성하자.
    각 도시의 인구는 변수에 저장되어 있다.
     
    대전을 추가하자.
    대전의 인구는 1,531천명이다.
    
    도시 중 인구가 가장 많은 도시와, 가장 적은 도시를 출력하고, 
    네 도시의 인구의 평균을 출력하자.
    max(), mim() 함수를 사용해 보고,
    반복문을 사용하여 출력해 보자.
'''
# 인구 통계(단위: 천명) 
Seoul = 9765
Busan = 3441
Incheon = 2954
city_pop = [ Seoul, Busan, Incheon ]    # 변수들로 리스트 생성
print('도시별 인구 리스트 : ', city_pop)    # 리스트 데이터를 출력

Daejeon = 1531
city_pop.append(Daejeon)
print('도시별 인구 리스트(대전 추가) : ',city_pop)
print('도시별 인구 리스트(반복문으로 출력하기) :', end=' ')

for element in city_pop :
    print(element, end=', ')

print()
print()

print(":: 함수로 최대, 최소, 평균 계산하기 ::")
print('최대 인구:', max(city_pop))
print('최소 인구:', min(city_pop))
print('평균 인구:', sum(city_pop) / len(city_pop))

print()

print(":: 반복문으로 최대, 최소, 평균 계산하기 ::")
max_pop = 0
min_pop = 1000000
pop_sum = 0
count = 0

for pop in city_pop:        # 순환문을 돌면서 최댓값, 최솟값을 구한다
    if pop > max_pop :      # pop가 최대값보다 크다면
        max_pop = pop       # 최대값에 pop를 저장한다.
    if pop < min_pop :      # pop가 최소값보다 작다면
        min_pop = pop       # 최소값에 pop를 저장한다.
    pop_sum += pop          # 합계를 계산한다.
    count += 1              # 개수 증가 시키기
    
print('최대 인구:', max_pop)
print('최소 인구:', min_pop)
print('평균 인구:', pop_sum / count)