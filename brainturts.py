#!/usr/bin/python

######Set path to a file where match statistics can be stored#####
file_path = "/home/uk/dev/sites/coding/learning/braintwister/stats.json"
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
 
def draw_bars(colorlist, x, y, x_offset, y_offset):
    peg_ts = []         
    for i in range(len(colorlist)):
        peg_ts.append(turtle.Turtle(visible = False))
        peg_ts[i].speed(0)
        peg_ts[i].color(colorlist[i])
        peg_ts[i].penup()
        peg_ts[i].setx(x + i * x_offset)
        peg_ts[i].sety(y + y_offset)
        peg_ts[i].pendown()
        peg_ts[i].begin_fill()
        peg_ts[i].left(90)
        peg_ts[i].forward(100)
        peg_ts[i].right(90)
        peg_ts[i].forward(10)
        peg_ts[i].right(90)
        peg_ts[i].forward(100)
        peg_ts[i].right(90)
        peg_ts[i].forward(10)
        peg_ts[i].right(180)
        peg_ts[i].end_fill()
 
    
def draw_marks(src, x, y, x_offset, y_offset, color):
    mark_ts = []
    for i in range(src):
        mark_ts.append(turtle.Turtle(visible = False))
        mark_ts[i].speed(0)
        mark_ts[i].penup()
        mark_ts[i].color(color, color)    
        mark_ts[i].setx(x + x_offset * i)
        mark_ts[i].sety(y + y_offset)
        mark_ts[i].pendown()
        mark_ts[i].begin_fill()    
        mark_ts[i].left(90)
        mark_ts[i].forward(20)
        mark_ts[i].right(90)
        mark_ts[i].forward(5)
        mark_ts[i].right(90)
        mark_ts[i].forward(20)
        mark_ts[i].right(90)
        mark_ts[i].forward(5)
        mark_ts[i].left(180)
        mark_ts[i].end_fill()        
    
def draw_header(t, msg, color, x, y, size='regular'):
    t.hideturtle()
    t.speed(0)
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
        
def create_col_ts(src, size, shape):
    global col_ts
    col_ts = list()
    for i in range(len(src)):                
        col_ts.append(turtle.Turtle(shape = 'circle', visible = False))
    if shape != 'default':
        for turt in col_ts:
            turt.shape(shape)
    if size != 'default':
        for turt in col_ts:
            turt.resizemode('user')
            turt.shapesize(2,2,2)

def color_wheel_submit(x, y):
    if x > -520 and x < -450 and y > -30 and y <-2:
        submit_t.color('grey')
        
def color_change(x, y):
    if x > -509 and x < -489:
        count = 0
    if x > -469 and x < -449:
        count = 1
    if x > -429 and x < -409:
        count = 2
    if x > -389 and x < -369:
        count = 3
    if col_ts[count].pencolor() == source_set[0]:
        col_ts[count].color(source_set[1])
    elif col_ts[count].pencolor() == source_set[1]:
        col_ts[count].color(source_set[2])
    elif col_ts[count].pencolor() == source_set[2]:
        col_ts[count].color(source_set[3])
    elif col_ts[count].pencolor() == source_set[3]:
        col_ts[count].color(source_set[4])
    elif col_ts[count].pencolor() == source_set[4]:
        col_ts[count].color(source_set[0])
    u_choice[count] = col_ts[count].pencolor()  

def draw_color_picker(colorlist, offset, x, y, size = 'default', shape = 'default'):
    draw_header(write_t, 'pick your colors', 'black', offset + -5, y + y_coord + 20)
    create_col_ts(colorlist, size, shape)
    for i in range(len(colorlist)):
        col_ts[i].penup()
        col_ts[i].setx(offset + x * i)    
        col_ts[i].sety(y + y_coord)        
        col_ts[i].color(colorlist[0])
        col_ts[i].showturtle()          
        col_ts[i].onclick(color_change)
    submit_t.penup()
    submit_t.setx(offset + -10)
    submit_t.sety(y + y_coord + -40)
    submit_t.color('green')
    submit_t.write('submit', move= True, font=('arial', 16, 'bold'))
    wn.onscreenclick(color_wheel_submit)
    
