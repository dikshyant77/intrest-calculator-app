from tkinter import *

root = Tk()
root.title("Interest Calculator")
root.geometry('400x400')

lbl1 = Label(root, text="Enter principle", bg='light blue')
lbl2 = Label(root, text="Enter the interest rate", bg='light blue')
lbl3 = Label(root, text="Enter time in years", bg='light blue')

principle_ent = Entry()
rate_ent = Entry()
time_ent = Entry()


def compound_interest():
   principle = float(principle_ent.get())
   rate = float(rate_ent.get())
   global time
   time = float(time_ent.get())
   total = principle * pow((1 + rate / 100), time)
   balance = f"Your total balance after {time} is $" + str(total) + "."
   tb.insert(END, balance)
tb = Text(bg='black', fg='white')
btn = Button(text="Show balance",command=compound_interest, bg='white', fg='black')

lbl1.place(x=20, y=60)
principle_ent.place(x=150, y=60)
lbl2.place(x=20, y=110)
rate_ent.place(x=150, y=110)
lbl3.place(x=20, y=160)
time_ent.place(x=150, y=160)
btn.place(x=130, y=210)
tb.place(y=250)

root.mainloop()