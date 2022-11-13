It just turned 00:00; you look at your phone: a new calendar notification just popped up. It reads \it{Mom's birthday @ 09.01.2023}, you are in shock, how could you have forgotten! You promised to be at home, but now you only have 24 hours to plan and get there from Rostock! So you open the site for the Deutsche Bahn, but you frown, it's in maintenance. Luckily you are a cunning programmer*, so you check it's API, and you see it's still up! However, the API only returns single train connections without transfers, not full routes. You decide to take matters into your own hands. Given a list of connections find the earliest time you can arrive at your home destination (it is guaranteed that you can arrive 23:59 or earlier, i.e. all connections depart and arrive on the same day).

* Assume that you are not cunning enough to check any of the other sites which may return a complete route!


\begin{center}
  \includegraphics{wartungsarbeiten.png} \\
  \small{Completely fictitious scenario}
\end{center}

## Input

The first line contains two integers and a string:

\begin{itemize}
  \item the number of cities $n$ ($2 <= n <= 200$),
  \item the number of directional connections in total $m$ ($1 <= m <= 10000$) and
  \item a city name $h$ consisting of lowercase English alphabet letters ($1 <= ||h|| <= 10$). This city name denotes the target city where your mom lives.
\end{itemize}

Then $m$ lines follow with the following format:

\t{from_city to_city mins trains [connection]*trains}. E.g.:

\t{rostock   dresden   50      2         10:21 12:21}. 

This means that there are 2 trains leaving from \t{rostock} to \t{dresden}, at 10:21 and at 12:21. They will arrive at 11:11 and 13:11 respectively.

## Output

A string of length 5 formatted as (\t{HH:MM}), the earliest time of arrival at your home city \it{h} from the city of \t{``rostock''}.


Alternative (previous text): You are in Rostock, but tomorrow you want to be at home! So you decide to go with deutsche bahn, however you see that their planning system is not working. So you take the matters in your own hands. You take all routes in the system and create your own timetable and routing. Of course the deutsche bahn trains may have some delay. Given the routes for the day and the maximum delay for each train, print the earliest possible time for arrival, and the latest possible time
