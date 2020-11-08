baris = 10
kolom = baris

for bar in range(baris):
    for col1 in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
