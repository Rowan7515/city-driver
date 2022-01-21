@namespace
class SpriteKind:
    Object = SpriteKind.create()
def SetColour():
    global zSprite_Car, colour, colourChosen
    zSprite_Car = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                    . . . 2 4 2 2 2 2 2 2 c 2 . . . 
                    . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
                    . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
                    . 2 c 2 e e e e e e e b c 4 2 2 
                    . 2 2 e b b e b b b e e b 4 2 2 
                    . 2 e b b b e b b b b e 2 2 2 2 
                    . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
                    . e e e e e e f e e e f e 2 d d 
                    . e e e e e e f e e f e e e 2 d 
                    . e e e e e e f f f e e e e e e 
                    . e f f f f e e e e f f f e e e 
                    . . f f f f f e e f f f f f e . 
                    . . . f f f . . . . f f f f . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    zSprite_Car.set_flag(SpriteFlag.INVISIBLE, True)
    while colourChosen == 0:
        colour = game.ask_for_string("What colour? (b= blue, r= red, p= pink)", 1)
        if colour == "b":
            zSprite_Car.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                                . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                                . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                                . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                                . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                                . 6 8 b b b 8 b b b b 8 6 6 6 6 
                                . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                                . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                                . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                                . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                                . 8 f f f f 8 8 8 8 f f f 8 8 8 
                                . . f f f f f 8 8 f f f f f 8 . 
                                . . . f f f . . . . f f f f . . 
                                . . . . . . . . . . . . . . . .
            """))
            colourChosen = 1
        elif colour == "r":
            zSprite_Car.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 2 2 2 2 2 2 c 2 . . . 
                                . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
                                . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
                                . 2 c 2 e e e e e e e b c 4 2 2 
                                . 2 2 e b b e b b b e e b 4 2 2 
                                . 2 e b b b e b b b b e 2 2 2 2 
                                . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
                                . e e e e e e f e e e f e 2 d d 
                                . e e e e e e f e e f e e e 2 d 
                                . e e e e e e f f f e e e e e e 
                                . e f f f f e e e e f f f e e e 
                                . . f f f f f e e f f f f f e . 
                                . . . f f f . . . . f f f f . . 
                                . . . . . . . . . . . . . . . .
            """))
            colourChosen = 1
        elif colour == "p":
            zSprite_Car.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 3 3 3 3 3 3 3 3 . . . . 
                                . . . 3 d 3 3 3 3 3 3 c 3 . . . 
                                . . 3 c d 3 3 3 3 3 3 c c 3 . . 
                                . 3 c c d d d d d d 3 c c d 3 d 
                                . 3 c 3 a a a a a a a b c d 3 3 
                                . 3 3 a b b a b b b a a b d 3 3 
                                . 3 a b b b a b b b b a 3 3 3 3 
                                . a a 3 3 3 a 3 3 3 3 3 a 3 3 3 
                                . a a a a a a f a a a f a 3 d d 
                                . a a a a a a f a a f a a a 3 d 
                                . a a a a a a f f f a a a a a a 
                                . a f f f f a a a a f f f a a a 
                                . . f f f f f a a f f f f f a . 
                                . . . f f f . . . . f f f f . . 
                                . . . . . . . . . . . . . . . .
            """))
            colourChosen = 1
        else:
            game.splash("Invalid response")
def setVariables():
    global gameRunning, colourChosen, boostCharge, speed, maxSpeed, finish
    gameRunning = 0
    colourChosen = 0
    boostCharge = 100
    speed = 0
    maxSpeed = 2.5
    finish = 0
def countdown():
    global zSprite_3, zSprite_2, zSprite_1, zSprite_Go
    pause(200)
    zSprite_3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . . 
                    . . 2 a a a a a a a a a 2 . . . 
                    . . . 2 a a a a a a a a 2 . . . 
                    . . . . 2 2 2 2 2 2 a a 2 . . . 
                    . . . . . . . . . 2 a a 2 . . . 
                    . . . . . . . 2 2 2 a a 2 . . . 
                    . . . . . . 2 a a a a a 2 . . . 
                    . . . . . 2 a a a a a a 2 . . . 
                    . . . . . . 2 a a a a a 2 . . . 
                    . . . . . . . 2 2 2 a a 2 . . . 
                    . . . . . . . . . 2 a a 2 . . . 
                    . . . . 2 2 2 2 2 2 a a 2 . . . 
                    . . . 2 a a a a a a a a 2 . . . 
                    . . 2 a a a a a a a a a 2 . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . .
        """),
        SpriteKind.Object)
    zSprite_3.set_position(80, 60)
    pause(1000)
    zSprite_3.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . 2 2 2 2 2 2 2 . . . . . . 
                    . . 2 a a a a a a a 2 . . . . . 
                    . . 2 a a a a a a a a 2 . . . . 
                    . . . 2 2 2 2 2 2 a a a 2 . . . 
                    . . . . . . . . . 2 a a 2 . . . 
                    . . . . . . . . 2 a a a 2 . . . 
                    . . . . . . . 2 a a a a 2 . . . 
                    . . . . . . 2 a a a a 2 . . . . 
                    . . . . . 2 a a a a 2 . . . . . 
                    . . . . 2 a a a a 2 . . . . . . 
                    . . . 2 a a a a 2 . . . . . . . 
                    . . 2 a a a a 2 2 2 2 2 . . . . 
                    . . 2 a a a a a a a a a 2 . . . 
                    . . 2 a a a a a a a a a 2 . . . 
                    . . . 2 2 2 2 2 2 2 2 2 . . . .
        """),
        SpriteKind.Object)
    zSprite_2.set_position(80, 60)
    pause(1000)
    zSprite_2.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_1 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 . . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . 2 a a 2 . . . . . . . 
                    . . . . . . 2 2 . . . . . . . .
        """),
        SpriteKind.Object)
    zSprite_1.set_position(80, 60)
    pause(1000)
    zSprite_1.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_Go = sprites.create(img("""
            ...2222222222222222...............2222222222222222.............222......
                    ..222222222222222222.............222222222222222222...........22222.....
                    .222aaaaaaaaaaaaaa222...........222aaaaaaaaaaaaaa222..........22222.....
                    222aa222222222222aa222.........222aa222222222222aa222.........22a22.....
                    22aa22222222222222aa22.........22aa22222222222222aa22.........22a22.....
                    22a222..........222a22.........22a222..........222a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22222.........22a22............22a22.........22a22.....
                    22a22.............222..........22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22..........................22a22............22a22.........22a22.....
                    22a22....22222222222...........22a22............22a22.........22a22.....
                    22a22...2222222222222..........22a22............22a22.........22a22.....
                    22a22...22aaaaaaaaa222.........22a22............22a22.........22a22.....
                    22a22...2222222222aa22.........22a22............22a22.........22a22.....
                    22a22....2222222222a22.........22a22............22a22.........22a22.....
                    22a22...........222a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22a22.....
                    22a22............22a22.........22a22............22a22.........22222.....
                    22a22............22a22.........22a22............22a22.........22222.....
                    22a22............22a22.........22a22............22a22..........222......
                    22a222..........222a22.........22a222..........222a22...................
                    22aa22222222222222aa22.........22aa22222222222222aa22..........222......
                    222aa222222222222aa222.........222aa222222222222aa222.........22222.....
                    .222aaaaaaaaaaaaaa222...........222aaaaaaaaaaaaaa222..........22a22.....
                    ..222222222222222222.............222222222222222222...........22222.....
                    ...2222222222222222...............2222222222222222.............222......
        """),
        SpriteKind.Object)
    zSprite_Go.set_position(80, 60)
    pause(500)
    zSprite_Go.set_flag(SpriteFlag.INVISIBLE, True)
