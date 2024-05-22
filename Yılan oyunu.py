import turtle
import time
import random

Oyun_ekranı = turtle.Screen()
Oyun_ekranı.title("Snake Game")
Oyun_ekranı.setup(width=1000, height=700)
Oyun_ekranı.bgcolor("black")
Oyun_ekranı.tracer(0)

Yılan_kafası = turtle.Turtle()
Yılan_kafası.speed(0)
Yılan_kafası.color("green")
Yılan_kafası.shape('circle')
Yılan_kafası.penup()
Yılan_kafası.goto(0,0)
Yılan_kafası.direction = 'stop'

Yılan_hızı = 0.1

yem = turtle.Turtle()
yem.speed(0)
yem.color("red")
yem.shape("circle")
yem.penup()
yem.goto(0,100)
yem.shapesize(1,1)

kuyruk = []

Puan = 0
puan_tahtası = turtle.Turtle()
puan_tahtası.speed(0)
puan_tahtası.color("orange")
puan_tahtası.shape('square')
puan_tahtası.penup()
puan_tahtası.goto(0,300)
puan_tahtası.hideturtle()
puan_tahtası.write('Score : {}'.format(Puan), align='center', font=('Courier',30,'normal'))


def hareket():
    if Yılan_kafası.direction == 'up':
        y = Yılan_kafası.ycor()
        Yılan_kafası.sety(y+20)
    if Yılan_kafası.direction == 'down':
        y = Yılan_kafası.ycor()
        Yılan_kafası.sety(y-20)
    if Yılan_kafası.direction == 'right':
        x = Yılan_kafası.xcor()
        Yılan_kafası.setx(x+20)
    if Yılan_kafası.direction == 'left':
        x = Yılan_kafası.xcor()
        Yılan_kafası.setx(x-20)

def Yukari_git():
    if Yılan_kafası.direction != 'down':
        Yılan_kafası.direction = 'up'
def Aşağı_git():
    if Yılan_kafası.direction != 'up':
        Yılan_kafası.direction = 'down'
def saga_git():
    if Yılan_kafası.direction != 'left':
        Yılan_kafası.direction = 'right'
def sola_git():
    if Yılan_kafası.direction != 'right':
        Yılan_kafası.direction = 'left'

Oyun_ekranı.listen()
Oyun_ekranı.onkey(Yukari_git,'Up')
Oyun_ekranı.onkey(Aşağı_git,'Down')
Oyun_ekranı.onkey(sola_git,'Left')
Oyun_ekranı.onkey(saga_git,'Right')

while True:
    Oyun_ekranı.update()

    if Yılan_kafası .xcor() > 480 or Yılan_kafası .xcor() < -480 or Yılan_kafası .ycor() > 335 or Yılan_kafası .ycor() < -332:
        time.sleep(1)
        Yılan_kafası.goto(0,0)
        Yılan_kafası.direction = 'stop'

        for i in kuyruk:
            i.goto((5000,5000))
        kuyruk = []
        Puan = 0
        puan_tahtası.clear()
        Yılan_hızı = 0.1

    if Yılan_kafası.distance(yem) < 15:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        yem.goto(x,y)

        Puan += 10
        puan_tahtası.clear()
        puan_tahtası.write('Score : {}'.format(Puan), align='center', font=('Courier', 30, 'normal'))

        Yılan_hızı = Yılan_hızı - 0.001

        ek_kuyruk = turtle.Turtle()
        ek_kuyruk.speed(0)
        ek_kuyruk.shape('circle')
        ek_kuyruk.color('green')
        ek_kuyruk.penup()
        if len(kuyruk) != 0:
            ek_kuyruk.goto(kuyruk[-1].xcor(), kuyruk[-1].ycor())
        else:
            ek_kuyruk.goto(Yılan_kafası.xcor(), Yılan_kafası.ycor())
        kuyruk.append(ek_kuyruk)

    for i in range(len(kuyruk) - 1, 0, -1):
        x = kuyruk[i-1].xcor()
        y = kuyruk[i-1].ycor()
        kuyruk[i].goto(x,y)

    if len(kuyruk) > 0:
        x = Yılan_kafası.xcor()
        y = Yılan_kafası.ycor()
        kuyruk[0].goto(x,y)

    for çarpışma in kuyruk[1:]:
        if Yılan_kafası.distance(çarpışma) < 20:
            time.sleep(1)
            Yılan_kafası.goto(0,0)
            Yılan_kafası.direction = 'stop'
            for çarpışma in kuyruk:
                çarpışma.goto(1000, 1000)
            kuyruk.clear()
            Puan = 0
            puan_tahtası.clear()
            Yılan_hızı = 0.1

    hareket()
    time.sleep(Yılan_hızı)
