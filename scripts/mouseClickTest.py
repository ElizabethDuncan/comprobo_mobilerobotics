#!/usr/bin/env python
from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk
import numpy as np
import scipy.misc.pilutil as smp
import pickle
import rospy
from map_manipulation import *
from astar import *

if __name__ == "__main__":
    root = Tk()

    #setting up a tkinter canvas ((((with scrollbars))))
    frame = Frame(root)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    #xscroll = Scrollbar(frame, orient=HORIZONTAL)
    #xscroll.grid(row=1, column=0, sticky=E+W)
    #yscroll = Scrollbar(frame)
    #yscroll.grid(row=0, column=1, sticky=N+S)
    #canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas = Canvas(frame, bd=0)
    canvas.grid(row=0, column=0)
    #xscroll.config(command=canvas.xview)
    #yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    #File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    #img = ImageTk.PhotoImage(Image.open(File))
    # ------------------------------------------------
    map_vis, map_info = open_files()
    #create_robot_goal(goal, map_vis)
    #create_robot_origin(origin, map_vis)
    map_info, map_vis = mapBuffer(map_info, map_vis)

    #store_changes(map_info, map_vis)

    #show_map(map_vis)
    img = ImageTk.PhotoImage(smp.toimage( map_vis ))
    img2 = ImageTk.PhotoImage(smp.toimage( map_vis ))
    #-------------------------------------------------
    canvas.create_image(0,0,image=img,anchor="nw",tag='image')
    #canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
        #outputting x and y coords to console
        #canvas.delete('image')
        #create_robot_goal((3,3), map_vis)
        #create_robot_origin((5,5), map_vis)
        #img = ImageTk.PhotoImage(smp.toimage( map_vis ))
        #canvas.create_image(0,0,image=img,anchor="nw",tag='image')
        
        #canvas.create_image(0,0,image=img2,anchor="nw",tag='image')
        #canvas.create_line(0, 100, 200, 0, fill="blue", dash=(4, 4))
        #root.update()
        print (event.x,event.y)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)

    root.mainloop()