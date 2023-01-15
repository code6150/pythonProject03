import random # module . 모듈
# #1. 임의의 두 자리 정수 10~99 를 입력받아서 십의 자리와 일의 자리로 분리하여 출력하는 프로그램
# 10 ~ 99 사이의 숫자를 입력하세요 >>> 15
# 십의 자리 : 1
# 일의 자리 : 5

num = random.randint(10,99)
print(num)
print(f"십의 자리 : {num//10}")
print(f"일의 자리 : {num%10}")

#float random
print(random.uniform(1.0,2.0))

#range ->
#start 만 걸어둔 경우 0~start-1 범위 (0,1,2,3,4)
#stop을 설정한 경우 start ~stop-1 범위 (5,6,7,8,9)
#step을 설정한 경우 설정 범위내에서 n씩 증가하는 형태의 범위 (default = 1)

print(random.randrange(5,10,2)) #5,7,9

#===================================================================

menu = ['짜장면','짬뽕','볶음밥']

#random.shuffle(menu)
#print(menu)

#가중치 시스템

#50%
#30%
#20%

print(random.choices(menu, weights=[50,30,20]))

    #2.1분은 60초 / 1시간 60분, 따라서 1시간은 3600초.
# 초를 임의로 입력받아서 해당 초를 시, 분, 초로 변환하여 출력하는 프로그램
sec = int(input("초를 입력하세요 >>> "))
#변환 결과는 ~시간 ~분 ~초 입니다.

hour = sec // 3600
min = sec // 60 % 60
sec = sec % 60

print(f"{hour}시 {min}분 {sec}초 입니다.")

#4. 한 박스에 라면이 20본 들어 갑니다. 라면이 21 본이 있다면 2박스가 있어야 포장이 가능합니다.
#라면의 갯수를 입력 받아서 필요한 박스의 수를 구하는 프로그램을 구현하세요.

ramyeaon = int(input("라면의 갯수 >>> "))

print(f"라면 박스가 {(ramyeaon // 20) + (1 if (0<(ramyeaon%20)<20) else 0)}개 필요합니다")
