"""
	제어문(조건문, 반복문)은 코드 블럭 {} 으로 표시 (C,C++,C# ,java)
	
	* python은 들여쓰기로 구역을 나눈다.*
	
	형식 1) if 조건문:
			  명령문
			  
	형식 2) if 조건문:
			  명령문
		   else:
		      명령문
	형식 3) if 조건문:
		      명령문
		   elif 조건문:
		      명령문
		   elif 조건문:
		      명령문			
"""

# 형식1) if
print("수를 입력해 주세요:")
su = int(input())

if su > 10 :
	print("10보다 큰수를 입력하였습니다.")

# 형식2) if ~ else
print("수를 입력해 주세요 :")
value= int(input())
if value%2==0:
	print("짝수를 입력하셨습니다.")
else:
	print("홀수를 입력하셨습니다.")

# 형식3) if ~elif
print("국어 점수를 입력하세요.")
kor = int(input())

print("수학 점수를 입력하세요.")
math = int(input())

print("영어 점수를 입력하세요.")
eng = int(input())

tot = kor+math+eng
avg = round(tot/3,1)

hakjum=""
if avg >=90:
	hakjum = "A"
elif avg >=80:
	hakjum = "B"
elif avg >=70:
	hakjum = "C"
elif avg >=60:
	hakjum = "D"
else:
	hakjum = "F"

print(tot, "\t", avg ,"\t", hakjum)
 



