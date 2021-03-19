name = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu"
counter = dict()
counted = list()
for ltr in name.lower():
    if ltr not in counted:
        counted.append(ltr)
        counter[ltr] = 1
    else:
        counter[ltr] += 1

print(counter)
