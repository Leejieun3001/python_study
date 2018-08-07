"""
	문자열 처리
	(1) 문자열 인덱싱
	(2) 문자열 슬라이싱
	(3) 문자열 길이 
    (4) in 연산자
	(5) 문자열 내장함수
	(6) 문자열 유효성 검사
	(7) 문자열 공백, 특정 문자 제거
	
"""

#1) 문자열 인덱싱
print("문자열 인덱싱")
a="Life is too short, You need Python"
print(a)
print(type(a))
print(a[0]) #L
print(a[12]) #s (공백 포함 12번째)
print(a[-1] , "\n\n") #n (문자열 맨 끝 출력)

#2)문자열 슬라이싱
print("문자열 슬라이싱")
b = "Good morning"
print(b[0:4]) #0번지부터 n-1 번지까지 str[0:n]
print(b[:4]) #처음부터 n-1 번지까지
print(b[4:11])
print(b[4:]) #n번지부터 끝까지

#3)문자열 길이 뽑아내기
print("문자열 길이" , len(b))

#4) in 연산자 : 문자열에 포함 여부를 체크할 떄 사용
c = "Good" in b
print(c)
d = "Bad" in b
print(d)

#5) 문자열 함수
str ="Hello World"
print(str, "\t", type(str))
print("문자열 치환" , str.replace("World" ,"Korea"))
print("문자열 대문자" , str.upper())
print("문자열 소문자" , str.lower())
print("문자열 H로 시작하는지 판단" , str.startswith("H"))
print("문자열 s로 시작하는지 판단" , str.startswith("s"))
print("문자열이 a로끝나는지 판단" , str.endswith("a"))
print("문자열이 o로끝나는지 판단" , str.endswith("o"))
print("문자열이 d로끝나는지 판단" , str.endswith("d"))
print("문자열 앞부터 위치 찾기" , str.find("H")) # 0
print("문자열 앞부터 위치 찾기" , str.find("e")) # 0
print("문자열 앞부터 위치 찾기" , str.find("F")) # 없으면 -1

# 문제) 주민번호를 
jumin = "801225-1234567"
num = jumin.find("-")
print(jumin[:num])
print(jumin[num+1:])

#6) 유효성 검사
x = 'ABCDefg'
y = '1234'
z = '1234ABC'
print("x는 문자열로 이루어져 있는가?(한글포함)", x.isalpha());
print("z는 문자열로 이루어져 있는가?(한글포함)", z.isalpha());
print("x 숫자로 이루어져 있는가?", x.isnumeric());
print("x 문자와 숫자로 이루어져 있는가?", x.isalnum());


#7) 공백 제거

i = "   안녕하세요"
j = "안녕하세요   "
k = "   안녕하세요  "
print(i.lstrip())
print(j.rstrip())
print(k.strip()) # 양쪽 공백 제거


ch = "Apple,Oranage,Kiwi"
# , 제거
chList = ch.split(",")
print("List로 반환 " , chList, " " , type(chList))

for str in chList:
	print(str)

