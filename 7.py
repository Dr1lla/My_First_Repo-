n = 6  # Висота піраміди

for i in range(n, 0, -1):  # Зовнішній цикл по рядках (починаємо з n і йдемо до 1)
    for j in range(i):  # Внутрішній цикл по кількості елементів у рядку
        print(j, end=" ")  # Виводимо числа від 0 до поточного значення i
    print()  # Перехід на новий рядок після завершення кожного рядка
