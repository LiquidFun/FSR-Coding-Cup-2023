// Author: Brutenis Gliwa

fun main() {
    val (n, h) = readln().split(" ").map { it.toInt() }
    val solved = (1..n)
        .map { readln().toInt() }
        .sorted()
        .scan(0) { s, e -> s+e }
        .filter { it <= h * 60 }
        .scan(0) { s, e -> s+e }
    println("${solved.size-2} ${solved.last()}")
}
