"""
 파이썬에만 있는 함수 기능

	(1)기본값 매개변수
	(2)키워드 매개변수
	(3)가변 매개변수
	(4)일반 매개변수와 가변 매개변수 같이 사용시
	(5)중첩 함수
	(6)함수를 변수, 리스트에 담아서 사용하다
	(7)함수의 결과를 함수로 반환	
	
보통 클래스보다 함수를 조금더 많이 사용하긴 한다
"""

#1)기본값 매개변수
def printString(text, count=3): #text (일반 매개변수), count (기본값 매개변수) 
	for i in range(count):
		print(text)
printString("안녕하세요") # 함수 호출 시 count는 생략가능
print("\n")
printString("허허허헣",10)
print("\n\n")

#2)키워드 매개변수 // 키워드는 반드시 명시해 줘야한다
def printPerson(name = "kim", position="staff", natinality = "korea"):
	print(name,'\t',position,'\t',natinality)

printPerson()
printPerson(name="홍길동")
printPerson(natinality="한국")
printPerson(position="인턴")

#3)가변 매개변수(딕셔너리와 튜플만 가능하게 하는것) - *tuple, **dic
#*tuple
def msgString(*text): # 튜플만 가능 //그렇지 않은 경우에는 생략가능 
	print(type(text), text)
	result =""
	
	for str in text:
		result = result + str
	return result
	
print(msgString("아버지가","방","에","들어가신다"))

#**dic
def printTeam(**players): #딕셔너리만 가능
	print(type(players))
	
	for key, value in players.items():
		print(key, '\t', value)
	print()
print(printTeam(카시아="GK", 호날드="FW", 알론스="MF", 페페="DF"))


#4)일반 매개변수와 가변 매개변수 같이 사용시
def printArgs(su, *str):
	for i in range(su):
		print(str[i])
	print()

printArgs(3, "apple","banana","melon")

def printAgrgss(*str, su):
	for i in range(su):
		print(str[i])
	print()
#가변길이 뒤에 정의된 일반 매개변수는 반드시 키워드 매개변수로 호출
printAgrgss("사과","바나나","멜론", "딸기", su=4)

#5)중첩 함수 //파이썬 에서만 존재
def ban_total(*subject):
	#pass #빠져나갈수 있는 명령어 (구현하지 않고 keep)
	
	def total():
		sum = 0
		for su in subject:
			sum = sum+su
		return sum
		
	def avg():
		average = total()/len(subject)
		return average
		
	return avg()


r = ban_total(100,100,80)
print("평균 : ", r)


#6)함수를 변수에 담아서 사용
def print_something(a):
	print(a)
print_something(10)

p = print_something
p(123)

p("\n")

#함수를 list의 요소에 넣기
def plus(a,b):
	return a+b
def minus(a,b):
	return a-b
list = [plus ,minus]
print("plus Fun : " , list[0](1,2))
print("minus Fun : " , list[1](300,200))


# 7)함수의 결과를 함수로 반환
def hello_korean():
	print("안녕하세요")

def hello_english():
	print("Hello")

def greet(hello):
	hello()


def get_greeting(where):
	if where=='k':
		return hello_korean
	else:
		return hello_english
greet(hello_korean)
greet(hello_english)
print("\n")

hello = get_greeting('k')
hello()


hello = get_greeting('E')
hello()