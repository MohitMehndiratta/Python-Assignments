import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Python Assignment-1 Solution')


# question-1
def assignment_ques_1():
    number_div_by7_not_div_by5 = [int(i) for i in range(2000, 3201) if int(i) % 7 == 0 and i % 5 != 0]
    sub_window = tk.Toplevel(window)
    sub_window.title('Q-1 Output')
    output_Text = tk.Text(sub_window)
    output_Text.insert(tk.INSERT, number_div_by7_not_div_by5, 0)
    output_Text.grid(row=0, column=0)


# question -2
def assignment_ques_2():
    global f_name_var, l_name_var
    sub_window = tk.Toplevel(window)
    sub_window.title('Q-2 Output')

    label_f_name = tk.Label(sub_window, text='Enter First Name')
    label_l_name = tk.Label(sub_window, text='Enter Last Name')

    f_name_var = tk.StringVar()
    l_name_var = tk.StringVar()

    f_name_input = tk.Entry(sub_window, textvariable=f_name_var)
    l_name_input = tk.Entry(sub_window, textvariable=l_name_var)
    label_f_name.grid(row=0, column=0)
    label_l_name.grid(row=1, column=0)
    f_name_input.grid(row=0, column=1)
    l_name_input.grid(row=1, column=1)

    get_name = tk.Button(sub_window, command=process_username, text="Generate Name")
    get_name.grid(row=2, column=0, columnspan=2)


def process_username():
    my_name = []
    # first_name = input('Enter your first name : ')
    # last_name = input('Enter your last name : ')
    first_name = f_name_var.get()
    last_name = l_name_var.get()

    if first_name != '' and last_name != '':
        my_name.append(first_name)
        my_name.append(' ')
        my_name.append(last_name)
        messagebox.showinfo('Congrats!', 'Your System Generated Id is : {} '.format(
            str(my_name[2]) + str(my_name[1] + str(my_name[0]))))
    else:
        print('Please enter complete details before proceeding')


# question-3
def assignment_ques_3():
    global diam_val
    sub_window = tk.Toplevel(window)
    sub_window.title('Q-2 Output')

    label_vol = tk.Label(sub_window, text='Enter Sphere Dimension')

    diam_val = tk.StringVar()
    diam_input = tk.Entry(sub_window, textvariable=diam_val)
    label_vol.grid(row=0, column=0)
    diam_input.grid(row=0, column=1)

    get_vol = tk.Button(sub_window, command=process_vol, text="Calculate Volume")
    get_vol.grid(row=1, column=0, columnspan=2)


def process_vol():
    diam = int(diam_val.get())
    r = diam / 2
    V = (4 / 3) * (3.14 * (r ** 3))
    messagebox.showinfo('Sphere Volume', 'Volume of the Sphere is : {} '.format(
        str(V)))


q_1_btn = tk.Button(window,
                    text='Run first assignment question solution [numbers in range(2000-3200) div by 7 and not by 5]',
                    command=assignment_ques_1, width=100)
q_1_btn.grid(row=1, column=1)

q_2_btn = tk.Button(window, text='Run Second assignment question solution', command=assignment_ques_2, width=100)
q_2_btn.grid(row=2, column=1)

q_3_btn = tk.Button(window, text='Run Third assignment question solution', command=assignment_ques_3, width=100)
q_3_btn.grid(row=3, column=1)

window.mainloop()
