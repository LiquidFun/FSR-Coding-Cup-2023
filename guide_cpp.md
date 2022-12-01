# Tips and introductory information

This guide contains c++ code. A seperate guide is given for python. You should use the programming language that you are most comfortable with in this contest. If you are still not sure, we suggest to use python.

## Basic problem structure

Every Competitive Problem basically has a similar structure.

For every problem there will be a description, a sample input and sample output.
The problem description introduces the real live problem to solve (think of
"Mathe Text Aufgaben :D") and precisely outlines what you have to compute. A
sample description could be the following:

- "You are bored in class and look around. You see $n$ sticks of varying sizes on
  the table. While examining their lengths you begin to wonder whether it is
  possible to stack **two** sticks on top of each other so that the height of
  the stack exactly equals the height of your water bottle."

The sample input section tells you how the input will look and also what ranges
the different numbers may have:

- "The first line will have two integers $(1 < n < 10^5)$ and $(1 <= h <= 10^9)$,
  the number of sticks and the height of your water bottle. The second line will
  have $n$ integers $(1 <= h_i <= 10^9)$, the height of the $i$-ith stick."

The sample output then describes how your anwser should look like:

- "Print the heights of the two used sticks in one line and `impossible!` if the
  described task is not possible. If there are multiple possible awnsers, you
  may print any one of them."

Given this problem desription, you are to write a solution which prints the
correct solution for each given input. Once you have made sure that your
solution is correct on the examples, you can submit it to a judge system, this
judge will then evaluate your solution on about 100 hidden test-cases. If your
solution is correct for all of them it will count as solved.

## Basic strategy

After you have read the problem description carefully you generally try to
extract the underlying mathematical problem. This will help you abtract from the
story told in the problem and concentrate on the task to solve. For the sample
this could be e.g.:

- "Given a list of $n$ positive whole (possibly repeating) numbers, find two
  numbers which exactly add up to $h$."

You can then start to work out a procedure which can solve the task. It is
generally the best idea to start with a very simple *brute-force* solution. On
the given task you could for example identify that the easiest way to solve the
described problem would be to test the sum of any two sticks of the list. You
start with the first stick and then compute the sum of it and each of the other
sticks and test if they sum up to $h$.

A sample python implementation could be the following:

```cpp
for(int i = 0; i < sticks.size(); i++) {
  for(int j = i+1; j < sticks.size(); j++) {
    if(sticks[i]+sticks[j] == h) {
      cout << sticks[i] << " " << sticks[j] << "\n";
      return 0;
    }
  }
}
cout << "impossible!" << "\n";
```

Note that the second for loop starts at the stick after stick $i$ to avert
testing pairs of sticks twice. Also note that starting at index 0 with both
*for* loops would not just be a slower solution, it would be an incorrect one!

The reason is that $i$ and $j$ can take the same value. Then you would test if
the same stick stacked on top of another twice would add up to the bottle. This
is not allowed. A big skill in competetitive programming is to find and fix
these small inaccuracies.

The `return 0;` on line 5 makes sure that you do not print multiple legible pairs
of sticks -- which would be counted as a wrong submission!

Now to the problem with the given solution. A competetitive programming solution
always consists of two things: correctness and speed. While the code does find
correct solutions and would not result in a *Wrong Awnser* submission, it is in
fact too slow and would result in a *Time Limit Exceeded* submission. The reason
for this is the following:

Note the the output description states that there may be up to $10^5$ sticks.
The solution then uses two for loops that go over all possible sticks twice,
resulting in an O($n^2$) solution since each pair needs to be checks. For a more
exact description, $n$ numbers result in $n*(n-1)/2$ pairs of numbers which is
about $10^10$. Your program usually has 1-5 seconds of computing time until you get
the *Time-Limit-Exceeded* verdict. A good estimate to use is to check the general 
complextiy O($n^2$) and check whether it falls below 10^7 operations. A lot of 
times the first awnser you think of is just fast enough but this time we need
to come up with a different one.

As you look at the problem you might find out that for each stick $n$, you
exactly know how the corresponding second stick should look like. It needs to
have the width ($h-h_i$). If you could find out faster whether this ($h-h_i$)
stick exists in the given list, you can solve the whole problem much faster! In
this case, you can use a Set, a data structure which allows for O(log $n$)
lookups. The resulting code could look like this in python:

```cpp
set<int> stick_set;
for(int i = 0; i < sticks.size(); i++) {
  stick_set.insert(sticks[i])
}

for(int i = 0; i < sticks.size(); i++) {
  if(2*sticks[i] == h) {
    if(sticks.count(h_i) >= 2) {
      cout << sticks[i] << " " << sticks[j] << "\n";
      return 0;
    }
  } else if(set.contains(h - sticks[i])) {
    cout << sticks[i] << " " << sticks[j] << "\n";
    return 0;
  }
}
cout << "impossible!" << "\n";
```

The complexity of this solution is O($n$ \* log $n$), as the *for* loop iterates
over all sticks and inside the *for* loop a set lookup is done which takes log
$n$ time. Note that here we have to account for sticks with height exactly
$h/2$, because the set only saves each stick once, so when we are checking the
stick of height $h/2$ we need to make sure there are at least of sticks of that
height. This time the solution is correct and fast enough! Time to submit.

## Reading input

We have one last thing to discuss before you are ready to solve some problems:
Reading input from stdin. In python, you read input using the `cin` keyword.
It takes the next element and parses it into a variable.

For our problem, the input might look like the following:

```cpp
4 5
1 2 3 4
```

A simple program to read said input would be:

```cpp
#include <vector>;

int n, h;
cin >> h >> n;
vector<int> sticks;
for(int i = 0; i<n; i++) {
  int stick;
  cin >> stick;
  sticks.push_back(stick);
}
```

The first `cin` reads in the integers n and h and the second one fills the vector.
A vector is simply a list which can only be appended to. Use `vec.push_back(x)` to
append an element and `vec[i]` to address them. You could alternatively use an
array and initialize it with highest possible n. (Note that a c++ array can not be initialized with dynamic size.) The code for this would be the following:

```cpp
int n, h;
cin >> h >> n;
int sticks[100000];
for(int i = 0; i<n; i++) {
  int stick;
  cin >> stick;
  sticks[i] = stick;
}
```

The complete program for our problem would be:

```cpp
using namespace std;

int main() {
  // input
  int n, h;
  cin >> h >> n;
  int sticks[100000];
  for(int i = 0; i<n; i++) {
    int stick;
    cin >> stick;
    sticks[i] = stick;
  }

  // solving the problem
  set<int> stick_set;
  for(int i = 0; i < sticks.size(); i++) {
    stick_set.insert(sticks[i])
  }
  for(int i = 0; i < sticks.size(); i++) {
    if(2*sticks[i] == h) {
      if(sticks.count(h_i) >= 2) {
        cout << sticks[i] << " " << sticks[j] << "\n";
        return 0;
      }
    } else if(set.contains(h - sticks[i])) {
      cout << sticks[i] << " " << sticks[j] << "\n";
      return 0;
    }
  }
  cout << "impossible!" << "\n";
  
  return 0;
}
```

Now you know all the basics to solve some simple competetive programing
problems! Thanks for reading and i hope this guide helped.

If you want to get accustomed to this process and solve some simple problems, you can go to codeforces and look for problems with difficulty 800 ([Codeforces 800 problems](https://codeforces.com/problemset?tags=800-800))

A good starting point might be the following problem
([Codeforces Problem Medium Numbers](https://codeforces.com/problemset/problem/1760/A))