def draw_full_set(colorlist, offset, x, y, size = 'default', shape = 'default'):
    create_col_ts(colorlist, size, shape)
    for (i, col) in enumerate(colorlist):
        col_ts[i].speed(0)
        col_ts[i].penup()
        col_ts[i].setx(offset + x * i)    
        col_ts[i].sety(y + y_coord)        
        col_ts[i].color(col)
        col_ts[i].showturtle()
        
def select_color(x,y):
    #calculate a number from x,y values, which is used to assign a color from the list to the pick_ts
    row = round((start_y - y) / y_offset)
    if row < 0:
        row = row * -1
    pos = round((start_x - x) / x_offset)
    if pos < 0:
        pos = pos * -1
    count = pos + row_length * row
    picked_colors.append(all_colors[count])
    for i in range(len(col_ts)):
        col_ts[i].color(picked_colors[(i + 1) * -1])


def draw_cols(colorlist, x_offset, y_offset, row_length, size = 'default', shape = 'default'):
    # draw dynamic grid of clickable colors
    create_col_ts(colorlist, size, shape)
    num_rows = 0
    if len(colorlist) % row_length == 0:
        num_rows = int(len(colorlist) / row_length)
    else:
        num_rows = int(len(colorlist) / row_length) + 1
    for rows in range(num_rows):
        for i in range(row_length):
            if i + row_length * rows < len(colorlist):
                col_ts[i + row_length * rows].speed(0)
                col_ts[i + row_length * rows].penup()
                col_ts[i + row_length * rows].setx(start_x + x_offset * i)    
                col_ts[i + row_length * rows].sety(start_y - y_offset * rows)        
                col_ts[i + row_length * rows].color(colorlist[i + row_length * rows])
                col_ts[i + row_length * rows].showturtle()
                col_ts[i + row_length * rows].onclick(select_color)
            i += 1
        rows += 1

def draw_picked_cols(colorlist, x_offset, y_offset, size = 'default', shape = 'default'):
    create_col_ts(colorlist, size, shape)
    for i in range(len(colorlist)):
        col_ts[i].hideturtle()
        col_ts[i].speed(0)
        col_ts[i].penup()
        col_ts[i].hideturtle()
        col_ts[i].color(colorlist[i * -1])
        col_ts[i].setx(start_x + x_offset * i)
        col_ts[i].sety(start_y + y_offset)
        col_ts[i].showturtle()

def color_submit(x, y):
    if x > start_x + x_offset * 4 and x < start_x + x_offset * 5 and y > start_y + y_offset * 1 and y < start_y + y_offset * 1.5:
        submit_t.pencolor('grey') 
        
def submit():
    submit_t.hideturtle()
    submit_t.penup()
    submit_t.setx(start_x + x_offset * 4)
    submit_t.sety(start_y + y_offset)
    submit_t.color('green')
    submit_t.write('submit', move= True, font=('arial', 16, 'bold'))
    wn.onscreenclick(color_submit)

        
def pause(t,x,y):
    t.hideturtle()
    t.up()
    t.setx(x)
    t.sety(y)
    t.speed(0)
    t.forward(0)     
    
#define turtles used in more than one mode
submit_t = turtle.Turtle(visible = False)
submit_t.shape('triangle')
pause_t = turtle.Turtle(visible = False)
write_t = turtle.Turtle(visible = False)
write_t.shape('square')
    
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
def get_set(src):
    new_set = []
    for i in range(0,max_num_color):
        for item in src:
            new_set.append(item)
    return new_set            

def duo_mode():
    mode[0] = 'duo'    
def opt_mode():
    mode[0] = 'options'
def end_mode():
    mode[0] = 'end'
