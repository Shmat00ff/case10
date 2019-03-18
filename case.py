from turtle import *


def k(a,n):
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
    return k(a*0.9, n-1)

def tree(a,n):
    """ Двоичное дерево """
    if a > 5:
        forward(a)
        right(20)
        tree(a-15,n)
        left(40)
        tree(a-15,n)
        right(20)
        backward(a)

def koch(n, a):
    """ Кривая Коха """
    if n == 0:
        forward(a)
    else:
        koch(n-1, a/3)
        left(60)
        koch(n-1, a/3)
        right(120)
        koch(n-1, a/3)
        left(60)
        koch(n-1, a/3)

#снежинка коха

def led_1(n, a):
    """ Ледяной фрактал """
    if n == 0:
        forward(a)
    else:
        led_1(n - 1, a)
        left(90)
        led_1(n - 1, a / 2)
        right(180)
        led_1(n - 1, a / 2)
        left(90)
        led_1(n - 1, a)

def led_2(n, a):
    """ Второй ледяной """
    if n == 0:
        forward(a)
    else:
        led_2(n - 1, a * 2)
        left(120)
        led_2(n - 1, a)
        right(180)
        led_2(n - 1, a)
        left(120)
        led_2(n - 1, a)
        right(180)
        led_2(n - 1, a)
        left(120)
        led_2(n - 1, a * 2)

def mink(n, a):
    """ Кривая Минковского """
    if n == 0:
        forward(a)
    else:
        mink(n-1, a/4)
        left(90)
        mink(n-1, a/4)
        right(90)
        mink(n-1, a/4)
        right(90)
        mink(n-1, a / 4)
        mink(n - 1, a / 4)
        left(90)
        mink(n - 1, a / 4)
        left(90)
        mink(n - 1, a / 4)
        right(90)
        mink(n - 1, a / 4)

def levi(n, a):
    """ Кривая Леви """
    if n == 0:
        forward(d)
    else:
        left(45)
        levi(n - 1, d)
        right(90)
        levi(n-1, d)
        left(45)

# дракон

def main():
    up()
    goto(-100,0)
    down()
    b = int(input('Выбирите рекурсию (1-10):'))
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    if b == 3:
        koch(n, a)

main()