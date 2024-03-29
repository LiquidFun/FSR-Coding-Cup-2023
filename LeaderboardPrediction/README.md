# Leaderboard Prediction

## Statement

You are a crazy good competitive programmer, so you are participating in the ACM ICPC World Finals 2022 in Egypt. You have $h$ hours for the contest in total. You have already read all $n$ problems, and since you are so good you immediately know how many minutes each problem will take you to solve. Print how many problems you will be able to solve in $h$ hours and what the time penalty will be for those solved problems. Note that you will of course make no mistakes, and each submission will be accepted on the first try.

The scoring for the ACM ICPC World Finals works just the same way as the competition you are participating in right now! Teams are scored by two values, firstly, by the number of correctly solved problems (higher is better), then by the sum of submission times in minutes for the correctly solved problems (lower is better). The second value is called the time penalty. For example, a team which has solved 3 problems at minute 14, 51 and 267 will have a time penalty of $14+51+267=332$. Unsolved problems, even if they have incorrect submissions, do not add to the time penalty.

A problem will count as solved if is solved at or before minute $h \cdot 60$. For example, if the contest is 5 hours long, then a problem can be solved at minute 300 since minute 300 is the last second of the contest at 5:00:00 where you can submit (and that is plenty of time for you).

## Input format

The first line will contain 2 integers $n$ ($1 <= n <= 15$) and $h$ ($1 <= h <= 10$).
Then $n$ lines follow, each with a single integer $m_i$ ($1 <= m_i <= 300$) specifying how many minutes you need in order to solve problem $i$. 

## Output format

Print 2 integers, the maximum number of problems you can solve during the contest, and the minimum penalty for those solved problems. 
