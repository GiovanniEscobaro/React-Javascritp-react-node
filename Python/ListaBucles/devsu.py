def find_duplicates(nums):
    duplicados = []
    for num in nums:
        if nums.count(num) > 1 and num not in duplicados:
            duplicados.append(num)
    return duplicados

# Prueba
lista = [8, 7, 10, 5, 1, 7, 5, 6, 2, 1, 4, 3, 2, 9, 8, 10]
print("Duplicados únicos:", find_duplicates(lista))