def mode_choice():
    wn.onkey(duo_mode, "1")
    wn.onkey(opt_mode, '2')
    wn.onkey(end_mode, '3')
    wn.listen()

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
    move_on[0] = 1
def move_switch():
    wn.onkey(move, 'g')
    wn.listen()

def c_turn():
    whos_on[0] = 'comp'
def u_turn():
    whos_on[0] = 'user'
def turn_choice():
    wn.onkey(u_turn, 'u')
    wn.onkey(c_turn, 'c')
    wn.listen()

#build stats, options dict
def match_stats(time, rounds, comp_attempts, user_attempts):
    m_stats = {time: {'rounds': rounds, 'comp_attempts': comp_attempts, 'user_attempts': user_attempts}}
    return m_stats

def user_options():
    vals = {'user options': {'u_name': u_name, 'u_colors': u_colors, 'max_num_color': max_num_color}}
    return vals
    
    
def game_stats(path):
    g_rounds = 0
    g_comp_attempts = 0
    g_user_attempts = 0
    with open(path) as storage:
        stored_stats = json.load(storage)
    for k, v in stored_stats.items():
        if k != 'user options':
            g_rounds += v['rounds']
            g_comp_attempts += v['comp_attempts']
            g_user_attempts += v['user_attempts']
    g_stats = [g_rounds, g_comp_attempts, g_user_attempts]
    return g_stats

#vars used in more than one mode
u_name = ''
if file_path != '':
    with open(file_path) as storage:
        options = json.load(storage)
        for k,v in options.items():
            if k == 'user options' and v['u_name'] != '':        
                u_name = options['user options']['u_name']
