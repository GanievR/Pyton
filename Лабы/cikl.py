stroka = "tadgdtrxxcb"
allsymb = []
flag=False
mas = []
stroka1 = []
for a in stroka:
    stroka1.append(a)
for i in stroka1:
    if i !=" ":
        count = stroka1.count(i)#количество повторений элемента в строке
        for j in mas:
            if j==i:
                flag=True
        if flag == False:
            print("Символ", i, "повторяется", count, "раз")
        mas.append(i)
        flag=False
    else:
        continue
