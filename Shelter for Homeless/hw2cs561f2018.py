def spla_max(spla_week, spla_arr, spla_parking):
    count = 0
    pt = 0
    spla_arra = []
    spla_arra = spla_arr
    for ind, max in enumerate(spla_week):
        maxim = 0
        for m in max:
            maxim = maxim + int(m)
        if maxim > count:
            count = maxim
            pt = ind
            for i in range(0,7):
                if spla_parking[i] - int(spla_arra[pt][13+i]) < 0:
                    del spla_arra[pt]
                    del spla_week[pt]
                    count = 0
                    pt = 0
                    break;

    return spla_arr[pt]
def permute(list):
    global week_count
    maxim = 0
    final = ""

    for jnd in list:
        weeks = jnd[0][13:21]
        counter = 0
        kt = 0
        while True:
            if int(weeks[0]) <= week_count[0] and int(weeks[1]) <= week_count[1] and int(weeks[2]) <= week_count[2] and int(weeks[3]) <= week_count[3] and int(weeks[4]) <= week_count[4] and int(weeks[5]) <= week_count[5] and int(weeks[6]) <= week_count[6]:
                for cnt in range(7):
                    week_count[cnt] -= int(weeks[cnt])
                    counter += 1

                kt += 1
                weeks = jnd[kt][13:21]
            else:
                break
        if counter > maxim:
            maxim = counter
            final = jnd[0][0:5]

    return final

import itertools
inp = open("input.txt","r")
out = open('output.txt','w')

lines = inp.readlines()
#print(lines)

beds = lines[0]
parking = lines[1]

spla_parking = []
for index in range(0,7):
    spla_parking.append(int(parking))

lahsa_beds = []
for index in range(0,7):
    lahsa_beds.append(int(beds))

no_applicants_lahsa = int(lines[2])
lahsa = []
spla = []
for i in range(no_applicants_lahsa):
    lines[i + 3] = lines[i+3].strip('\n')
    lahsa.append(lines[i+3])

no_applicants_spla = int(lines[3 + no_applicants_lahsa])

for i in range(no_applicants_spla):
    lines[i + (4 + no_applicants_lahsa)] = lines[i + (4 + no_applicants_lahsa)].strip('\n')
    spla.append(lines[i+(4 + no_applicants_lahsa)])


tot_app = int(lines[4 + no_applicants_lahsa + no_applicants_spla]);
#print(tot_app)

applicants = []
index = []

for i in range(tot_app):
    lines[(5 + no_applicants_lahsa + no_applicants_spla) + i] = lines[(5 + no_applicants_lahsa + no_applicants_spla) + i].strip('\n')
    applicants.append(lines[(5 + no_applicants_lahsa + no_applicants_spla)+i])
    index.append(applicants[i][0:5])


spla_count  = []
lahsa_count = []
for i in spla:
    for j in applicants:
        if i[0:5] == j[0:5]:
            spla_count.append(j)


for i in lahsa:
    for j in applicants:
        if i[0:5] == j[0:5]:
            lahsa_count.append(j)

for i in spla_count:
        spla_parking[0] = spla_parking[0] - int(i[13])
        spla_parking[1] = spla_parking[1] - int(i[14])
        spla_parking[2] = spla_parking[2] - int(i[15])
        spla_parking[3] = spla_parking[3] - int(i[16])
        spla_parking[4] = spla_parking[4] - int(i[17])
        spla_parking[5] = spla_parking[5] - int(i[18])
        spla_parking[6] = spla_parking[6] - int(i[19])


for i in lahsa_count:
        lahsa_beds[0] = lahsa_beds[0] - int(i[13])
        lahsa_beds[1] = lahsa_beds[1] - int(i[14])
        lahsa_beds[2] = lahsa_beds[2] - int(i[15])
        lahsa_beds[3] = lahsa_beds[3] - int(i[16])
        lahsa_beds[4] = lahsa_beds[4] - int(i[17])
        lahsa_beds[5] = lahsa_beds[5] - int(i[18])
        lahsa_beds[6] = lahsa_beds[6] - int(i[19])

