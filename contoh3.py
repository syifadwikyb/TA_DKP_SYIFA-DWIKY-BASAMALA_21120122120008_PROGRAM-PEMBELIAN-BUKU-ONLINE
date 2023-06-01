import tkinter as tk
from tkinter import messagebox

def submit():
    if not entry1.get() or not entry2.get() or not entry3.get():
        messagebox.showinfo("Peringatan", "Harap isi semua input.")
    else:
        ""
        # Proses ketika semua input terisi
        # ...

# Membuat window
window = tk.Tk()
window.title("Contoh Pemberitahuan Input")

# Membuat label dan entry untuk input
label1 = tk.Label(window, text="Input 1:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Input 2:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

label3 = tk.Label(window, text="Input 3:")
label3.pack()
entry3 = tk.Entry(window)
entry3.pack()

# Membuat tombol submit
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Menjalankan loop tkinter
window.mainloop()