def timer():
    global time
    while not (finish == 1):
        time += 0.1
        pause(100)
    return time
def updateBoostBar(num: number):
    if num == 50:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 49:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 48:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 47:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 46:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 45:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 44:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 43:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 42:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 41:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 40:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 39:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 38:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 37:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 36:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 35:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 34:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 33:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 32:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 31:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 30:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 29:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 28:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 27:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 26:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 26:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 25:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 24:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 23:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 22:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 21:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 20:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 19:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 18:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 17:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 16:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 15:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 14:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 13:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 12:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 11:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 10:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 9:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 8:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 7:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 6:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 5:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 4:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    elif num == 3:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
    else:
        zSprite_boost_charge_bar.set_image(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                        b d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        b d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
                        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """))
xTrail = 0
time = 0
zSprite_Go: Sprite = None
zSprite_1: Sprite = None
zSprite_2: Sprite = None
zSprite_3: Sprite = None
finish = 0
maxSpeed = 0
boostCharge = 0
colour = ""
colourChosen = 0
gameRunning = 0
speed = 0
zSprite_Car: Sprite = None
zSprite_boost_charge_bar: Sprite = None
setVariables()
SetColour()
countdown()
zSprite_boost_charge_bar = sprites.create(img("""
        . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
    """),
    SpriteKind.Object)
zSprite_Car.set_flag(SpriteFlag.INVISIBLE, False)
controller.move_sprite(zSprite_Car, speed, 100)
tiles.set_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(zSprite_Car, assets.tile("""
    Start0
"""))
zSprite_Car.set_stay_in_screen(True)
scene.camera_follow_sprite(zSprite_Car)
gameRunning = 1
score = timer()
gameRunning = 0
game.splash(score)

def on_forever():
    global xTrail, speed, boostCharge, finish
    if gameRunning == 1:
        xTrail = zSprite_Car.x
        speed += (maxSpeed - speed) / 50
        zSprite_Car.x += speed
        if xTrail == zSprite_Car.x:
            speed = 0
        if controller.A.is_pressed() and boostCharge > 4:
            zSprite_Car.x += 2
            boostCharge += -1
        if boostCharge < 100:
            boostCharge += 0.1
        if boostCharge >= 100:
            boostCharge = 100
        boostCharge = Math.round(boostCharge * 10) / 10
        updateBoostBar(Math.round(boostCharge / 2))
        zSprite_boost_charge_bar.set_position(zSprite_Car.x - 50, zSprite_Car.y + 50)
        if zSprite_Car.tile_kind_at(TileDirection.CENTER, assets.tile("""
            Finish
        """)):
            finish = 1
forever(on_forever)
