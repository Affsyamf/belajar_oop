class Mangga:
    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah
        
    # dipakai kalau saat debuging
    def __repr__(self):
        return "Debug: Mangga: {} berjumlah: {}".format(self.nama, self.jumlah)
    
    # kalau program sudah produksi
    def __str__(self):
        return "Mangga: {} berjumlah: {}".format(self.nama, self.jumlah)
        
    def __add__(self, objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "objek nama dan jumlah"
        
        
belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("medan",5)
print(belanja1)
print(belanja2)
print(repr(belanja1))
print(belanja1 + belanja2)
print(belanja1.__dict__)