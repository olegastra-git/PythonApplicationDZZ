# ������ 26:
# �������� ���������, ������� �� ���� ��������� ��� ����� A � B,
# � �������� ����� � � ����� ������� B � ������� ��������.

# x = int(input(" vvedite chislo a: "))
# y = int(input(" vvedite chislo b: "))

# def z(a, n):
#  if (n == 1):
#     return a
#  else:
#     return a * z(x, n - 1)
# print (z(x, y))

# ������ 28:
# �������� ����������� ������� sum(a, b), ������������ ����� ���� ����� ��������������� �����.
# �� ���� �������������� �������� ����������� ������ +1 � -1. ����� ������ ������������ �����.

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