#  Задача
# Вывести на экран:
# - сумму всех элементов списка
# - среднее арифметическое всех элементов списка
# - максимальное значение списка
# - минимальное значение списка
def asd(arr):
    summ=sum(arr)
    sr=sum(arr) / len(arr)
    minn =min(arr)
    maxx =max(arr)
    print(f'Сумма: {summ}')
    print(f'Среднее арифметическое: {sr}')
    print(f'Минимальное значение: {minn}')
    print(f'Максимальное значение: {maxx}')
    return(summ,sr,minn,maxx)
'''
first_arr=[]
for i in range(10):
    num=int(input(f"Введите {i+1} элемент:"))
    first_arr.append(num)
asd(first_arr)
'''
second_arr=[12,5,456,-15,64,54,-24]
asd(second_arr)
print("-"*41)
rif=asd(second_arr)[0]
ref=asd(second_arr)[1]
reff=asd(second_arr)[2]
refff=asd(second_arr)[3]
print(rif)
print(ref)
print(reff)
print(refff)
