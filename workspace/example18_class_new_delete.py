"""
	python 클래스 : 생성자, 소멸자
	생성자 =>  __init__(self)
	소멸자 =>  __del__(self)
"""

클래스의 생성자(생성자명=클래스명)__init__(self):/소멸자 __del__(self):
#생성자 중복 x
class Sub:
	def __init__(self):
		print("생성자")
		
	def function(self):
		print("일반함수 호출")
		
	def __del__(self):
		print("소멸자")
		
sub = Sub()
print()
sub.function()