global week_count
week_count = spla_parking

index = [n for n in index if n not in lahsa]
index = [n for n in index if n not in spla]

app_final = []

for i in applicants:
    for j in index:
        if j == i[0:5]:
            app_final.append(i)


spla_lahsa_week = []
spla_lahsa_arr = []
spla_array = []
global count

num_app_final = []

for k in app_final:
    value = int(k[13])+int(k[14])+int(k[15])+int(k[16])+int(k[17])+int(k[18])+int(k[19])
    num_app_final.append(k[0:13]+str(value))

rem_arr = []
rem_week = []

if int(parking) <= 3:
    if spla_parking[0] <= 3 and spla_parking[1] <= 3 and spla_parking[2] <= 3 and spla_parking[3] <= 3 and spla_parking[4] <= 3 and spla_parking[5] <= 3 and spla_parking[6] <= 3:
        for i in app_final:
            if i[5] == 'F'and int(i[6:9]) > 17 and i[9] == 'N' and i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                spla_lahsa_week.append(i[13:20])
                spla_lahsa_arr.append(i)
            elif i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                rem_week.append(i[13:20])
                rem_arr.append(i)

        merged_list = spla_lahsa_arr + rem_arr

        if int(len(merged_list)) <= 10:

            my_list = list(itertools.permutations(merged_list))
            final = permute(my_list)
            out.write(final)

