#문자열 연산하기
length=len("You need python")
print("문장의 길이: "+str(length))

#문자열 포매팅
#1) 숫자 바로 대입하기
print("I read %d books." %6)

#2) 문자열 바로 대입하기
print("I read %s books." %"six")

#3) 숫자 값을 나타내는 변수로 대입하기
num=6
print("I read %d books." %num)

#포매팅 연산자와 %를 같이 사용하는 경우에는 %%로 쓴다.
print("The accuracy of this program is %d%%." %96)

#format 함수를 사용한 포매팅
print("I read {0} books.".format(6))        #숫자 바로 대입하기
print("I read {0} books.".format("six"))    #문자열 바로 대입하기
print("I read {0} books.".format(num))      #숫자 값을 가진 변수로 대입하기

year=2021
month="September"
print("Today is {0} {1}".format(month, year))   #2개 이상의 값 넣기
print("I ate {num1} apples and {num2} bananas.".format(num1=5, num2=3))    #이름으로 넣기
print("I ate {0} apples and {num3} bananas.".format(5, num3=3))            #인덱스와 이름을 혼용해서 넣기
print("pi={0:0.4f}".format(3.141592))   #소수점 표현하기(반올림)

#f 문자열 포매팅
name="블랙핑크"
member=4
print(f"Pretty Savage는 {name}의 노래입니다. {name}의 멤버 수는 {member}명입니다.")

#딕셔너리
d={'name':'블랙핑크', 'member':4}
print(f'{d["name"]}의 멤버 수는 {d["member"]}입니다.')

#문제. format함수 또는 f 문자열 포매팅을 사용해 '!!!python!!!' 문자열을 출력해보자
print("{0:!^12}".format("python"))


#문자열 관련 함수
a="bicycle"
print(a.count('b'))     #문자 b의 개수세기

a="Life is too short"
print(a.replace("Life", "Your leg"))     #문자열 바꾸기  

#문자열 나누기
print(a.split())    #공백을 기준으로 문자열을 나눈다                   
b="a:b:c:d"
b.split(':')        # : 기호를 기준으로 문자열을 나눈다
