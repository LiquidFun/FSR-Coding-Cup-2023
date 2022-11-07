# FSR Cup 2023 Problems


## List of possible problem ideas

<details> 
  <summary>[DONE; needs other solvers, better problem text] Aquarium Maze (click me!)</summary>

  * *Preliminary problem idea*: you are given a 2D matrix of # and . (an aquarium). How much water fits inside of it? (Water does not flow up into airpockets)
  * *Difficulty*: 2-3/10
  * *Solution idea*: dfs or bfs
  * *Missing*: [**problem-text (improve)**, **solution2**, **solution-slide**]
  * *Variation*: given a maze as a 2D matrix of # and . print the length of the shortest path.
</details>

<details> 
  <summary>[DONE; needs other solvers] Bicycle Lock (click me!)</summary>

  * *Preliminary problem idea*: your gloves are too thick for the bicycle lock. Can only turn 2 dials at once, 2-100 numbers from 0 to 9 on lock. How many steps to turn to correct solution (if possible) given start position and correct position.
  * *Difficulty*: 2/10
  * *Solution idea*: greedy, start at left and check whether rightmost digit is correct
  * *Missing*: [**solution2**, **image of gloves + lock**, **solution-slide**]
</details>

<details> 
  <summary>[DONE; needs other solvers] Dam Construction (click me!)</summary>

  * *Preliminary problem idea*: you have a limited number of 3 types of lego bricks, 1, 2 and 4 wide. What is the highest wall of width w you can build?
  * *Difficulty*: 1-2/10
  * *Solution idea*: greedy
  * *Missing*: [**problem-text**, **solution2**, **solution-slide**, **image-in-problem**]
</details>

<details> 
  <summary>[DONE; needs other solvers] Fascinating Books (click me!)</summary>

  * *Preliminary problem idea*: You wonder around the library looking for the best book on visual basic, but you see so many books that any book title you read starts to lose its meaning. You just see letters, and you start to wonder. Do these books on this shelf contain each letter of the english alphabet at least once? Print "yes" or "no"
  * *Difficulty*: 1/10
  * *Solution idea*:
  * *Missing*: [**solution2**, **solution-slide**]
</details>

<details> 
  <summary>[DONE; needs other solvers] Train Scheduling (click me!)</summary>

  * *Preliminary problem idea*: you are in Rostock, but tomorrow you want to be at home! So you decide to go with deutsche bahn, however you see that their planning system is not working. So you take the matters in your own hands. You take all routes in the system and create your own timetable and routing. Of course the deutsche bahn trains may have some delay. Given the routes for the day and the maximum delay for each train, print the earliest possible time for arrival, and the latest possible time
  * *Difficulty*: 3-4/10
  * *Solution idea*: make graph, traverse with dijkstra
  * *Missing*: [**solution2**, **solution-slide**]
</details>

<details> 
  <summary>[DONE; REALLY needs other solvers] Keyboard Robot (click me!)</summary>

  * *Preliminary problem idea*: you are given a 6x6 keyboard layout and a list of words. You are building a robot with 2 separately movable fingers which can type letters on that keyboard. The fingers can only move along the grid, not diagonally, but they can move at the same time. Each movement costs 1 second, what is the minimal number seconds required to type all words correctly?
  * *Difficulty*: 5-6/10
  * *Solution idea*: shortest path? dp?
  * *Missing*: [**problem-text**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>

<details> 
  <summary>[FREE] Wordle Hell (click me!)</summary>

  * *Preliminary problem idea*: While again not paying attention in the lecture, you are playing wordle on your phone. You see that you only have 4 guesses left. You wonder what is the best way to test as many letters as possible. Given a list of 5-letter words (may not be valid wordle words), find 4 words which maximize the number of distinct letters across them.
  * *Difficulty*: 3-6/10
  * *Solution idea*: 
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>


<details> 
  <summary>[Marian] Compilers & Brackets (click me!)</summary>

  * *Preliminary problem idea*: You just completed the lecture on how to create compilers, and now that you are an expert at it you want to test your skills. You decide to create your own programming language. First steps first, however, so you decide the most important thing is brackets, and lots of them. You want to write a parser which tells you whether a list of open and closed brackets is valid. Print "valid" or "invalid"
  * *Difficulty*: 2-3/10
  * *Solution idea*: track sum of open/closed brackets, if negative: print invalid
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>

<details> 
  <summary>[DONE-ish, needs solvers and problem text] Leaderboard Prediction (click me!)</summary>

  * *Preliminary problem idea*: You are a crazy good competitive programmer, you have read all 8 problems, you have 3 hours and 50 minutes of the contest remaining, and now you know how long each problem will take you in minutes. Print how many problems you will be able to solve in 3:50 and what the time penalty will be for those solved problems.
  * *Difficulty*: 1/10
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution2**, **upload**, **solution-slide**]
</details>

<details> 
  <summary>[FREE] Hidden Words (click me!)</summary>

  * *Preliminary problem idea*: Given a list of words, construct a string of minimal length which contains each given word. Much easier variation: words have to appear in order. A bit harder: words appear in order, but may be shifted.
  * *Difficulty*: 2-4/10
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>


<details> 
  <summary>[FREE] Flawed Cryptography (click me!)</summary>

  * *Preliminary problem idea*: You are a pretty good white-hat-hacker and so you have found a backdoor on a website. Its security is at least not entirely terrible, you have gotten only the access to test the hashing algorithm of the website. You try it out, to see whether its SHA256 or something similar, but to your surprise you see that it seems to be neither, in fact it looks very short and not very good. For "password" you got "??e?b???" Immediately, you try a couple of other words
  * *Difficulty*: 1-3/10
  * *Solution idea*: leave "0-9a-f" as is in the original, calculate ascii index of rest of chars, take mod 16, index of "0-9a-f" list. Harder: + shift entire string by 3
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>

