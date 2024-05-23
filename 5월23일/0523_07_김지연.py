'''
    작성일 : 2024년 5월 23일
    작성자 : 학과 학번 이름
    설명 : readlines() 메소드 사용법
'''
print("== readlines() 메소드 이용하여 읽기 ==")

# readlines() 메소드는 파일의 모든 내용을 읽어 들인다.
# readline() 메소드와 다른점은 각각 줄을 읽어 리스트로 반환한다.
# readlines() 메소드는 파일로부터 읽어 들인 
# 한 줄을 리스트의 한 항목으로 만든다.

# with open을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt", "r") as f : 
    # 파일에 있는 모든 줄을 하나의 리스트로 만든다.
    textlist = f.readlines()
    
    print(textlist)
    print("textlist의 자료형 : ", type(textlist))
    
# with open을 사용하면 f.close() 쓸 필요 없다.