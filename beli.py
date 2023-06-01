import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class Tampilan:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg="white")
        self.window.geometry("500x700")
        self.window.resizable(False, False)
        self.window.title("Tugas Akhir Syifa Dwiky Basamala")

        self.input_frame = ttk.Frame(self.window)
        self.input_frame.pack(padx=10, pady=10, fill="x", expand=True)
        self.input_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        judul = ttk.Label(self.input_frame, text="Pesanan Buku", font=("Times New Roman", 14))
        judul.pack(pady=13)
        
        # Menampilkan objek
        self.biodata_objek = Biodata(self.input_frame)
        self.pilihan_objek = Pilihan(self.input_frame)
        self.jumlah_objek = Jumlah(self.input_frame)
        self.pembayaran_objek = Pembayaran(self.input_frame)
        self.total_objek = Pentotalan(self.input_frame)
        self.oke_button = ButtonOke(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
        self.lagi_button = ButtonLagi(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
        self.sub_button = ButtonSub (self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
    


        # Menjalankan loop tkinter
        self.window.mainloop()
        
    def isi_pemesanan(self):
        while self.jumlah_pembelian < 3:  # Perulangan berdasarkan jumlah_pembelian
            # Menampilkan objek
            self.biodata_objek = Biodata(self.input_frame)
            self.pilihan_objek = Pilihan(self.input_frame)
            self.jumlah_objek = Jumlah(self.input_frame)
            self.pembayaran_objek = Pembayaran(self.input_frame)
            self.oke_button = ButtonOke(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
            self.lagi_button = ButtonLagi(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)
            self.sub_button = ButtonSub(self.input_frame, self.jumlah_objek, self.pilihan_objek, self.total_objek)

            # Menunggu sampai pengguna menekan tombol "Beli Lagi" atau "Submit"
            self.window.wait_window(self.lagi_button.top)  # Menunggu jendela "Beli Lagi" ditutup

            if self.lagi_button.clicked:  # Jika tombol "Beli Lagi" ditekan
                self.jumlah_pembelian += 1
                if self.jumlah_pembelian == 3:
                    messagebox.showinfo("Batas Maksimal Pembelian", "Anda telah mencapai batas maksimal pembelian (3 kali).")
                    break  # Keluar dari perulangan jika mencapai batas maksimal

                # Menghapus objek yang digunakan dalam pemesanan sebelumnya
                self.biodata_objek.input_frame.destroy()
                self.pilihan_objek.input_frame.destroy()
                self.jumlah_objek.input_frame.destroy()
                self.pembayaran_objek.input_frame.destroy()
                self.oke_button.ingin.destroy()
                self.lagi_button.okey.destroy()
                self.sub_button.submit.destroy()
                self.total_objek.total_label.destroy()

                self.total_objek = Pentotalan(self.input_frame)  # Membuat objek total harga baru

            else:  # Jika tombol "Submit" ditekan
                break  # Keluar dari perulangan dan selesai

        

class Biodata:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        nama1 = ttk.Label(self.input_frame, text="Nama", font=("Times New Roman", 14))
        nama1.place(x=13, rely=0.1, y=5)

        alamat1 = ttk.Label(self.input_frame, text="Alamat", font=("Times New Roman", 14))
        alamat1.place(x=13, rely=0.1, y=45)

        no = ttk.Label(self.input_frame, text="No.Hp ", font=("Times New Roman", 14))
        no.place(x=13, rely=0.1, y=85)

        self.nama_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        self.nama_label.pack(padx=10, pady=10, fill="x", expand=True)
        self.nama_label.place(relx=0.05, rely=0.1, y=5, relwidth=0.65, relheight=0.05, x=100)

        self.alamat_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        self.alamat_label.pack(padx=10, pady=10, fill="x", expand=True)
        self.alamat_label.place(relx=0.05, rely=0.175, relwidth=0.65, relheight=0.05, x=100)

        def validate_input(text):
            if text.isdigit() or text == "":
                return True
            else:
                return False

        validation = (self.input_frame.register(validate_input), '%P')

        self.no_label = ttk.Entry(self.input_frame, validate="key", validatecommand=validation, font=("Times New Roman", 12))
        self.no_label.pack(padx=10, pady=10, fill="x", expand=True)
        self.no_label.place(relx=0.05, rely=0.25, relwidth=0.65, relheight=0.05, x=100)

class Pilihan:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        self.option_var = tk.StringVar()

        #  Label Nama Buku
        buku_label = ttk.Label(self.input_frame, text="Buku", font=("Times New Roman", 14))
        buku_label.place(x=13, rely=0.1, y=130)

        #  Opsi Buku
        self.option_menu = ttk.OptionMenu(self.input_frame, self.option_var, "Pilih Buku", "Buku Legendaris", "Buku Masak", "Buku Origami", "Buku Sulap")
        self.option_menu.pack(padx=10, pady=10, fill="x", expand=True )
        self.option_menu.place(relx=0.05, rely=0.1, y=130, relwidth=0.35, relheight=0.05, x=100)
        
        # Keterangan
        self.select_button = ttk.Button(self.input_frame, text="Keterangan", command=self.select_option)
        self.select_button.pack(padx=10, pady=10, fill="x", expand=True)
        self.select_button.place(relx=0.7, rely=0.1, y=130, relwidth=0.2, relheight=0.05)

    def select_option(self):
        selected_option = self.option_var.get()
        if selected_option == "Buku Legendaris":
            harga = 100000
            messagebox.showinfo("Keterangan", f"Harga buku {selected_option}: \nRp {harga}")
        elif selected_option == "Buku Masak":
            harga = 120000
            messagebox.showinfo("Keterangan", f"Harga buku {selected_option}: \nRp {harga}")
        elif selected_option == "Buku Origami":
            harga = 75000
            messagebox.showinfo("Keterangan", f"Harga buku {selected_option}: \nRp {harga}")
        elif selected_option == "Buku Sulap":
            harga = 50000
            messagebox.showinfo("Keterangan", f"Harga buku {selected_option}: \nRp {harga}")    
        else:
            messagebox.showerror("Error", "Harap pilih buku terlebih dahulu.")

class Jumlah:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        namajumlah = ttk.Label(self.input_frame, text="Jumlah", font=("Times New Roman", 14))
        namajumlah.place(x=13, rely=0.38, y=5)

        self.jumlah = tk.StringVar()

        # Memberikan jumlah dan maksimal 3
        def validate_input(text):
            if text.isdigit() and 1 <= int(text) <= 3 or text == "":
                return True
            else:
                return False

        validation = (self.input_frame.register(validate_input), '%P')

        jumlah_entry = ttk.Entry(self.input_frame, validate="key", validatecommand=validation, textvariable=self.jumlah, font=("Times New Roman", 12))
        jumlah_entry.pack(padx=10, pady=10, fill="x", expand=True)
        jumlah_entry.place(relx=0.05, rely=0.37, y=5, relwidth=0.65, relheight=0.05, x=100)

class Pembayaran:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        metode_label = ttk.Label(self.input_frame, text="Metode Pembayaran", font=("Times New Roman", 14))
        metode_label.place(x=13, rely=0.1, y=220)

        self.metode_var = tk.StringVar()
        self.metode_radio1 = ttk.Radiobutton(self.input_frame, text="Transfer Bank", variable=self.metode_var, value="Transfer Bank")
        self.metode_radio1.pack(padx=10, pady=10, fill="x", expand=True)
        self.metode_radio1.place(relx=0.18, rely=0.1, y=218, relwidth=0.65, relheight=0.05, x=100)

        self.metode_radio2 = ttk.Radiobutton(self.input_frame, text="COD", variable=self.metode_var, value="COD")
        self.metode_radio2.pack(padx=10, pady=10, fill="x", expand=True)
        self.metode_radio2.place(relx=0.18, rely=0.175, y=210, relwidth=0.65, relheight=0.05, x=100)

class Pentotalan:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        self.total_label = ttk.Label(self.input_frame, text="Total Harga: Rp 0", font=("Times New Roman", 14))
        self.total_label.pack(pady=10)
        self.total_label.place(x=150, rely=0.1, y=310)

class ButtonLagi:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        self.total_harga = 0  # Variabel untuk mengakumulasi total harga

        self.okey = ttk.Button(self.input_frame, text="Beli Lagi", command=self.add_item)
        self.okey.pack(padx=10, pady=10, fill="x", expand=True)
        self.okey.place(relx=0.09, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
    
    def add_item(self):
        self.pilihan_objek.option_var.set("Pilih Buku")
        self.jumlah_objek.jumlah.set("")
        self.total_harga = 0  # Mengatur ulang total harga ke 0
        self.total_objek.total_label.config(text=f"Total Harga: Rp {self.total_harga}")
        self.total_objek.total_label.config(text=f"Total yang harus dibayar adalah Rp {self.total_harga}")

        self.total_objek.total_harga = self.total_harga  # Mengupdate total harga pada objek total

class ButtonOke:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        self.total_harga = 0  # Variabel untuk mengakumulasi total harga
        self.book_label_text = ""  # Variabel untuk menyimpan teks total harga per buku

        self.ingin = ttk.Button(self.input_frame, text="Okey", command=self.calculate_total)
        self.ingin.pack(padx=10, pady=10, fill="x", expand=True)
        self.ingin.place(relx=0.7, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
        
        self.total_label = ttk.Label(self.input_frame, text="Total Harga: Rp 0", font=("Times New Roman", 12))
        self.total_label.pack(pady=5)
        self.total_label.place(relx=0.12, rely=0.8)

    def calculate_total(self):
        jumlah = int(self.jumlah_objek.jumlah.get())
        selected_option = self.pilihan_objek.option_var.get()
        book_name = ""

        if selected_option == "Buku Legendaris":
            harga = 100000
            book_name = "Buku Legendaris"
        elif selected_option == "Buku Masak":
            harga = 120000
            book_name = "Buku Masak"
        elif selected_option == "Buku Origami":
            harga = 75000
            book_name = "Buku Origami"
        elif selected_option == "Buku Sulap":
            harga = 50000
            book_name = "Buku Sulap"

        total_harga = jumlah * harga
        self.total_harga += total_harga  # Mengakumulasi total harga
        self.total_objek.total_harga = self.total_harga  # Mengupdate total harga pada objek total
        self.total_objek.total_label.config(text=f"Total Harga: Rp {total_harga}")
        self.book_label_text += f"{book_name}: Rp {total_harga}\n"  # Menyimpan teks total harga per buku
        self.total_label.config(text=self.book_label_text + f"\nTotal yang harus dibayar adalah Rp {self.total_harga}")

class ButtonLagi:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        self.counter = 0  # Variabel penghitung

        self.okey = ttk.Button(self.input_frame, text="Beli Lagi", command=self.add_item)
        self.okey.pack(padx=10, pady=10, fill="x", expand=True)
        self.okey.place(relx=0.09, rely=0.25, y=270, relwidth=0.2, relheight=0.07)
    
    def add_item(self):
        while self.counter < 2:  # Batasan pembelian lagi (2 kali)
            self.pilihan_objek.option_var.set("Pilih Buku")
            self.jumlah_objek.jumlah.set("")
            self.total_objek.total_label.config(text="Total Harga: Rp 0")
            self.counter += 1
            break

        if self.counter >= 2:
            messagebox.showinfo("Batas Maksimum", "Anda telah mencapai batas maksimum pembelian lagi.")

class ButtonSub:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek
        
        self.submit= ttk.Button(self.input_frame, text="Submit")
        self.submit.pack(padx=10, pady=10, fill="x", expand=True)
        self.submit.place(relx=0.4, rely=0.25, y=270, relwidth=0.2, relheight=0.07)


# Membuat objek Tampilan
tampilan = Tampilan()
