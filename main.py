def fibb(n):
    result = [1, 1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])

    return result

print("Ciąg Fibonnaciego:")
print("Wynik = " + str(fibb(12)) + ".")
print("Aleksandra Kobylska --- IMST2.1.2")