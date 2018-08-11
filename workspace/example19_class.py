'''
	클래스 연습
class AA{
	public int su
	public int value
	
	public AA(int su, int value){
		this.su=su;
		this.value=value;
	}
}
'''
class Human:
	def createHuman(self,name,weight):
		self.name=name
		self.weight=weight

	def eat(self):
		self.weight += 0.1
		print("{}가 먹어서 {}kg이 됐습니다".format(self.name,self.weight))
	def walk(self):
		self.weight -= 0.1
		print("{}가 운동을 해서 {}kg이 됐습니다".format(self.name,self.weight))
	
hong = Human()
hong.createHuman('홍길동', 75.5)#객체가 함수를 호출하기만해도 self
hong.eat()
hong.walk()

print()

class Car:
	def createCar(self,color,wheelSize,displacement):
		self.color=color
		self.wheelSize=wheelSize
		self.displacement=displacement
	def forward(self):
		print("{} {} {}의 자동차가 전진합니다.".format(self.color,self.wheelSize,self.displacement))
	def backward(self):
		print("{} {} {}의 자동차가 후진합니다.".format(self.color,self.wheelSize,self.displacement))
sonata = Car()
sonata.createCar("red",16,2000)
sonata.forward()
sonata.backward()




class Human:
	def __init__(self,name,weight):
		self.name=name
		self.weight=weight
	def eat(self):
		self.weight +=0.1
	def walk(self):
		self.weight-=0.5
	def disp(self):
		print("{}님의 현재 몸무게는 {}kg이 되었습니다.".format(self.name, round(self.weight,1)))
	def __str__(self):	#tostring
		return"{}님 현재 몸무게는 {}kg이 되었습니다".format(self.name, round(self.weight,1))
	def __del__(self):
		print("소멸자")
kim=Human("김길동",77.7)
kim.eat()
kim.eat()
kim.eat()
kim.walk()
kim.disp()
kim.walk()
kim.walk()
print("tostring 호출\n",kim)