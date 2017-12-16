#!/usr/bin/python

######Set path to a file where match statistics can be stored#####
file_path = ''
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

def set_screensize():
    return gsize

#set grid measures for gui with factor allowing to adjust to different screen sizes
gsize = 1

x0 = -1000 * gsize
x1 = -500 * gsize
x2 = -300 * gsize
x3 = 0 * gsize
x4 = 300 * gsize
y1 = 440 * gsize
y2 = 360 * gsize
y3 = 240 * gsize
y4 = 20 * gsize
y5 = -70 * gsize
y6 = -305 * gsize
y7 = -420 * gsize
x_off = 5 * gsize
y_off = 10 * gsize
bar_height = 100 * gsize
bar_width = 10 * gsize
mark_height = 20 * gsize
mark_width = 5 * gsize
turtle_size_regular = round(1 * gsize)
turtle_size_big = round(2 * gsize)
line_space = 25 * gsize
line_space_small = 18 * gsize
short_row = round(15 * gsize)
long_row = round(24 * gsize)
font_small = round(12 * gsize)
font_regular = round(16 * gsize)
font1 = 'arial'
font2 ='helvetica'

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
        peg_ts[i].forward(bar_height)
        peg_ts[i].right(90)
        peg_ts[i].forward(bar_width)
        peg_ts[i].right(90)
        peg_ts[i].forward(bar_height)
        peg_ts[i].right(90)
        peg_ts[i].forward(bar_width)
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
        mark_ts[i].forward(mark_height)
        mark_ts[i].right(90)
        mark_ts[i].forward(mark_width)
        mark_ts[i].right(90)
        mark_ts[i].forward(mark_height)
        mark_ts[i].right(90)
        mark_ts[i].forward(mark_width)
        mark_ts[i].left(180)
        mark_ts[i].end_fill()        
    
def draw_header(t, msg, font, color, x, y, size='regular'):
    t.hideturtle()
    t.speed(0)
    t.penup()    
    t.setx(x - x_off)
    t.sety(y)
    t.pendown()
    t.pencolor(color)
    if size == 'small':
        t.write(msg, move=False, align="left", font=(font, font_small, "normal"))
    elif size == 'bold':
        t.write(msg, move=False, align="left", font=(font, font_regular, "bold"))
    else:
        t.write(msg, move=False, align="left", font=(font, font_regular, "normal"))
        
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
            turt.shapesize(turtle_size_big,turtle_size_big,turtle_size_big)

def color_wheel_submit(x, y):
    if x > x1 - x_off *2 and x < x1 + x_off * 14 and y > y4 - y_off * 4 and y < y4 - y_off * 2:
        submit_t.color('grey')
        
def color_change(x, y):
    if x > x1 - x_off * 2 and x < x1 + x_off * 2:
        count = 0
    if x > x1 + x_off * 6 and x < x1 + x_off * 10:
        count = 1
    if x > x1 + x_off * 14 and x < x1 + x_off * 18:
        count = 2
    if x > x1 + x_off * 22 and x < x1 + x_off * 26:
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

def draw_color_picker(colorlist, x, y, x_offset, y_offset, size = 'default', shape = 'default'):    
    create_col_ts(colorlist, size, shape)
    for i in range(len(colorlist)):
        col_ts[i].speed(0)
        col_ts[i].penup()
        col_ts[i].setx(x + x_offset * i)    
        col_ts[i].sety(y)        
        col_ts[i].color(colorlist[0])
        col_ts[i].showturtle()          
        col_ts[i].onclick(color_change)
    submit_t.penup()
    submit_t.setx(x - x_off *2)
    submit_t.sety(y4 + y_offset * -2)
    submit_t.color('green')
    submit_t.write('submit', move= True, font=('arial', 16, 'bold'))
    wn.onscreenclick(color_wheel_submit)
    
