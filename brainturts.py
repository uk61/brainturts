#!/usr/bin/python

######Set path to a file where match statistics can be stored#####
file_path = "/home/uk/dev/sites/coding/learning/braintwister/newdata.json"
########

import turtle
from time import localtime, strftime, sleep
import random
import json

#set up screen
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
wn.title('Mindturts')
wn.listen()

# define drawing functions
def draw_bars(t, x, y, color):
    t.hideturtle()
    t.speed(10)
    t.color(color)
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(10)
    t.right(180)
    t.end_fill()        
    
def draw_mark(t, x, y, color):
    t.speed(10)
    t.hideturtle()
    t.penup()
    t.color(color, color)    
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.begin_fill()    
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.left(180)
    t.end_fill()        
    
def draw_header(t, msg, color, x, y, size='regular'):
    t.hideturtle()
    t.speed(10)
    t.penup()    
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.pencolor(color)
    if size == 'small':
        t.write(msg, move=False, align="left", font=("Arial", 12, "normal"))
    elif size == 'bold':
        t.write(msg, move=False, align="left", font=("Arial", 16, "bold"))
    else:
        t.write(msg, move=False, align="left", font=("Arial", 16, "normal"))      

def color_submit(x, y):
    if x > -520 and x < -450 and y > -30 and y <-2:
        submit_turt.color('grey')
        
def color_change(x, y):
    if x > -509 and x < -489:
        count = 0
    if x > -469 and x < -449:
        count = 1
    if x > -429 and x < -409:
        count = 2
    if x > -389 and x < -369:
        count = 3
    if pick_turts[count].pencolor() == 'red':
        pick_turts[count].color('blue')
    elif pick_turts[count].pencolor() == 'blue':
        pick_turts[count].color('green')
    elif pick_turts[count].pencolor() == 'green':
        pick_turts[count].color('orange')
    elif pick_turts[count].pencolor() == 'orange':
        pick_turts[count].color('yellow')
    elif pick_turts[count].pencolor() == 'yellow':
        pick_turts[count].color('red')
    u_choice[count] = pick_turts[count].pencolor()  

def draw_color_picker(offset, x, y, turts):
    draw_header(write_turt, 'pick your colors', 'black', offset + -5, y + y_coord + 20)
    for i in range(0, len(turts)):
        turts[i].shape('circle')
        turts[i].penup()
        turts[i].setx(offset + x * i)    
        turts[i].sety(y + y_coord)        
        turts[i].color('red', 'red')
        turts[i].showturtle()          
        turts[i].onclick(color_change)
    submit_turt.penup()
    submit_turt.setx(offset + -10)
    submit_turt.sety(y + y_coord + -40)
    submit_turt.color('green')
    submit_turt.write('submit', move= True, font=('arial', 16, 'bold'))
    wn.onscreenclick(color_submit)
    
def draw_full_set(turts, offset, x, y, src):
    for (i, col) in enumerate(src):
        turts[i].speed(10)
        turts[i].shape('circle')
        turts[i].penup()
        turts[i].setx(offset + x * i)    
        turts[i].sety(y + y_coord)        
        turts[i].color(col)
        turts[i].showturtle()    
        
def pause(t,x,y):
    t.hideturtle()
    t.up()
    t.setx(x)
    t.sety(y)
    t.speed(10)
    t.forward(0)     
    
'''prepare games logic'''
#define counting functions
def white_count(list1,list2):
    #count occurrences of identical items in two lists
    shared = set(list1).intersection(list2)
    counts = {num:(list1.count(num), list2.count(num)) for num in shared}
    x = 0
    for key in counts:
        list = counts[key]
        if list[0] <= list[1]:
            x += list[0]
        else:
            x += list[1]
    return x

def black_count(list1,list2):
    #count occurrences of identical items in same index positions in two lists
    y = len([i for i, j in zip(list1,list2) if i == j])
    return y

