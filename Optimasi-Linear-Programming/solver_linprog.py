from scipy.optimize import linprog

# 1. Koefisien Fungsi Tujuan (Z = 6x1 + 4x2)
# Karena linprog melakukan minimalisasi, kita ubah tanda menjadi negatif untuk maksimasi
c = [-6, -4] 

# 2. Koefisien Kendala (Sisi Kiri / Matrix A)
# [ [2, 1],   -> Waktu Programmer (2x1 + 1x2)
#   [1, 2] ]  -> Kapasitas Server (1x1 + 2x2)
A = [[2, 1], [1, 2]]

# 3. Batas Kendala (Sisi Kanan / Matrix b)
b = [100, 80]

# 4. Batas Nilai Variabel (x1 >= 0, x2 >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# 5. Eksekusi Solver
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Output Hasil
print("--- HASIL OPTIMASI ---")
print(f"Jumlah Aplikasi Mobile (x1)  : {res.x[0]:.0f} unit")
print(f"Jumlah Aplikasi Desktop (x2) : {res.x[1]:.0f} unit")
print(f"Keuntungan Maksimal (Z)      : Rp{abs(res.fun):.0f} juta")