#!/usr/bin/python3

######Set path to a file where statistics and user options can be stored
file_path = ""
########

import turtle
from time import localtime, strftime, sleep
import random
import json
import tkinter.simpledialog
import itertools

#set up screen
screen_width = 1.0
screen_height = 1.0
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setup(width = screen_width, height = screen_height)
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
    t.setx(x - x_off * 2)
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
    if size == 'default':
        for turt in col_ts:
            turt.resizemode('user')
            turt.shapesize(turtle_size_regular,turtle_size_regular,turtle_size_regular)
    else:
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
    submit_t.write('submit', move= True, font=(font1, font_regular, "bold"))
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
    count = int(pos + short_row * row)
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

def draw_cols(colorlist, x, y, x_offset, y_offset, size = 'default', shape = 'default'):
    # draw dynamic grid of clickable colors
    create_col_ts(colorlist, size, shape)
    num_rows = 0
    if gsize < 0.7:
        row_length = long_row
    else:
        row_length = short_row
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
    if x > x2 and x < x2 + x_off * 13 and y > y2 -y_off * 2 and y < y2 + y_off * 2:
        submit_t.pencolor('grey') 
        
def submit(x, y):
    submit_t.hideturtle()
    submit_t.penup()
    submit_t.setx(x)
    submit_t.sety(y)
    submit_t.color('green')
    submit_t.write('submit', move = False, font=('arial', 16, 'bold'))
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
pause_t = turtle.Turtle(visible = False)
write_t = turtle.Turtle(visible = False)
    
'''games logic'''
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

def get_set(src):
    new_set = []
    for i in range(max_num_color):
        for item in src:
            new_set.append(item)
    return new_set            

def bin_search(xs, t):
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub: 
           return -1
        mid = (lb + ub) // 2
        probe = xs[mid]
        if probe == t:
            return 1
        if probe < t:
            lb = mid +1
        else:
            ub = mid

def rm_dups(xs):
    xs = sorted(xs)
    the_list = []
    for item in xs:
        if bin_search(the_list, item) == -1:
            the_list.append(item)        
    return the_list
 
def all_combs(src):
    perms = list(itertools.permutations(src,4))
    combs = rm_dups(perms)
    return combs

def possible_solutions(attempts, combs):
    i = len(attempts)
    final_sols = []
    for comb in combs:
        a = 0
        while a < i:
            if white_count(comb, attempts[a]) != white_count(attempts[a],assignm) or black_count(comb, attempts[a]) != black_count(attempts[a],assignm):
                break
            else:
                a += 1
        if a / i == 1:
            final_sols.append(comb)
    return final_sols

# user interaction
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
    vals = {'user options': {'u_name': u_name, 'u_colors': u_colors, 'max_num_color': max_num_color, 'gsize': gsize}}
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

#read stored user options
u_name = ''
gsize = 1
if file_path != '':
    with open(file_path) as storage:
        options = json.load(storage)
        for k,v in options.items():
            if k == 'user options' and v['u_name'] != '':        
                u_name = options['user options']['u_name']
            if k == 'user options':
                gsize = options['user options']['gsize']
               
#set grid measures for gui with factor allowing to adjust to different screen sizes
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
turtle_size_regular = int((1 * gsize))
turtle_size_big = round(2 * gsize)
line_space = 25 * gsize
line_space_small = 18 * gsize
short_row = round(15 * gsize)
long_row = round(24 * gsize)
font_small = round(12 * gsize)
font_regular = round(16 * gsize)
font1 = 'arial'
font2 ='helvetica'

