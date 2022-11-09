Your gloves are too thick for the bicycle lock. You can only turn 2 dials at once, 2-100 numbers from 0 to 9 on lock. How many steps to turn to correct solution (if possible) given start position and correct position.


Variation: instead of 2 dials at once, give m dials to turn.
Variation 2: instead of saying whether a given position is possible, give the number of possible positions for a given m and a given target position

=== 

As you arrive at the KZH with your bicycle, you notice that your lock may be hard to unlock, because you are wearing thick gloves. 

===

# Bicycle Lock

\it{Based on a real story.}

You just arrived at the Konrad-Zuse-Haus, it is already 17:13! Your lecture starts in 2 minutes and you still have to lock your bike. Unfortunately it is winter, so you are wearing gloves, which means that inputting the correct code into your bicycle lock will be hard! You realize that because of your gloves you can only turn \it{exactly} \bf{2} dials at once. You bite the bullet this time, sacrificing your bare hands to the bitter cold. But as you step in the 037 you keep wondering, was it possible to unlock the lock without undoing your gloves? And if yes, how many dial turns would you have needed?

\begin{itemize}
\item A dial always contains 10 numbers, 0 to 9. It rotates in such a way that 0 and 9 are adjacent.
\item A dial turn is considered 1 rotation of 2 adjacent dials by 1 step. For example, to go from \t{3 9 1} to \t{5 1 1} is 2 dial turns.
\end{itemize}


## Input format

You are given 3 lines: 

\begin{itemize}
\item The first line contains an integer $n$ ($1 <= n <= 100$), specifying the number of dials on your bicycle lock.
\item The second line contains $n$ integers $c_i$ ($0 <= c_i <= 9$) the current position of the $n$ dials.
\item The third line contains $n$ integers $t_i$ ($0 <= t_i <= 9$) the target position of the $n$ dials.
\end{itemize}

## Output 

Print "impossible" if it is not possible to turn the dials without undoing the gloves. Otherwise print the number of turns to reach the target position
