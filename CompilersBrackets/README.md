# Problem Name

## Statement

You just completed the lecture on how to create compilers by professor Wolf, and now that you are an expert at it you want to test your skills. You decide to create your own programming language. First steps first, however, so you decide the most important thing is brackets, and lots of them. You want to write a parser which tells you whether a string of open and closed brackets is valid. 

A string of brackets is defined as valid if: 

\begin{itemize}
\item Each open bracket is closed by a closed bracket.
\item A closed bracket can only close a single open bracket.
\item No closed bracket exists that does not close an open bracket.
\end{itemize}

Where:

\begin{itemize}
\item ``\t{\{}'' - is an open bracket.
\item ``\t{\}}'' - is a closed bracket.
\end{itemize}

## Input format

A single line containing a string $s$ ($1 <= ||s|| <= 1000$) entirely consisting of the characters ``\t{\{}'' and ``\t{\}}''.

## Output format

Print ``valid'' if the given string is a valid sequence of brackets, otherwise print ``invalid''.
