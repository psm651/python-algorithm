import sys
N = int(sys.stdin.readline())
matrix = [sys.stdin.readline().split() for _ in range(N)]
bluePaper = 0
whitePaper = 0

def devidePaper(startX, startY, lineCount):
    global bluePaper, whitePaper
    type = matrix[startX][startY]
    shouldDevideMatrix = True

    for i in range(startX, startX + lineCount):
        if not shouldDevideMatrix:
            break
        for j in range(startY, startY + lineCount):
            if type != matrix[i][j]:
                shouldDevideMatrix = False
                devidePaper(startX, startY, lineCount // 2)
                devidePaper(startX + lineCount // 2, startY, lineCount // 2)
                devidePaper(startX, startY + lineCount // 2, lineCount // 2)
                devidePaper(startX + lineCount // 2, startY + lineCount // 2, lineCount // 2)
                break

    if shouldDevideMatrix:
        if type == '1':
            bluePaper += 1
        else:
            whitePaper += 1


devidePaper(0, 0, N)
print(whitePaper)
print(bluePaper)