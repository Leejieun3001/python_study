"""
	(1) 문자열 포맷 (출력 형식)
	(2) 형 변환
""" 
#1) 문자열 포맷
number = 20
greeting = "안녕하세요"
place = "문자열 포맷의 세계"
welcome = "환영합니다"
print(number, "번 손님 ",greeting, "!! ", place,"에 오신것을 " , welcome,"!!!")

print("{0}번 손님 {1}!! {2}에 오신것을 {3}!!!".format(number,greeting,place,welcome))
print("{}번 손님 {}!! {}에 오신것을 {}!!!".format(number,greeting,place,welcome))

mine="가위"
yours="바위"
result = "졌다"
print("나는 {}, 너는{}, 그래서 {}".format(mine,yours,result))
print("\n\n\n")


#2)형 변환
# 내 소스 밖으로 나가거나 들어오는 데이터는 다 문자열 이다.
# 정수, 실수 ->  문자열로 변환 /  문자열 -> 정수, 실수 변환 가능해야한다.

su = 10
print("첫번째 수를 입력하세요")
x = input();

print("두번째 수를 입력하세요")
y= input()
print(type(x), " " , type(y))
print(x, " " , y)

result = int(x) + int(y)
print(result)


z =77
zStr = str(z)
print(zStr, "",type(zStr))
