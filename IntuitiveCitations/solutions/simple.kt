// Author: Brutenis Gliwa

fun main() {
    var n = readln().toInt()
    (1..n)
        .map { readln().split(' ')[1] }
        .sorted()
        .take(1)
        .map { println("$it et al.") }
}
