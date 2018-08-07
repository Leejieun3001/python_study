"""
	자료형 : 정수 실수 문자 "" '' 둘 다가능
	연산자 : + - / * // % **
	내장함수 : 

	python은 ++ ,-- 연산자가 없다!!!!!!!!!!!!!!!

"""


#내장 함수 : 객체를 생성하지 않아도 사용가능한 함수
#자바에서는 없다 (system.in) 이것도 클래스에서 가져온것
#2진수 bin() /ob , 8진수 oct() /0o, 16진수 hex() /ox
print("10진수를 2진수, 8진수, 16진수로 변환") 
temp =10
busu = bin(temp)
osu = oct(temp)
hsu = hex(temp)

print("2진수 :" , busu)
print("8진수 :" , osu)
print("16진수 :" , hsu)

print("2진수, 8진수, 16진수를 10진수로 변환")
dbsu = 0b1010
dosu = 0o12
dxsu = 0xb

print("10진수 :" , dbsu )
print("8진수 :", dosu )
print("16진수 :", dxsu ,"\n\n")

su =1234.45678
print("반올림" , round(su,3)) #소수 네째자리에서 소수 세째자리 출력
print("반올림" , round(su,2)) #소수 세째자리에서 소수 두째자리 출력



