a simple game like mindmaster, braintwister. A row of four pegs out of five colors is 
built so that the player does not see which pegs are used. 
Player must then propose rows until one of those matches the hidden first row exactly. 
Feedback to each proposal comes in form of black marks for each color in correct position 
and addtional white marks for matching colors.

#### good to know, when playing against comp:
computer does not use brute force to solve 
the problem. Instead the process is built to match the human logic as much as possible. Basically comp comes up with random solutions and then step by step compares against 
the clues provided by white and black marks of previous attempts. 

Game is currently implemented in python3 using Turtle for GUI  
