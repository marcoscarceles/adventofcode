#!/usr/bin/env kscript

val total = generateSequence(::readLine).map(String::toInt).fold(Pair(Int.MAX_VALUE,0)) { acc, next ->
    val increased = acc.first < next
    Pair(next, if (increased) acc.second+1 else acc.second )
}.second

print(total)

