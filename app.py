print(
    """
GEROBAK FRIED CHICKEN
==============================
KODE | JENIS POTONG | HARGA
D    | DADA         | RP. 2500
S    | SAYAP        | RP. 2000
P    | PAHA         | RP. 1500
==============================
"""
)

jml_tipe = int(input("Banyak jenis : "))
q = 1

hasil = """
GEROBAK FRIED CHICKEN
=============================================================
NO | JENIS POTONG | HARGA SATUAN | BANYAK BELI | JUMLAH HARGA
=============================================================
"""

while q <= jml_tipe:
    print(f"Jenis ke-{q}")
    kode_pemotongan = input("Kode Potong [D/P/S] : ").upper()
    jumlah_potong = int(input("Banyak Potong : "))

    if kode_pemotongan == "D":
        harga = 2500
        jenis_potong = "DADA"
    elif kode_pemotongan == "S":
        harga = 2000
        jenis_potong = "SAYAP"
    elif kode_pemotongan == "P":
        harga = 1500
        jenis_potong = "PAHA"
    else:
        print("salah input kode potong!!")

    subtotal = harga * jumlah_potong
    hasil += (
        f"{q:<4} {jenis_potong:<15} {harga:<15,} {jumlah_potong:<13} {subtotal:,}\n"
    )
    q += 1

total_subtotal = subtotal * jml_tipe
pajak = int(total_subtotal * 0.1)
total_pembayaran = int(total_subtotal + pajak)

print(hasil)
print("=" * 61)
print(f"Jumlah Bayar : Rp. {total_subtotal:,}")
print(f"Pajak 10% : Rp. {pajak:,}")
print(f"Total Bayar : Rp. {total_pembayaran:,}")
