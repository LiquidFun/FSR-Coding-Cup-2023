# Keyboard Robot

## Statement

Everyone knows that the most important thing for a programmer is their typing speed! And you have been on a journey to improve your typing speed for a while, employing the fastest typing method known to man: 2 finger-typing. You have tested various keyboard layouts, such as Qwerty, Colemak, Dvorak and so on. But none of these are good enough for, you so you have decided to design your own. To streamline this process you have also created a robot which is used to test such a keyboard layout. Of course such a robot only has 2 mechanical fingers, which matches your superior typing preference.

Given a 6x6 keyboard layout you have designed and a sequence of characters, calculate the minimum possible distance travelled by 2 mechanical fingers in order to type that character sequence. Assume that fingers may not travel diagonally, only in a straight line horizontally or vertically. The distance between two adjacent keyboard buttons is 1, therefore the maximum distance on the keyboard between the top-left and bottom-right buttons is $5+5 = 10$.

## Input format

The first 6 lines contain your keyboard layout, each of those lines contains exactly 6 characters. Among these 36 characters it is guaranteed that each letter in the English alphabet appears exactly once. Additionally, the space-bar is encoded as a underscore \t{_}. Dots (\t{.}) denote empty parts of the keyboard and may be ignored.

The next line contains a string $s$ ($1 <= ||s|| <= 200$) consisting of letters in the english alphabet + spaces (which are encoded as underscores (\t{_})).

## Output format

Print a single integer number, the minimum possible distance needed to type the given character sequence.
