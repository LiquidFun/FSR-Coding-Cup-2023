# Keyboard Robot

## Statement

Everyone knows that the most important thing for a programmer is their typing speed! And you have been on a journey to improve your typing speed for a while, employing the fastest typing method known to man: 2 finger-typing. You have tested various keyboard layouts, such as Qwerty, Colemak, Dvorak and so on. But none of these are good enough for you, so you have decided to design your own. To streamline this process you have also created a robot which is used to test such a keyboard layout. Of course such a robot only has 2 mechanical fingers, which matches your superior typing preference.

Given a 6x6 keyboard layout you have designed and a sequence of characters, calculate the minimum possible number of seconds needed by 2 mechanical fingers in order to type that character sequence. The fingers start in the top left corner of the keyboard. The fingers can move 1 key up, down, left or right in \textbf{1} second, they cannot move diagonally. It takes them \textbf{0} seconds to type a character (a finger can immediately move again after arriving at a character it needs to press). After a second has passed you can use \bf{either} finger or \bf{both} fingers to type a letter. In case you use both to type a letter at the same time you have enough control of them that you can type them in either order you want.

Both fingers will be initially at the top left key (even if the key is empty). The fingers do not hinder each other and can stay at or move to the same position. The keyboard does not loop around, therefore the maximum time to move between any two buttons on the keyboard is between the top-left and bottom-right buttons: $5+5 = 10$ seconds.


## Input format

The first 6 lines contain your keyboard layout, each of those lines contains exactly 6 characters. Among these 36 characters it is guaranteed that each letter in the English alphabet and the space-bar appear \bf{exactly} once (in its lowercase form). The space-bar is encoded as a underscore \t{_}. The 9 remaining dots (\t{.}) denote empty parts of the keyboard where there is no key. The fingers can move over or stay on empty parts of the keyboard.

The next line contains a string $s$ ($1 <= ||s|| <= 200$) consisting of lowercase letters in the English alphabet + spaces (which are encoded as underscores (\t{_})).

## Output format

Print a single integer number, the minimum possible time in seconds needed to type the given character sequence.

## Notes 

Sample 3 explained:

Type letters \t{a-k} with finger 1, meanwhile, move finger 2 to the key \t{l}. Immediately after the first finger types the key k, the second finger can type the key l (now 9 seconds have passed, 11 characters have been typed).

Repeat this process with the letters \t{m-s} and \t{t}. Now use finger 2 to type the letters \t{m-s}, move finger 1 meanwhile to the key \t{t}. As soon finger 2 types the letter \t{s}, type the letter \t{t} with finger 1 (now 16 seconds have passed, 19 characters have been typed).

Same process with \t{u-x} and \t{y} (now 21 seconds have passed, and 25 characters have been typed).

Use the last second to move a finger from \t{y} to the key \t{z}, getting a time of 22 seconds in total.
