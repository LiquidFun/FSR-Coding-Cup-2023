# Tips and introductory information

## Basic problem structure

Every Competetive Problem basically has a similar structure.

For every problem there will be a description, a sample input and sample output.
The problem description introduces the real live problem to solve (think of
"Mathe Text Aufgaben :D") and precisely outlines what you have to compute. A
sample description could be the following:

- "You are bored in class and look around. You see n sticks of varying sizes on
  the table. While examining their lengths you begin to wonder whether it is
  possible to stack **two** sticks on top of each other so that the height of
  the stack exactly equals the height of you water bottle."

The sample input section tells you how the input will look and also what ranges
the different numbers may have:

- "The first line will have two integers $(1 < n < 10^5)$ and $(1 < h < 10^9)$,
  the number of sticks and the height of your waterbottle. The second line will
  have $n$ integers, the heights of the sticks."

The sample output then describes how your awnser should look like:

- "Print the heights of the two used sticks in one line and "impossible!" if the
  described task is not possible. If there are multiple possible awnsers, you
  may print any one of them."

Given this Problem desription, you are to write a solution which prints the
correct solution for each given input. Once you have made sure that your
solution is correct on the examples, you can submit it to a judge system, this
judge will then evaluate your solution on about 100 hidden test-cases. If your
solution is correct for all of them it will count as solved.

## Basic strategy

After you have read the problem description carefully you generally try to
extract the underlying mathematical problem. This will help you abtract from the
story told in the problem and concentrate on the task to solve. For the sample
this could be e.g.:

- "Given a list of n positive whole (possible repeating) numbers, find two
  numbers which exactly add up to h."

You can then start to work out a procedure which can solve the task. It is
generally the best idea to start with a very simple *brute-force* solution. On
the given task you could for example identify that the easiest way to solve the
described problem would be to test the sum of any two sticks of the list. You
start with the first stick and then compute the sum of it and each of the other
sticks and test if they sum up to one.

A sample python implementation could be the following:

```python
1. for i in range(len(sticks)):
2.    for j in range(i+1, len(sticks)):
3.        if sticks[i]+sticks[j] == h:
4.            print(sticks[i],sticks[j])
5.            return
6. print("impossible!")
``` 

Note that the second for loop starts at the stick after stick i to avert testing
pairs of sticks twice. Also note that starting at index 0 with both for loops
would not just be a slower solution, it would be an incorrect one!

The reason is that i and j can take the same value. Then you would test if the
same stick stacked on top of another twice would add up to the bottle. This is
not allowed. A big skill in competetive programming is to find and fix these small
inaccuracies.

The `return` on line 5 makes sure that you do not print multiple allegible pairs
of sticks -- which would be counted as a wrong submission!

Now to the problem with the given solution. A competetive programming solution
always consists of two things: Correctness and speed. While the code does find
correct solutions and would not result in a "Wrong Awnser" submission, it is in
fact too slow and would result in a "Time Limit Exceeded" submission. The reason
for this is the following:

Note the the output description states that there may be up to $10^5$ sticks.
The solution then uses two for loops that go over all possible sticks twice,
resulting in an O(n^2) solution since each pair needs to be checks. For a more
exact description, n numbers result in $n*(n-1)/2$ pairs of numbers which is
about $10^10$. Your program usually has 1 second of computing time until you get
"TLE". A good estimate to use is to check the general complextiy O(n^2) and
check whether it falls below 10^7 operations. A lot of times the first awnser
you think of is just fast enough but this time we need to come up with a
different one.

As you look at the problem you might find out that for each stick n, you exactly
know how the corresponding second stick should look like. It needs to have the
width (n-h). If you could find out faster whether this (n-h) stick exists in the
given list, you can solve the whole problem much faster! In this case, you can
use a Set, a datastructure which allows for O(logn) lookups. The resulting code
could look like this in python:

TODO: wrong, can find i i if i*2 == h
```python
1. stick_set = set(sticks)
2. for i in range(len(sticks)):
3.   if h-i in stick_set:
4.      print(i, h-i)
5.      return      
6. print("impossible!")
``` 

The complexity of this solution is O(n*logn), as the for loop loops through all
sticks and inside the for loop a set lookup is done which takes logn time. The
solution is correct and fast enough! Time to submit.

