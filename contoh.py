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
        self.input_frame.place(relx=0.05,rely=0.05, relwidth=0.9, relheight=0.9)

        judul = ttk.Label(self.input_frame, text="Pesanan Buku", font=("Times New Roman", 14))
        judul.pack(pady=13)

        # Membuat objek Biodata dan Pilihan
        self.biodata_objek = Biodata(self.input_frame)
        self.pilihan_objek = Pilihan(self.input_frame)
        self.jumlah_objek = Jumlah(self.input_frame)
        self.pembayaran_objek = Pembayaran(self.input_frame)
        self.total_objek = Pentotalan(self.input_frame)
        self.total_button = Button (self.input_frame,self.jumlah_objek,self.pilihan_objek,self.total_objek)

        # Menjalankan event loop tkinter
        self.window.mainloop()

class Biodata:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        
        nama1 = ttk.Label(self.input_frame, text="Nama", font=("Times New Roman", 14))
        nama1.place(x=13, rely=0.1, y=5)
        
        alamat1 = ttk.Label(self.input_frame, text="Alamat", font=("Times New Roman", 14))
        alamat1.place(x=13, rely=0.1, y=45)

        no = ttk.Label(self.input_frame, text="No.Hp ", font=("Times New Roman", 14))
        no.place(x=13,rely=0.1,y=85)

        # Label
        nama_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        nama_label.pack(padx=10, pady=10, fill="x", expand=True)
        nama_label.place(relx=0.05, rely=0.1,y=5, relwidth=0.65, relheight=0.05, x=100)
        
        alamat_label = ttk.Entry(self.input_frame, font=("Times New Roman", 12))
        alamat_label.pack(padx=10, pady=10, fill="x", expand=True)
        alamat_label.place(relx=0.05, rely=0.175, relwidth=0.65, relheight=0.05, x=100)

        def validate_input(text):
            if text.isdigit() or text == "":
                return True
            else:
                return False
        
        validation = (self.input_frame.register(validate_input), '%P')
        
        no_label = ttk.Entry(self.input_frame, validate="key", validatecommand=validation, font=("Times New Roman", 12))
        no_label.pack(padx=10, pady=10, fill="x", expand=True)
        no_label.place(relx=0.05, rely=0.243, relwidth=0.65, relheight=0.05, x=100)

class Pilihan:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        self.option_var = tk.StringVar()
        self.option_var.set("Pilih Buku")

        opsi = ["Buku Legendaris", "Buku Masak", "Buku Mantan", "Buku Sulap", "Buku Origami"]
        self.opsi_menu = tk.OptionMenu(self.input_frame, self.option_var, *opsi)
        self.opsi_menu.pack(pady=10)
        self.opsi_menu.place(rely=0.343, relwidth=0.35, relheight=0.1, x=13)

        # Keterangan Buku
        self.keterangan = tk.Label(input_frame, text="Pilihan : ", background="white")
        self.keterangan.pack(padx=10, pady=10, fill="x", expand=True)
        self.keterangan.place(relx=0.19, rely=0.343, relwidth=0.5, relheight=0.1, x=103)

        self.jud_buku()

        self.option_var.trace('w', self.select_option)

    def jud_buku(self):
        opsi = ["Buku Legendaris", "Buku Masak", "Buku Mantan", "Buku Sulap", "Buku Origami"]
        self.opsi_menu['menu'].delete(0, 'end')  # Menghapus opsi sebelumnya
        for option in opsi:
            self.opsi_menu['menu'].add_command(label=option, command=lambda value=option: self.select_option(value))

    def select_option(self, option):
        self.selected_option = option
        if option == "Buku Legendaris":
            self.keterangan.config(text="Buku karya: Penulis Terkenal\nTerbit pada: Tahun X\nRp 120.000")
        elif option == "Buku Masak":
            self.keterangan.config(text="Buku karya: Koki Terkenal\nTerbit pada: Tahun Y\nRp 100.000")
        elif option == "Buku Mantan":
            self.keterangan.config(text="Buku karya: Penulis Ternama\nTerbit pada: Tahun Z\nRp 150.000")
        elif option == "Buku Sulap":
            self.keterangan.config(text="Buku karya: Pesulap Terkenal\nTerbit pada: Tahun W\nRp 50.000")
        elif option == "Buku Origami":
            self.keterangan.config(text="Buku karya: Orang Kreatif\nTerbit pada: Tahun V\nRp 90.000")
        else:
            self.keterangan.config(text="")
        
        self.option_var.set(option)




