# Hidden Words

## Statement

As part of the operating systems course you have designed your own ingenious protocol for transmitting a list of words. You have noticed that transmitting spaces is a waste of data, since everyone obviously can decipher where they should be, so you cut those. And then you notice that some words share letters, so in order to save precious bytes you only send that part of the word once. However, you deem that a word that comes later must begin at or after the start of the previous word, i.e. given the words \it{at} and \it{bat}, you may not print \it{bat}, because \it{bat} would begin before \{at} despite appearing later in the sequence (\it{atbat} would be correct).

## Input format

The first line contains an integer $n$ ($1 <= n <= 1000$), the number of given words.
The second line contains $n$ words $w$, each separated by a space. Each word will have at least 1 and at most 50 characters. All characters are lowercase english letters.

## Output format

Print the string of minimal length, which appears when you apply your ingenious protocol.
