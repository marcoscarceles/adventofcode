#!/usr/bin/env kscript

data class Controls(val aim:Int, val x: Int, val y: Int)

val final = generateSequence(::readLine).fold(Controls(0,0,0), { controls, line ->
    val (direction, increase) = line.split(Regex("""\s+"""))

    when (direction) {
        "up"        -> { val up = increase.toInt(); controls.copy(aim = controls.aim - up) }
        "down"      -> { val down = increase.toInt(); controls.copy(aim = controls.aim + down) }
        "forward"   -> { val forward = increase.toInt(); controls.copy(x = controls.x + forward, y = controls.y + controls.aim*forward) }
        else        -> throw Exception("Unexpected direction [$direction]")
    }
})

print(final.x * final.y)