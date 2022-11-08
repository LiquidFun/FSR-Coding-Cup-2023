# Problem Name

## Statement

You just completed the lecture on how to create compilers by professor Wolf, and now that you are an expert at it you want to test your skills. You decide to create your own programming language. First steps first, however, so you decide the most important thing is brackets, and lots of them. You want to write a parser which tells you whether a string of open and closed brackets is valid. 

A string of brackets is defined as valid if: 
\begin{itemize}
* Each open bracket (\left) is closed by a closed bracket (\right)
* No closed bracket (\right) exists, that does not close an open bracket (\left)
\end{itemize}

## Input format

A single line containing a string $s$ ($1 <= ||s|| <= 1000$) consisting of the characters \left and \right.

## Output format

Print ``valid'' if the given string is a valid sequence of brackets, otherwise print ``invalid''.
