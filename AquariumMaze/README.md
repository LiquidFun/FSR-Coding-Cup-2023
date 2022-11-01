# Aquarium Maze

## Statement

TODO: besser begründen

Again you are sitting in the 037 and enjoying a lecture, and you keep having very insightful thoughts about the lecture: ``what if the left wall of the 037 was made of an aquarium?!''. But a plain aquarium is boring, what if it had various walls inside of it. And then you realize if you were to manufacture it and then starting pouring in water from the top, that various parts of the aquarium might never be filled with water? You wonder, what is the maximum amount of water that such an aquarium can contain?

Given a grid representing the aquarium, you may add water to it using any of the top air parts of the aquarium. The water then will either move left, right, or down in the aquarium (it will not move up into air-pockets). 

## Input format

The first line contains 2 numbers, $r$ the number of rows ($3 <= r <= 100$), and $c$ the number of columns ($3 <= c <= 200$) in the aquarium.

Then $r$ rows follow, each with $c$ characters consisting of air \t{.} or glass \t{#}. It is guaranteed that the left and right columns and the bottom row consist of only glass \t{#} characters (i.e. no water can exit the aquarium once added).

## Output format

Print a single integer, the maximum number of litres that you can fill into the aquarium if you fill from the top.
