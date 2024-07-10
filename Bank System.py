from tkinter import *
from tkinter import messagebox

money = 0.0

def withdraw():
    global money
    try:
        value = float(enterBox.get())
        if value < 0:
            messagebox.showerror(title="ERROR",message="Given Amount is INVALID")
        elif value > money:
            messagebox.showerror(title="ERROR",message="INSUFFICIENT FUND!!")
        else:
            money = money - value
            messagebox.showinfo(title="SUCCESS",message="Withdrawn Successfully")
    except ValueError:
        messagebox.showerror(title="ERROR",message="Given Amount is INVALID")
    except Exception:
        messagebox.showerror(title="ERROR",message="Something went wrong!!")
def deposit():
    try:
        value = float(enterBox.get())
        if value == "":
            messagebox.showerror("Error", "Please enter a Amount")
        elif value > 0:
            global money
            money = money + value
            messagebox.showinfo(title="Deposit",message=("Deposit Successfuly"))
    except ValueError:
        messagebox.showerror(title="ERROR",message="Given Amount is INVALID")
    except Exception:
        messagebox.showerror(title="ERROR",message="Something went wrong!!")
def balance():
    messagebox.showinfo(title="Balance",message=("Balance : "+"$" + str(money)))
def transfer():
    messagebox.showinfo(title="Transfer",message="Transfer functionality is not implemented yet.")
def exit():
    if (messagebox.askokcancel(title="Exit",message="Do you Want to Quit?")):
        window.destroy()

window = Tk()
window.title("Banking System")
window.config(background="#101720")

lable = Label(window,
                font=("Airal",15,"bold"),
                fg="white",
                bg="#101720",
                activebackground="#101720",
                activeforeground="yellow",
                text="Enter Amount")

enterBox = Entry(window,font=("Airal",20),fg="white",background="#101720")
withdraw_button = Button(window,
                         text="Withdraw",
                         command=withdraw,
                         font=("Airal",15),
                         fg="white",
                         bg="#101720",
                         activebackground="#101720",
                         activeforeground="yellow")
deposit_button = Button(window,
                        text="Deposit",
                        command=deposit,
                        font=("Airal",15),
                        fg="white",
                        bg="#101720",
                        activebackground="#101720",
                        activeforeground="yellow")
show_balance = Button(window,
                        text="Balance",
                        command=balance,
                        font=("Airal",15),
                        fg="white",
                        bg="#101720",
                        activebackground="#101720",
                        activeforeground="yellow")
exit_button = Button(window,
                        text="Exit",
                        command=exit,
                        font=("Airal",15),
                        fg="white",
                        bg="#101720",
                        activebackground="#101720",
                        activeforeground="yellow")
transfer_button = Button(window,
                        text="Transfer",
                        command=transfer,
                        font=("Airal",15),
                        fg="white",
                        bg="#101720",
                        activebackground="#101720",
                        activeforeground="yellow")

withdraw_button.grid(row=2,
                     column=1,
                     padx=10,
                     pady=10)
deposit_button.grid(row=1,
                    column=2,
                    padx=10,
                    pady=10)
show_balance.grid(row=1,
                  column=1,
                  padx=10,
                  pady=10)
exit_button.grid(row=2,
                 column=2,
                 padx=10,
                 pady=10)
transfer_button.grid(row=3,column=1,columnspan=2,padx=10,pady=10)

enterBox.grid(row=0,
              column=1,
              columnspan=2,
              padx=10,
              pady=10)
lable.grid(row=0,column=0,padx=10,pady=10)

window.mainloop()