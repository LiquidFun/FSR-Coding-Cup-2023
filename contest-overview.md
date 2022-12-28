# FSR Coding Cup 2023 🧑‍💻

![](POSTER)

## Who? What? Why? When? Where?

* **Who?** Everyone who is a student in **any** semester in **any** course of study can participate in **teams** of **1** to **3** people. Each team only has **a single** computer though. Basic programming skills are enough to solve multiple problems! Everyone is welcome!

* **What?** A programming competition where you code a solution to **12** problems in **4** hours, submit it online in a judge system, and get immediate feedback whether the solution was correct.

* **Why?** Participate in order to solve interesting problems, have fun with friends, test your programming skills and win some small monetary **prizes** and **t-shirts** (and eat **pizza** of course).

* **When?** **Saturday, 07.01.2023** from **14:00** to **21:00**, see *Schedule*. The contest itself will be from **15:00** to **19:00**.

* **Where?** 
    * On-site: **Konrad-Zuse-Haus** (institute of computer science) **Albert-Einstein-Straße 22, 18059** Room **301**.
    * Online (ineligible for prizes): https://codeforces.com/group/18t0uBAFk1/contests (create an account on codeforces and register to the contest as a participant a couple of hours before the contest)
## "Really? But I'm just a newbie programmer?"

Everyone who can code at least a little bit is able to participate. There will be 12 problems to solve, some of them will be easy enough that anyone with any coding experience can solve them. To encourage this there will be a **prize for first-year students** ("erstis"). In fact, internet access is allowed during this contest, so if you are a beginner you don't have to know any programming language by memory (communicating with other teams or asking for solutions is strongly disallowed though, see below for exact rules).

Also, many problems are not simply "coding" problems, often you have to have the right insight and idea, therefore even non-computer-scientists have good chances of winning!

But of course the hardest problem will be even a tough nut to crack for even the best programmers. So if you are someone who dreams in code you can be sure that you will find something interesting for you. In short, there will be something for everyone!

## Contest format

This section gives an overview of the contest and how it works, for the full rules see the *rules* section below.

### Schedule 

* **14:00** Arrival
* **14:20** Last tips, registration/login to https://codeforces.com, last Q&A regarding contest
* **15:00** Contest begin
* **19:00** Contest end, pizza time!
* **~19:15** Solution presentation
* **~19:45** Scoreboard reveal (unfreeze, last 1 hour of contest the exact standings are not shown, see rules)
* **~20:00** Prizes & end, you may stay longer if you want to discuss problems or just want to chat
* **21:00** Official end (we are not sure how long the last 3 topics will take, so there is some leeway)

### Problems

The contest will go for **4** hours and will have **12** problems. The problems will **not** be sorted according to difficulty, it is part of the competition to figure out which problems are easy, it **will** be possible to view which other teams have solved which problems though. This usually means that in the first half an hour you have to find the easy problems yourself, from then on you can see which problems have been solved most of the time.

The problems are usually little riddles which have multiple solutions. You have to come up with an idea which works for that solution, sometimes this is easy, sometimes it is not. Then you will have to implement your idea correctly, such that it handles all edge-cases.

For a detailed overview of a problem structure including example problem and solution see [here](guide.md).


For every problem there will be a description, a sample input and sample output. You are to write a solution which accepts input on `stdin` and prints on `stdout`. Once you have made sure that the solution is correct on the examples, you can submit it to a judge system, this judge system will then evaluate your solution on about 100 hidden test-cases. If your solution is correct for all of them it will count as solved. The test cases usually test every possibility and even hard cases which might not appear in the samples. To make it easier for you to know what the samples could be there is always a range provided for every number. For example, if the problem says that there will be a list of n numbers, there will be a range in the *Input* section which will give range like `2 <= n <= 1000`. For every test case your solution will have between 0.5 and 5 seconds to print out a correct answer, otherwise it will be stopped.

The teams are ranked by number of solved problems, then by a second value, a penalty which is the cumulative sum of submission times (see the rules for a complete description).


### Programming languages

The following programming languages may be used: **C, C++, C#, D, Go, OCaml, Delphi, Pascal, Perl, PHP, Java, Kotlin, Haskell, Python, Scala, Rust, Ruby, JavaScript**.

<!--
Goal is to support all of Tier 1, most of tier 2 and 3

Codeforces supported languages:
Essential:
* Tier 1 languages: C, C++, Python, Java
Some people will have used:
* Tier 2 languages: C#, Haskell, Rust, JavaScript, Scala
Nice to have:
* Tier 3 languages: Go, Pascal, Kotlin, Ruby.
Naaaah:
* Tier 4 languages: D, OCaml, Delphi, Perl, PHP
-->

It is guaranteed that all problems are solvable with Python.

It is recommended to use the language you are most comfortable with. If you are not sure, Python or C++ is a great choice.

### Teams


Each team may have between **1** to **3** students, however each team will only have access to **a single** computer. This format is heavily inspired by the ACM-ICPC type of programming contests. Having multiple people on the team allows you to:

* Code together, it may be easier to spot mistakes
* Have more fun, sometimes even not getting the right answer is more fun together
* Bounce ideas on each other, sometimes everyone is stuck

However, sometimes multiple teammates may only distract you. Everyone can decide for themselves what is more fun to them and we believe that any team whether of size 1 or 3 has equal chances to win. Therefore all teams will be evaluated in the same leaderboard. 

If you are looking for a teammate, but do not know anyone who wants to participate please reach out to *brutenis dot gliwa at uni-rostock.de*.



## Registration

