# Hidden Words

## Statement

As part of the operating systems course you have designed your own ingenious protocol for transmitting a list of words. You have noticed that transmitting spaces is a waste of data, since everyone obviously can decipher where they should be, so you cut those. And then you notice that some words share letters, so in order to save precious bytes you only send that part of the word once.  For example, given the words \it{lint} and \it{inter}, you may send \it{linter}, because both words share \it{int}.

However, you deem that the first character of a word that comes later in the sequence cannot appear before the first character of a previous word, because otherwise it would not be clear in which order the words are! For example, given the words \it{bob}, \it{at} and \it{bat}, you may not print \it{bobat}, because \it{bat} would begin before \it{at} despite appearing later in the sequence (\it{bobatbat} would be correct).

## Input format

The first line contains an integer $n$ ($1 <= n <= 1000$), the number of given words.
The second line contains $n$ words $w_i$, each separated by a space. Each word $w_i$ will have at least 1 and at most 50 characters. All characters are lowercase english letters.

## Output format

Print the string of minimal length, which appears when you apply your ingenious protocol.
