S = input("Введите строку: ")


def solution(word):
    S = changeWord(word)
    print(S)
    a = S[::-1]
    if S == a:
        print("Да, это палиндром", a)
    else:
        print("Ничего не получилось")


def changeWord(word, i=-1):
    for letter in word:
        i += 1
        if letter == "?":
            # print("индекс", i)
            # print("слово", word)
            # print("символ", letter)
            # print("буква", word[len(word) - 1 - i])
            if letter == word[len(word) - 1 - i]:
                word = word.replace(letter, "b", 1)
            else:
                word = word.replace(letter, word[len(word)-1-i], 1)
    return word


print(solution(S))

