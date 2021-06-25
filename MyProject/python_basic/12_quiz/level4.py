import random

words = ["apple", "banana", "orange", "melon", "pineapple"]
alphabet_lst = []
answer_lst = []

random_word = words[random.randint(0, len(words) - 1)]
for aword in random_word:
    alphabet_lst.append(aword)
    answer_lst.append("_")

cnt = 10
i = 1

while (i <= 10):
    alphabet = input("알파벳을 입력하세요 : ")

    # for idx in
    #
    # i += 1
