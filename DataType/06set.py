s1=set([1,2,3])
s2=set("loco")
print(s1, s2)   #집합 자료형은 리스트/튜플과 달리 중복을 허락하지 않고, 순서가 없다.

#집합형은 순서가 없어 인덱싱할 수 없다. 따라서 리스트 or 튜플로 변환해준 후 인덱싱을 진행해야 한다.
s1=set([1,2,3,4,5])
l1=list(s1)
print(l1[2])

s2=set([2,3,4,5,6])
l2=tuple(s2)
print(l2[2])

#교집합(& 또는 intersection함수), 합집합(| 또는 union함수), 차집합(- 또는 difference)
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8])

print(s1&s2, s1.intersection(s2))
print(s1|s2, s1.union(s2))
print(s1-s2, s1.difference(s2))

# 집합 자료형 함수
# 값 한 개 추가하기 (add함수)
s1=set([1,2,3,4])
s1.add(5)
print(s1)

# 값 여러 개 추가하기 (update함수)
s1.update([6,7,8])
print(s1)

# 특정 값 제거하기 (remove함수)
s1.remove(2)
s1.remove(4)
print(s1)


