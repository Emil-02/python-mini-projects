import math
data = [
    {'range': '16-20', 'f': 8, 'bawah': 16, 'atas': 20},
    {'range': '21-25', 'f': 10, 'bawah': 21, 'atas': 25},
    {'range': '26-30', 'f': 7, 'bawah': 26, 'atas': 30},
    {'range': '31-35', 'f': 27, 'bawah': 31, 'atas': 35},
    {'range': '36-40', 'f': 9, 'bawah': 36, 'atas': 40},
    {'range': '41-45', 'f': 14, 'bawah': 41, 'atas': 45},
    {'range': '46-50', 'f': 32, 'bawah': 46, 'atas': 50}
]
sum_f = 0
sum_fx = 0
for row in data:
    xi = (row['bawah'] + row['atas']) / 2
    row['xi'] = xi
    fx = row['f'] * xi
    row['fx'] = fx
    sum_f += row['f']
    sum_fx += row['fx']
mean = sum_fx / sum_f
mean = round(mean, 2) 
print("="*85)
print("LANGKAH AWAL: MENCARI RATA-RATA (MEAN)")
print("="*85)
print(f"Rumus: Rata-rata (X) = Total (f.x) / Total (f)")
print(f"       Rata-rata (X) = {sum_fx} / {sum_f}")
print(f"       Rata-rata (X) = {mean}")
print("\n")
print("="*85)
print("1. DEVIASI RATA - RATA (Mean Deviation)")
print("="*85)
print(f"{'Kelas':<5} | {'Interval':<10} | {'f':<5} | {'Titik Tengah(x)':<15} | {'f.x':<8} | {'|x - X|':<10} | {'f.|x - X|':<10}")
print("-" * 85)
sum_f_abs_dev = 0
for i, row in enumerate(data, 1):
    xi = row['xi']
    abs_dev = abs(xi - mean)
    abs_dev = round(abs_dev, 2) 
    f_abs_dev = row['f'] * abs_dev
    f_abs_dev = round(f_abs_dev, 2) 
    sum_f_abs_dev += f_abs_dev
    print(f"{i:<5} | {row['range']:<10} | {row['f']:<5} | {xi:<15} | {row['fx']:<8} | {abs_dev:<10.2f} | {f_abs_dev:<10.2f}")
print("-" * 85)
print(f"{'Total':<18} | {sum_f:<5} | {'':<15} | {sum_fx:<8} | {'':<10} | {sum_f_abs_dev:<10.2f}")
md = sum_f_abs_dev / sum_f
md = round(md, 4) 
print(f"\nRumus MD = Total f.|x - X| / Total f")
print(f"MD       = {sum_f_abs_dev:.2f} / {sum_f}")
print(f"MD       = {md}")
print("\n")
print("="*95)
print("2. SIMPANGAN BAKU (Standard Deviation)")
print("="*95)
header = f"{'Kelas':<10} {'Frekuensi (fi)':<15} {'Nilai Tengah (Xi)':<18} {'fi.Xi':<10} {'Xi - X':<10} {'(Xi - X)^2':<12} {'fi(Xi - X)^2':<15}"
print(header)
print("-" * 95)
sum_f_sq_dev = 0
for row in data:
    xi = row['xi']
    dev = xi - mean
    dev = round(dev, 2)
    sq_dev = dev ** 2
    sq_dev = round(sq_dev, 2)
    f_sq_dev = row['f'] * sq_dev
    f_sq_dev = round(f_sq_dev, 2)
    sum_f_sq_dev += f_sq_dev
    print(f"{row['range']:<10} {row['f']:<15} {xi:<18} {row['fx']:<10} {dev:<10.2f} {sq_dev:<12.2f} {f_sq_dev:<15.2f}")
print("-" * 95)
print(f"{'Total':<10} {sum_f:<15} {'':<18} {sum_fx:<10} {'':<10} {'':<12} {sum_f_sq_dev:<15.2f}")
varians = sum_f_sq_dev / sum_f
sd = math.sqrt(varians)
print(f"\nRumus S = Akar( Total fi(Xi - X)^2 / Total f )")
print(f"S       = Akar( {sum_f_sq_dev:.2f} / {sum_f} )")
print(f"S       = Akar( {varians:.4f} )")
print(f"S       = {sd:.2f}")