import os     
import time  


CSI = '\x1b['            
ERASE = f'{CSI}2K'       
ZERO = f'{CSI}0G'        
RESET = f'{CSI}0m'      
HIDE = f'{CSI}?25l'     
SHOW = f'{CSI}?25h'     

GREEN = 29              
RED = 197              

def clear():
    os.system("cls")
def set_bg(color):
    return f'{CSI}48;5;{color}m'
def set_fg(color):
    return f'{CSI}38;5;{color}m'

# 1. ФЛАГ БАНГЛАДЕША
def draw_flag_line(y, width, height, radius, circle_color):
    center_x = width * 0.45          
    center_y = (height - 1) / 2      
    line = ''                       
    for x in range(width):        
        inside = (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2 
        color = circle_color if inside else GREEN       
        line += f'{set_bg(color)}  '           
    print(f'{line}{RESET}')                    

def draw_flag(radius=6, width=30, height=18,circle_color=RED):
    for y in range(height):
        draw_flag_line(y, width, height, radius,circle_color)


# 2. УЗОР b
TILE = [                  
    "###### ",          
    "#    # ",            
    "# ## # ",           
    "# #  # ",
    "# #### ",            
    "#      ",           
    "#######",            
    "       ",           
]
def draw_pattern_line(tile_line, cols):
    line = ''
    for i in range(cols):                  
        for ch in tile_line:               
            line += '██' if ch == '#' else '  '
    print(f'{set_fg(GREEN)}{line}{RESET}')  
def draw_pattern(cols=8, rows=4):
    for _ in range(rows):                  
        for tile_line in TILE:             
            draw_pattern_line(tile_line, cols)


# 3. АНИМАЦИЯ
def animate():
    height = 18                       
    print(HIDE, end='')             
    clear()                          
    try:
        while True:                               
            for color in range(20, 60):               
                draw_flag(circle_color=color, height=height)   
                print(f'{CSI}{height}A{ZERO}{ERASE}', end='', flush=True)
                time.sleep(0.1)                        
    except KeyboardInterrupt:         
        pass
    finally:
        print(f'{CSI}{height}B{SHOW}{RESET}')   

# 4. ДИАГРАММА 
def diagram():
    with open('sequence.txt') as file:
        numbers = [float(x) for x in file.read().split()]
    first = sum(abs(x) for x in numbers[:125])
    second = sum(abs(x) for x in numbers[125:250])
    percent1 = first / (first + second) * 100
    percent2 = 100 - percent1
    width = 50
    n1 = round(percent1 / 100 * width)
    n2 = width - n1
    print(f'{set_bg(GREEN)}{" " * n1}{set_bg(RED)}{" " * n2}{RESET}')
    print(f'Первые 125: {percent1:.1f}%')
    print(f'Вторые 125: {percent2:.1f}%')

#Доп задание
def f(x):
    return 2 * x + 3       
def put(row, col, text):
    print(f'{CSI}{row};{col}H{text}', end='')
def graph():
    height = 12              
    width = 20               
    x_max = 10              
    y_max = 24           
    top = 3                 
    left = 6                 
    clear()
    print(HIDE, end='')
    for r in range(height + 1):                                   
        put(top + r, left - 1, f'{set_fg(GREEN)}│{RESET}')
    for c in range(width + 1):                                   
        put(top + height + 1, left + c, f'{set_fg(GREEN)}─{RESET}')
    put(top + height + 1, left - 1, f'{set_fg(GREEN)}└{RESET}')   

    for y in range(0, y_max + 1, 6):                             
        r = round(y / y_max * height)                            
        put(top + height - r, left - 4, f'{y:>2}')
    for x in range(0, x_max + 1, 2):                              
        c = round(x / x_max * width)                             
        put(top + height + 2, left + c, str(x))
    put(top - 1, left - 4, 'y')
    put(top + height + 2, left + width + 3, 'x')

    for c in range(width + 1):                                   
        x = x_max * c / width                               
        y = f(x)                                               
        if y > y_max:                                             
            break
        r = int(y / y_max * height + 0.5)                        
        put(top + height - r, left + c, f'{set_fg(RED)}█{RESET}')

    put(top - 1, left + 8, 'y = 2x + 3')                          
    put(top + height + 4, 1, SHOW)                               
    print()

if __name__ == '__main__':
    clear()
    draw_flag()
    input('\nEnter — дальше...')
    clear()
    draw_pattern()
    input('\nEnter — дальше...')
    animate()
    input('\nEnter — дальше...')
    clear()
    diagram()
    input('\nEnter — дальше...')
    graph()
