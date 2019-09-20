def attack(matrix, row, col):
    for b in range(col):
        if matrix[row][b] == 1:
            return False

    a, b = row, col
    while a >= 0 and b >= 0:
        if matrix[a][b] == 1:
            return False
        a -= 1
        b -= 1

    x, y = row, col
    while x < size and y >= 0:
        if matrix[x][y] == 1:
            return False
        x += 1
        y -= 1

    return True


def nqueens(matrix, j):
    if j >= size:
        return

    for i in range(size):
            if attack(matrix, i, j):
                matrix[i][j] = 1
                if j == size - 1:
                    print_max(matrix)
                    matrix[i][j] = 0
                    return
                nqueens(matrix, j + 1)
                matrix[i][j] = 0


def print_max(matrix):
    global maxim
    global count
    count = 0
    for g in range(size):
        for h in range(size):
            boa[g][h] = matrix[g][h]
    for a in range(size):
        for b in range(size):
            if boa[a][b] == 1:
                count = count + val[a][b]
                if count > maxim:
                    maxim = count

def eliminate(row,col):
    if mat[row][col] == 0:
        return False
    else:
        for i in range(size):
            for j in range(size):
                mat[row][j] = 0
                mat[i][col] = 0
                if (row-col) == (i-j):
                    mat[i][j] = 0
                if (row+col) == (i+j):
                    mat[i][j] = 0
        return True

def initialize(mat):
    for i in range(size):
        for j in range(size):
            mat[i][j]=1;

inp = open("input.txt","r")
lines = inp.readlines()
global size

size = lines[0]
p = lines[1]
s = lines[2]

size = int(size)
p = int(p)
s = int(s)

last =((s*12)+2)
inp.close()
inp = open("input.txt","r+")
for g, h in enumerate(inp):
    if g == last:
        inp.write('\n')

inp.close()
inp = open("input.txt","r")
out = open("output.txt", "w")
lines = inp.readlines()

dic={}

keys = lines[3:]

del keys[-1]
keys =  map(str, keys)

for ki in keys:
    ki = ki.strip('\r\n')
    ki = ki.strip()
    if ki not in dic:
        dic[ki] = 1
    else:
        dic[ki] = dic[ki] + 1


if size == p:
    global val
    global boa

    matrix = [[0 for x in range(size)] for y in range(size)]
    val = [[0 for x in range(size)] for y in range(size)]
    boa = [[0 for x in range(size)] for y in range(size)]


    for t in dic:
        r1,c1 = t.split(',')
        vr = int(r1)
        vc = int(c1)
        val[vr][vc] = dic[t]

    global maxim
    global count
    count = 0
    maxim = 0

    nqueens(matrix, 0)
    out.write(str(maxim))
    out.write('\n')
else:
    import operator
    maxim = 0
    mat = [[0 for x in range(size)] for y in range(size)]
    initialize(mat)
    sorted_d = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    for a1 in sorted_d:
            initialize(mat)
            police_score = 0
            k1 = a1[0]
            v1 = a1[1]
            i1,j1 = k1.split(",")
            j1 = j1.strip('\n\r')

            row1 = int(i1)
            col1 = int(j1)

            bol = eliminate(row1, col1)
            if bol == True:
                police_score = police_score + v1
                if p == 1:
                    if police_score > maxim:
                        maxim = police_score

                if p > 1:
                    for a2 in sorted_d:
                        k2 = a2[0]
                        v2 = a2[1]

                        i2,j2 = k2.split(",")
                        j2 = j2.strip('\n\r')

                        row2 = int(i2)
                        col2 = int(j2)

                        bol = eliminate(row2, col2)
                        if bol == True:
                            police_score = police_score + v2

                            if p == 2:
                                if police_score > maxim:
                                    maxim = police_score
                            if p > 2:
                                for a3 in sorted_d:
                                    k3 = a3[0]
                                    v3 = a3[1]

                                    i3, j3 = k3.split(",")
                                    j3 = j3.strip('\n\r')

                                    row3 = int(i3)
                                    col3 = int(j3)
                                    bol = eliminate(row3, col3)
                                    if bol == True:
                                        police_score = police_score + v3

                                        if p == 3:
                                            if police_score > maxim:
                                                maxim = police_score

                                        if p > 3:
                                            for a4 in sorted_d:
                                                k4 = a4[0]
                                                v4 = a4[1]

                                                i4, j4 = k4.split(",")
                                                j4 = j4.strip('\n\r')

                                                row4 = int(i4)
                                                col4 = int(j4)
                                                bol = eliminate(row4, col4)
                                                if bol == True:
                                                    police_score = police_score + v4

                                                    if p == 4:
                                                        if police_score > maxim:
                                                            maxim = police_score
                                                    if p > 4:
                                                        for a5 in sorted_d:
                                                            k5 = a5[0]
                                                            v5 = a5[1]

                                                            i5, j5 = k5.split(",")
                                                            j5 = j5.strip('\n\r')

                                                            row5 = int(i5)
                                                            col5 = int(j5)
                                                            bol = eliminate(row5, col5)
                                                            if bol == True:
                                                                police_score = police_score + v5

                                                                if p == 5:
                                                                    if police_score > maxim:
                                                                        maxim = police_score

                                                                initialize(mat)
                                                                bol = eliminate(row1, col1)
                                                                bol = eliminate(row2, col2)
                                                                bol = eliminate(row3, col3)
                                                                bol = eliminate(row4, col4)
                                                                police_score = police_score - v5

                                                    initialize(mat)
                                                    bol = eliminate(row1, col1)
                                                    bol = eliminate(row2, col2)
                                                    bol = eliminate(row3, col3)
                                                    police_score = police_score - v4

                                        initialize(mat)
                                        bol = eliminate(row1, col1)
                                        bol = eliminate(row2, col2)
                                        police_score = police_score - v3

                            initialize(mat)
                            bol = eliminate(row1, col1)
                            police_score = police_score - v2

    out.write(str(maxim))
    out.write('\n')
