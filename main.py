def on_forever():
    music.play(music.string_playable("C C C C D E C A ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C C C D C D E E ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C G A E G E C D ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C G E A B A G C ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("D C D E C C E G ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E E C E G G - - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("E E E C E G G C ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G C C C C D E E ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G C C E G C C C ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("G C - - - - - - ", 150),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C G G G C C E G ", 150),
        music.PlaybackMode.UNTIL_DONE)
    for index in range(10):
        basic.show_leds("""
            . # # # .
            # . . . .
            # # # # .
            # . . . .
            # . . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
        basic.pause(1000)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        basic.pause(1000)
        basic.show_leds("""
            # # . # #
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.pause(1000)
basic.forever(on_forever)
