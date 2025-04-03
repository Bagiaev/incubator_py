from tkinter import *
import math

root = Tk()
root.configure(bg='#808080')
root.title('Calculator')
root.geometry('492x380')

Display = Entry(root, font=('Helvetica', 20, 'bold'),
                 foreground='white', background='#2F4F4F',
                 borderwidth=30, width=29, justify=RIGHT)
Display.grid(row=0, column=0, columnspan=4, pady=1)
Display.insert(0, '0')

def update_display(value):
    current = Display.get()
    if current == '0':
        Display.delete(0, END)
    Display.insert(END, value)

def clear_display():
    Display.delete(0, END)
    Display.insert(0, '0')

def calculate():
    try:
        result = eval(Display.get().replace('x', '*').replace('÷', '/'))
        clear_display()
        Display.insert(0, str(result))
    except Exception as e:
        clear_display()
        Display.insert(0, 'Error')

numberpad = "789456123"
width_for_numbers = [15, 17, 17]
i = 0
for j in range(2, 5):
    for k in range(3):
        Button(root, text=f'{numberpad[i]}', width=width_for_numbers[k], height=4,
               command=lambda value=numberpad[i]: update_display(value)).grid(row=j, column=k)
        i += 1

Button(root, text='C', bg='#778899', width=15, height=4, command=clear_display).grid(row=1, column=0)
Button(root, text='sqrt', bg='#778899', width=17, height=4, command=lambda: update_display('sqrt(')).grid(row=1, column=1)
Button(root, text='+', bg='#778899', width=17, height=4, command=lambda: update_display('+')).grid(row=1, column=2)
Button(root, text='-', bg='#778899', width=17, height=4, command=lambda: update_display('-')).grid(row=1, column=3)

Button(root, text='x', bg='#778899', width=17, height=4, command=lambda: update_display('x')).grid(row=2, column=3)
Button(root, text='÷', bg='#778899', width=17, height=4, command=lambda: update_display('÷')).grid(row=3, column=3)
Button(root, text='=', bg='#778899', width=17, height=4, command=calculate).grid(row=4, column=3)

Button(root, text='sqrt', bg='#778899', width=17, height=4, command=lambda: update_display('sqrt(')).grid(row=1, column=1)

Button(root, text='.', bg='#778899', width=17, height=4, command=lambda: update_display('.')).grid(row=4, column=2)

root.mainloop()
