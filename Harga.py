class Harga:
    @staticmethod
    def get_harga_print_hitam_putih(ukuran):
        if ukuran == "A3":
            return 1000
        elif ukuran == "A4":
            return 500
        elif ukuran == "F4":
            return 750
        else:
            return 0

    @staticmethod
    def get_harga_print_berwarna(ukuran):
        if ukuran == "A3":
            return 2000
        elif ukuran == "A4":
            return 1000
        elif ukuran == "F4":
            return 1500
        else:
            return 0

    @staticmethod
    def get_harga_fotocopy(ukuran):
        if ukuran == "A3":
            return 500
        elif ukuran == "A4":
            return 250
        elif ukuran == "F4":
            return 375
        else:
            return 0
