"""
	상속

	python 다중 상속이 존재함
"""

# 상속
class Animal:
	def walk(self):
		print("걷는다")
		
	def eat(self):
		print("먹는다")


#상속받을 클래스를 ()안에다 적어준다.
class Human(Animal):
	#walk(), eat()
	def wave(self):
		print("손을 흔든다")


class Dog(Animal):
	def wag(self):
		print("꼬리를 흔든다")


Kim = Human()
Kim.walk()
Kim.eat()
Kim.wave()
print()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()
print()
	