mode = ['start']    
u_colors = []
move_on = [0]
num_pegs = 4
max_num_color = 2

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
        if file_path != '':
            g_stats = game_stats(file_path)
            draw_header(write_t, 'previous matches: ', font1, 'red', x1, y5 - line_space * 4)
            draw_header(write_t, 'matches total: '+ str(int(g_stats[0])), font1, 'black', x1, y5 - line_space * 5)
            draw_header(write_t, 'totals user attempts: '+ str(g_stats[2]), font1, 'black', x1, y5 - line_space * 6)
            draw_header(write_t, 'totals comp attempts: '+ str(g_stats[1]), font1, 'black', x1, y5 - line_space * 7)
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
        picked_colors = ['white', 'white','white','white','white']
        draw_header(write_t, 'Please choose your name', font1, 'black', x2, y2)
        u_name = tkinter.simpledialog.askstring('username:', 'please, type your name')
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        #ask user for for doublettes
        draw_header(write_t, "Are double colors allowed?", font1, 'black', x2, y2)
        doubles = tkinter.simpledialog.askstring('doubles allowed:', 'yes or no?')
        if doubles in ('yes', 'Yes', 'y'):
            max_num_color = 2
        else:
            max_num_color = 1
        wn.clearscreen()        
        wn.bgcolor('lightgreen')
        write_t.hideturtle()
        choose_color_msg = 'thanks, '+ u_name + ', please choose five colors to play with'
        draw_header(write_t, choose_color_msg, font1, 'black', x1, y1)
        wn.tracer(2)
        draw_cols(all_colors, x1, y3, x_off * 12, y_off * 6, 'big', 'square')
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
        draw_header(write_t, "you may change the game size to accomodate your screen.\n default is 1, which works well on a 1280 * 1048 screen. \n a value like 0.5 works well on a 800 * 600 screen.", font1, 'black', x2, y2 - y_off * 4)
        gsize = turtle.numinput('Resize factor', 'default is 1.0')
        wn.clearscreen()        
        wn.bgcolor('lightgreen')
        draw_header(write_t, 'thanks, ' + u_name, font1, 'black', x1, y1)
        draw_header(write_t, 'these are the colors you have picked', font2, 'black', x1, y2)
        for i in range(5):
            u_colors.append(picked_colors[(i + 1) * -1])    
        draw_cols(u_colors, x1, y2 - y_off * 4, x_off * 12, y_off * 6, 'big', 'circle')
        if max_num_color == 2:
            draw_header(write_t, 'double colors are allowed', font2, 'black', x1, y3 - y_off * 2)
        else:
            draw_header(write_t, 'double colors are not allowed', font2, 'black', x1, y3 - y_off * 2)
        draw_header(write_t, 'the factor for adjusting game size is at ' + str(gsize), font2, 'black', x1, y3 - line_space *2)
        draw_header(write_t, "press 'g' when you are ready to move on", font2, 'blue', x1, y6)
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
        #second calling of grid values in case user has changed gsize in options mode
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
        turtle_size_regular = int((1 * gsize))
        turtle_size_big = round(2 * gsize)
        line_space = 25 * gsize
        line_space_small = 18 * gsize
        short_row = round(15 * gsize)
        long_row = round(24 * gsize)
        font_small = round(12 * gsize)
        font_regular = round(16 * gsize)
        
        wn.bgcolor('lightgreen')
        wn.tracer(1)
        wn.title('mindturts - human vs. computer')
        #set up vars for game logic
        i = 0
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
        alert = []
        grey_bars = ['grey', 'grey', 'grey', 'grey']    
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
                #create set of pegs
                full_set = get_set(source_set)
                wn.tracer(2)    
                wn.clearscreen()
                pause_t.hideturtle()                
            
            '''user assigns problem, comp solves'''
            if whos_on[0] == 'comp':
                if mode[0] != 'duo':
                    break
                wn.bgcolor('lightgreen')
                wn.title('mindturts - human vs. computer')
                i = 0
                next_round[0] = 0
                move_on = [0]
                solution = []
                solutions = []
                possible_sols = [0]
                #draw full set, comp is on
                draw_header(write_t, 'comp is on', font1, 'red', x1, y1)
                draw_full_set(full_set, x1, y7, x_off * 8)
                draw_marks(4, x3, y7 - y_off, x_off * 2, y_off * -12 * i, 'black')
                draw_marks(4, x3 + x_off * 14, y7 - y_off, x_off * 2, y_off * -12 * i, 'white')
                #let user choose colors
                u_choice = []
                for j in range(4):
                    u_choice.append(source_set[0])
                draw_header(write_t, 'pick your colors', font1, 'black', x1, y4 + y_off * 2)
                wn.tracer(1)
                draw_color_picker(u_choice, x1, y4, x_off * 8, y_off * 2)
                while True:
                    pause(pause_t, x0, y4)
                    if submit_t.pencolor() == 'grey':
                        wn.tracer(2)
                        break                    
                wn.clearscreen()                
                #draw hidden assignm + header
                wn.bgcolor('lightgreen')
                wn.tracer(2)
                draw_header(write_t, 'comp is on', font1, 'red', x1, y1)
                draw_full_set(full_set, x1, y7, x_off * 8)
                draw_marks(4, x3, y7 - y_off, x_off * 2, y_off * -12 * i, 'black')
                draw_marks(4, x3 + x_off * 14, y7 - y_off, x_off * 2, y_off * -12 * i, 'white')
                assignm = u_choice
                draw_header(write_t, 'Assignment', font1, 'black', x1, y2)
                wn.tracer(1)
                draw_bars(grey_bars, x1, y3, x_off * 4, y_off * 0)
                possible_combs = all_combs(full_set)
                ''' Enter attempt loop'''                
                while True:
                    if whos_on[0] != 'comp' or mode[0] != 'duo':
                        break
                    while True:
                        #choose random colors, make sure it's not the same set as previous attempts
                        x = random.sample(full_set,4)    
                        solution.append(x)
                        if solution[i] in solutions:
                            del solution[-1]
                            break      
                        #check for black count against assignment
                        black_counts_absolute.append(black_count(assignm, solution[i]))                
                        if black_counts_absolute[i] == 4:                    
                        #if success, i. e. attempt matches assignment, draw assignm, solution, stats; clean out vars & break        
                            wn.tracer(1)
                            #draw solution + header
                            wn.title('solved!')
                            draw_header(write_t, 'Solution', font1, 'black', x2, y2)
                            draw_bars(solution[i], x2, y3, x_off * 4, y_off * 0)
                            draw_bars(assignm, x1, y3, x_off * 4, y_off * 0)
                            #collect match and game stats and display
                            wn.tracer(1)
                            rounds_played += 0.5
                            comp_attempts += i
                            time = strftime("%d.%m.%Y, %H:%M", localtime())
                            m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)                    
                            draw_header(write_t, "match stats:", font1, 'red', x1, y5)
                            draw_header(write_t, "rounds played: "+ str(int(rounds_played)), font1, 'black', x1, y5 - line_space)
                            draw_header(write_t, 'user attempts: '+ str(user_attempts), font1, 'black', x1, y5 - line_space * 2)
                            draw_header(write_t, 'comp attempts: '+ str(comp_attempts), font1, 'black', x1, y5 - line_space * 3)
                            if file_path != '':
                                g_stats = game_stats(file_path)
                                draw_header(write_t, 'previous matches: ', font1, 'red', x1, y5 - line_space * 4)
                                draw_header(write_t, 'matches total: '+ str(int(g_stats[0])), font1, 'black', x1, y5 - line_space * 5)
                                draw_header(write_t, 'totals user attempts: '+ str(g_stats[2]), font1, 'black', x1, y5 - line_space * 6)
                                draw_header(write_t, 'totals comp attempts: '+ str(g_stats[1]), font1, 'black', x1, y5 - line_space * 7)
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
                                whos_on[0] = 'user'                    
                                wn.clearscreen()
                                break
                            else:                           
                                mode[0] = 'end' 
                                break                    
                        #if attempt didn't match assignment
                        else:
                            #when not the first attempt, let's compare marks to marks of previous attempts
                            if i >= 1:
                                a = 0
                                while a < i:             
                                    if black_count(solution[a], solution[i]) != black_counts_absolute[a]:
                                        del black_counts_absolute[-1]
                                        del solution[-1]
                                        break                        
                                    else:
                                        a += 1    
                                if a == i:
                                    white_counts_absolute.append(white_count(assignm, solution[i]))
                                    a = 0
                                    while a < i:
                                        if white_count(solution[a], solution[i]) != white_counts_absolute[a]:
                                            del white_counts_absolute[-1]
                                            del black_counts_absolute[-1]
                                            del solution[-1]
                                            break                     
                                        else:
                                            a += 1    
                                    if a == i:
                                        solutions.append(solution[i])                        
                                        #draw solution, black, white marks
                                        draw_bars(solution[i], x3, y3, x_off * 4, y_off * -12 * i)
                                        possible_sols.append(possible_solutions(solutions, possible_sols[i-1]))
                                        if possible_sols[i] == 1:
                                            sols_msg = 'only ' + str(len(possible_sols[i])) +' legit solution left'
                                        else:
                                            sols_msg = 'still ' + str(len(possible_sols[i])) +' legit solutions to choose from'
                                        wn.title(sols_msg)
                                        draw_marks(black_counts_absolute[i], x_off * 24, y3, x_off * 2, y_off * -12 * i, 'black')
                                        draw_marks( white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * -12 * i, 'white')
                                        sleep(2)
                                        i += 1
                                        break      
                            else:
                                white_counts_absolute.append(white_count(assignm, solution[i]))
                                solutions.append(solution[i])                    
                                #draw attempts header, solution, marks header and marks
                                draw_header(write_t, 'Attempts', font1, 'black', x3, y2)
                                draw_bars(solution[i], x3, y3, x_off * 4, y_off * 0)
                                draw_header(write_t, 'Marks', font1, 'black', x_off * 24, y2)
                                possible_sols[i] = possible_solutions(solutions, possible_combs)
                                sols_msg = 'still ' + str(len(possible_sols[i])) +' possible solutions available'
                                wn.title(sols_msg)
                                draw_marks(black_counts_absolute[i], x_off * 24, y3, x_off * 2, y_off * 0, 'black')
                                draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * 0, 'white')
                                sleep(2)
                                i += 1
                                break
            
            '''comp assigns problem, user solves'''
            if whos_on[0] == 'user':
                if mode[0] != 'duo':
                    break
                wn.bgcolor('lightgreen')
                wn.title('mindturts - human vs. computer')
                wn.tracer(2)
                i = 0
                next_round[0] = 0
                move_on = [0]
                solutions = []
                possible_sols = [0]
                raise_alert = 0
                #draw full set, human is on
                if u_name != '':
                    draw_header(write_t, u_name + ' is on', font1, 'red', x1, y1, 'bold')
                else:    
                    draw_header(write_t, 'human is on', font1, 'red', x1, y1, 'bold')
                draw_full_set(full_set, x1, y7, x_off * 8)
                draw_marks(4, x3, y7 - y_off, x_off * 2, y_off * -12 * i, 'black')
                draw_marks(4, x3 + x_off * 14, y7 - y_off, x_off * 2, y_off * -12 * i, 'white')
                assignm = random.sample(full_set,4)
                possible_combs = all_combs(full_set)
                wn.tracer(1)
                #draw mystery assignm + header
                draw_header(write_t, 'Assignment', font1, 'black', x1, y2)
                draw_bars(grey_bars, x1, y3, x_off * 4, y_off * 0)
                while True:
                    #let user choose colors
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
                    #...if success, draw assignm, stats, analysis and break
                    if black_counts_absolute[i] == 4:
                        wn.title('solved!')
                        draw_header(write_t, 'Solution', font1, 'black', x2, y2)
                        draw_bars(solutions[i], x2, y3, x_off * 4, y_off * 0)
                        draw_bars(assignm, x1, y3, x_off * 4, y_off * 0)
                        #collect match and game stats and display
                        wn.tracer(1)
                        rounds_played += 0.5
                        user_attempts += i
                        time = strftime("%d.%m.%Y, %H:%M", localtime())
                        m_stats = match_stats(time, int(rounds_played), comp_attempts, user_attempts)                    
                        draw_header(write_t, "match stats:", font1, 'red', x1, y5)
                        draw_header(write_t, "rounds played: "+ str(int(rounds_played)), font1, 'black', x1, y5 - line_space)
                        draw_header(write_t, 'user attempts: '+ str(user_attempts), font1, 'black', x1, y5 - line_space * 2)
                        draw_header(write_t, 'comp attempts: '+ str(comp_attempts), font1, 'black', x1, y5 - line_space * 3)
                        if file_path != '':
                            g_stats = game_stats(file_path)
                            draw_header(write_t, 'previous matches: ', font1, 'red', x1, y5 - line_space * 4)
                            draw_header(write_t, 'matches total: '+ str(int(g_stats[0])), font1, 'black', x1, y5 - line_space * 5)
                            draw_header(write_t, 'totals user attempts: '+ str(g_stats[2]), font1, 'black', x1, y5 - line_space * 6)
                            draw_header(write_t, 'totals comp attempts: '+ str(g_stats[1]), font1, 'black', x1, y5 - line_space * 7)
                        #store attempts and counts for analysis
                        stored_solutions = solutions
                        stored_black_counts = black_counts_absolute
                        stored_white_counts = white_counts_absolute
                        #clean out vars
                        white_counts_absolute = []
                        black_counts_absolute = []
                        #close down user's turn
                        if raise_alert < 1:
                            draw_header(write_t, str(i) + " perfect attempts, couldn't have done it better myself...", font1, 'blue', x1, y6)
                            draw_header(write_t, "press 'g' when you are ready to move on", font1, 'blue', x1, y6 - line_space * 2)
                            move_on[0] = 0
                            wn.tracer(1)
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
                                wn.clearscreen()
                                break
                            else:                           
                                mode[0] = 'end'
                                break
                        #ask for analysis and close down user's turn
                        else:
                            draw_header(write_t, "you've had some inconsistencies in your attemps", font1, 'blue', x1, y6 - line_space * 2)
                            draw_header(write_t, "press 'a' to get an analysis, else press 's'", font1, 'blue', x1, y6 - line_space * 3)
                            see_analysis[0] = 0
                            show_analysis()
                            while True:
                                pause(pause_t, x0, y4)                                                
                                if see_analysis[0] != 0:               
                                    break                
                            wn.clearscreen()
                            #display analysis
                            if see_analysis[0] == 1:
                                wn.bgcolor('lightgreen')
                                wn.tracer(2)
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
                                        draw_header(write_t, 'sorry, too many errors to display on screen... ', font2, 'blue', x1, y3 - y_off * 6 - line_space_small * 29, 'small')
                                draw_header(write_t, "press 'g' when you are ready to move on", font1, 'blue', x1, y6 - line_space * 4)
                                move_on[0] = 0
                                wn.tracer(1)
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
                                    wn.clearscreen()
                                    break
                                else:                           
                                    mode[0] = 'end'
                                    break 
                            #in case analysis is not requested, ask for another round or move to 'comp is on'        
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
                                if next_round[0] is 1:
                                    whos_on[0] = 'comp'
                                    wn.clearscreen()                    
                                    break
                                else:                           
                                   mode[0] = 'end'
                                   wn.clearscreen()
                                   break                      
                    
                    #if attempt was not successfull, calculate white marks, prepare analysis and draw attempt bars, marks
                    if i >= 1:
                        possible_sols.append( possible_solutions(solutions, possible_sols[i-1]))
                    else:
                        possible_sols[i] = possible_solutions(solutions, possible_combs)
                    if possible_sols[i] == 1:
                        sols_msg = 'only ' + str(len(possible_sols[i])) +' legit solution left'
                    else:
                        sols_msg = 'still ' + str(len(possible_sols[i])) +' legit solutions to choose from'
                    wn.title(sols_msg)
                    draw_header(write_t, 'Attempts', font1, 'black', x3, y2)                   
                    if i > 4:
                        draw_bars(solutions[i], x4, y3, x_off * 4, y_off * -12 * (i -5))
                    else:
                        draw_bars(solutions[i], x3, y3, x_off * 4, y_off * -12 * i)
                    white_counts_absolute.append(white_count(assignm, solutions[i]))            
                    draw_header(write_t, 'Marks', font1, 'black', x3 +x_off * 24, y2)                    
                    if i > 4:
                        if i > 4:
                            draw_marks(black_counts_absolute[i], x4 + x_off * 28, y3, x_off * 2, y_off * -12 * (i - 5), 'black')
                            draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x4 + x_off * 36, y3, x_off * 2, y_off * -12 * (i - 5), 'white')
                    else:
                        draw_marks(black_counts_absolute[i], x3 + x_off * 28, y3, x_off * 2, y_off * -12 * i, 'black')
                        draw_marks(white_counts_absolute[i] - black_counts_absolute[i], x_off * 32, y3, x_off * 2, y_off * -12 * i, 'white')
                    #analyse attempts, prepare analysis messages
                    if i >= 1:                                                
                        a = 0
                        alert_counter = 0
                        raise_alert = 0
                        while a < i:             
                            if black_count(solutions[a], solutions[i]) != black_counts_absolute[a]:
                                alert.append('in attempt ' + str((i + 1)) + ', we see ' + str(black_count(solutions[a], solutions[i])) + ' black(s) against attempt ' +  str(a + 1) + ', which had ' + str(black_counts_absolute[a]))
                                alert_counter += 1
                                raise_alert = 1
                            if white_count(solutions[i], solutions[a]) - black_count(solutions[i], solutions[a]) != white_count(solutions[a], assignm) - black_count(solutions[a], assignm):
                                alert.append('in attempt ' + str((i + 1)) + ', we find ' + str(white_count(solutions[a], solutions[i]) - black_count(solutions[a], solutions[i])) + ' white(s) against attempt ' +  str(a + 1) + ', which had ' + str(white_counts_absolute[a] - black_counts_absolute[a]))
                                alert_counter += 1
                                raise_alert = 1
                            a += 1
                        if alert_counter < 1:
                            alert.append('attempt ' + str((i + 1)) + ' was perfectly congruent with earlier attempts')
                        alert.append('')
                    i += 1
    
        '''Shut down game'''
    elif mode[0] == 'end':
        wn.clearscreen()
        wn.bgcolor('lightgreen')
        wn.title('bye')
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
        sleep(2)
        break