#set up set
def get_set(set):
    new_set = []
    for i in range(0,max_num_color):
        for item in set:
            new_set.append(item)
    return new_set            

#play again or quit
def play():
    next_round[0] = 1    
def stop():
    next_round[0] = 2
def play_again():
    wn.onkey(stop, "n")
    wn.onkey(play, 'y')
    wn.listen()
    
def analyse():
    see_analysis[0] = 1
def no_analyse():
    see_analysis[0] = 2
def show_analysis():
    wn.onkey(analyse, 'a')
    wn.onkey(no_analyse, 's')
    wn.listen()

def move():
    next_stage[0] = 1
def move_on():
    wn.onkey(move, 'g')
    wn.listen()

def c_start():
    mode[0] = 0
def u_start():
    mode[0] = 1
def mode_choice():
    wn.onkey(u_start, 'u')
    wn.onkey(c_start, 'c')
    wn.listen()

#build stats dict
def match_stats(time, rounds, comp_attempts, user_attempts):
    m_stats = {time: {'rounds': rounds, 'comp_attempts': comp_attempts, 'user_attempts': user_attempts}}
    return m_stats
    
def game_stats(path):
    g_rounds = 0
    g_comp_attempts = 0
    g_user_attempts = 0
    with open(path) as storage:
        stored_stats = json.load(storage)
    for k, v in stored_stats.items():
        g_rounds += v['rounds']
        g_comp_attempts += v['comp_attempts']
        g_user_attempts += v['user_attempts']
    g_stats = [g_rounds, g_comp_attempts, g_user_attempts]
    return g_stats
    
#set up vars for game logic
i = 0
proceed = 0
solution = []
solutions = []
black_counts_absolute = []
white_counts_absolute = []
y_coord = 240
rounds_played = 0
user_attempts = 0
comp_attempts = 0
mode = [-1]
next_round = [0]
next_stage = [0]
see_analysis = [0]

