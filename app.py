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

qty_types = int(input("Banyak jenis : "))
q = 1

result = """
GEROBAK FRIED CHICKEN
=============================================================
NO | JENIS POTONG | HARGA SATUAN | BANYAK BELI | JUMLAH HARGA
=============================================================
"""

while q <= qty_types:
    print(f"Jenis ke-{q}")
    code_cutting = input("Kode Potong [D/P/S] : ").upper()
    qty_cutting = int(input("Banyak Potong : "))

    if code_cutting == "D":
        price = 2500
        type_cutting = "DADA"
    elif code_cutting == "S":
        price = 2000
        type_cutting = "SAYAP"
    elif code_cutting == "P":
        price = 1500
        type_cutting = "PAHA"
    else:
        print("salah input kode potong!!")

    subtotal = price * qty_cutting
    result += f"{q:<4} {type_cutting:<15} {price:<15,} {qty_cutting:<13} {subtotal:,}\n"
    q += 1

total_subtotal = subtotal * qty_types
tax = int(total_subtotal * 0.1)
total_payment = int(total_subtotal + tax)

print(result)
print("=" * 61)
print(f"Jumlah Bayar : Rp. {total_subtotal:,}")
print(f"Pajak 10% : Rp. {tax:,}")
print(f"Total Bayar : Rp. {total_payment:,}")
