# answer = list(input())
#
# total = 0
# current = 0
#
# for i in range(len(answer)):
#     if answer[i] == 'O':
#         current += 1
#         total += current
#     else:
#         current = 0
#         total += current
#
# print(total)
#

# def calNums(base, *nums):
#     for i in nums:
#         total = 1
#         for j in range(i):
#             total *= base
#         print(f'{base}의 {i} 제곱 값은 {total}이다.')
#
# calNums(5, 1, 2, 3)
# calNums(2, 1, 2, 3, 4)

# def maxFunc(A):
#     max = 0
#     for i in A:
#     if max(A):


# from random import randint
# rand_number = randint(1, 10)
#
# while True:
#     input_data = int(input())
#     if rand_number>input_data:
#         print("숫자가 작습니다.")
#     elif rand_number<input_data:
#         print("숫자가 큽니다.")
#     else:
#         print("정답입니다. 입력한 숫자는 {} 입니다.".format(rand_number))
#         break


# def f(x):
#     return 2 * x + 7
# def g(x):
#     return x ** 2
#
# print(f(2))
# print(g(2))
# print(f(g(2)))
# print(g(f(2)))
# print(f(2)+g(2)+f(g(2))+g(f(2)))

# year = int(input())
# age = 2021 - year + 1
#
# if age<=26 and age>=20:
#     print('대학생')
# elif age<20 and age>=17:
#     print('고등학생')
# elif age<17 and age>=14:
#     print('중학생')
# elif age<14 and age>=8:
#     print('초등학생')
# else:
#     print('학생이 아닙니다.')

sum = 0

# for i in range(101):
#     if i % 7 == 0:
#         sum += i
# print(sum)
#
# grade = [[49, 80, 20, 100, 80], [43, 60, 85, 30, 90], [49, 82, 48, 50, 100]]
# sum = 0
# avg = 0
# sub = ['국어', '수학', '영어']
# student = ['A', 'B', 'C', 'D', 'E']
#
# for i in range(len(student)):
#     for j in range(len(sub)):
#         sum += grade[j][i]
#     avg = sum / 3
#     print('{}의 평균은 {}입니다.'.format(student[i], avg))
#     sum = 0
#     avg = 0


# import random
#
# a = random.randint(1, 100)
# print(a)

# from random import randint
#
# a = randint(1, 101)
# print(a)


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# A = sorted(A)
# F = open('data_out.txt', 'w')
#
# for i in A:
#     data = str(i)
#     F.write(data)
# F.close()

# F = open('.txt', 'r')
#
# s = F.read()                  # 파일에서 문자열 읽기
# print(s)
# F.close()



f = open('about_python.txt', 'r')
sentences = []
i = 0

while True:
    data = f.readline()
    if not data:
        break
    else:
        numbering = '%i번 문장 ' % (i+1)
        data = numbering + data
        sentences.append(data)
        i+=1
f.close()

f = open('data/about_python.txt', 'w')
for i in range(len(sentences)):
     f.write(sentences[i])
f.close()

f = open('about_python.txt', 'r')
print(f.read())

f.close()

