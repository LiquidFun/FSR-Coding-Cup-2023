// Author: Brutenis Gliwa

fun main() {
    val n = readln().toInt()
    val is_full = (1..n)
        .map { readln() }
        .joinToString("")
        .lowercase()
        .filter { it !in ":' " }
        .toHashSet()
        .size == 26
    println(if (is_full) "yes" else "no")
}
