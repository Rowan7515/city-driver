@namespace
class SpriteKind:
    Object = SpriteKind.create()
def SetColour():
    global zSprite_Red, zSprite_Purple, zSprite_Blue, zSprite_Cursor, zSprite_Car, zSprite_boost_charge_bar, colourChosen
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    """))
    zSprite_Red = sprites.create(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        SpriteKind.player)
    zSprite_Red.set_position(30, 60)
    zSprite_Purple = sprites.create(img("""
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
        """),
        SpriteKind.Object)
    zSprite_Purple.set_position(80, 60)
    zSprite_Blue = sprites.create(img("""
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        """),
        SpriteKind.Object)
    zSprite_Blue.set_position(130, 60)
    zSprite_Cursor = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . 1 1 d d d d 1 . . . . . 
                    . . . . 1 d d d d d d 1 . . . . 
                    . . . . 1 d d d d d d 1 . . . . 
                    . . . . 1 d d d d d d 1 . . . . 
                    . . . . 1 d d d d d d 1 . . . . 
                    . . . . 1 1 d d d d 1 1 . . . . 
                    . . . . . 1 1 1 1 1 1 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.Object)
    zSprite_Cursor.set_position(80, 80)
    controller.move_sprite(zSprite_Cursor)
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
    zSprite_boost_charge_bar = sprites.create(img("""
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
                    b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
                    b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
                    . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b .
        """),
        SpriteKind.Object)
    zSprite_Car.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_boost_charge_bar.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_Cursor.set_position(80, 80)
    while colourChosen == 0:
        if controller.A.is_pressed() and zSprite_Cursor.overlaps_with(zSprite_Purple):
            colourChosen = 1
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
        elif controller.A.is_pressed() and zSprite_Cursor.overlaps_with(zSprite_Red):
            colourChosen = 1
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
        elif controller.A.is_pressed() and zSprite_Cursor.overlaps_with(zSprite_Blue):
            colourChosen = 1
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
        else:
            pause(10)
    zSprite_Cursor.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_Purple.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_Red.set_flag(SpriteFlag.INVISIBLE, True)
    zSprite_Blue.set_flag(SpriteFlag.INVISIBLE, True)
def setVariables():
    global gameRunning, colourChosen, boostCharge, speed, maxSpeed
    gameRunning = 0
    colourChosen = 0
    boostCharge = 100
    speed = 0
    maxSpeed = 2.5
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
zSprite_Go: Sprite = None
zSprite_1: Sprite = None
zSprite_2: Sprite = None
zSprite_3: Sprite = None
maxSpeed = 0
speed = 0
boostCharge = 0
colourChosen = 0
zSprite_Blue: Sprite = None
zSprite_Purple: Sprite = None
zSprite_Red: Sprite = None
zSprite_boost_charge_bar: Sprite = None
zSprite_Cursor: Sprite = None
zSprite_Car: Sprite = None
gameRunning = 0
setVariables()
SetColour()
countdown()
gameRunning = 1
zSprite_Car.set_flag(SpriteFlag.INVISIBLE, False)
controller.move_sprite(zSprite_Cursor, 0, 0)
controller.move_sprite(zSprite_Car, 0, 100)
tiles.set_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(zSprite_Car, assets.tile("""
    Start
"""))
zSprite_Car.set_stay_in_screen(True)
scene.camera_follow_sprite(zSprite_Car)
zSprite_boost_charge_bar.set_flag(SpriteFlag.INVISIBLE, False)

def on_forever():
    global xTrail, speed, boostCharge
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
forever(on_forever)
