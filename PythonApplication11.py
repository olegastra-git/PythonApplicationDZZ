# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# x = int(input(" vvedite chislo a: "))
# y = int(input(" vvedite chislo b: "))

# def z(a, n):
#  if (n == 1):
#     return a
#  else:
#     return a * z(x, n - 1)
# print (z(x, y))

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(A, B):
 if (B==0):
    return A
    else:
  return sum(A+1,B-1)

A = int(input("Input A>>"))
print()
B = int(input("Input B>>"))
print()
if (A>=B):
 print (sum(A,B))
    else:
    print(sum(A,B))