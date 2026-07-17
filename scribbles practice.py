'''
PROBLEM STATEMENT 1 : To animate a square that moves from the left side to the middle of the canvas
'''
import tkinter as tk
import time
canvas_height = 500
canvas_width = 500
box_size = 100
velocity = 2 #how many pixels the square will move in each pulse/heartbeat
delay = 100 #root.after takes values in int for milliseconds only

def main():
    root = tk.Tk() #this is the correct way to do this instead of just p.object labelling
    canvas = tk.Canvas (root, height = canvas_height, width = canvas_width)
    start_x = 0
    start_y = canvas_height/2 - box_size/2
    block = canvas.create_rectangle(start_x,
                                    start_y,
                                    start_x + box_size,
                                    start_y + box_size,
                                    fill = 'light blue')

    line = canvas.create_line(0,250,500,250)
    line = canvas.create_line(250,0,250,500)
    #for horizontal movement x changes while y remains constant, vice versa for vertical movement
    ''' 
    THIS IS WHAT MEHRAN DID IN CIP, THIS DOESN"T WORK EXACTLY LIKE THIS IN TKINTER
    while True: #world update
        (start_x + box_size/2) < (canvas_width/2);
        start_x += velocity
        canvas.moveto(block, start_x, start_y)
        #intentional delay for visibility
        time.sleep(delay)
    '''
    def update():
        nonlocal start_x, start_y
        if (start_x + box_size/2) < (canvas_width/2):
            start_x += velocity
            canvas.coords (block, start_x, start_y,start_x + box_size,start_y + box_size)
            root.after(delay, update)
        elif (start_x + box_size/2) == (canvas_width/2):
            start_y += velocity
            canvas.coords (block, start_x, start_y,start_x + box_size,start_y + box_size)
            root.after(delay, update)
        else:
            print("we are done!")
    update()
    canvas.pack()
    root.mainloop()
if __name__ == '__main__':
    main()