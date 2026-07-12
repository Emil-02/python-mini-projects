import cv2
import matplotlib.pyplot as plt

# === BACA GAMBAR ===
image = cv2.imread('img/sample.jpg')
if image is None:
    print("Gambar tidak ditemukan. Pastikan file 'img/sample.jpg' ada di folder yang sama dengan file ini.")
    exit()

# Konversi BGR ke RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# === GRAYSCALE ===
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# === BINARY ===
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# === TAMPILKAN CITRA ===
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Citra RGB")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap='gray')
plt.title("Citra Grayscale")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Citra Biner")
plt.axis('off')

plt.tight_layout()
plt.show()

# === CETAK NILAI INTENSITAS ===
print("\n=== Nilai Intensitas RGB (Contoh 5 piksel pertama) ===")
print(image_rgb.reshape(-1, 3)[:5])

print("\n=== Nilai Intensitas Grayscale (Contoh 5 piksel pertama) ===")
print(gray_image.reshape(-1)[:5])

print("\n=== Nilai Intensitas Biner (Contoh 5 piksel pertama) ===")
print(binary_image.reshape(-1)[:5])