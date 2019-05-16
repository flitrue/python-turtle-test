#!/usr/bin/env python3
#encoding=utf-8
#author: flitrue

import turtle as t
import time

t.setup(400,400)
t.color("red", "yellow")
t.hideturtle()
t.speed(6)
t.penup()
t.goto(-100, 0)
t.pendown()
t.begin_fill()
for _ in range(36):
    t.forward(200)
    t.left(170)
time.sleep(1)
t.end_fill()
t.done()