"""
	for 문을 이용한 python 자료형 출력 (list, tuple, dic)
"""

# 1)리스트 출력
names = ["철수","영희","지은","귀도"]

print(names)
print(names[0])

for name in names:
	print(name,  end="\t")
print()

# 2)튜플 출력
su = (1,2,3)
print(su)
print(su.index(1))

for value in su:
	print(value)
print()


# 3)딕셔너리 출력

ages = {
	"홍길동":23,
	"이순신":25,
	"이영자":26
}

print(ages)
print(ages["홍길동"])
print(ages.keys())
print(ages.values())
print(ages.items())
print()


for key in ages.keys(): #key 값만 출력
	print(key)
print()


for value in ages.values(): # value 값만 출력
	print(value)
print()


for key ,value in ages.items(): # key, value 둘다 출력
	print("{}의 나이는{}입니다.".format(key, value))
print()

