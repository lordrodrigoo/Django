# for k in range(0, 4, -1):
#     print(k)


# def e(b):
#     a = b * b 
#     return a 

# a = 10 
# e(a)
# e(a)
# print(e(a))

# lista = [x + 5 for x in [0, 1, 2, 3, 4, 5] if x < 3]
# print(lista)


# def inicio(a, b, c):

#     a = int(input('1° lado: '))
#     b = int(input('2° lado: '))
#     c = int(input('3° lado: '))

#     if a == b and a == c:
#         print('Caso 1 ')
    
#     elif a == b or b ==c or c == a:
#         print('caso 2 ')
    
#     else:
#         print('Caso 3 ')
    

# inicio(10, 11, 11)


# l = range(0, 12)
# for num in l:
#     print(num, end=' ')

# def foo(n):
#     if n > 1:
#         return n * foo(n-1)
#     return n 

# print(foo(4))

# num = 10 
# num += 1
# num = num + 2 * 5 

# # print(num)
# print(num // 7)
# print(num %  5)
# print(num %  7)

# a = 0
# b = 2 

# while b < 20:
#     a, b = b, a + b + 1 
#     print(b)

# def foo(a):
#     return a + a + a 

# b = 1
# print(foo(b))
# print(foo(b))
# print(foo(b))


def fc(x, y):
    s = 0
    a = x.lower()
    for i in a:
        if (i == y) :
            s = s + 1 
    return s 

a = 'Aracajú/Sergipe'
x = fc(a, 'a') * 100
y = fc(a, 'e') * 10 
z = fc(a, 'i')

print(x + y + z)