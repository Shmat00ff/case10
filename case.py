"""Case-study #10 рекурсии
Разработчики: Shmatov D. 70%, Bayanova A. 70% """


from turtle import *

def kvdrt(a, n):
    """ Убегающий квадрат """
    if n == 0:
        return
    up()
    right(20)
    forward(a//4)
    down()
    for _ in range(4):
        forward(a)
        right(90)
    return kvdrt(a * 0.9, n-1)

def binary_tree(a, n):
    """ Двоичное дерево """
    if a > 5:
        forward(a)
        right(20)
        binary_tree(a-15, n)
        left(40)
        binary_tree(a-15, n)
        right(20)
        backward(a)

def koch_curve(n, a):
    """ Кривая Коха """
    if n == 0:
        forward(a)
    else:
        koch_curve(n-1, a/3)
        left(60)
        koch_curve(n-1, a/3)
        right(120)
        koch_curve(n-1, a/3)
        left(60)
        koch_curve(n-1, a/3)

#снежинка коха

def fractal1(n, a):
    """ Ледяной фрактал """
    if n == 0:
        forward(a)
    else:
        fractal1(n - 1, a)
        left(90)
        fractal1(n - 1, a / 2)
        right(180)
        fractal1(n - 1, a / 2)
        left(90)
        fractal1(n - 1, a)

def fractal2(n, a):
    """ Второй ледяной """
    if n == 0:
        forward(a)
    else:
        fractal2(n - 1, a * 2)
        left(120)
        fractal2(n - 1, a)
        right(180)
        fractal2(n - 1, a)
        left(120)
        fractal2(n - 1, a)
        right(180)
        fractal2(n - 1, a)
        left(120)
        fractal2(n - 1, a * 2)

def minkovsky_curve(n, a):
    """ Кривая Минковского """
    if n == 0:
        forward(a)
    else:
        minkovsky_curve(n-1, a/4)
        left(90)
        minkovsky_curve(n-1, a/4)
        right(90)
        minkovsky_curve(n-1, a/4)
        right(90)
        minkovsky_curve(n-1, a / 4)
        minkovsky_curve(n - 1, a / 4)
        left(90)
        minkovsky_curve(n - 1, a / 4)
        left(90)
        minkovsky_curve(n - 1, a / 4)
        right(90)
        minkovsky_curve(n - 1, a / 4)

def levi_curve(n, a):
    """ Кривая Леви """
    if n == 0:
        forward(a)
    else:
        left(45)
        levi_curve(n - 1, a)
        right(90)
        levi_curve(n-1, a)
        left(45)

# дракон

def main():
    up()
    goto(-100,0)
    down()
    b = int(input('Выбирите рекурсию (1-9):'))
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    if b == 1:
        kvdrt(a,n)
    if b == 2:
        binary_tree(a, n)
    if b == 3:
        koch_curve(n, a)
    if b == 5:
        fractal1(n, a)
    if b == 6:
        fractal2(n, a)
    if b == 7:
        minkovsky_curve(n, a)
    if b == 8:
        levi_curve(n, a)




main()