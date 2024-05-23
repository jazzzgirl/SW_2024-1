'''
    작성일 : 2024년 5월 23일
    작성자 : 학과 학번 이름
    설명 : 사용자로부터 5명의 학생의 이름과 3과목의 성적을 입력 받아
           student.txt 파일에 저장하시오.
           
           write() 메소드를 사용합니다.
           
    [알고리즘]
        1. 학생 이름과 성적을 저장 할 파일 만들기.
        2. 학생 이름과 3과목을 입력 받아 파일에 저장.
            1번 학생 이름과 3과목의 성적 입력 : 홍길동 90 89 77
            
    open() + close()
    with open()
    
    쓰기 모드 => w
    파일에 쓰기 = write()
'''
with open("student.txt", "w") as f:
    for i in range(1, 6) :
        student = input(str(i) + "번 학생 이름과 3과목 성적 입력(예 : 홍길동 90 89 77) : ")
        f.write(student + "\n")
