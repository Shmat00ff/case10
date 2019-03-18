from turtle import *


def k(d,n):
    """ Убегающий квадрат """
    if n == 0:
        return
    up()
    right(20)
    forward(d//4)
    down()
    for _ in range(4):
        forward(d)
        right(90)
    return k(d*0.9, n-1)

def tree(branchLen,t):
    """ Двоичное дерево """
    if branchLen > 5:
        forward(branchLen)
        right(20)
        tree(branchLen-15,t)
        left(40)
        tree(branchLen-15,t)
        right(20)
        backward(branchLen)

def koch(order, size):
    """ Кривая Коха """
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

#снежинка коха

def led_1(n, size):
    """ Ледяной фрактал """
    if n == 0:
        forward(size)
    else:
        led_1(n - 1, size)
        left(90)
        led_1(n - 1, size / 2)
        right(180)
        led_1(n - 1, size / 2)
        left(90)
        led_1(n - 1, size)

def led_2(n, size):
    """ Второй ледяной """
    if n == 0:
        forward(size)
    else:
        led_2(n - 1, size * 2)
        left(120)
        led_2(n - 1, size)
        right(180)
        led_2(n - 1, size)
        left(120)
        led_2(n - 1, size)
        right(180)
        led_2(n - 1, size)
        left(120)
        led_2(n - 1, size * 2)

def mink(order, size):
    """ Кривая Минковского """
    if order == 0:
        forward(size)
    else:
        mink(order-1, size/4)
        left(90)
        mink(order-1, size/4)
        right(90)
        mink(order-1, size/4)
        right(90)
        mink(order-1, size / 4)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)

def levi(n, d):
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