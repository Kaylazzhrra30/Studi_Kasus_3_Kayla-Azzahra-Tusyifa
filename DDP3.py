Buku = ("Dasar Pemrograman", "Pendidikan Agama Islam",
        "Matematika Diskrit", "PKN", "Jaringan Komputer")

pinjaman = []
batal = False

print("Daftar Buku :", Buku)

while True:
    pinjam_Buku = input("Buku apa yang ingin dipinjam? ")

    if pinjam_Buku == "selesai":
        break

    if pinjam_Buku in Buku:
        pinjaman.append(pinjam_Buku)
        print("Buku tersedia dan bisa dipinjam")

        lagi = input("Tambah buku? (ya/tidak) ")

        if lagi == "ya":
            continue
        else:
            break

    else:
        print("Buku tidak tersedia")
        ganti = input("Ganti buku? (ya/tidak) ")

        if ganti == "ya":
            continue
        else:
            batal = True
            break

if batal == False:
    print("Daftar pinjaman :", pinjaman)

    hapus = input("hapus buku? (ya/tidak) ")

    if hapus == "ya":
        buku_hapus = input("Buku apa yang ingin dihapus? ")

        if buku_hapus in pinjaman:
            pinjaman.remove(buku_hapus)
            print("Buku berhasil dihapus")
        else:
            print("Buku tidak ada dalam daftar pinjaman")

    print("Buku yang dipinjam :", pinjaman)