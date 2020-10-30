def drop_duplicates(original):

    new = [original[0]]
    for i in range(1, len(original)):
        adding = True
        for j in range(len(new)):
            if original[i] == new[j]:
                adding = False
        if adding:
            new.append(original[i])
    return new

if __name__ == '__main__':
    print(drop_duplicates([1, 2, 3, 1]))
    print(drop_duplicates([1, 3, 2, 1, 5, 3, 5, 1, 4]))
    print(drop_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 10]))


# Асимптотическая сложность данной функции - O(n^2)
# Грубо говоря, для каждого из n элементов оригинального массива (не считая первого)
# мы просматриваем до n-1 элементов нового массива,
# чтобы понять, не собираемся ли мы добавить туда дубликат.
# Получается до (n - 1)^2 операций.
# В O-нотации нас интересует только самый быстрорастущий член - n^2.
