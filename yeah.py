
#산술 연산자
# +,-,*,**,/,//,%
# +,-,*,/ -> 사칙연산

# ** -> 제곱
# // -> 몫
# %  -> 나머지

#시퀀스 연산 [시퀀스 타입에서 산술 연산] +, *, in
#str, list, tuple ...
#tuple -> 수정 불가능 (?)
#"hello" + " " + "world"
#"hel" in "hello" => True (논리값으로 출력)

print(1 in (1,2,3))

s = "hello"
s1 = " "
s2 = "world"
s3 = s + s1 + s2
print(s3)

#"hello" * 2 = "hellohello"

print("=" * 32)

#대입 연산자(=)
#값을 대입할 때 사용

a = 10 #이런 식으로
b = 20
c = "hello"

#복합 대입 연산자 -> +=, -=, *=, /=, //=, %=

a += 5 #a = 10 + 5
c *= 2 #c = "hello" * 2 -> "hellohello"

# 변수 안에 있던 값에 오른쪽의 값을 연산하여 새로 대입


#관계 연산자 (비교연산자)
# >,>=,<,<=,==,!=
num1 = 10
num2 = 20
n = int(input('숫자를 입력하세요 : '))
print(num1 < n < num2)

#논리 연산자
#논리 값을 묶어서 연산하는데 사용
#and - 양쪽의 논리 값이 True 일때 True / 이 외의 경우 False
#or - 양쪽의 논리 값이 False 일때 False / 이 외의 경우 True
#[not - 단항] - [단항] 뒤에 붙은 논리 값을 반대로 돌려줌 False -> False -> True/ -> False

print((True and True)and True) # 이때만 True
print(True and False)
print(False and True)
print(False and False)

# 비트 연산자
#&  -> and
#|  -> or
#^  -> xor
#~  -> not
#<< -> left shift
#>> -> right shift


#기타 연산자
#삼항 조건 연산자 -> 가독성 떨어짐
#참 if 논리값 else 거짓

print(1) if False else print(2)

number = 10
print("10보다 작습니다" if number < 10 else "10보다 큽니다" if number > 10 else "10입니다.")

tree = '#'
space = ' '

print(space * 4 + tree *1)
print(space * 3 + tree *3)
print(space * 2 + tree *5)
print(space * 1 + tree *7)
print(space * 0 + tree *9)

