  #  Сложный (С) Иван Краснов ИИ-71
  # 1.  Напишите алгоритм для подсчета суммы положительных элементов в списке.
import random
try:
    num1 = input().split("Введите числа")
    num1 = [int(i) for i in num1]
    sum = 0
    for elem in num1:
        if elem > 0:
            sum += elem
    print(sum)


  #  2.  Пользователь вводит число. Определить принадлежит ли это число заданному промежутку [а,b].
    num1 = int(input())
    num2 = int(input())
    num_select = int(input())
    if num_select >= num1 and num_select <= num2:
        print('true')
    else:
        print('false')


  #  3. Сгенерируйте n случайных чисел. Найдите максимальное и минимальное число.
    size_lst = int(input())
    lst = []
    for i in range(size_lst):
        lst.append(random.randint(1, 9))
        lst.sort()
    m_max = lst[0]
    m_min = lst[0]
    for i in lst:
        if m_max < i:
            m_max = i
        if m_min > i:
            m_min = i
    print(f'Максимальное: {m_max}', f'Минимальное: {m_min}')
except:
    print('Error:SymbholError')