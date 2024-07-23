from tkinter import *

# ============================ settings =============================

root = Tk()
root.geometry('280x240')
root.title("calculator")
root.resizable(width=False, height=False)
color = "gray9"
root.configure(bg=color)

# ============================ variables =============================

text_input = StringVar()
calc_operator = ''

# ============================ frames =============================

top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_fourth = Frame(root, width=400, height=50, bg=color)
top_fourth.pack(side=TOP)

top_fifth = Frame(root, width=400, height=50, bg=color)
top_fifth.pack(side=TOP)

top_sixth = Frame(root, width=400, height=50, bg=color)
top_sixth.pack(side=TOP)

# ============================ functions =============================

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)


def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-' + calc_operator
    calc_operator = temp
    text_input.set(temp)


def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op


def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

# ============================ display =============================

text_display = Entry(top_first, textvariable=text_input)
text_display.pack(padx=5, pady=5)

# ============================ buttons of functions =============================

btn_plus = Button(top_second, text='+', width=7, command=lambda: button_click('+'))
btn_plus.pack(side=RIGHT, padx=5, pady=5)

btn_minus = Button(top_third, text='-', width=7, command=lambda: button_click('-'))
btn_minus.pack(side=RIGHT, padx=5, pady=5)

btn_mul = Button(top_fourth, text='*', width=7, command=lambda: button_click('*'))
btn_mul.pack(side=RIGHT, padx=5, pady=5)

btn_div = Button(top_fifth, text='/', width=7, command=lambda: button_click('/'))
btn_div.pack(side=RIGHT, padx=5, pady=5)

# ============================ buttons of numbers=============================

btn_one = Button(top_second, text='1', width=5, command=lambda: button_click('1'))
btn_one.pack(side=LEFT, padx=5, pady=5)

btn_two = Button(top_second, text='2', width=5, command=lambda: button_click('2'))
btn_two.pack(side=LEFT, padx=5, pady=5)

btn_three = Button(top_second, text='3', width=5, command=lambda: button_click('3'))
btn_three.pack(side=LEFT, padx=5, pady=5)

btn_four = Button(top_third, text='4', width=5, command=lambda: button_click('4'))
btn_four.pack(side=LEFT, padx=5, pady=5)

btn_five = Button(top_third, text='5', width=5, command=lambda: button_click('5'))
btn_five.pack(side=LEFT, padx=5, pady=5)

btn_six = Button(top_third, text='6', width=5, command=lambda: button_click('6'))
btn_six.pack(side=LEFT, padx=5, pady=5)

btn_seven = Button(top_fourth, text='7', width=5, command=lambda: button_click('7'))
btn_seven.pack(side=LEFT, padx=5, pady=5)

btn_eight = Button(top_fourth, text='8', width=5, command=lambda: button_click('8'))
btn_eight.pack(side=LEFT, padx=5, pady=5)

btn_nine = Button(top_fourth, text='9', width=5, command=lambda: button_click(9))
btn_nine.pack(side=LEFT, padx=5, pady=5)

btn_sign = Button(top_fifth, text='sign', width=5, command=lambda: sign_change())
btn_sign.pack(side=LEFT, padx=5, pady=5)

btn_zero = Button(top_fifth, text='0', width=5, command=lambda: button_click('0'))
btn_zero.pack(side=LEFT, padx=5, pady=5)

btn_point = Button(top_fifth, text='.', width=5, command=lambda: button_click('.'))
btn_point.pack(side=LEFT, padx=5, pady=5)

left_par = Button(top_sixth, text='(', width=5, command=lambda: button_click('('))
left_par.pack(side=LEFT, padx=5, pady=5)

right_par = Button(top_sixth, text=')', width=5, command=lambda: button_click(')'))
right_par.pack(side=LEFT, padx=5, pady=5)

delete_one = Button(top_sixth, text='DEL', width=5, command=lambda: button_delete())
delete_one.pack(side=LEFT, padx=5, pady=5)

btn_equal = Button(top_sixth, text='=', width=7, command=lambda: button_equal())
btn_equal.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()