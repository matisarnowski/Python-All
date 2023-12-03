"""Import modules to create a new window with my API."""
import tkinter as tk
import requests

root = tk.Tk()
root.grid()

my_string_with_all = tk.StringVar(root)

def my_function():
    """Function which makes all computed."""
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={amount.get()}&from={from_currency.get().upper()}&to={to_currency.get().upper()}",
        timeout=10,
    )
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"{amount.get()} {from_currency.get().upper()} to {round(response.json()["rates"][to_currency.get().upper()], 1)} {to_currency.get().upper()}.")

tk.Label(
    root,
    text="Wprowadź walutę, którą chcesz przekonwertować: ",
    font=("calibre", 10, "normal"),
).grid(row=0, column=0)
from_currency = tk.StringVar(root)
from_currency_text_box = tk.Entry(
    root, textvariable=from_currency, font=("calibre", 10, "bold")
)
from_currency_text_box.grid(row=0, column=1)
tk.Label(
    root,
    text="Wprowadź walutę, na którą chcesz przekonwertować: ",
    font=("calibre", 10, "normal"),
).grid(row=1, column=0)
to_currency = tk.StringVar(root)
to_currency_text_box = tk.Entry(
    root, textvariable=to_currency, font=("calibre", 10, "bold")
)
to_currency_text_box.grid(row=1, column=1)
tk.Label(
    root,
    text="Wprowadź ilość waluty, którą chcesz przekonwertować: ",
    font=("calibre", 10, "normal"),
).grid(row=2, column=0)
amount = tk.DoubleVar(root)
amount_text_box = tk.Entry(root, textvariable=amount, font=("calibre", 10, "bold"))
amount_text_box.grid(row=2, column=1)
tk.Button(
    root, text="Przelicz!", command=my_function, font=("calibre", 10, "bold")
).grid(row=3, column=0)
 
output = tk.Text(root, height = 5, width = 25, bg = "light cyan")
output.grid(row=3, column=1)
root.mainloop()
