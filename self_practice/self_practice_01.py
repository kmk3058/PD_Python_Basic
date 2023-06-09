# onceCycle = 0.15
# currentStatus = 30
# minStatus = 20
# rotationCount = 0
#
# while currentStatus >= minStatus:
#     rotationCount += 1
#     currentStatus -= onceCycle
#
#
# safeRotationCount = rotationCount - 1
# print("운행 가능 횟수 : {}".format(safeRotationCount))

# import random
#
# sum = 0
# data = 1
# flag = True
#
# while flag:
#     patientCount = random.randint(50,100)
#     sum += patientCount
#     data += 1
#     print("날짜 : {}, 오늘 환자 수 : {}, 누적 환자수 : {}"
#           .format(data, patientCount, sum))
#     if sum >= 10000:
#         flag = False

# for i in range(100):
#     if i % 8 != 0:
#         continue
#     print('{}는 8의 배수 입니다.'.format(i))

# cnt = 0
# for i in range(100):
#     if i % 8 != 0:
#         continue
#
#     print('{}는 8의 배수 입니다.'.format(i))
#     cnt += 1
#
# else:
#     print('99까지의 정수 중 8의 배수는 {}개 입니다.'.format(cnt))

# continue 는 해당 조건 성립 후 밑 생략
# break 조건 후 break를 만나면 반복문을 빠져나온다.

# sum = 0
# for i in range(1,101):
#     sum += i
#
#     if sum >= 1000:
#         searchNum = i
#         break
#
# print('1부터 100까지 정수를 더할 때, 합계가 1000이 넘는 최초의 정수는 '
#       '{}입니다.'.format(searchNum))

# result = 1
# num = 0
# for i in range(1,11):
#     result *= i
#
#     if result > 1000:
#         num = i
#         break
#
# print('num : {}, result : {}'.format(num, result))

# limitG = 2200
# onceAmount = 70
# currentAmount = 800
# count = 1
#
# while True:
#     if currentAmount >= limitG:
#         break
#
#     count += 1
#     currentAmount += onceAmount
#
#
# print('count : {}'.format(count))
# print('currentAmount : {}'.format(currentAmount))

# for i in range(1,10):
#     for j in range(i):
#         print('*', end='')
#     print()
#
# for i in range(10,0,-1):
#     for j in range(i):
#         print('*', end='')
#
#     print()

# def greet(customer):
#     print(f'{customer} 고객님 안녕하세요.')
#
# greet('고지현')

# def printScore(kor, eng, mat):
#     sum = kor + eng + mat
#     avg = round(sum / 3, 2)
#
#     print('sum : {}, avg : {}'.format(sum, avg))
#
# korScore, engScore, matScore = map(int, input('점수 입력: ').split())
#
# printScore(korScore, engScore, matScore)

# def cmTomMm(cm):
#     result = cm * 10
#
#     return result
#
# length = float(input('길이(cm)입력: '))
# returnValue = cmTomMm(length)
# print(f'reuturnValue : {returnValue:.2f}mm')

import random

def getOddRandomNumbe