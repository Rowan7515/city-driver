namespace SpriteKind {
    export const Object = SpriteKind.create()
}
function SetColour () {
    zSprite_Car = sprites.create(img`
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
        `, SpriteKind.Player)
    zSprite_Car.setFlag(SpriteFlag.Invisible, true)
    while (colourChosen == 0) {
        colour = game.askForString("What colour? (b= blue, r= red, p= pink)", 1)
        if (colour == "b") {
            zSprite_Car.setImage(img`
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
                `)
            colourChosen = 1
        } else if (colour == "r") {
            zSprite_Car.setImage(img`
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
                `)
            colourChosen = 1
        } else if (colour == "p") {
            zSprite_Car.setImage(img`
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
                `)
            colourChosen = 1
        } else {
            game.splash("Invalid response")
        }
    }
}
function setVariables () {
    gameRunning = 1
    colourChosen = 0
    boostCharge = 100
    speed = 0.2
    maxSpeed = 2.5
    finish = 0
    highScore = 0
    score = 0
    timeStart = 0
    timeEnd = 0
    time = 0
}
function countdown () {
    pause(200)
    zSprite_3 = sprites.create(img`
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
        `, SpriteKind.Object)
    zSprite_3.setPosition(80, 60)
    pause(1000)
    zSprite_3.setFlag(SpriteFlag.Invisible, true)
    zSprite_2 = sprites.create(img`
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
        `, SpriteKind.Object)
    zSprite_2.setPosition(80, 60)
    pause(1000)
    zSprite_2.setFlag(SpriteFlag.Invisible, true)
    zSprite_1 = sprites.create(img`
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
        `, SpriteKind.Object)
    zSprite_1.setPosition(80, 60)
    pause(1000)
    zSprite_1.setFlag(SpriteFlag.Invisible, true)
    zSprite_Go = sprites.create(img`
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
        `, SpriteKind.Object)
    zSprite_Go.setPosition(80, 60)
    pause(500)
    zSprite_Go.setFlag(SpriteFlag.Invisible, true)
}
function updateBoostBar (num: number) {
    if (num == 50) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 49) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 48) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 47) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 46) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 45) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 44) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 43) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 42) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 41) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 40) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 39) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 38) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 37) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 36) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 35) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 34) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 33) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 32) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 31) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 30) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 29) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 28) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 27) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 26) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 26) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 25) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 24) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 23) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 22) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 21) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 20) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 19) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 18) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 17) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 16) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 15) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 14) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 13) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 12) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 11) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 10) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 9) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 8) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 7) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 6) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 5) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 4) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else if (num == 3) {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b 6 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    } else {
        zSprite_boost_charge_bar.setImage(img`
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            b d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            b d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d b 
            . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
            `)
    }
}
let xTrail = 0
let zSprite_Go: Sprite = null
let zSprite_1: Sprite = null
let zSprite_2: Sprite = null
let zSprite_3: Sprite = null
let finish = 0
let maxSpeed = 0
let boostCharge = 0
let colour = ""
let colourChosen = 0
let highScore = 0
let timeEnd = 0
let score = 0
let timeStart = 0
let gameRunning = 0
let time = 0
let speed = 0
let zSprite_Car: Sprite = null
let zSprite_boost_charge_bar: Sprite = null
setVariables()
SetColour()
countdown()
zSprite_boost_charge_bar = sprites.create(img`
    . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
    b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
    b 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 b 
    . b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b . 
    `, SpriteKind.Object)
zSprite_Car.setFlag(SpriteFlag.Invisible, false)
controller.moveSprite(zSprite_Car, speed, 100)
tiles.setTilemap(tilemap`level1`)
tiles.placeOnRandomTile(zSprite_Car, assets.tile`Start0`)
zSprite_Car.setStayInScreen(true)
scene.cameraFollowSprite(zSprite_Car)
let zSprite_Time = textsprite.create(convertToText(time), 1, 15)
gameRunning = 1
timeStart = time
score = timeEnd - timeStart
if (score > highScore) {
    highScore = score
}
game.splash("Score: ", score)
game.splash("Highscore: ", highScore)
forever(function () {
    if (gameRunning == 1) {
        xTrail = zSprite_Car.x
        speed += (maxSpeed - speed) / 50
        zSprite_Car.x += speed
        if (xTrail == zSprite_Car.x) {
            speed = 0
        }
        if (controller.A.isPressed() && boostCharge > 4) {
            zSprite_Car.x += 2
            boostCharge += -1
        }
        if (boostCharge < 100) {
            boostCharge += 0.1
        }
        if (boostCharge >= 100) {
            boostCharge = 100
        }
        boostCharge = Math.round(boostCharge * 10) / 10
        updateBoostBar(Math.round(boostCharge / 2))
        zSprite_boost_charge_bar.setPosition(zSprite_Car.x - 50, zSprite_Car.y + 50)
        zSprite_Time.setPosition(zSprite_Car.x + 50, zSprite_Car.y + 50)
        if (zSprite_Car.tileKindAt(TileDirection.Center, assets.tile`Finish`)) {
            gameRunning = 0
            timeEnd = time
        }
    }
})
forever(function () {
    time += 0.1
    time = Math.round(time * 100) / 100
    pause(100)
})
