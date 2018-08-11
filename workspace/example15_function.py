"""
	함수 구현
	(1)call by name
	(2)call by value
	(3)call by value ~ return
"""
# 1) call by name
def sub():
	print("Hi")

print("start")
sub();
print("connect")
sub();
print("end")
sub();
	
# 2)call by value - 일반 자료형 (정수, 실수,문자열)
def fun(a,b,c):
	print(type(a),"\t",type(b),"\t",type(c))
	print(a,"\t",b,"\t",c)

fun(1,2,3)
fun(55.5,66.6,77.7)
fun("fun","안녕","hi")
fun(2020,1212,"으하하하")

# 3)call by value - list, tuple, dictionary
list =['A','B','C']
tuple = (11,12,13,14)
dic ={"apple" : "사과","banana":"바나나"}

fun(list,tuple,dic) # 자료형 상관없이 다 가능!
print()

#call by value ~ return
def hap(su, value):
	return su +value

r = hap(10,20)
print(r)

s = hap('A','B')
print(s)

# 튜플을 이용한 함수 리턴
def sub():
	x=10
	y=20
	return x,y

rx,ry = sub()
print(rx, " ", ry)



