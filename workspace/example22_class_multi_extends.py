"""
	다중 상속 : 90년대 중반 이후의 객체 지향언어(java,c#) 다중상속이 없어졌다.
	사용하는 것을 추천하지 않음
	(포인터도 없어짐)
"""

# 위의경우 C 에서 B, A 모두 접근 가능하다!! 계속적인 상속은 가능함
# 프로그램이 무거워진다.
# python은 이렇게 사용하지 않는다. (java, C#)은 사용
class A:
	pass
class B(A):
	pass
class C(B):
	pass

#파이썬 다중 상속 -> 복잡해 져서 거의 사용하지 않는다.
class A:
	pass
class B(A):
	pass
class C(A):
	pass
class D(B,C):
	pass

	
#예제
class A:
	def sub(self):
		print("A class sub Function")

	def method(self):
		print("A class method Function")
		
class B(A): #sub(), method(), aa()
	def aa(self):
		print("B class aa Function")
class C(A): #sub(), method(),xx()
	def xx(self):
		print("C class xx Function")
	
class D(B,C): #sub(), method(),aa(), xx(),ii()
	def ii(self):
		print("D class ii  Function")

obj =D()
obj.sub()
obj.method()
obj.aa()
obj.xx()
obj.ii()


		
		
		
		
		
		
		