import tkinter as tk
from tkinter import messagebox

def treugol():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a + b > c and a + c > b and b + c > a:
            result_label.config(text="Этот треугольник существует!", fg="green")
        else:
            result_label.config(text="Этот треугольник не существует!", fg="red")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа!")

root = tk.Tk()
root.title("Проверка треугольника")
root.geometry("300x250")

tk.Label(root, text="Введите сторону a:").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Введите сторону b:").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Введите сторону c:").pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack()

check_btn = tk.Button(root, text="Проверить", command=treugol)
check_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
