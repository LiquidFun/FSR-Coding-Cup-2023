# Leaderboard Prediction

## Statement

You are a crazy good competitive programmer, so you are participating in the ACM ICPC World Finals 2022 in Egypt. You have $h$ hours for the contest in total. You have already read all $n$ problems, and since you are so good you immediately know how long each problem will take you in minutes. Print how many problems you will be able to solve in $h$ hours and what the time penalty will be for those solved problems. Note that you will of course make no mistakes, and each submission will be accepted on the first try.

A problem will count as solved if is solved at or before minute $h \cdot 60$. For example, if the contest is 5 hours long, then a problem can be solved at minute 300 since minute 300 is the time from 4:59:00 up to and including 4:59:59.

## Input format

The first line will contain 2 integers $n$ ($1 <= n <= 15$) and $h$ ($1 <= h <= 10$).
Then $n$ lines follow, each with a single integer $m_i$ ($1 <= m_i <= 300$) specifying how many minutes you need in order to solve problem $i$. 

## Output format

Print 2 integers, the maximum number of problems you can solve during the contest, and the minimum penalty for those solved problems. 
