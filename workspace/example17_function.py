"""
	재귀 함수
"""
# 함수 호출
def no_idea():
	print("덥다")
	print("짜증난다")
	#no_idea()	#자신을 호출시 멈추라는 설정을 해줘야함
	
no_idea()
print("그다음 문장을 실행한다.")
print()

# 재귀 함수
def some_fun(count):
	if count >0:
		print(count)
		some_fun(count-1)
		
some_fun(10)


#팩토리얼 
def factorial(n):
	if n==0:
		return 1
	elif n >0:
		return factorial(n-1)*n

print(factorial(5))