else:
    spla_lahsa_week = []
    spla_lahsa_arr = []
    spla_array = []
    rem_arr = []
    rem_week = []

    if spla_parking[0] >= 2 and spla_parking[1] >= 2 and spla_parking[2] >= 2 and spla_parking[3] >= 2 and spla_parking[4] >= 2 and spla_parking[5] >= 2 and spla_parking[6] >= 2:
        for i in app_final:
            if i[5] == 'F'and int(i[6:9]) > 17 and i[9] == 'N' and i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                spla_lahsa_week.append(i[13:20])
                spla_lahsa_arr.append(i)
            elif i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                rem_week.append(i[13:20])
                rem_arr.append(i)

        if spla_lahsa_arr:
            final = spla_max(spla_lahsa_week, spla_lahsa_arr, spla_parking)

        elif rem_arr:
                final = spla_max(rem_week, rem_arr, spla_parking)

        else:
            final = '00000'
        out.write(final[0:5])

    else:
        for i in app_final:
            if i[5] == 'F' and int(i[6:9]) > 17 and i[9] == 'N' and i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                spla_lahsa_week.append(i[13:20])
                spla_lahsa_arr.append(i)
            elif i[10] == 'N' and i[11] == 'Y' and i[12] == 'Y':
                rem_week.append(i[13:20])
                rem_arr.append(i)
        if spla_lahsa_arr:
            max_spla_lahsa = spla_max(spla_lahsa_week, spla_lahsa_arr, spla_parking)
        else:
            max_spla_lahsa = '00000000000000000000'

        if rem_arr:
            max_rem = spla_max(rem_week, rem_arr, spla_parking)
        else:
            max_rem = '00000000000000000000'

        sum = []

        for i in range(0,7):
            sum.append(int(max_spla_lahsa[13+i])+int(max_rem[13+i]))

        if sum[0] <= spla_parking[0] and sum[1] <= spla_parking[1] and sum[2] <= spla_parking[2] and sum[3] <= spla_parking[3] and sum[4] <= spla_parking[4] and sum[5] <= spla_parking[5] and sum[6] <= spla_parking[6]:
            f = int(max_spla_lahsa[13]) + int(max_spla_lahsa[14]) + int(max_spla_lahsa[15]) + int(max_spla_lahsa[16]) + int(
                max_spla_lahsa[17]) + int(max_spla_lahsa[18]) + int(max_spla_lahsa[19])
            m = int(max_rem[13]) + int(max_rem[14]) + int(max_rem[15]) + int(max_rem[16]) + int(max_rem[17]) + int(
                max_rem[18]) + int(max_rem[19])
            k = max(f, m)
            if k == f:
                if int(max_spla_lahsa[13]) <= spla_parking[0] and int(max_spla_lahsa[14]) <= spla_parking[1] and int(max_spla_lahsa[15]) <= spla_parking[2] and int(max_spla_lahsa[16]) <= spla_parking[3] and int(max_spla_lahsa[17]) <= spla_parking[4] and int(max_spla_lahsa[18]) <= spla_parking[5] and int(max_spla_lahsa[19]) <= spla_parking[6]:
                    final = max_spla_lahsa
                elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[4] and int(max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                    final = max_rem
                else:
                    final = '00000'
            elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[4] and int(max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                final = max_rem
            else:
                final = '00000'
        elif sum[0] > spla_parking[0] and sum[1] > spla_parking[1] and sum[2] > spla_parking[2] and sum[3] > spla_parking[3] and sum[4] > spla_parking[4] and sum[5] > spla_parking[5] and sum[6] > spla_parking[6]:
            f = int(max_spla_lahsa[13]) + int(max_spla_lahsa[14]) + int(max_spla_lahsa[15]) + int(max_spla_lahsa[16]) + int(
                max_spla_lahsa[17]) + int(max_spla_lahsa[18]) + int(max_spla_lahsa[19])
            m = int(max_rem[13]) + int(max_rem[14]) + int(max_rem[15]) + int(max_rem[16]) + int(max_rem[17]) + int(
                max_rem[18]) + int(max_rem[19])
            k = max(f, m)
            if k == f:
                if int(max_spla_lahsa[13]) <= spla_parking[0] and int(max_spla_lahsa[14]) <= spla_parking[1] and int(max_spla_lahsa[15]) <= spla_parking[2] and int(max_spla_lahsa[16]) <= spla_parking[3] and int(max_spla_lahsa[17]) <= spla_parking[4] and int(max_spla_lahsa[18]) <= spla_parking[5] and int(max_spla_lahsa[19]) <= spla_parking[6]:
                    final = max_spla_lahsa
                elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[4] and int(max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                    final = max_rem
                else:
                    final = '00000'
            elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[4] and int(max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                final = max_rem
            else:
                final = '00000'

        else:
            f = int(max_spla_lahsa[13]) + int(max_spla_lahsa[14]) + int(max_spla_lahsa[15]) + int(max_spla_lahsa[16]) + int(max_spla_lahsa[17]) + int(max_spla_lahsa[18]) + int(max_spla_lahsa[19])
            m = int(max_rem[13]) + int(max_rem[14]) + int(max_rem[15]) + int(max_rem[16]) + int(max_rem[17]) + int(max_rem[18]) + int(max_rem[19])
            k = max(f, m)
            if k == f:
                if int(max_spla_lahsa[13]) <= spla_parking[0] and int(max_spla_lahsa[14]) <= spla_parking[1] and int(
                        max_spla_lahsa[15]) <= spla_parking[2] and int(max_spla_lahsa[16]) <= spla_parking[3] and int(
                        max_spla_lahsa[17]) <= spla_parking[4] and int(max_spla_lahsa[18]) <= spla_parking[5] and int(
                        max_spla_lahsa[19]) <= spla_parking[6]:
                    final = max_spla_lahsa
                elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= \
                        spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[
                    4] and int(max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                    final = max_rem
                else:
                    final = '00000'
            elif int(max_rem[13]) <= spla_parking[0] and int(max_rem[14]) <= spla_parking[1] and int(max_rem[15]) <= \
                    spla_parking[2] and int(max_rem[16]) <= spla_parking[3] and int(max_rem[17]) <= spla_parking[4] and int(
                    max_rem[18]) <= spla_parking[5] and int(max_rem[19]) <= spla_parking[6]:
                final = max_rem
            else:
                final = '00000'

        print('iam final')
        if final == '00000000000000000000':
            final = '00000'
        out.write(final[0:5])