# Задача 2: Найдите сумму цифр трехзначного числа.
n = int(input(""))
a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n % 10
print ("Сумаа цифр введенного числа равна:", a + b + c)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно, что Петя
#и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int (input ("Введите колличстов журавликов: ")) # вводим кол-во журавликово, которые сделали дети
x = s // 6                # число 6 т.к. это кол-во x в уравнении: x+x+4x=6x. т.к. Катя сделала: (Петя(х) + Сережа(х))*2 = 4х
print (x, "журавлик(ов)(а) сделал Петя") 
print (x*4, "журавлик(ов)(а) сделала Катя")
print (x, "журавлик(ов)(а) сделал Сережа")

#Счастливый билет
n = int(input("Введите номер Вашего билета: "))
a_6 = n % 10 
a_5 = n // 10 % 10
a_4 = n // 100 % 10
a_3 = n // 1000 % 10
a_2 = n // 10000 % 10
a_1 = n // 100000
if a_1 + a_2 + a_3 == a_4 + a_5 + a_6:
    print ("Ура! Вам попался счастлиыый билет!")
else:
    print ("Вам попался обычный билет, повезет в следующий раз")

#Шоколадка#задачу не понял
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print ('YES')
else:
    ('NO')