weight = int(input())
plastic_bag = weight // 5
while plastic_bag >= 0:
    surplus = weight - (plastic_bag * 5)
    if surplus % 3 == 0:
        plastic_bag += surplus //3
        print(plastic_bag)
        break
    elif surplus % 3 != 0:
        if plastic_bag == 0:
            print(-1)
            break
        plastic_bag -= 1