<details> 
  <summary>[FREE] Elastic Ball (click me!)</summary>

  * *Preliminary problem idea*: you are given a n x m grid of `.`, `O` or `#` characters, you are to compute the trajectory of a ball such that it hits the target `O`s. Print the trajectory, the ball bounces in a parabola
  * *Difficulty*: 2-4/10
  * *Solution idea*: bruteforce various throwing strengths
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>


<details> 
  <summary>[FREE] Stubborn Students (click me!)</summary>

  * *Preliminary problem idea*: you are to manage a n x m room full of seats for students, you expect near full occupancy so you decide in order to make the seating smoother to create an algorithm for automatic seating. Each row can only be accessed from one side. You are given a list of n students, and which time slots they have lectures (each student will only be in the room during those time slots.) Students are stubborn though, once seated they will not leave their place until they don't have a time slot in that room. Print a seating which minimizes the number of times a student has to stand up in order to allow another student through.
  * *Difficulty*: 5-7/10
  * *Solution idea*: dp?
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>


---


<details> 
  <summary>[TOO HARD (?)] Keyboard Redesign (click me!)</summary>

  * *Preliminary problem idea*: You have decided to redesign the keyboard. Given a list of words, create an optimal keyboard on a integer grid, such that the distances between letters is minimized when typing the given words."Easier" alternative: 1x26 row of numbers, still really hard, no idea how to solve?
  * *Difficulty*: 6-10/10
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>


<details> 
  <summary>[TOO HARD] Hidden Words (Hard) (click me!)</summary>

  * *Preliminary problem idea*: Construct a n x n grid of letters.  You are given m words, each word should occur exactly once in that grid either horizontally or vertically. 
  * *Difficulty*: 6-10/10
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>

<details> 
  <summary>[BAD PROBLEM; ignore] Coffee-Maker 3000 (click me!)</summary>

  * *Preliminary problem idea*: Tomorrow is the last submission day for your seminar paper, you have written exactly 0 words so far. It is time to work you say, it will be a long day. You prepare your custom self-built coffee machine for the next t hours. You have enough coffee for x coffee cups in that time. Each time it brews a coffee you drink it immediately and you gain a boost to your productivity for m minutes. Drinking multiple coffee cups in the same time is not as effective, it follows the formula sqrt(x), where x is the number of boosts active during that timeframe. Each minute you write n words, what is the maximum number of words you can write if you optimize the coffee machine?
  * *Difficulty*: 
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>



## Testing a solution

Use the `eval-solution.py` script, it will clone the git submodule and use the program-tester.sh in the scripts folder to evaluate the solution. The first argument can be a pattern or a file path to a solution which is to be tested. If nothing is added then the most recently saved solution will be tested. (In the future this might get replaced by a custom pip module).

## Creating a problem


**To add a problem idea**: 

1. Copy the following `<details>` spoiler block. 
2. Replace `Problem Template` with the problem name, leave the `[FREE]` if you are not intending to create its files yourself. Mark it as `[/NAME/]` if you are working on it. Mark it as `[DONE]` once everything for that problem has been completed.

If a problem is being worked on, additional solutions may be added without asking. Each problem should have at least 2 solutions by different people, because then easy mistakes can be found.

```html
<details> 
  <summary>[FREE] Problem Template (click me!)</summary>

  * *Preliminary problem idea*: 
  * *Difficulty*: 
  * *Solution idea*:
  * *Missing*: [**problem-text**, **solution1**, **solution2**, **tests**, **validator**, **checker**, **upload**, **solution-slide**]
</details>
```

In the spoiler tag the following attributes can be found:

* *Preliminary problem idea*: describe the problem description and or idea. Can be formal as well, may not be most up to date version!
* *Difficulty*: example: 1/10, subjective difficulty of problem. 1 is "add all given numbers", 5 is around easiest dp, 10 is ICPC world final problem. Give range if solution unknown
* *Solution idea*: describe your intended solution in a couple words or sentences, e.g.: build graph + dijkstra
* *Missing*: a list of parts which are still missing for that problem (remove once complete)

The following things are required for each problem:

* _problem-text_: problem description, input format, output format (use basic latex commands, as [supported by codeforces' polygon system](https://polygon.codeforces.com/docs/statements-tex-manual?ccid=0024b28061a8a61a73208fdecd433e9e&session=6ac53d17b6402d9f6a2692326b91989a06fa6000))
* _solution1_: main solution 
* _solution2_: secondary solution by someone else (possibly in a different programming language)
* _tests_: test input files ending with `.in`, usually easier to create with a generator
* validator: a program which tests whether a test is valid according to the problem statement (e.g. `1 <= n <= 100`, no negative integers, all strings below length 50, etc.)
* checker: a program which tests whether the solution is correct. Usually one of the pre-made ones from codeforces is enough, but this needs to be a separate program if multiple solutions are possible.
* upload: whether the problem has been uploaded to codeforces


**To start working on a problem:**

1. Mark the problem with your name in this file.
2. Duplicate the template folder, name it according to the problem name
3. Add files there as you see fit, the problem statement can be added in the README.md

Each solution, validator and checker should accept test cases via `stdin`, and print stuff via `stdout`. 

