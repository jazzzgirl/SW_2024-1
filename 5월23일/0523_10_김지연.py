'''
    작성일 : 2024년 5월 23일
    작성자 : 학과 학번 이름
    설명 : 학생 정보 입력된 파일의 내용을 출력하시오.
           
    [알고리즘]
        1. 학생 이름과 성적을 읽어 옿 객체 만들기.
        2. 반복하면서 내용 읽어오기
            2-1. 출력하기

    with open()
    
    읽기 모드 => r
    파일에 읽기 = readline()   => while True 사용.
'''
with open("student.txt", "r") as f:
    while True :
        student = f.readline()
        
        if student == '' :
            break
        print(student)