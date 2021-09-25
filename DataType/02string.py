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
print("Today is {0} {1}".format(month, year))

