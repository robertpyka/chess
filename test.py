from Tkinter import *

def msg(event):
    print 'widget:', event.widget,
        '   (x,y):', event.x, event.y,
        '   (x_root,y_root):', event.x_root, event.y_root

    if str(event.widget) != '.': # wykluczamy mastera
        event.widget['text'] = 'kliknięty'

master = Tk()
master.geometry('300x150+100+100')

b_a = Button(master, text="Button A")
b_a.grid(row=0, column=0)

b_b = Button(master, text="Button B")
b_b.grid(row=0, column=1)

b_c = Button(master, text="Button C")
b_c.grid(row=0, column=2)

master.bind_all('', msg)

master.mainloop()
