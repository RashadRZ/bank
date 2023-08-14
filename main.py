from tkinter import *
from PIL import ImageTk, Image

# heap
queue = []
business_n = 1
personal_n = 1


# UI functions
def call_counter1():
    pass


def call_counter2():
    pass


def add_regular():
    pass


def add_priority():
    pass


def show_next():
    pass


# window setup
root = Tk()
root.title('Bank')
root.iconbitmap('images/money.ico')

app_width = 1280
app_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False, False)
root.configure(bg='#ADCCCB')

# UI widget
top_frame = Frame(root, bg='#ADCCCB')
header_label = Label(top_frame, text='BANK', font=('Arial', 28, 'bold'), bg='#ADCCCB', fg='white')
my_image = ImageTk.PhotoImage(Image.open('images/money.png'))
header_image = Label(top_frame, image=my_image, bg='#ADCCCB')

middle_frame = Frame(root, bg='#ADCCCB')
counter1_label = Label(middle_frame, text='TICKET COUNTER 1', font=('Arial', 18, 'bold'), bg='#ADCCCB', fg='white', height=2)
counter1 = Button(middle_frame, command=call_counter1, text='', font=('Arial', 26, 'bold'), bg='white', fg='#366473', borderwidth=0, width=16, height=4)

counter2_label = Label(middle_frame, text='TICKET COUNTER 2', font=('Arial', 18, 'bold'), bg='#ADCCCB', fg='white', height=2)
counter2 = Button(middle_frame, command=call_counter2, text='', font=('Arial', 26, 'bold'), bg='white', fg='#366473', borderwidth=0, width=16, height=4)

next_queue_label = Label(middle_frame, text='NEXT', font=('Arial', 18, 'bold'), bg='#ADCCCB', fg='white', height=2)
next_queue = Button(middle_frame, text='', font=('Arial', 26, 'bold'), bg='#366473', fg='white', borderwidth=0, width=16, height=4, default='active')

bottom_frame = Frame(root, bg='#ADCCCB')
priority = Button(bottom_frame, command=add_priority, text='BUSINESS', font=('Arial', 18, 'bold'), bg='#366473', fg='white', borderwidth=0, width=11)
regular = Button(bottom_frame, command=add_regular, text='PERSONAL', font=('Arial', 18, 'bold'), bg='white', fg='#366473', highlightthickness=1, highlightbackground='#366473', highlightcolor='#366473', borderwidth=0, width=11, default='active')

# UI positioning
top_frame.pack(pady=50)
header_label.grid(row=0, column=0)
header_image.grid(row=0, column=1)

middle_frame.pack(pady=50)
counter1_label.grid(row=0, column=0)
counter1.grid(row=1, column=0, padx=30)

counter2_label.grid(row=0, column=1)
counter2.grid(row=1, column=1, padx=30)

next_queue_label.grid(row=0, column=2)
next_queue.grid(row=1, column=2, padx=30)

bottom_frame.pack(pady=50)
priority.grid(row=0, column=0, padx=10, pady=10)
regular.grid(row=0, column=1, padx=10, pady=10)

# run
root.mainloop()
