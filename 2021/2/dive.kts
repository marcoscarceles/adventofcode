#!/usr/bin/env kscript

val final = generateSequence(::readLine).fold(Pair(0,0), { position, line ->
    val (direction, increase) = line.split(Regex("""\s+"""))

    when (direction) {
        "forward"   -> Pair(position.first + increase.toInt(), position.second)
        "up"        -> Pair(position.first, position.second - increase.toInt())
        "down"     -> Pair(position.first, position.second + increase.toInt())
        else        -> throw Exception("Unexpected direction [$direction]")
    }
})

print(final.first * final.second)