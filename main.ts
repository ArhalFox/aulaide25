basic.forever(function () {
    music.play(music.stringPlayable("C C C C D E C A ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C C C D C D E E ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C G A E G E C D ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C G E A B A G C ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("D C D E C C E G ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("E E C E G G - - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("E E E C E G G C ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("G C C C C D E E ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("G C C E G C C C ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("G C - - - - - - ", 150), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C G G G C C E G ", 150), music.PlaybackMode.UntilDone)
    for (let index = 0; index < 10; index++) {
        basic.showLeds(`
            . # # # .
            # . . . .
            # # # # .
            # . . . .
            # . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            `)
        basic.pause(1000)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        basic.pause(1000)
        basic.showLeds(`
            # # . # #
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            `)
        basic.pause(1000)
    }
})
