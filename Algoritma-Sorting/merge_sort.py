def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]  # Bagian kiri
        R = arr[mid:]  # Bagian kanan

        # Rekursif untuk memecah bagian kiri dan kanan
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Menggabungkan kembali dua sub-list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Cek sisa elemen di L, jika ada
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Cek sisa elemen di R, jika ada
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Data yang digunakan sesuai contoh
data_awal = [38, 27, 43, 3, 9, 82, 10]

print(f"Data awal: {data_awal}")

# Buat salinan data untuk diurutkan
data_terurut = data_awal[:] 
merge_sort(data_terurut)

print(f"Hasil akhir: {data_terurut}")

# Contoh lain dari gambar 1:
# data_lain = [105000, 89000, 120000, 75000, 95000]
# print(f"\nData awal: {data_lain}")
# merge_sort(data_lain)
# print(f"Hasil akhir: {data_lain}")