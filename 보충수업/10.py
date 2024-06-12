'''
   온도를 입력받아 섭씨 온도는 화씨 온도로, 
   화씨 온도는 섭씨 온도로 변환하는 프로그램을 작성하시오.
   섭씨, 화씨 온도로 변환하는 부분은 함수로 작성합니다.
   함수를 변환된 온도를 리턴합니다.
   사용자가 온도를 입력 할때 섭씨, 화씨를 구분할 수 있도록 입력해야 합니다.

   예를 들어 섭씨 온도는 27C, 화씨 온도는 27F 로 입력합니다.
   입력된 문자가 C이면 섭씨 온도이므로 화씨 온도를 구하고,
   입력된 문자가 F이면 화씨 온도이므로 섭씨 온도를 구합니다.

   섭씨 온도 = (화씨 온도 - 32) * (5 / 9)
   화씨 온도 = (섭씨 온도 * (9 / 5)) + 32

   [출력 결과]
      섭씨 또는 화씨 온도를 입력하세요(27C 또는 27F) : 27C
      화씨 온도 27C는 섭씨 온도 80.60F 입니다.
      섭씨 또는 화씨 온도를 입력하세요(27C 또는 27F) : 80F
      섭씨 온도 80F는 화씨 온도 26.67C 입니다.
      섭씨 또는 화씨 온도를 입력하세요(27C 또는 27F) : 23D
      온도를 잘 못 입력하셨습니다.
'''
def Cel_123(temperature) :
   result = (temperature - 32) * (5 / 9)
   return result

def Fah_123(temperature) :
   result = (temperature * (9 / 5)) + 32
   return result

temp = input("섭씨 또는 화씨 온도를 입력하세요(27C 또는 27F) : ")

if "F" in temp or "f" in temp :
   result = Cel_123(float(temp[0:2]))
   print(f'섭씨 온도 {temp}는 화씨 온도 {result:.2f}C 입니다.')
elif "C" in temp or "c" in temp :
   result = Fah_123(float(temp[0:2]))
   print(f'화씨 온도 {temp}는 섭씨 온도 {result:.2f}F 입니다.')
else :
   print("온도를 잘 못 입력하셨습니다.")