mode = ['start']    
u_colors = []
move_on = [0]
'''START OF GAME'''
while True:
    if mode[0] == 'start':
        start_x = -520
        start_y = 300
        if u_name != '':
            draw_header(write_t, 'welcome back to mindturts, ' + u_name, 'black', -200, start_y + 55)
        else:
            draw_header(write_t, 'welcome to mindturts!', 'black', -200, start_y + 55)
        draw_header(write_t, 'be smarter than the computer', 'black', -200, start_y + 30)
        draw_header(write_t, 'mission: find out which four colored pegs the opponent secretely has chosen', 'black', -200, start_y + 10)
        draw_header(write_t, 'the computer can not err, so you better make no mistakes either...', 'black', -200, start_y + -30)
        draw_header(write_t, 'good luck!', 'black', -200, start_y + -60)
        draw_header(write_t, "press '1' to start a new match", 'blue', -510, start_y + -545)
        draw_header(write_t, "press '2' to set game options", 'blue', -510, start_y + -570)
        draw_header(write_t, "press '3' to end the game", 'blue', -510, start_y + -595)
        while True:
            pause(pause_t, -1000,-0)
            mode_choice()
            if mode[0] != 'start':
                wn.tracer(2)
                break
        wn.clearscreen()
        
    if mode[0] == 'options':
        wn.bgcolor('lightgreen')
        wn.title('mindturts - options')
        all_colors = ['Black', 'Navy', 'DarkBlue', 'MediumBlue', 'Blue', 'DarkGreen', 'Green', 'DarkCyan', 'DeepSkyBlue', 'DarkTurquoise', 'MediumSpringGreen', 'Lime', 'SpringGreen', 'Aqua', 'Cyan', 'MidnightBlue', 'DodgerBlue', 'LightSeaGreen', 'ForestGreen', 'SeaGreen', 'DarkSlateGray', 'LimeGreen', 'MediumSeaGreen', 'Turquoise', 'RoyalBlue', 'SteelBlue', 'DarkSlateBlue', 'MediumTurquoise', 'Indigo', 'DarkOliveGreen', 'CadetBlue', 'CornflowerBlue', 'RebeccaPurple', 'MediumAquaMarine', 'DimGray', 'SlateBlue', 'SlateGray', 'LightSlateGray', 'MediumSlateBlue', 'Chartreuse', 'Aquamarine', 'Maroon', 'Purple', 'Olive', 'Grey', 'SkyBlue', 'LightSkyBlue', 'PaleGreen', 'DarkGray', 'DarkGrey', 'LightBlue', 'GreenYellow', 'PaleTurquoise', 'LightSteelBlue', 'PowderBlue', 'FireBrick', 'DarkGoldenRod', 'MediumOrchid', 'RosyBrown', 'DarkKhaki', 'Silver', 'MediumVioletRed', 'IndianRed', 'Peru', 'Chocolate', 'LightGray', 'Orchid', 'GoldenRod', 'Gainsboro', 'Plum', 'BurlyWood', 'LightCyan', 'Lavender', 'DarkSalmon', 'Violet', 'PaleGoldenRod', 'LightCoral', 'Khaki', 'AliceBlue', 'HoneyDew', 'Azure', 'SandyBrown', 'Wheat', 'Beige', 'MintCream', 'GhostWhite', 'Salmon', 'AntiqueWhite', 'Linen', 'LightGoldenRodYellow', 'OldLace', 'Red', 'Fuchsia', 'Magenta', 'DeepPink', 'OrangeRed', 'Tomato', 'HotPink', 'Coral', 'DarkOrange', 'LightSalmon', 'Orange', 'LightPink', 'Pink', 'Gold', 'PeachPuff', 'NavajoWhite', 'Moccasin', 'Bisque', 'MistyRose', 'BlanchedAlmond', 'PapayaWhip', 'LavenderBlush', 'SeaShell', 'Cornsilk', 'LemonChiffon', 'Snow', 'Yellow', 'LightYellow']
        #all_colors = ['Black', 'Navy', 'DarkBlue', 'Orange', 'Beige']

        start_x = -520
        start_y = 300
        x_offset = 60
        y_offset = 60
        row_length = 15
        picked_colors = ['white', 'white','white','white','white']

        draw_header(write_t, 'Please choose your name', 'black', start_x + 250, start_y + 115)
        u_name = wn.textinput('username', 'Please, type your name')
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        write_t.hideturtle()
        #ask user for for number of doublettes
        draw_header(write_t, "Are double colors allowed?", 'black', start_x + 250, start_y + 115)
        doubles = turtle.textinput('Doubles allowed', 'Yes or no?')
        if doubles in ('yes', 'Yes', 'y'):
            max_num_color = 2
        else:
            max_num_color = 1
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        write_t.hideturtle()
        choose_color_msg = 'thanks, '+ u_name + ', please choose five colors to play with'
        draw_header(write_t, choose_color_msg, 'black', start_x, start_y + 115)
        write_t.hideturtle()
        wn.tracer(2)
        draw_cols(all_colors, 60, 60, 15, 'big', 'square')
        draw_picked_cols(picked_colors, 30, 70)
        submit()        
        while True:
            pause(pause_t, -1000,-0)
            if submit_t.pencolor() == 'grey':               
                break
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        for i in range(5):
            u_colors.append(picked_colors[(i + 1) * -1])    
        draw_cols(u_colors, 60, 60, 15, 'big', 'circle')
        draw_header(write_t, "press 'g' when you are ready to move on", 'blue', -510, start_y + -545)
        while True:
            pause(pause_t, -1000,-0)
            move_switch()                    
            if move_on[0] == 1:
                wn.clearscreen()
                u_options = user_options()
                if file_path != '':
                    with open(file_path) as storage:
                        options = json.load(storage)
                        options.update(u_options)
                    with open(file_path, 'w') as storage:    
                        json.dump(options, storage)
                mode[0] = 'duo'
                break
          
    #elif mode == 'single':
        #start_single

    elif mode[0] == 'duo':
        wn.bgcolor('lightgreen')
        wn.tracer(1)
        wn.title('mindturts - human vs. computer')
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
        whos_on = ['notset']
        next_round = [0]
        next_stage = [0]
        see_analysis = [0]
        max_num_color = 2
        if file_path != '':
            with open(file_path) as storage:
                options = json.load(storage)
                u_colors = options['user options']['u_colors']
                u_name = options['user options']['u_name']
                max_num_color = options['user options']['max_num_color']
        
        while True:
            #draw opening screen, set up the game
            if whos_on[0] == 'notset':
                #ask user who begins
                draw_header(write_t, "who is first? type 'u' for your turn or 'c' for my turn!", 'blue', -500, y_coord + -500)
                write_t.hideturtle()
                while True:
                    pause(pause_t, -1000,-0)
                    turn_choice()
                    if whos_on[0] != 'notset':
                        break
                start_mode = whos_on[0]
                #define set
                if u_colors != []:
                    source_set = u_colors
                else:
                    source_set = ['blue','red','green','yellow','orange']
                #num_pegs = int(turtle.numinput('Number of slots', 'How many pegs?'))
                num_pegs = 4
                #create set of pegs
                full_set = get_set(source_set)
                #create turtles, set up for drawing pegs, results, headers etc.
                wn.tracer(2)    
                wn.clearscreen()
                pause_t.hideturtle()
                
            '''user assigns problem, comp solves'''
            if whos_on[0] == 'comp':
                if mode[0] != 'duo':
                    break
                wn.bgcolor('lightgreen')
                i = 0
                next_round[0] = 0
                solution = []
                solutions = []
                #draw full set, comp is on
                wn.tracer(1)
                draw_header(write_t, 'comp is on', 'red', -510, y_coord + 185, 'bold')
                draw_full_set(full_set, -500, 40, -660)
                #let user choose colors
                u_choice = []
                for j in range(4):
                    u_choice.append(source_set[0])                
                draw_color_picker(u_choice, -500, 40, -220)        
                while True:
                    pause(pause_t, -1000,-0)
                    if submit_t.pencolor() == 'grey':
                        wn.tracer(2)
                        break                    
                #reset screen and all turtles
                wn.clearscreen()                
                #draw hidden assignm + header
                wn.bgcolor('lightgreen')
                assignm = u_choice
                draw_header(write_t, 'Assignment', 'black', -500, y_coord + 115)
                draw_bars(assignm, -500, y_coord, 20, 0)
                while True:
                    if proceed == 0:
                        wn.tracer(1)
                        #choose random colors, make sure it's not the same as previous attempts
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
                    #if success, i.e. identical colors in identical positions as assignment, draw assignm, solution, stats; clean out vars & break        
                    if proceed == 5:
                        wn.tracer(1)
                        #draw solution + header
                        draw_header(write_t, 'Solution', 'black', -300, y_coord + 115)
                        draw_bars(solution[i], -300, y_coord, 20, 0)
                        draw_bars(assignm, -500, y_coord, 20, 0)
                        #collect match and game stats and display
                        wn.tracer(1)
                        rounds_played += 0.5
                        comp_attempts += i
                        time = strftime("%d.%m.%Y, %H:%M", localtime())
                        m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)                    
                        draw_header(write_t, "Match stats:", 'red', -510, y_coord + -310)
                        draw_header(write_t, "Rounds played: "+ str(int(rounds_played)), 'black', -510, y_coord + -335)
                        draw_header(write_t, 'User attempts: '+ str(user_attempts), 'black', -510, y_coord + -360)
                        draw_header(write_t, 'Comp attempts: '+ str(comp_attempts), 'black', -510, y_coord + -385)
                        if file_path != '':
                            g_stats = game_stats(file_path)
                            draw_header(write_t, 'Previous games: ', 'red', -510, y_coord + -420)
                            draw_header(write_t, 'Games total: '+ str(int(g_stats[0])), 'black', -510, y_coord + -445)
                            draw_header(write_t, 'Totals user attempts: '+ str(g_stats[2]), 'black', -510, y_coord + -470)
                            draw_header(write_t, 'Totals comp attempts: '+ str(g_stats[1]), 'black', -510, y_coord + -495)
                        #store attempts and counts for analysis
                        stored_solutions = solutions
                        stored_black_counts = black_counts_absolute
                        stored_white_counts = white_counts_absolute
                        #clean out vars
                        white_counts_absolute = []
                        black_counts_absolute = []                
                        #ask user for another round
                        if start_mode == 'user':
                            draw_header(write_t, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                            while True:
                                pause(pause_t, -1000,-0)
                                play_again()                    
                                if next_round[0] != 0:               
                                    break
                        else:
                            next_round[0] = 1
                            draw_header(write_t, "press 'g' when you are ready to move on", 'blue', -510, y_coord + -545)
                            while True:
                                pause(pause_t, -1000,-0)
                                move_switch()                    
                                if move_on[0] == 1:
                                    wn.tracer(2)
                                    break
                        if next_round[0] == 1:
                            proceed = 0
                            whos_on[0] = 'user'                    
                            #reset screen and all turtles
                            wn.clearscreen()
                            break
                        else:                           
                            mode[0] = 'end' 
                            break
                    
                    if proceed == 2:
                        #black and white count of this solution against each previous solution must be same as absolute black and white counts of those previous solutions
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
                                draw_bars(solution[i], 0, y_coord, 20, i * -120)    
                                #draw black, white marks
                                draw_marks(black_counts_absolute[i], 120, y_coord, 10, -120 * i, 'black')
                                draw_marks( white_counts_absolute[i] - black_counts_absolute[i], 160, y_coord, 10, -120 * i, 'white')
                                sleep(2)
                                i += 1
                                proceed = 0                   
                        
                        else:
                            white_counts_absolute.append(white_count(assignm, solution[i]))
                            solutions.append(solution[i])                    
                            #draw attempts header
                            draw_header(write_t, 'Attempts', 'black', 0, y_coord + 115)
                            #draw solution
                            draw_bars(solution[i], 0, y_coord, 20, 0)
                            #draw marks header, black, white marks
                            draw_header(write_t, 'Marks', 'black', 120, y_coord + 115)
                            draw_marks(black_counts_absolute[i], 120, y_coord, 10, 0, 'black')
                            draw_marks(white_counts_absolute[i] - black_counts_absolute[i], 160, y_coord, 10, 0, 'white')
                            sleep(2)
                            i += 1
                            proceed = 0
            
            '''comp assigns problem, user solves'''
            if whos_on[0] == 'user':
                if mode[0] != 'duo':
                    break
                wn.bgcolor('lightgreen')
                wn.tracer(1)
                mark_turts = list()
                for l in range(len(source_set)):
                    mark_turts.append(turtle.Turtle(visible = False))
                i = 0
                next_round[0] = 0
                solutions = []
                #draw full set, human is on
                if u_name != '':
                    draw_header(write_t, u_name + ' is on', 'red', -510, y_coord + 185, 'bold')
                else:    
                    draw_header(write_t, 'human is on', 'red', -510, y_coord + 185, 'bold')
                draw_full_set(full_set, -500, 40, -660)
                assignm = random.sample(full_set,4)        
                #draw mystery assignm + header
                draw_header(write_t, assignm, 'black', -500, y_coord + 115)
                grey_bars = ['grey', 'grey', 'grey', 'grey']
                draw_bars(grey_bars, -500, y_coord, 20, 0)
                while True:
                    #let user choose colors
                    wn.tracer(2)
                    u_choice = []
                    for j in range(4):
                        u_choice.append(source_set[0])
                    draw_color_picker(u_choice, -500, 40, -220)        
                    while True:
                        pause(pause_t, -1000,-0)
                        if submit_t.color() == ('grey', 'grey'):               
                            break                             
                    #calculate black marks, and...
                    solutions.append(u_choice)
                    black_counts_absolute.append(black_count(assignm, solutions[i]))
                    wn.tracer(1)
                    #...if success, draw assignm, break
                    if black_counts_absolute[i] == 4:                
                        #draw solution + header
                        draw_header(write_t, 'Solution', 'black', -300, y_coord + 115)
                        draw_bars(solutions[i], -300, y_coord, 20, 0)
                        draw_bars(assignm, -500, y_coord, 20, 0)
                        #collect, display match and game stats
                        rounds_played += 0.5
                        user_attempts += i
                        time = strftime("%d.%m.%Y, %H:%M", localtime())
                        m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)
                        draw_header(write_t, "Match stats:", 'red', -510, y_coord + -310)
                        draw_header(write_t, "Rounds played: "+ str(int(rounds_played)), 'black', -510, y_coord + -335)
                        draw_header(write_t, 'User attempts: '+ str(user_attempts), 'black', -510, y_coord + -360)
                        draw_header(write_t, 'Comp attempts: '+ str(comp_attempts), 'black', -510, y_coord + -385)
                        if file_path != '':
                            g_stats = game_stats(file_path)
                            draw_header(write_t, 'Previous games: ', 'red', -510, y_coord + -420)
                            draw_header(write_t, 'Games total: '+ str(int(g_stats[0])), 'black', -510, y_coord + -445)
                            draw_header(write_t, 'Totals user attempts: '+ str(g_stats[2]), 'black', -510, y_coord + -470)
                            draw_header(write_t, 'Totals comp attempts: '+ str(g_stats[1]), 'black', -510, y_coord + -495)
                        #store attempts and counts for analysis
                        stored_solutions = solutions
                        stored_black_counts = black_counts_absolute
                        stored_white_counts = white_counts_absolute
                        #clean out vars
                        white_counts_absolute = []
                        black_counts_absolute = []
                        draw_header(write_t, "press 'a' for analysis of your attempts, else press 's'", 'blue', -510, y_coord + -545)
                        see_analysis[0] = 0
                        show_analysis()
                        while True:
                            pause(pause_t, -1000,-0)                                                
                            if see_analysis[0] != 0:               
                                break                
                        wn.clearscreen()                            
                        if see_analysis[0] == 1:
                            wn.bgcolor('lightgreen')
                            wn.tracer(2)
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
                                        #if white_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_white_counts[a] and white_count(stored_solutions[a], stored_solutions[attempt_counter]) != black_count(stored_solutions[a], stored_solutions[attempt_counter]):
                                        if white_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_white_counts[a] - stored_white_counts[attempt_counter]:
                                            alert += 'In attempt ' + str((attempt_counter + 1)) + ', we find ' + str(white_count(stored_solutions[a], stored_solutions[attempt_counter]) - black_count(stored_solutions[a], stored_solutions[attempt_counter])) + ' white(s) against attempt ' +  str(a + 1) + ', which had ' + str(stored_white_counts[a] - stored_black_counts[a]) + '\n'
                                            alert_counter += 1
                                        #print(a)
                                        a +=1
                                    if alert_counter < 1:
                                        alert += 'No errors in attempt ' + str((attempt_counter + 1)) + ' \n '
                                    attempt_counter += 1
                            #print(alert)
                            draw_header(write_t, 'Analysis', 'red', -510, y_coord + 115)                            
                            #draw solution
                            draw_header(write_t, 'Attempts', 'black', 80, y_coord + 115)
                            draw_header(write_t, 'Marks', 'black', 200, y_coord + 115)
                            draw_header(write_t, 'Solution', 'black', -300, y_coord + 115)
                            draw_header(write_t, str(len(stored_solutions)), 'black', 280, y_coord + 115)                           
                            #draw attempts, black and white counts
                            draw_bars(stored_solutions[-1], -300, y_coord, 20, 0)
                            for i in range(len(stored_solutions) - 1):    
                                if i > 4:
                                    draw_bars(stored_solutions[i], 380, y_coord, 20, -120 * (i -5))
                                else:
                                    draw_bars(stored_solutions[i], 80, y_coord, 20, -120 * i)
                                if i > 4:
                                    draw_marks(stored_black_counts[i], 520, y_coord, 10, -120 * (i -5), 'black')
                                    draw_marks(stored_white_counts[i] - stored_black_counts[i], 560, y_coord, 10, -120 * (i -5), 'white')
                                else:
                                    draw_marks(stored_black_counts[i], 200, y_coord, 10, -120 * i, 'black')
                                    draw_marks(stored_white_counts[i] - stored_black_counts[i], 240, y_coord, 10, -120 * i, 'white')
                            #draw analysis message        
                            draw_header(write_t, alert, 'black', -510, 0, 'small')
                            draw_header(write_t, "press 'g' when you are ready to move on", 'blue', -510, y_coord + -545)
                            move_on[0] = 0
                            while True:
                                pause(pause_t, -1000,-0)
                                move_switch()                    
                                if move_on[0] == 1:               
                                    break
                            wn.tracer(2)
                            wn.clearscreen()                                    
                            #ask user for another round
                            if start_mode == 'comp':
                                wn.bgcolor('lightgreen')
                                draw_header(write_t, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                                next_round[0] = 0
                                while True:
                                    pause(pause_t, -1000,-0)                            
                                    play_again()                    
                                    if next_round[0] != 0:               
                                        break
                            else:
                                next_round[0] = 1
                            if next_round[0] is 1:
                                whos_on[0] = 'comp'
                                #reset screen and all turtles
                                wn.clearscreen()
                                break
                            else:                           
                                mode[0] = 'end'
                                break 
                                
                        if see_analysis[0] == 2:
                            wn.bgcolor('lightgreen')
                            wn.tracer(2)
                            #ask user for another round
                            if start_mode == 'comp':
                                draw_header(write_t, "press 'y' for another round, press 'n' to quit", 'blue', -510, y_coord + -545)
                                next_round[0] = 0
                                while True:
                                    pause(pause_t, -1000,-0)                            
                                    play_again()                    
                                    if next_round[0] != 0:               
                                        break
                            else:
                                next_round[0] = 1
                                #sleep(3)
                            if next_round[0] is 1:
                                whos_on[0] = 'comp'
                                wn.clearscreen()                    
                                break
                            else:                           
                               mode[0] = 'end'
                               wn.clearscreen()
                               break  
                    
                    #draw solution
                    draw_header(write_t, 'Attempts', 'black', 0, y_coord + 115)                   
                    if i > 4:
                        draw_bars(solutions[i], 300, y_coord, 20, -120 * (i -5))
                    else:
                        draw_bars(solutions[i], 0, y_coord, 20, -120 * i)
                    #calculate white marks
                    white_counts_absolute.append(white_count(assignm, solutions[i]))            
                    #draw marks header, black, white marks
                    draw_header(write_t, 'Marks', 'black', 120, y_coord + 115)
                    if i > 4:
                        draw_marks(black_counts_absolute[i], 440, y_coord, 10, -120 * (i -5), 'black')
                        draw_marks(white_counts_absolute[i] - black_counts_absolute[i], 480, y_coord, 10, -120 * (i -5), 'white')
                    else:
                        draw_marks(black_counts_absolute[i], 120, y_coord, 10, -120 * i, 'black')
                        draw_marks(white_counts_absolute[i] - black_counts_absolute[i], 160, y_coord, 10, -120 * i, 'white')
                    i += 1
                    
    elif mode[0] == 'end':
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        if file_path != '' and 'm_stats' in locals():
            with open(file_path) as storage:
                g_stats = json.load(storage)
            g_stats.update(m_stats)
            with open(file_path, 'w') as storage:    
                json.dump(g_stats, storage)
        write_t.hideturtle()
        if u_name != '':
            draw_header(write_t, 'bye, '+ u_name, 'black', 0, 0)
        else:
            draw_header(write_t, 'bye', 'black', 0, 0)        
        break    
wn.mainloop()
