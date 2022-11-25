# Aquarium Maze

## Statement

Again, you are sitting in the lecture hall 037 and enjoying a thoroughly exciting lecture; but you can't help it, your mind starts to drift into the depths of your thoughts. At first you wonder why the professor picked that font in the slides, then you remember that you forgot to do the maths homework for yesterday. After some more deep insights, most of which you have already left behind you in a forgotten realm, you catch yourself in the blue with the remarkably appealing question: ``What if the wall behind the professor was made of an aquarium?!''

It is too late to listen now, you note to yourself, this is now a question of utmost priority. You start the inception process of such an undertaking, making various improvements on the plan. You realize that a plain aquarium is boring, what if it had various walls inside of it? And then you grasp that if you were to manufacture it and then starting pouring in water from the top, that various parts of the aquarium might never be filled with water, because air-pockets would form! You wonder, what is the maximum amount of water that such an aquarium can contain?

You are given a grid representing a 2D aquarium, each character represents 1 litre of volume. You may add water to it using any of the air parts in the first row of the aquarium. The water added in such a way, will then either flow left, right, or down in the aquarium (it will not move up into air-pockets). What is the maximum number of litres you can add to the aquarium by filling it with any of the air openings in the first row?

## Input format

The first line contains 2 numbers, $r$ the number of rows ($3 <= r <= 100$), and $c$ the number of columns ($3 <= c <= 200$) in the aquarium.

Then $r$ rows follow, each with $c$ characters consisting of air \t{.} or glass \t{#}. It is guaranteed that the left and right columns and the bottom row consist of only glass \t{#} characters (i.e. no water can exit the aquarium once added).

## Output format

Print a single integer, the maximum number of litres that you can fill into the aquarium if you fill it from all of the openings in the first row of the aquarium.