Please create an account on [codeforces.com](https://codeforces.com) and register your team [here](https://files.studicloud.uni-rostock.de/apps/forms/bgtDTq5yg2jDcEsQ)! One account is enough per team, your username does not have to match your teamname, as you will be able to create a team for the contest. 

Please remember and/or write your username and password down for the contest. You will have to login on university computers and you may not have access to your password manager there.

## Rules

### Scoring 

The scoring works as follows:

* The first criteria is `#problems-solved-correctly` (higher is better).
* The second criteria (if multiple teams have the same number of solved problems) is `#penalty` (lower is better).

The `#penalty` is the sum of all submission times for your correctly solved problems. For example, if you have solved 3 problems *on the first attempt* at minutes 13, 32 and 67 your total penalty will be `13+32+67=112`. This means that a team with:

* 2 solved problems and penalty of 75 will have a **worse** ranking than your team
* 3 solved problems and penalty of 224 will have a **worse** ranking than your team
* 3 solved problems and penalty of 85 will have a **better** ranking than your team
* 4 solved problems and penalty of 332 will have a **better** ranking than your team

Notice the *on the first attempt* above, incorrect submissions add a penalty of **20** (but only if you solve the problem later). Therefore it is always better to try to solve a problem, as the penalty only applies once you have actually correctly submitted it. 

**Which incorrect solutions have a penalty?**

Not every incorrect submission is subject to a penalty, if your solution:

* does not compile, or
* fails on the first test-case

then the penalty of **20** will **not** be added.


### Additional tools & resources

You will be provided the following during the contest:

* A PC in one of the Pools including keyboard and mouse and enough room for your team members
* 1 set problem statements
* Drinks

You **may not** use the following items during the contest:

* Phones
* Headphones or earbuds
* Any device which can be used to communicate with other teams

You **may not** do the following things during the contest:

* Communicate with other teams
* Ask questions online
* Try to hack the system

You **may** bring to the contest:

* Your own keyboard and/or mouse (avoid loud keyboards such as ones with MX-Blue switches, we may ask you to use the provided keyboard in such a case). You may not use more than 1 keyboard or mouse at the same time.
* Any written materials you like: books, handwritten notes, paper, pens and pencils
* Drinks (however these are provided for you as well) 
* A calculator (it is unlikely you will need one)

You **may** use:

* The **internet** to search for information online, this includes any search engine you like as well as documentation (note that this is usually not the case in such contests. We decided to allow it in order to make it easier for beginners to participate). You are **not** allowed to ask questions online, or to communicate to anyone outside your team.
* Any tool installed locally such as browsers, the shell, or any script you write yourself.


### System

#### Hardware

TBA

#### Software

The software configuration will consist of the following:

* OS:
    * Ubuntu 22.04 LTS Linux (64-bit)
* Desktop Environment:
    * Gnome
    * Keyboard layouts:
        * en (default)
        * de
        * (others available via settings)
* Editors:
    * vim
    * gvim
    * nano
    * neovim
    * emacs
    * gedit
    * geany
    * kate
* IDEs:
    * PyCharm Community
        * Version: 2022.3
        * Plugins:
            * IdeaVim
    * IntelliJ Community
        * Version: 2022.3
        * Plugins:
            * IdeaVim
            * Rust
            * Scala
    * Eclipse
        * Version: 2022-12
    * Visual Studio Code
        * Version: 1.74
        * Plugins:
            * C/C++ - Microsoft
            * C# - Microsoft
            * Code Runner - Jun Han
            * Debugger for Java - Microsoft
            * ESLint - Microsoft
            * Language Support for Java - Red Hat
            * Python - Microsoft
            * Haskell - Haskell
            * Kotlin - fwcd

### Verdicts

Once submitted your solution will have one of the following verdicts:

* *Accepted* (AC) - your solution is correct for all test-cases
* *Wrong Answer* (WA) - your solution is incorrect for one of the test-cases
* *Time-Limit-Exceeded* (TLE) - your solution ran too long on one of the test-cases
* *Runtime Error* - your solution quit unexpectedly with a non-zero error
* *Compilation Error* - your solution did not compile correctly
* *Formatting Error* - your solution did not print the output correctly (rare)

Only *Accepted* solutions count, no other criteria are looked at. Your coding style,
best practices or any other otherwise important things in programming are not accounted for.

### Language (English)

All problem statements will be provided in English, however you are allowed to use online translators as well as dictionaries. Furthermore, if there are unclarities in the problem statements you may ask for a clarification as detailed in the next section.

### Asking for clarifications during the contest

To ask for problem clarifications you can either:

* Ask any of the people overseeing the contest
* Ask a question via codeforces. Go to the list of problems for that, and at the bottom you can see a "Ask a question" button.

Note that the organizers may not answer a question if they deem it is sufficiently explained in a solution.

## My motivation

This contest is not a one-off, in fact there is a huge community of competitive programmers. The ACM-ICPC competitions are yearly competitions where 60000 students participate annually. The finals are notoriously hard to get to, so there are regionals, for example there is the NWERC (north western europe) and GCPC (germany-only) contests. These competitions are a big deal for many people, including me. I have been participating in such contests for many years and have also participated in the NWERC for the last 3 years. 

Unfortunately, despite Uni-Rostock winning the NWERC in [2012](https://idw-online.de/de/news509736) there has been barely any activity here for this type of contests since. This contest is a opportunity to gauge interest in such things and to possibly spark a new team of active people who want to compete and who want to solve problems with the same joy as me.

## Questions

If you have questions email me at *brutenis dot gliwa at uni-rostock.de*.
