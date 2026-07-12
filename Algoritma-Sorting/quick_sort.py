def quick_sort(arr, depth=0):
    """
    Fungsi untuk mengurutkan array menggunakan algoritma Quick Sort
    dan menampilkan setiap langkah prosesnya.
    """
    # Mencetak setiap kali fungsi dipanggil untuk analisis rekursif
    print(f"{'  ' * depth}Memanggil quick_sort untuk: {arr}")

    # Basis kasus: jika array memiliki 1 elemen atau kosong, array sudah terurut
    if len(arr) <= 1:
        print(f"{'  ' * depth}Kembalikan: {arr}")
        return arr
    else:
        # Memilih pivot dari elemen tengah array
        pivot = arr[len(arr) // 2]

        # Membagi array menjadi tiga bagian:
        # - left: elemen yang lebih kecil dari pivot
        # - middle: elemen yang sama dengan pivot
        # - right: elemen yang lebih besar dari pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Menampilkan proses pembagian berdasarkan pivot
        print(f"{'  ' * depth}Pivot: {pivot}")
        print(f"{'  ' * depth}Kiri: {left}, Tengah: {middle}, Kanan: {right}")

        # Panggilan rekursif untuk mengurutkan bagian kiri dan kanan
        sorted_left = quick_sort(left, depth + 1)
        sorted_right = quick_sort(right, depth + 1)

        # Menggabungkan hasil yang sudah terurut
        hasil = sorted_left + middle + sorted_right
        print(f"{'  ' * depth}Hasil penggabungan: {hasil}") # Menampilkan hasil penggabungan
        return hasil

# --- Program Utama ---

# Data yang akan diurutkan
data = [570, 766, 232, 897, 213, 114, 55]

# Mencetak data awal
print("Data awal:", data)

# Memanggil fungsi quick_sort dan menyimpan hasilnya
sorted_data = quick_sort(data)

# Mencetak hasil akhir
print("\nHasil akhir:", sorted_data)









