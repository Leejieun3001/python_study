"""
	dictoionary: key-value 로 구성
	dic 선언 , 추가, 삭제, 변경
"""
a={
	'name' : '홍길동',
	'phone' : '010-123-1234',
	'birth':'1225'
}

print(a['name'])
print(a['phone'])
print(a['birth'])

b={}  #초기화 (리스트 초기화 list=[])
b['파이썬'] = 'www.python.org'
b['마이크로소프트'] = 'www.microsoft.com'
b['애플'] = 'www.apple.com'

print(b['애플'])
print(b)
print("key : ", b.keys())
print("value : ", b.values())
print("key & value : ", b.items())

b["two"] = 99
print("추가", b)
b["애플"] = 'www.naver.com'
print("변경", b)

del(b["파이썬"])
print("삭제 :", b)

print("애플" in b.keys)
