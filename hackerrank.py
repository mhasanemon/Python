if __name__ == '__main__':
    list = []
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        scorelist.append(score)
        list.append([name,score])
    scorelist.sort()
    print(scorelist[2])

    for student in list:
        if student[1] is scorelist[-2]:
            print(student[0])