'''Game starts'''
while True:
    #draw opening screen, set up the game
    if mode[0] == -1:
        #define set
        source_set = ['blue','red','green','yellow','orange']
        #num_pegs = int(turtle.numinput('Number of slots', 'How many pegs?'))
        num_pegs = 4
        #create turtles, set up for drawing pegs, results, headers etc.
        write_turt = turtle.Turtle(visible = False)
        sol_turts = list()
        mark_turts = list()        
        for i in range(len(source_set)):
            sol_turts.append(turtle.Turtle(visible = False))
            mark_turts.append(turtle.Turtle(visible = False))       
        pick_turts = list()
        for i in range(0, num_pegs):
            pick_turts.append(turtle.Turtle(visible = False))        
        submit_turt = turtle.Turtle(visible = False)
        pause_turt = turtle.Turtle(visible = False)
        
        draw_header(write_turt, 'mindturts!', 'black', -200, y_coord + 115)
        draw_header(write_turt, 'be smarter than the computer', 'black', -200, y_coord + 90)
        draw_header(write_turt, 'mission: find out which four colored pegs the opponent secretely has chosen', 'black', -200, y_coord + 50)
        draw_header(write_turt, 'the computer can not err, so you better make no mistakes...', 'black', -200, y_coord + 10)
        draw_header(write_turt, 'good luck!', 'black', -200, y_coord + -30)
        
        #ask user for for number of doublettes
        #max_num_color = int(turtle.numinput('Doubles', 'How many doubles should we allow?'))
        max_num_color = 2
        full_set = get_set(source_set)
        col_turts = list()
        for i in range(len(full_set)):
            col_turts.append(turtle.Turtle(visible = False))

        #ask user for mode
        draw_header(write_turt, "who is first? type 'u' for your turn or 'c' for my turn!", 'blue', -500, y_coord + -500)
        while True:
            pause(pause_turt, -1000,-0)
            mode_choice()
            if mode[0] != -1:
                break
        start_mode = mode[0]
        turtle.resetscreen()
        pause_turt.hideturtle()
        submit_turt.hideturtle()
        write_turt.hideturtle()
        for t in pick_turts:
            t.hideturtle()        
        for t in sol_turts:
            t.hideturtle()
        for t in mark_turts:
            t.hideturtle()    
   
    '''user assigns problem, comp solves'''
    if mode[0] == 0:
        i = 0
        next_round[0] = 0
        solution = []
        solutions = []
        #draw full set, comp is on
        draw_header(write_turt, 'comp is on', 'red', -510, y_coord + 185, 'bold')
        draw_full_set(col_turts, -500, 40, -660, full_set)
        #let user choose colors
        u_choice = ['red', 'red','red', 'red']        
        draw_color_picker(-500, 40, -220, pick_turts)        
        while True:
            pause(pause_turt, -1000,-0)
            if submit_turt.color() == ('grey', 'grey'):               
                break                    
        #reset screen and all turtles
        turtle.resetscreen()
        for t in col_turts:
            t.hideturtle()
        pause_turt.hideturtle()
        submit_turt.hideturtle()
        write_turt.hideturtle()
        for t in pick_turts:
            t.hideturtle()        
        for t in sol_turts:
            t.hideturtle()
        for t in mark_turts:
            t.hideturtle()        
        
        #draw hidden assignm + header
        assignm = u_choice
        draw_header(write_turt, 'Assignment', 'black', -500, y_coord + 115)
        x = -500
        y = y_coord
        for (key, color) in enumerate(assignm):
            draw_bars(sol_turts[key], x, y, 'grey')
            x += 20
    
        while True:
            if proceed == 0:
                #choose random colors, make sure it's not the same as previous solutions
                x = random.sample(full_set,4)    
                solution.append(x)
                if solution[i] in solutions:
                    del solution[-1]
                    proceed = 0
                else:
                    proceed = 1        
            if proceed == 1:
                #check for black count against assignment
                black_counts_absolute.append(black_count(assignm, solution[i]))                
                if black_counts_absolute[i] == 4:                    
                    proceed = 5                
                else:
                    proceed = 2
            #if success, i.e. identical colors in identical positions as assignment, draw assignm,
            #solution, stats; clean out vars & break        
            if proceed == 5:                                     
                #draw solution + header
                draw_header(write_turt, 'Solution', 'black', -300, y_coord + 115)
                x = -300
                y = y_coord
                for (key, color) in enumerate(solution[i]):
                    draw_bars(sol_turts[key],x,y,color)
                    x += 20
                #draw assignm     
                x = -500
                y = y_coord
                for (key, color) in enumerate(assignm):
                    draw_bars(sol_turts[key], x,y,color)
                    x += 20                           
                #collect match and game stats
                rounds_played += 0.5
                comp_attempts += i
                time = strftime("%d.%m.%Y, %H:%M", localtime())
                m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)
                g_stats = game_stats(file_path)
                #display stats
                draw_header(write_turt, "Match stats:", 'red', -510, y_coord + -310)
                draw_header(write_turt, "Rounds played: "+ str(int(rounds_played)), 'black', -510, y_coord + -335)
                draw_header(write_turt, 'User attempts: '+ str(user_attempts), 'black', -510, y_coord + -360)
                draw_header(write_turt, 'Comp attempts: '+ str(comp_attempts), 'black', -510, y_coord + -385)
                draw_header(write_turt, 'Previous games: ', 'red', -510, y_coord + -420)
                draw_header(write_turt, 'Games total: '+ str(int(g_stats[0])), 'black', -510, y_coord + -445)
                draw_header(write_turt, 'Totals user attempts: '+ str(g_stats[2]), 'black', -510, y_coord + -470)
                draw_header(write_turt, 'Totals comp attempts: '+ str(g_stats[1]), 'black', -510, y_coord + -495)
                #store attempts and counts for analysis
                stored_solutions = solutions
                stored_black_counts = black_counts_absolute
                stored_white_counts = white_counts_absolute
                #clean out vars
                white_counts_absolute = []
                black_counts_absolute = []                
                #ask user for another round
                if start_mode == 1:
                    draw_header(write_turt, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                    while True:
                        pause(pause_turt, -1000,-0)
                        play_again()                    
                        if next_round[0] != 0:               
                            break
                else:
                    next_round[0] = 1
                    sleep(3)
                if next_round[0] == 1:
                    proceed = 0
                    mode[0] = 1                    
                    #reset screen and all turtles
                    turtle.resetscreen()
                    for t in col_turts:
                        t.hideturtle()
                    pause_turt.hideturtle()
                    submit_turt.hideturtle()
                    write_turt.hideturtle()
                    for t in pick_turts:
                        t.hideturtle()        
                    for t in sol_turts:
                        t.hideturtle()
                    for t in mark_turts:
                        t.hideturtle()        
                    break
                else:                           
                   mode[0] = 3
                   break
            
            if proceed == 2:
                #black and white count of this solution against each previous solution
                #must be same as absolute black and white counts of those previous solutions
                if i >= 1:
                    a = 0
                    while a < i:             
                        if black_count(solution[a], solution[i]) != black_counts_absolute[a]:
                            a = i + 1                    
                        else:
                            a += 1    
                    if a == i:
                        proceed = 3
                    if a > i:
                        del black_counts_absolute[-1]
                        del solution[-1]
                        proceed = 0            
                    if proceed == 3:
                        white_counts_absolute.append(white_count(assignm, solution[i]))
                        a = 0
                        while a < i:
                            if white_count(solution[a], solution[i]) != white_counts_absolute[a]:
                                a = i + 1                    
                            else:
                                a += 1    
                        if a == i:
                            proceed = 4
                        if a > i:
                            del white_counts_absolute[-1]
                            del black_counts_absolute[-1]
                            del solution[-1]
                            proceed = 0                   
                    if proceed == 4:
                        solutions.append(solution[i])                        
                        #draw solution
                        x = 0
                        y = y_coord + i * -120
                        for (key, color) in enumerate(solution[i]):
                            draw_bars(sol_turts[key], x, y, color)
                            x += 20
                        #draw black marks
                        x = 120
                        yy = y_coord + i * -120
                        for blacks in range(black_counts_absolute[i]):
                            draw_mark(mark_turts[blacks], x, y, 'black')
                            x += 10
                        #draw white marks
                        x = 160
                        y = y_coord + i * -120
                        for whites in range(white_counts_absolute[i] - black_counts_absolute[i]):
                            draw_mark(mark_turts[whites], x, y, 'white')
                            x +=10                          
                        i += 1
                        proceed = 0                   
                
                else:
                    white_counts_absolute.append(white_count(assignm, solution[i]))
                    solutions.append(solution[i])                    
                    #draw attempts header
                    draw_header(write_turt, 'Attempts', 'black', 0, y_coord + 115)
                    #draw solution
                    x = 0
                    y = y_coord
                    for (key, color) in enumerate(solution[i]):
                        draw_bars(sol_turts[key], x, y, color)
                        x += 20                        
                    #draw marks header
                    draw_header(write_turt, 'Marks', 'black', 120, y_coord + 115)
                    #draw black marks
                    x = 120
                    y = y_coord
                    for blacks in range(black_counts_absolute[i]):
                        draw_mark(mark_turts[blacks], x, y, 'black')
                        x +=10
                    #draw white marks
                    x = 160
                    y = y_coord
                    for whites in range(white_counts_absolute[i] - black_counts_absolute[i]):
                        draw_mark(mark_turts[whites], x, y, 'white')
                        x +=10                        
                    i += 1
                    proceed = 0        
     
    '''comp assigns problem, user solves'''
    if mode[0] == 1:
        i = 0
        next_round[0] = 0
        solutions = []
        #draw full set, human is on
        draw_header(write_turt, 'human is on', 'red', -510, y_coord + 185, 'bold')
        draw_full_set(col_turts, -500, 40, -660, full_set)
        assignm = random.sample(full_set,4)        
        #draw mystery assignm + header
        draw_header(write_turt, assignm, 'black', -500, y_coord + 115)
        x = -500
        y = y_coord
        for (key, color) in enumerate(assignm):
            draw_bars(sol_turts[key], x, y, 'grey')
            x += 20        
        while True:
            #let user choose colors
            u_choice = ['red', 'red','red', 'red']    
            draw_color_picker(-500, 40, -220, pick_turts)        
            while True:
                pause(pause_turt, -1000,-0)
                if submit_turt.color() == ('grey', 'grey'):               
                    break                             
            #calculate black marks, and...
            solutions.append(u_choice)
            black_counts_absolute.append(black_count(assignm, solutions[i]))
            
            #...if success, draw assignm, break
            if black_counts_absolute[i] == 4:                
                #draw solution + header
                draw_header(write_turt, 'Solution', 'black', -300, y_coord + 115)
                x = -300
                y = y_coord
                for (key, color) in enumerate(solutions[i]):
                    draw_bars(sol_turts[key],x,y,color)
                    x += 20                     
                #draw assignm
                x = -500
                y = y_coord
                for (key, color) in enumerate(assignm):
                    draw_bars(sol_turts[key], x,y,color)
                    x += 20
                #collect match and game stats
                rounds_played += 0.5
                user_attempts += i
                time = strftime("%d.%m.%Y, %H:%M", localtime())
                m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)
                g_stats = game_stats(file_path)
                #display stats
                draw_header(write_turt, "Match stats:", 'red', -510, y_coord + -310)
                draw_header(write_turt, "Rounds played: "+ str(int(rounds_played)), 'black', -510, y_coord + -335)
                draw_header(write_turt, 'User attempts: '+ str(user_attempts), 'black', -510, y_coord + -360)
                draw_header(write_turt, 'Comp attempts: '+ str(comp_attempts), 'black', -510, y_coord + -385)
                draw_header(write_turt, 'Previous games: ', 'red', -510, y_coord + -420)
                draw_header(write_turt, 'Games total: '+ str(int(g_stats[0])), 'black', -510, y_coord + -445)
                draw_header(write_turt, 'Totals user attempts: '+ str(g_stats[2]), 'black', -510, y_coord + -470)
                draw_header(write_turt, 'Totals comp attempts: '+ str(g_stats[1]), 'black', -510, y_coord + -495)
                #store attempts and counts for analysis
                stored_solutions = solutions
                stored_black_counts = black_counts_absolute
                stored_white_counts = white_counts_absolute
                #clean out vars
                white_counts_absolute = []
                black_counts_absolute = []
                draw_header(write_turt, "press 'a' for analysis of your attempts, else press 's'", 'blue', -510, y_coord + -545)
                see_analysis[0] = 0
                while True:
                    pause(pause_turt, -1000,-0)
                    show_analysis()                    
                    if see_analysis[0] != 0:               
                        break                
                turtle.resetscreen()
                pause_turt.hideturtle()
                submit_turt.hideturtle()
                write_turt.hideturtle()
                for t in pick_turts:
                    t.hideturtle()        
                for t in sol_turts:
                    t.hideturtle()
                for t in mark_turts:
                    t.hideturtle()
                for t in col_turts:
                    t.hideturtle()
                    
                if see_analysis[0] == 1:
                    alert = ''
                    i = len(stored_solutions) -1
                    if i <= 1:
                        alert += 'at least two attempts needed for analysis, you got lucky!'
                    if i >= 1:
                        attempt_counter = 1            
                        while attempt_counter < i:
                            a = 0
                            alert_counter = 0
                            alert += '\n'
                            while a < attempt_counter:
                                if black_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_black_counts[a]:
                                    alert += 'In attempt ' + str((attempt_counter + 1)) + ', we see ' + str(black_count(stored_solutions[a], stored_solutions[attempt_counter])) + ' black(s) against attempt ' +  str(a + 1) + ', which had ' + str(stored_black_counts[a]) + '\n'
                                    alert_counter += 1
                                if white_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_white_counts[a] and white_count(stored_solutions[a], stored_solutions[attempt_counter]) != black_count(stored_solutions[a], stored_solutions[attempt_counter]):                            
                                    alert += 'In attempt ' + str((attempt_counter + 1)) + ', we find ' + str(white_count(stored_solutions[a], stored_solutions[attempt_counter]) - black_count(stored_solutions[a], stored_solutions[attempt_counter])) + ' white(s) against attempt ' +  str(a + 1) + ', which had ' + str(stored_white_counts[a] - stored_black_counts[a]) + '\n'
                                    alert_counter += 1
                                #print(a)
                                a +=1
                            if alert_counter < 1:
                                alert += 'No errors in attempt ' + str((attempt_counter + 1)) + ' \n '
                            attempt_counter += 1
                    #print(alert)
                    draw_header(write_turt, 'Analysis', 'red', -510, y_coord + 115)
                    
                    #draw solution
                    draw_header(write_turt, 'Attempts', 'black', 80, y_coord + 115)
                    draw_header(write_turt, 'Marks', 'black', 200, y_coord + 115)
                    draw_header(write_turt, 'Solution', 'black', -300, y_coord + 115)
                    draw_header(write_turt, str(len(stored_solutions)), 'black', 280, y_coord + 115)
                    x = -300
                    for (key, color) in enumerate(stored_solutions[-1]):
                            draw_bars(sol_turts[key], x, y_coord, color)
                            x += 20
                    for i in range(len(stored_solutions) - 1):    
                        if i > 4:
                            x = 380
                            y = y_coord + -120 * (i -5)
                        else:
                            x = 80
                            y = y_coord + -120 * i
                        for (key, color) in enumerate(stored_solutions[i]):
                            draw_bars(sol_turts[key], x, y, color)
                            x += 20            
                        if i > 4:
                            x = 520
                            y = y_coord + -120 * (i -5)
                        else:
                            x = 200
                            y = y_coord + -120 * i
                        for blacks in range(stored_black_counts[i]):
                            draw_mark(mark_turts[blacks], x, y, 'black')
                            x += 10
                        #draw white marks
                        if i > 4:
                            x = 560
                            y = y_coord + -120 * (i -5)
                        else:
                            x = 240
                            y = y_coord + -120 * i
                        for whites in range(stored_white_counts[i] - stored_black_counts[i]):
                            draw_mark(mark_turts[whites], x, y, 'white')
                            x += 10 
                    
                    draw_header(write_turt, alert, 'black', -510, 0, 'small')
                    draw_header(write_turt, "press 'g' when you are ready to move on", 'blue', -510, y_coord + -545)
                    next_stage[0] = 0
                    while True:
                        pause(pause_turt, -1000,-0)
                        move_on()                    
                        if next_stage[0] == 1:               
                            break
                    turtle.resetscreen()
                    for t in col_turts:
                        t.hideturtle()
                    for t in sol_turts:
                        t.hideturtle()
                    for t in pick_turts:
                        t.hideturtle()
                    pause_turt.hideturtle()
                    submit_turt.hideturtle()
                    write_turt.hideturtle()                                 
                    for t in mark_turts:
                        t.hideturtle()
                    #ask user for another round
                    if start_mode == 0:
                        draw_header(write_turt, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                        next_round[0] = 0
                        while True:
                            pause(pause_turt, -1000,-0)                            
                            play_again()                    
                            if next_round[0] != 0:               
                                break
                    else:
                        next_round[0] = 1
                        #sleep(3)
                    if next_round[0] is 1:
                        mode[0] = 0
                        #reset screen and all turtles
                        turtle.resetscreen()
                        for t in col_turts:
                            t.hideturtle()
                        for t in sol_turts:
                            t.hideturtle()
                        for t in pick_turts:
                            t.hideturtle()
                        pause_turt.hideturtle()
                        submit_turt.hideturtle()
                        write_turt.hideturtle()                                 
                        for t in mark_turts:
                            t.hideturtle()                    
                        break
                    else:                           
                       mode[0] = 3
                       break 
                        
                if see_analysis[0] ==2:
                    turtle.resetscreen()
                    for t in col_turts:
                        t.hideturtle()
                    for t in sol_turts:
                        t.hideturtle()
                    for t in pick_turts:
                        t.hideturtle()
                    pause_turt.hideturtle()
                    submit_turt.hideturtle()
                    write_turt.hideturtle()                                 
                    for t in mark_turts:
                        t.hideturtle()
                    #ask user for another round
                    if start_mode == 0:
                        draw_header(write_turt, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                        next_round[0] = 0
                        while True:
                            pause(pause_turt, -1000,-0)                            
                            play_again()                    
                            if next_round[0] != 0:               
                                break
                    else:
                        next_round[0] = 1
                        sleep(3)
                    if next_round[0] is 1:
                        mode[0] = 0
                        #reset screen and all turtles
                        turtle.resetscreen()
                        for t in col_turts:
                            t.hideturtle()
                        for t in sol_turts:
                            t.hideturtle()
                        for t in pick_turts:
                            t.hideturtle()
                        pause_turt.hideturtle()
                        submit_turt.hideturtle()
                        write_turt.hideturtle()                                 
                        for t in mark_turts:
                            t.hideturtle()                    
                        break
                    else:                           
                       mode[0] = 3
                       break  
            
            #draw solution
            draw_header(write_turt, 'Attempts', 'black', 0, y_coord + 115)
            if i > 4:
                x = 300
                y = y_coord + -120 * (i -5)
            else:
                x = 0
                y = y_coord + -120 * i
            for (key, color) in enumerate(solutions[i]):
                draw_bars(sol_turts[key], x, y, color)
                x += 20            
            #calculate white marks
            white_counts_absolute.append(white_count(assignm, solutions[i]))            
            #draw marks header
            draw_header(write_turt, 'Marks', 'black', 120, y_coord + 115)
            #draw black marks
            if i > 4:
                x = 440
                y = y_coord + -120 * (i -5)
            else:
                x = 120
                y = y_coord + -120 * i
            for blacks in range(black_counts_absolute[i]):
                draw_mark(mark_turts[blacks], x, y, 'black')
                x += 10
            #draw white marks
            if i > 4:
                x = 480
                y = y_coord + -120 * (i -5)
            else:
                x = 160
                y = y_coord + -120 * i
            for whites in range(white_counts_absolute[i] - black_counts_absolute[i]):
                draw_mark(mark_turts[whites + black_counts_absolute[i]], x, y, 'white')
                x += 10                
            i += 1
    #quit the game
    if mode[0] == 3:
        if file_path != '':
            with open(file_path) as storage:
                g_stats = json.load(storage)
            g_stats.update(m_stats)
            with open(file_path, 'w') as storage:    
                json.dump(g_stats, storage)
        turtle.resetscreen()
        pause_turt.hideturtle()
        submit_turt.hideturtle()
        write_turt.hideturtle()
        for t in pick_turts:
            t.hideturtle()        
        for t in sol_turts:
            t.hideturtle()
        for t in mark_turts:
            t.hideturtle()
        for t in col_turts:
            t.hideturtle()
        draw_header(write_turt, 'bye', 'black', 0, 0)
        turtle.done()
        break      
wn.mainloop()