def draw_full_set(colorlist, x, y, x_offset, size = 'default', shape = 'default'):
    create_col_ts(colorlist, size, shape)
    for (i, col) in enumerate(colorlist):
        col_ts[i].speed(0)
        col_ts[i].penup()
        col_ts[i].setx(x + x_offset * i)    
        col_ts[i].sety(y)        
        col_ts[i].color(col)
        col_ts[i].showturtle()
        
def select_color_s(x,y):
    #deduce the corresponding colorlist item from the x/y-values
    row = round((y3 - y) / (y_off * 6))
    if row < 0:
        row = row * -1
    pos = round((x1 - x) / (x_off * 12))
    if pos < 0:
        pos = pos * -1
    count = pos + short_row * row
    picked_colors.append(all_colors[count])
    for i in range(len(col_ts)):
        col_ts[i].color(picked_colors[(i + 1) * -1])

def select_color_l(x,y):
    #calculate a number from x,y values, which is used to assign a color from the list to the pick_ts
    row = round((y3 - y) / (y_off * 6))
    if row < 0:
        row = row * -1
    pos = round((x1 - x) / (x_off * 12))
    if pos < 0:
        pos = pos * -1
    count = pos + long_row * row
    picked_colors.append(all_colors[count])
    for i in range(len(col_ts)):
        col_ts[i].color(picked_colors[(i + 1) * -1])

def draw_cols(colorlist, x, y, x_offset, y_offset, row_length, size = 'default', shape = 'default'):
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
                col_ts[i + row_length * rows].setx(x + x_offset * i)    
                col_ts[i + row_length * rows].sety(y - y_offset * rows)        
                col_ts[i + row_length * rows].color(colorlist[i + row_length * rows])
                col_ts[i + row_length * rows].showturtle()
                if row_length == short_row:
                    col_ts[i + row_length * rows].onclick(select_color_s)
                if row_length == long_row:
                    col_ts[i + row_length * rows].onclick(select_color_l)
            i += 1
        rows += 1

def draw_picked_cols(colorlist, x, y, x_offset, y_offset, size = 'default', shape = 'default'):
    create_col_ts(colorlist, size, shape)
    for i in range(len(colorlist)):
        col_ts[i].hideturtle()
        col_ts[i].speed(0)
        col_ts[i].penup()
        col_ts[i].hideturtle()
        col_ts[i].color(colorlist[i * -1])
        col_ts[i].setx(x + x_offset * i)
        col_ts[i].sety(y + y_offset)
        col_ts[i].showturtle()

def color_submit(x, y):
    if x > x2 and x < x2 + x_off * 20 and y > y2 and y < y2 + y_off * 3:
        submit_t.pencolor('grey') 
        
def submit(x, y):
    submit_t.hideturtle()
    submit_t.penup()
    submit_t.setx(x)
    submit_t.sety(y)
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

''' START OF GAME '''

