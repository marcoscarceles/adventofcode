#!/usr/bin/env kscript

fun List<Any>.half():Double = (this.size / 2.0)
fun List<Int>.toInt(): Int =
        this.reversed().withIndex().map { it.value * Math.pow(2.0, it.index.toDouble()) }.toList().sum().toInt()

fun getSummary(diagnostic: List<List<Int>>): List<Int> =
        diagnostic.reduce { acc, next ->
            acc.zip(next) { a, b -> a + b }
        }


fun getMostFrequent(diagnostic: List<List<Int>>): List<Int> =
        getSummary(diagnostic).map { if (it >= diagnostic.half()) 1 else 0 }


fun getLeastFrequent(diagnostic: List<List<Int>>): List<Int> =
        getSummary(diagnostic).map { if (it >= diagnostic.half()) 0 else 1 }


fun filterByRating(diagnostic: List<List<Int>>, reference: (List<List<Int>>) -> List<Int>): List<Int> =
        (0..diagnostic[0].size - 1).fold(diagnostic) { acc, i ->
            val filter = reference(acc)
            val match = acc.filter { it[i] == filter[i] }
//            println("""
//                ========================
//                --- Comparing
//                ${acc}
//                ---- Against
//                ${filter}[${i}] = ${filter[i]}
//                ---- Match
//                ${match}
//            """.trimIndent())
            if (match.size > 0) match else listOf(acc.first())
        }.first()

/**
 * Part 1
 */
val diagnostic = generateSequence(::readLine)
        .map { it.chunked(1) }
        .map { it.map(String::toInt) }
        .toList()


println("--------")
diagnostic.forEach(::println)
println("--------")

val gammaArray = getMostFrequent(diagnostic)

val epsilonArray = getLeastFrequent(diagnostic)

val gamma = gammaArray.toInt()

val epsilon = epsilonArray.toInt()

println("Gammma: $gamma * Epsilon: $epsilon = ${gamma * epsilon}")

/**
 * Part 2
 */

println("Diagnostics")
println(diagnostic.map { it.toInt() })

println("Getting oxygen ...")
val oxygen = filterByRating(diagnostic, this::getMostFrequent).toInt()
println("Getting co2 ...")
val co2 = filterByRating(diagnostic, this::getLeastFrequent).toInt()

println("oxygen: $oxygen * co2: $co2 = ${oxygen * co2}")