class Jumlah:
    def __init__(self, input_frame):
        self.input_frame = input_frame
        
        namajumlah = ttk.Label(self.input_frame, text="Jumlah", font=("Times New Roman", 14))
        namajumlah.place(x=13, rely=0.47, y=5)
        
        def validate_input(text):
            if text.isdigit() and 1 <= int (text) <= 3 or text == "":
                return True
            else:
                return False
        
        validation = (self.input_frame.register(validate_input), '%P')
        
        jumlah = ttk.Entry(self.input_frame, validate="key", validatecommand=validation, font=("Times New Roman", 12))
        jumlah.pack(padx=10, pady=10, fill="x", expand=True)
        jumlah.place(relx=0.05, rely=0.47,y=5, relwidth=0.65, relheight=0.05, x=100)

        

class Pembayaran:
    def __init__(self, input_frame):
        self.input_frame = input_frame

        hehe_var = tk.StringVar()
        hehe_var.set("Metode Pembayaran")

        bayar_menu = tk.OptionMenu(input_frame, hehe_var, "")
        bayar_menu.pack(pady=10)
        bayar_menu.place(relx=0.05, rely=0.63,y=5, relwidth=0.65, relheight=0.05, x=100)

        def jud_pembayaran():
            
            nama_bayar = ttk.Label(self.input_frame, text="Pembayaran", font=("Times New Roman", 14))
            nama_bayar.place  (x=13, rely=0.63, y=5)
            
            pembayaran = ["Dana, 08543632", "Ovo, 08543632", "BRI, 08543632"]
            bayar_menu['menu'].delete(0, 'end')
            for hehe in pembayaran:
                bayar_menu['menu'].add_command(label=hehe, command=lambda value=hehe: hehe_opsi(value))

        def hehe_opsi(hehe):
            hehe_var.set(hehe)

        jud_pembayaran()


class Pentotalan:
    def __init__(self,input_frame):
        self.input_frame= input_frame
        
        nama_total = ttk.Label(self.input_frame, text="Total Harga", font=("Times New Roman", 14))
        nama_total.place  (x=13, rely=0.71, y=5)
        
        tulisan_total = ttk.Label(self.input_frame, text="", font=("Times New Roman", 14),background="white")
        tulisan_total.place (relx=0.05, rely=0.71,y=5, relwidth=0.65, relheight=0.05, x=100)



class Button:
    def __init__(self, input_frame, jumlah_objek, pilihan_objek, total_objek):
        self.input_frame = input_frame
        self.pilihan_objek = pilihan_objek
        self.jumlah_objek = jumlah_objek
        self.total_objek = total_objek

        submit = ttk.Button(self.input_frame, text="Submit", command=self.calculate_total)
        submit.place(relx=0.30, rely=0.82, y=5, relwidth=0.22, relheight=0.09, x=100)

    def calculate_total(self):
        pilihan = self.pilihan_objek.option_var.get()
        jumlah = int(self.jumlah_objek.jumlah.get())

        if pilihan == "Buku Legendaris":
            total_harga = 120000 * jumlah
        elif pilihan == "Buku Mantan":
            total_harga = 10000 * jumlah
        else:
            total_harga = 0

        self.total_objek.tulisan_total.config(text=total_harga)

        messagebox.showinfo("Total Harga", f"Total Harga: Rp {total_harga}")

            
        
        
        
        
        
        
        
        submit = ttk.Button(self.input_frame,text= "Submit")
        submit.place  (relx=0.30, rely=0.82,y=5, relwidth=0.22, relheight=0.09, x=100)

        
        
        
        
        
        
        
        
        
        
        # submit = ttk.Button(self.input_frame,text= "Submit")
        # submit.place  (relx=0.022, rely=0.82,y=5, relwidth=0.22, relheight=0.09, x=100)
        
        









if __name__ == "__main__":
    app = Tampilan()
    