while True:
    ''' START MODE '''
    if mode[0] == 'start':
        if u_name != '':
            draw_header(write_t, 'welcome back to mindturts, ' + u_name, font1, 'black', x2, y2)
        else:
            draw_header(write_t, 'welcome to mindturts!', font1, 'black', x2, y2)
        draw_header(write_t, 'be smarter than the computer', font1, 'black', x2, y2 - line_space * 2)
        draw_header(write_t, 'mission: find out which four colored pegs the opponent secretely has chosen', font1, 'black', x2, y2 - line_space * 3)
        draw_header(write_t, 'the computer can not err, so you better make no mistakes either...', font1, 'black', x2, y2 - line_space * 4)
        draw_header(write_t, 'good luck!', font1, 'black', x2, y2 - line_space * 5)
        draw_header(write_t, "press '1' to start a new match", font1, 'blue', x1, y6)
        draw_header(write_t, "press '2' to set game options", font1, 'blue', x1, y6 - line_space * 1)
        draw_header(write_t, "press '3' to end the game", font1, 'blue', x1, y6 - line_space * 2)
        while True:
            pause(pause_t, x0, y4)
            mode_choice()
            if mode[0] != 'start':
                wn.tracer(2)
                break
        wn.clearscreen()
    ''' SET USER OPTIONS '''
    if mode[0] == 'options':
        wn.bgcolor('lightgreen')
        wn.title('mindturts - options')
        all_colors = ['Black', 'Navy', 'DarkBlue', 'MediumBlue', 'Blue', 'DarkGreen', 'Green', 'DarkCyan', 'DeepSkyBlue', 'DarkTurquoise', 'MediumSpringGreen', 'Lime', 'SpringGreen', 'Aqua', 'Cyan', 'MidnightBlue', 'DodgerBlue', 'LightSeaGreen', 'ForestGreen', 'SeaGreen', 'DarkSlateGray', 'LimeGreen', 'MediumSeaGreen', 'Turquoise', 'RoyalBlue', 'SteelBlue', 'DarkSlateBlue', 'MediumTurquoise', 'Indigo', 'DarkOliveGreen', 'CadetBlue', 'CornflowerBlue', 'RebeccaPurple', 'MediumAquaMarine', 'DimGray', 'SlateBlue', 'SlateGray', 'LightSlateGray', 'MediumSlateBlue', 'Chartreuse', 'Aquamarine', 'Maroon', 'Purple', 'Olive', 'Grey', 'SkyBlue', 'LightSkyBlue', 'PaleGreen', 'DarkGray', 'DarkGrey', 'LightBlue', 'GreenYellow', 'PaleTurquoise', 'LightSteelBlue', 'PowderBlue', 'FireBrick', 'DarkGoldenRod', 'MediumOrchid', 'RosyBrown', 'DarkKhaki', 'Silver', 'MediumVioletRed', 'IndianRed', 'Peru', 'Chocolate', 'LightGray', 'Orchid', 'GoldenRod', 'Gainsboro', 'Plum', 'BurlyWood', 'LightCyan', 'Lavender', 'DarkSalmon', 'Violet', 'PaleGoldenRod', 'LightCoral', 'Khaki', 'AliceBlue', 'HoneyDew', 'Azure', 'SandyBrown', 'Wheat', 'Beige', 'MintCream', 'GhostWhite', 'Salmon', 'AntiqueWhite', 'Linen', 'LightGoldenRodYellow', 'OldLace', 'Red', 'Fuchsia', 'Magenta', 'DeepPink', 'OrangeRed', 'Tomato', 'HotPink', 'Coral', 'DarkOrange', 'LightSalmon', 'Orange', 'LightPink', 'Pink', 'Gold', 'PeachPuff', 'NavajoWhite', 'Moccasin', 'Bisque', 'MistyRose', 'BlanchedAlmond', 'PapayaWhip', 'LavenderBlush', 'SeaShell', 'Cornsilk', 'LemonChiffon', 'Snow', 'Yellow', 'LightYellow']
        #all_colors = ['Black', 'Navy', 'DarkBlue', 'Orange', 'Beige']
        picked_colors = ['white', 'white','white','white','white']
        draw_header(write_t, 'Please choose your name', font1, 'black', x2, y2)
        u_name = wn.textinput('username', 'Please, type your name')
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        write_t.hideturtle()
        #ask user for for number of doublettes
        draw_header(write_t, "Are double colors allowed?", font1, 'black', x2, y2)
        doubles = turtle.textinput('Doubles allowed', 'Yes or no?')
        if doubles in ('yes', 'Yes', 'y'):
            max_num_color = 2
        else:
            max_num_color = 1
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        write_t.hideturtle()
        choose_color_msg = 'thanks, '+ u_name + ', please choose five colors to play with'
        draw_header(write_t, choose_color_msg, font1, 'black', x1, y1)
        write_t.hideturtle()
        wn.tracer(2)
        draw_cols(all_colors, x1, y3, x_off * 12, y_off * 6, short_row, 'big', 'square')
        draw_picked_cols(picked_colors, x1, y2, x_off *6, y_off * 0)
        submit(x2, y2 - y_off)
        wn.tracer(1)
        while True:
            pause(pause_t, x0, y4)
            if submit_t.pencolor() == 'grey':
                wn.tracer(2)
                break
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        for i in range(5):
            u_colors.append(picked_colors[(i + 1) * -1])    
        draw_cols(u_colors, x1, y2, x_off * 12, y_off * 6, short_row, 'big', 'circle')
        draw_header(write_t, "press 'g' when you are ready to move on", font1, 'blue', x1, y6)
        wn.tracer(1)
        while True:
            pause(pause_t, x0, y4)
            move_switch()                    
            if move_on[0] == 1:
                wn.tracer(2)
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
            
        '''PLAY AGAINST COMP'''      
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
        rounds_played = 0
        user_attempts = 0
        comp_attempts = 0
        whos_on = ['notset']
        next_round = [0]
        next_stage = [0]
        see_analysis = [0]
        max_num_color = 2
        test_c = 0
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
                if u_name != '':
                    draw_header(write_t, 'mindturts - ' + u_name + ' against comp', font1, 'red', x1, y1)
                else:
                    draw_header(write_t, 'mindturts - human against comp', font1, 'red', x1, y1)
                draw_header(write_t, "who is first? type 'u' for your turn or 'c' for my turn!", font1, 'blue', x1, y6)
                write_t.hideturtle()
                while True:
                    pause(pause_t, x0, y4)
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
                move_on = [0]
                solution = []
                solutions = []
                #draw full set, comp is on
                wn.tracer(1)
                draw_header(write_t, 'comp is on', font1, 'red', x1, y1)
                draw_full_set(full_set, x1, y7, x_off * 8)
                #let user choose colors
                u_choice = []
                for j in range(4):
                    u_choice.append(source_set[0])
                draw_header(write_t, 'pick your colors', font1, 'black', x1, y4 + y_off * 2)
                draw_color_picker(u_choice, x1, y4, x_off * 8, y_off * 2)        
                while True:
                    pause(pause_t, x0, y4)
                    if submit_t.pencolor() == 'grey':
                        wn.tracer(2)
                        break                    
                #reset screen and all turtles
                wn.clearscreen()                
                #draw hidden assignm + header
                wn.bgcolor('lightgreen')
                draw_header(write_t, 'comp is on', font1, 'red', x1, y1)
                assignm = u_choice
                draw_header(write_t, 'Assignment', font1, 'black', x1, y2)
                draw_bars(assignm, x1, y3, x_off * 4, y_off * 0)
                while True:
                    if proceed == 0:
                        wn.tracer(1)
                        #choose random colors, make sure it's not the same set as previous attempts
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
                        draw_header(write_t, 'Solution', font1, 'black', x2, y2)
                        draw_bars(solution[i], x2, y3, x_off * 4, y_off * 0)
                        draw_bars(assignm, x1, y3, x_off * 4, y_off * 0)
                        #collect match and game stats and display
                        wn.tracer(1)
                        rounds_played += 0.5
                        comp_attempts += i
                        time = strftime("%d.%m.%Y, %H:%M", localtime())
                        m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)                    
                        draw_header(write_t, "Match stats:", font1, 'red', x1, y5)
                        draw_header(write_t, "Rounds played: "+ str(int(rounds_played)), font1, 'black', x1, y5 - line_space)
                        draw_header(write_t, 'User attempts: '+ str(user_attempts), font1, 'black', x1, y5 - line_space * 2)
                        draw_header(write_t, 'Comp attempts: '+ str(comp_attempts), font1, 'black', x1, y5 - line_space * 3)
                        if file_path != '':
                            g_stats = game_stats(file_path)
                            draw_header(write_t, 'Previous games: ', font1, 'red', x1, y5 - line_space * 4)
                            draw_header(write_t, 'Games total: '+ str(int(g_stats[0])), font1, 'black', x1, y5 - line_space * 5)
                            draw_header(write_t, 'Totals user attempts: '+ str(g_stats[2]), font1, 'black', x1, y5 - line_space * 6)
                            draw_header(write_t, 'Totals comp attempts: '+ str(g_stats[1]), font1, 'black', x1, y5 - line_space * 7)
                        #store attempts and counts for analysis
                        stored_solutions = solutions
                        stored_black_counts = black_counts_absolute
                        stored_white_counts = white_counts_absolute
                        #clean out vars
                        white_counts_absolute = []
                        black_counts_absolute = []                
                        #ask user for another round
                        if start_mode == 'user':
                            draw_header(write_t, "press 'y' for another round, press 'n' to quit", font1, 'blue', x1, y6)
                            while True:
                                pause(pause_t, x0, y4)
                                play_again()                    
                                if next_round[0] != 0:               
                                    break
                        else:
                            next_round[0] = 1
                            draw_header(write_t, "press 'g' when you are ready to move on", font1, 'blue', x1, y6)
                            while True:
                                pause(pause_t, x0, y4)
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
                                draw_bars(solution[i], x3, y3, x_off * 4, y_off * -12 * i)    
                                #draw black, white marks
                                draw_marks(black_counts_absolute[i], x_off * 24, y3, x_off * 2, y_off * -12 * i, 'black')
                                draw_marks( white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * -12 * i, 'white')
                                sleep(2)
                                i += 1
                                proceed = 0      
                        else:
                            white_counts_absolute.append(white_count(assignm, solution[i]))
                            solutions.append(solution[i])                    
                            #draw attempts header
                            draw_header(write_t, 'Attempts', font1, 'black', x3, y2)
                            #draw solution
                            draw_bars(solution[i], x3, y3, x_off * 4, y_off * 0)
                            #draw marks header, black, white marks
                            draw_header(write_t, 'Marks', font1, 'black', x_off * 24, y2)
                            draw_marks(black_counts_absolute[i], x_off * 24, y3, x_off * 2, y_off * 0, 'black')
                            draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * 0, 'white')
                            sleep(2)
                            i += 1
                            proceed = 0
            
            '''comp assigns problem, user solves'''
            if whos_on[0] == 'user':
                if mode[0] != 'duo':
                    break
                wn.bgcolor('lightgreen')
                wn.tracer(1)
                i = 0
                next_round[0] = 0
                move_on = [0]
                solutions = []
                #draw full set, human is on
                if u_name != '':
                    draw_header(write_t, u_name + ' is on', font1, 'red', x1, y1, 'bold')
                else:    
                    draw_header(write_t, 'human is on', font1, 'red', x1, y1, 'bold')
                draw_full_set(full_set, x1, y7, x_off * 8)
                assignm = random.sample(full_set,4)        
                #draw mystery assignm + header
                draw_header(write_t, 'Assignment', font1, 'black', x1, y2)
                grey_bars = ['grey', 'grey', 'grey', 'grey']
                draw_bars(grey_bars, x1, y3, x_off * 4, y_off * 0)
                while True:
                    #let user choose colors
                    wn.tracer(1)
                    u_choice = []
                    for j in range(4):
                        u_choice.append(source_set[0])
                    draw_header(write_t, 'pick your colors', font1, 'black', x1, y4 + y_off * 2)
                    draw_color_picker(u_choice, x1, y4, x_off * 8, y_off * 2)
                    while True:
                        pause(pause_t, x0, y4)
                        if submit_t.pencolor() == 'grey':               
                            break
                    #calculate black marks, and...
                    solutions.append(u_choice)
                    black_counts_absolute.append(black_count(assignm, solutions[i]))
                    #...if success, draw assignm, break
                    if black_counts_absolute[i] == 4:
                        draw_header(write_t, 'Solution', font1, 'black', x2, y2)
                        draw_bars(solutions[i], x2, y3, x_off * 4, y_off * 0)
                        draw_bars(assignm, x1, y3, x_off * 4, y_off * 0)
                        #collect match and game stats and display
                        wn.tracer(1)
                        rounds_played += 0.5
                        user_attempts += i
                        time = strftime("%d.%m.%Y, %H:%M", localtime())
                        m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)                    
                        draw_header(write_t, "Match stats:", font1, 'red', x1, y5)
                        draw_header(write_t, "Rounds played: "+ str(int(rounds_played)), font1, 'black', x1, y5 - line_space)
                        draw_header(write_t, 'User attempts: '+ str(user_attempts), font1, 'black', x1, y5 - line_space * 2)
                        draw_header(write_t, 'Comp attempts: '+ str(comp_attempts), font1, 'black', x1, y5 - line_space * 3)
                        if file_path != '':
                            g_stats = game_stats(file_path)
                            draw_header(write_t, 'Previous games: ', font1, 'red', x1, y5 - line_space * 4)
                            draw_header(write_t, 'Games total: '+ str(int(g_stats[0])), font1, 'black', x1, y5 - line_space * 5)
                            draw_header(write_t, 'Totals user attempts: '+ str(g_stats[2]), font1, 'black', x1, y5 - line_space * 6)
                            draw_header(write_t, 'Totals comp attempts: '+ str(g_stats[1]), font1, 'black', x1, y5 - line_space * 7)
                        #store attempts and counts for analysis
                        stored_solutions = solutions
                        stored_black_counts = black_counts_absolute
                        stored_white_counts = white_counts_absolute
                        #clean out vars
                        white_counts_absolute = []
                        black_counts_absolute = []
                        draw_header(write_t, "press 'a' for analysis of your attempts, else press 's'", font1, 'blue', x1, y6 - line_space * 2)
                        see_analysis[0] = 0
                        show_analysis()
                        while True:
                            pause(pause_t, x0, y4)                                                
                            if see_analysis[0] != 0:               
                                break                
                        wn.clearscreen()                            
                        if see_analysis[0] == 1:
                            wn.bgcolor('lightgreen')
                            wn.tracer(2)
                            alert = []
                            i = len(stored_solutions) -1
                            if i <= 1:
                                alert.append('at least two attempts needed for analysis, you got lucky!')
                            if i >= 1:
                                attempt_counter = 1            
                                while attempt_counter < i:
                                    a = 0
                                    alert_counter = 0
                                    #alert += '\n'
                                    while a < attempt_counter:
                                        if black_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_black_counts[a]:
                                            alert.append('In attempt ' + str((attempt_counter + 1)) + ', we see ' + str(black_count(stored_solutions[a], stored_solutions[attempt_counter])) + ' black(s) against attempt ' +  str(a + 1) + ', which had ' + str(stored_black_counts[a]))
                                            alert_counter += 1
                                        if white_count(stored_solutions[a], stored_solutions[attempt_counter]) - black_count(stored_solutions[a], stored_solutions[attempt_counter]) != stored_white_counts[a] - stored_black_counts[a]:
                                            alert.append('In attempt ' + str((attempt_counter + 1)) + ', we find ' + str(white_count(stored_solutions[a], stored_solutions[attempt_counter]) - black_count(stored_solutions[a], stored_solutions[attempt_counter])) + ' white(s) against attempt ' +  str(a + 1) + ', which had ' + str(stored_white_counts[a] - stored_black_counts[a]))
                                            alert_counter += 1
                                        #print(a)
                                        a +=1
                                    if alert_counter < 1:
                                        alert.append('Couldn\'t find any errors in attempt ' + str((attempt_counter + 1)))
                                    attempt_counter += 1
                                    alert.append('')
                            #print(alert)
                            draw_header(write_t, 'Analysis', font1, 'red', x1, y2)                            
                            #draw headers, solution
                            draw_header(write_t, 'Attempts', font1, 'black', x3, y2)
                            draw_header(write_t, 'Marks', font1, 'black', x3 + x_off * 24, y2)
                            draw_header(write_t, 'Solution', font1, 'black', x2, y2)
                            draw_bars(stored_solutions[-1], x2, y3, x_off * 4, y_off * 0)                           
                            #draw attempts, black and white counts
                            for i in range(len(stored_solutions) - 1):    
                                if i > 4:
                                    draw_bars(stored_solutions[i], x4, y3, x_off * 4, y_off * -12 * (i -5))
                                else:
                                    draw_bars(stored_solutions[i], x3, y3, x_off * 4, y_off * -12 * i)
                                if i > 4:
                                    draw_marks(stored_black_counts[i], x4 + x_off * 28, y3, x_off * 2, y_off * -12 * (i -5), 'black')
                                    draw_marks(stored_white_counts[i] - stored_black_counts[i], x4 + x_off * 36, y3, x_off * 2, y_off * -12 * (i -5), 'white')
                                else:
                                    draw_marks(stored_black_counts[i], x3 + x_off * 28, y3, x_off * 2, y_off * -12 * i, 'black')
                                    draw_marks(stored_white_counts[i] - stored_black_counts[i], x_off * 32, y3, x_off * 2, y_off * -12 * i, 'white')
                            #draw analysis message        
                            if len(alert) <= 28:
                                for msg in range(len(alert)):
                                    if 'errors' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'blue', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                                    if 'black' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'DarkSlateBlue', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                                    if 'white' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'DarkSlateGrey', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                            else:
                                for msg in range(28):
                                    if 'no errors' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'blue', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                                    if 'black' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'DarkSlateBlue', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                                    if 'white' in alert[msg]:
                                        draw_header(write_t, alert[msg], font2, 'DarkSlateGrey', x1, y3 - y_off * 6 - line_space_small * msg, 'small')
                                    draw_header(write_t, 'sorry, too many errors to display on screen... ', font1, 'blue', x1, y3 - y_off * 6 - line_space_small * 29, 'small')
                            draw_header(write_t, "press 'g' when you are ready to move on", font1, 'blue', x1, y6 - line_space * 4)
                            move_on[0] = 0
                            while True:
                                pause(pause_t, x0, y4)
                                move_switch()                    
                                if move_on[0] == 1:               
                                    break
                            wn.tracer(2)
                            wn.clearscreen()                                    
                            #ask user for another round
                            if start_mode == 'comp':
                                wn.bgcolor('lightgreen')
                                if u_name != '':
                                    draw_header(write_t, 'mindturts - ' + u_name + ' against comp', font1, 'red', x1, y1)
                                else:
                                    draw_header(write_t, 'mindturts - human against comp', font1, 'red', x1, y1)
                                draw_header(write_t, "press 'y' for another round, press 'n' to quit", font1, 'blue', x1, y6)
                                next_round[0] = 0
                                wn.tracer(1)
                                while True:
                                    pause(pause_t, x0, y4)                            
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
                                if u_name != '':
                                    draw_header(write_t, 'mindturts - ' + u_name + ' against comp', font1, 'red', x1, y1)
                                else:
                                    draw_header(write_t, 'mindturts - human against comp', font1, 'red', x1, y1)
                                draw_header(write_t, "press 'y' for another round, press 'n' to quit", font1, 'blue', x1, y6)
                                next_round[0] = 0
                                while True:
                                    pause(pause_t, x0, y4)                            
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
                    draw_header(write_t, 'Attempts', font1, 'black', x3, y2)                   
                    if i > 4:
                        draw_bars(solutions[i], x4, y3, x_off * 4, y_off * -12 * (i -5))
                    else:
                        draw_bars(solutions[i], x3, y3, x_off * 4, y_off * -12 * i)
                    #calculate white marks
                    white_counts_absolute.append(white_count(assignm, solutions[i]))            
                    #draw marks header, black, white marks
                    draw_header(write_t, 'Marks', font1, 'black', x3 +x_off * 24, y2)
                    if i > 4:
                        draw_marks(black_counts_absolute[i], x4 + x_off * 28, y3, x_off * 2, y_off * -12 * (i -5), 'black')
                        draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x4 + x_off * 36, y3, x_off * 2, y_off * -12 * (i -5), 'white')
                    else:
                        draw_marks(black_counts_absolute[i], x3 + x_off * 28, y3, x_off * 2, y_off * -12 * i, 'black')
                        draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * -12 * i, 'white')
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
            draw_header(write_t, 'bye, '+ u_name, font1, 'black', x3, y4)
        else:
            draw_header(write_t, 'bye', font1, 'black', x3, y4)        
        break    

wn.mainloop()