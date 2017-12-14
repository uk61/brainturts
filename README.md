A simple game like mindmaster, braintwister. A row of four pegs out of five colors is 
built so that the player does not see which pegs are used. 
Player must then propose rows until one of those matches the hidden first row exactly. 
Feedback to each proposal comes in form of black marks for each color in correct position 
and addtional white marks for matching colors.

User can choose colors, pick a user name and decide if double colors are allowed. To store 
those options along with match stats, a path to a writable file must be provided at the top of the script.

#### Good to know, when playing against comp:
Computer does not use brute force to solve the problem. Instead the logic is built to match 
human process as much as possible. Basically comp comes up with random solutions and then step by step
compares against the clues provided by white and black marks of previous attempts. 

The game is currently implemented in python3 using turtle for GUI.
