a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)   # a와 b가 같은지(가리키는 메모리 주소가 같음. 같은 객체.) 출력. 같으면 true, 다르면 false

a[1] = 4
print(a, b)

# [:]
a = [1, 2, 3]
b = a[:]
a[1]=5
print(a, b)
print(a is b)

#copy
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a, b)
print(a is b)   #모양은 같아보이지만 가리키는 메모리 주소가 다름. 다른 객체임

#변수를 만드는 여러 가지 방법
a, b = ('python', 'life')   #튜플
(a, b) = 'python', 'life'
print(a, b)

[a,b] = ['python', 'life']  #리스트
a = b = 'python'    #변수에 대입

#변수 값 교환
a=3
b=5
a,b=b,a
print(a,b)

c='name'
d='age'
c,d=d,c
print(c,d)