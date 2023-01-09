def je_suis_ton_pere(list):
    list2 = []
    for i in list:
        if i >= 40 and i % 5 >= 3:
            i += 5 - i % 5 
            list2.append(i)
        else:
            list2.append(i)
    return list2

list = [10,54,82,83]
print(je_suis_ton_pere(list))