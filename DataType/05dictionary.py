dic={'name':'pey','phone':'01012345678','birth':'001010'}
#value에는 list값도 넣을 수 있다.

#딕셔너리 쌍 추가하기
a={1:'a'}
a[2]='b'
print(a)
a['name']='pey'
a[3]=[1,2,3]
print(a)

#딕셔너리 요소 삭제하기
del(a[1])
print(a)

#딕셔너리 key값을 이용해 value 얻기
grade={'pey':10, 'julliet':90}
print(grade['julliet'])
print(grade['pey'])    #key가 pey인 요소를 반환
print(grade['julliet'])

#딕셔너리 관련 함수
a={'name': 'pey', 'phone':'01012345678', 'birth':'001010'}
print(a.keys())     #딕셔너리의 key값들만 출력
print(a.values())   #딕셔너리의 value 리스트 만들기
print(a.items())    #딕셔너리의 key, value 쌍 얻기
print(a.clear())    #딕셔너리의 key:value쌍 모두 지우기

a={'name': 'pey', 'phone':'01012345678', 'birth':'001010'}
print(a.get('phone'))   #key값으로 value 얻기
print(a.get('hobby','hello'))   #get(x, '디폴트 값'): 딕셔너리 안에 찾으려는 key값(x)이 없을 경우, 미리 정해둔 디폴트값(hello)을 출력하도록 한다.

#in: 해당 key가 딕셔너리 안에 있는지 조사하기
a={'name': 'pey', 'phone':'01012345678', 'birth':'001010'}
print('name' in a)  #결과는 True 혹은 False로 출력

#문제
dic_a={'name':'홍길동', 'birth':'1128', 'age':'30'}
print(dic_a)

