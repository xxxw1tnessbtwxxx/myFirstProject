def declineExtremals(list1: list):
    copy = list1
    array = []
    min, max = int(input("Введите минимальное значение: ")), int(input("Введите максимальное значение: "))

    for i in list1:
        print(i)
        print(int(i) < 79 and i > 5)
        if int(i) < 79 and i > 5:
            array.append(i)

    print(list1, array, sep="\n")


a = [1, 2, 3, 4, 78, 79, 80]
declineExtremals(a)