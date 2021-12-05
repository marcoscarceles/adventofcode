#!/usr/bin/env kscript



val windows = mutableListOf<MutableList<Int>>()
val first = readLine()!!.toInt()
windows.add(mutableListOf<Int>(first))
val second = readLine()!!.toInt()
windows[0].add(second)
windows.add(mutableListOf<Int>(second))

var current = Int.MAX_VALUE
var total = 0

generateSequence(::readLine).map(String::toInt).forEach {
    windows[windows.lastIndex].add(it)
    windows[windows.lastIndex-1].add(it)
    windows.add(mutableListOf<Int>(it))
    println(windows)
    if(windows[0].size == 3) {
        val next = windows.removeFirst().sum()
        println ("Comparing $current against $next")
        if (next > current) {
            total++
        }
        current = next
    }
}

print(total)

