"""
	관계 연산자 : = != > < 
    논리 연산자 : && || !
"""

print("관계 연산자")# > , >= , < , <= , == , !=, is , isnot 
su = 10
value = 20

result1 = su > value
result2 = su >= value
result3 = su < value
result4 = su <= value
result5 = su == value
result6 = su != value

print("result1 : ",result1 , "  ", type(result1))
print("result2 : ",result2)
print("result3 : ",result3)
print("result4 : ",result4)
print("result5 : ",result5)
print("result6 : ",result6)
print("\n\n")

print("논리 연산자") #and, or, not
result7 = su>0 and su <20 # su=10
result8 = su==10 or su==20
result9 = not(su%2==0)
print("result7 : ",result7)
print("result8 : ",result8)
print("result9 : ",result9)

