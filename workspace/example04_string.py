"""
	문자열 데이터 출력
"""
#문자열 데이터 : "" or '' or '''

print("문자열")
a="Hello World"
b= "안녕하세요"
print(a,'\t',b,'\t',type(a))

c = '''파이썬의 문자열은 줄바꿈 
처리가 됩니다.
안
녕
하
세
요'''
print(c , '\n\n')

#문자열 안에 작은 따옴표 포함
# ' 을 출력시키고 싶을 경우 "" 로 묶기
food = "Python's favorite food is perl"

#문자열에 큰 따옴표 포함
# " 을 출력시키고 싶을 경우 '' 로 묶기
say = 'Python"s favorite food is perl'

print(food,'\n', say,'\n')

print("문자열 연산")
x="안녕하세요"
y=str(10)
z=x+y
print(z)
i = "1980"
j = "2000"
k = i+j
print(k)


#파이썬에만 있는 문법 
str = "python"
print(str*3)
print("="*100)


