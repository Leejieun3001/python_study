"""
	static(정적) 함수: java 처럼 많이 사용하지 않는다.
					클래스 안에서 선언하지만 메모리 영역이 달라서 객체명으로 접근하지 않고 클래스 명으로 
					접근하지 않고 클래스 명으로 접근.					

"""

class Yonsan:
	def plus(self,a,b):
		return a+b

	@staticmethod
	def minus(a,b):
		return a-b
		
	def multiply(self, a,b):
		return a*b
	
	@staticmethod
	def divde(a,b):
		return a/b
	

yonsan = Yonsan()
print("plus", yonsan.plus(10,20))
print("minus:" , Yonsan.minus(77,1))
print("plus", yonsan.multiply(1,2))
print("plus", yonsan.divde(1,2))
