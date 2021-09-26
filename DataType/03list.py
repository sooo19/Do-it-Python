a=[1,2,3,['a','b','c']]
print(a[3])
print(a[-1][0])

a=[1,2,['a','b',['Life','is']]]     #삼중 구조의 리스트
print(a[2][2][0])   #Life 요소 출력

A=[1,2,3,4,5]
print(A[1:3])

#중첩된 리스트에서 슬라이싱하기
a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

#리스트 관련 함수: append, sort, reverse, index, insert, remove, pop, count, extend
a=[1,2,3]
a.append([4,5])
print(a)

a=[1,4,3,9,6]
a.sort()    #sort함수: 정렬
print(a)

a=['b','c','a']
a.reverse()
print(a)    #output: ['a','c','b'] reverse 함수는 sort된 값의 역순이 아니라, 현재 배열의 역순으로 값을 출력한다.

a=[1,2,3]
print(a.index(3)) #3의 위치 출력

a=['b','c','d']
a.insert(0, 'a')  #a[0]자리에 a 추가
print(a)

a=[1,3,5,2,5,6]
a.remove(5)
print(a)    #remove 함수는 가장 앞에 나오는 해당 값을 삭제

a=[1,2,3]
print(a.pop())
print(a)    #pop()함수는 리스트의 맨 마지막에 있는 요소를 돌려주고, 해당 요소를 삭제한다.

a=[4,5,6]
print(a.pop(2)) #pop(x)함수는 리스트의 해당 위치에 있는 요소를 돌려주고, 해당 요소를 삭제한다.
print(a)

a=[1,2,2,3,3,3,4,4,4,4]
print(a.count(3))  #count(x) 함수는 리스트에 해당 요소가 몇 개 있는지 세어주는 역할을 한다.

#extend(x) 함수의 x에는 리스트만 올 수 있으며, 원래의 리스트에 x리스트를 더해준다.
a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7,8]
a.extend(b)
print(a)