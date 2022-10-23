It just turned 00:00; you look at your phone: a new calendar notification just popped up. It reads "Mom's birthday [date of tomorrow]", you are in shock, how could you have forgotten! You promised to be at home, but now you only have 24 hours to plan and get there from Rostock! So you open the site for the deutsche bahn, but you frown, it's in maintenance. Luckily you are a cunning programmer*, so you check it's API, and you see it's still up! However, the API only returns single train connections, not full routes. You decide to take matters into your own hands. Given a list of connections find the earliest time you can arrive at your home destination (it is guaranteed that you can arrive 23:59 or earlier).

## Input

The first line contains two integers __n__ (`2 <= n <= 200`) and __m__ (`1 <= m <= 10000`) and a city name __h__ consisting of lowercase English alphabet letters (`1 <= ||h|| <= 10`). __n__ is the number of cities, __m__ is the number connections between cities. Then __m__ lines follow with the following format. `from to mins connection_count [connection]*connection_count`. TODO explain

## Output

A string of length 5 formatted as ("HH:MM"), the earliest time of arrival at your home city from the city of `"rostock"`.


* Assume that you are not cunning enough to check any of the other sites which may return a complete route!

Alternative (previous text): You are in Rostock, but tomorrow you want to be at home! So you decide to go with deutsche bahn, however you see that their planning system is not working. So you take the matters in your own hands. You take all routes in the system and create your own timetable and routing. Of course the deutsche bahn trains may have some delay. Given the routes for the day and the maximum delay for each train, print the earliest possible time for arrival, and the latest possible time
