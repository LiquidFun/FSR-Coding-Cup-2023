# Dam Construction

## Statement

You are the manager for a dam construction company called \it{Damn Dams Inc.}, and now you have a new contract. Luckily for you, the company is based in Rostock, so the dams are rather small. In fact, they are built from lego bricks! You are to oversee the construction of a new dam, you are not sure though whether you have enough materials (lego bricks) for it. 

Your company only uses three types of bricks to build dams: 1x1, 2x1 and 4x1 bricks (see picture). The contract requires the dam to be of exact width $w$. In order to estimate if you can build the required dam, you need to evaluate your available resources first. What is the maximum height you can build the dam to using the available resources, such that there are no holes? Only count complete layers for this. It does not matter how bricks in two adjacent layers overlap, because you will be using \it{Damn Dams Inc.} patented sealant for structural integrity.

\begin{center}
  \includegraphics{bricks4.png} \\
  \small{Example solution for sample 1}
\end{center}

The bricks are all of the same height and cannot be rotated, due to the pins on the bricks. No brick may extend the given width $w$.

## Input format

The first line contains a single integer $w$ ($1 <= w <= 10^9$), the exact width which each layer of the dam needs to be.
The second line contains three integers $b_1$, $b_2$ and $b_4$ ($0 <= b_1, b_2, b_4 <= 10^9$), the number of bricks of width 1, 2 and 4 respectively. 

## Output format

A single integer: the maximum height $h$ which is possible to build to with complete layers with the given bricks.
