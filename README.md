# Simple Banking System

A simple banking system application created using Python and Tkinter. This application allows users to perform basic banking operations such as depositing money, withdrawing funds, checking the balance, and has a placeholder for future transfer functionality.

## Features

- **Deposit Money**: Allows users to deposit a specified amount of money.
- **Withdraw Money**: Allows users to withdraw a specified amount of money, with validation for insufficient funds.
- **Check Balance**: Displays the current balance in the account.
- **Transfer Money**: Placeholder for future transfer functionality.
- **Exit**: Option to exit the application.

## Requirements

- Python 3.x
- Tkinter library (comes with standard Python installations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LennyDany-03/Bank-System-simple-.git
   cd Bank-System-simple-


   
Here is the Example Code

from tkinter import *
from tkinter import messagebox

money = 0.0

def withdraw():
    global money
    try:
        value = float(enterBox.get())
        if value < 0:
            messagebox.showerror(title="ERROR", message="Given Amount is
