# Jolly Fishing

## Statement

As part of your new job in the digitalisation of the government of Rostock you are tasked to implement a responsible fishing policy, ``just like the Norwegians do'', you were told. You are supposed to set a policy for a year (365 days) for fishers where you maximize the number of fishes caught, but you make sure that at the end of the year there is still at least as many fish as at the start of the year. 

On each day you can give the fishers a permit to fish, otherwise they are not allowed to fish, and since this is Germany you are sure they won't. On each day of the 365 days the fishers will fish exactly $c‰$ (‰=per mille) of fish (i.e. $c / 1000$ of fish will be fished on such a day). On days where fishers are not allowed to fish the fish population will increase by a factor of $b$ per mille (i.e. the fish population will increase by a factor of $b / 1000$ fish). On days where fishing is allowed fishes will of course not reproduce, because the fish are too scared when they are being fished.

\begin{center}
  \includegraphics[width=8cm]{fisher-small.png} \\
  \small{A fisher calculating his profits, by DALL-E 2}
\end{center}


## Input format

You are given one line with 3 integers: 

\begin{itemize}
\item $a$ ($1 <= a <= 1000$) the number of fish at the beginning of the year, expressed as units of \it{Mf} (Megafish = millions of fish)
\item $b$ ($1 <= b <= 50$) the growth factor of the fish in per mille ($‰$)
\item $c$ ($1 <= c <= 999$) the fishing factor of the fishers in per mille ($‰$)
\end{itemize}

## Output format

Print a single floating point number, the maximum number of fishes possible to fish in \it{Mf} (Megafish), in such a way that there are \bf{at least as many} fish after 365 days as there were at the beginning of the year. 

In this problem your answer does not have to match exactly with the jury answers, it is enough if your floating point number matches at least to $10^{-6}$ absolute or relative error. Make sure to use \bf{double-precision} instead of single-precision in order to achieve the required precision. 
