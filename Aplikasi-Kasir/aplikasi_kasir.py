# Simulasi Database Sederhana menggunakan Dictionary & List
db_user = ["081122334455"] # Database Nomor HP
db_hutang = {"Budi": 500000} # Database Nama Pelanggan : Sisa Hutang
print("=== APLIKASI GORDEN ===")
# 1. Sesi Buka Aplikasi & Login/Daftar
status = input("Apakah Anda ingin Login atau Daftar? (login/daftar): ").lower()
if status == "daftar":
    no_hp_baru = input("Input Nomor HP: ")
    db_user.append(no_hp_baru) # Simpan Data User ke Database
    print("[Sistem] Data User berhasil disimpan ke Database.\n")
# Alur masuk setelah daftar atau jika langsung login
no_hp = input("Input Nomor HP untuk masuk: ")
if no_hp in db_user:
    print("\n=== DASHBOARD / BERANDA ===")
    # Percabangan Transaksi? (YA / Bayar Hutang)
    jenis_transaksi = input("Pilih Transaksi (baru / hutang): ").lower()

    if jenis_transaksi == "hutang": # Alur Bayar Hutang
        nama = input("Input Nama Pelanggan: ")
        
        # Cek Data Ada di database?
        if nama in db_hutang:
            print(f"Sisa hutang atas nama {nama}: Rp{db_hutang[nama]}")
            bayar = int(input("Input jumlah bayar: Rp"))
            
            # Proses sisa: Hutang - Input jumlah bayar
            db_hutang[nama] -= bayar 
            print("[Sistem] Update database sukses!")
            
            # Cetak Nota
            print("\n==============================")
            print("         NOTA PEMBAYARAN        ")
            print(f" Nama Pelanggan : {nama}")
            print(f" Jumlah Bayar   : Rp{bayar}")
            print(f" Sisa Hutang    : Rp{db_hutang[nama]}")
            print("==============================")
        else:
            print("[Sistem] Data pelanggan tidak ditemukan di database.")
    elif jenis_transaksi == "baru": # Alur Transaksi YA
        nama = input("Input Nama Pelanggan: ")
        harga = int(input("Input harga: Rp"))
        # Percabangan Bayar Tunai?
        metode = input("Bayar Tunai? (ya / kredit): ").lower()
        if metode == "ya":
            uang_pas = int(input("Input uang pas: Rp"))
            # Proses Hitung
            kembalian = uang_pas - harga
            # Simpan ke Database (Diasumsikan berhasil)
            print("[Sistem] Data transaksi lunas tersimpan ke database.")
            # Cetak Nota
            print("\n==============================")
            print("           NOTA LUNAS           ")
            print(f" Nama Pelanggan : {nama}")
            print(f" Total Harga    : Rp{harga}")
            print(f" Tunai          : Rp{uang_pas}")
            print(f" Kembalian      : Rp{kembalian}")
            print("==============================")
        elif metode == "kredit":
            dp = int(input("Input DP: Rp"))
            sisa_hutang = harga - dp
            # Simpan data Hutang & Simpan ke Database
            db_hutang[nama] = db_hutang.get(nama, 0) + sisa_hutang
            print(f"[Sistem] Data hutang tersimpan. Total hutang {nama}: Rp{db_hutang[nama]}")
            # Cetak Nota
            print("\n==============================")
            print("          NOTA KREDIT           ")
            print(f" Nama Pelanggan : {nama}")
            print(f" Total Harga    : Rp{harga}")
            print(f" DP Dibayar     : Rp{dp}")
            print(f" Sisa Hutang    : Rp{sisa_hutang}")
            print("==============================")

else:
    print("Login Gagal: Nomor HP tidak terdaftar!")