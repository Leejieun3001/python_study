"""
	2018-08-06 파이썬 첫번째 예제 입니다.
	(1) python 여러줄 주석 : """"""
	    python 한줄 주석 #
	
	(2) 출력 print()
	
	(3)자료형 :
	정수, 실수, 문자 // +복소수
	자료형 선언을 안해도 사용 할 수 있다!

	(4) 연산자
	(5)내장함수 : 객체 발생을 안해도 사용 가능 (예,type), 컴파일러에 미리 있는 것 

"""
# 출력하기
print("안녕하세요")  #주석
print("빈가워요")
print("Hi \n")
print("배고파요 \n\n")

# 자료형 (다른 언어에 비해 비교적 자유롭다)

#1) 정수 : 무한대 정수를 다룰 수 있다.
print("정수")
a = 10
print("a의 값 : ", a)
print("자료형 타입 : ", type(a)) 

#2) 실수 : 무한대 정수를 다룰 수 있다.
print("실수")
b = 25.1234
print("b의 값 : ", b)
print("자료형 타입 : ", type(b)) 

#3) 문자
print("문자")
c = '안녕'
d = "안녕하세요"

print("c의 값 : ", c, "\t", type(c))
print("d의 값 : ", d, "\t", type(d) , "\n\n")

#연산자
su =10
value = 88.8
hap = su + value
sub = su - value
mul = su * value
div = su / value #round 함수 이용하여 소숫 점을 잘라 줄 수 있음 

print("합 : ", hap)
print("뺄셈 : ", sub)
print("곱 : ", mul)
print("나눗셈 : ", div)

x = 10
y = 3
q = x//y   #몫 3 (파이썬에만 있는 기능)
r = x%y    #나머지 1
p = 2**10  #거듭제곱 1024
print("몫 :" , q)
print("나머지 : " ,r)
print("거듭제곱 : " , p)

#복소수
print("복소수")
z= 2+3j  # 2+3i (실제 수학계에서 쓰는 기호는 i, python 에서는j
print(z, "\t",type(z))
print("실수부 : " , z.real)
print("허수부 : " , z.imag)


#내장함수 : 객체 발생을 안해도 사용 가능 (예,type), 컴파일러에 미리 있는 것 
