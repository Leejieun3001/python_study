#list(array)  , tuple(*파이썬의 고유한 기능*), dict (hash map)
'''
	list 자료형
	추가, 삭제, 변경,출력
'''
#1) list =[]
#2) tuple =()
#3) dict ={}

a = ["이지은","이지은2","이지은3","이지은4"]
print("a = " ,a)

print("a[0] : " , a[0])
print("a[1] : " , a[1])
print("a[2] : " , a[2])

print("a[-1] : " , a[-1])


b=[1,2,3,4]
print("b",b)
b[0] = 77
b[2] = 88
print("b",b)

b.append(5) # 츄가

print("b",b)
b.insert(0,100) # 특정번지 추가

print("b",b)
del(b[2]) #삭제 번지
b.remove(100) # 삭제 값

print("b",b)


print("슬라이싱")
c = [1,2,3,4,5,6,7,8,9,10]
print(c[4:6])
print(c[:6])
print(c[4:])

#파이썬에 서만 있는 기능
c[0:3] = [77,88,99]
print(c)

c[3:6] = ['A','B','C']
print(c)
