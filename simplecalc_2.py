import tkinter as tk

def button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def key_input(event):
    key = event.char
    if key in '0123456789.+-*/':
        button(key)
    elif event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    elif event.keysym == 'Escape':
        clear_entry()

root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)
root.configure(bg="#2e2e2e")
root.bind("<Key>", key_input)

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right',
                 bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    cmd = calculate if text == '=' else lambda val=text: button(val)
    btn = tk.Button(root, text=text, width=6, height=3, font=('Arial', 16), command=cmd,
                    bg="#3c3c3c", fg="#ffffff", activebackground="#505050", activeforeground="#ffffff")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

clear_btn = tk.Button(root, text="Clear", padx=85, pady=20, font=('Arial', 16), command=clear_entry,
                      bg="#3c3c3c", fg="#ffffff", activebackground="#505050", activeforeground="#ffffff")
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()