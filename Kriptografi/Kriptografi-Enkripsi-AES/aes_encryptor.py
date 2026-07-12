import os
import hashlib
from Crypto.Cipher import AES
def generate_key_dari_password(password_user):
    return hashlib.sha256(password_user.encode()).digest()
def encrypt_file(nama_file, password):
    if not os.path.exists(nama_file):
        print("[-] File tidak ditemukan!")
        return None
    key = generate_key_dari_password(password)
    with open(nama_file, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nama_dasar = nama_file.split('.')[0]
    file_enkripsi = f"{nama_dasar}_Enkripsi"
    with open(file_enkripsi, "wb") as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)
    print(f"[+] File berhasil dienkripsi menjadi: {file_enkripsi}")
    return file_enkripsi
def decrypt_file(file_enkripsi, nama_file_asli, password):
    key = generate_key_dari_password(password)
    with open(file_enkripsi, "rb") as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)
        nama_dasar = nama_file_asli.split('.')[0]
        ekstensi = nama_file_asli.split('.')[-1]
        file_dekripsi = f"{nama_dasar}_Dekripsi.{ekstensi}"
        with open(file_dekripsi, "wb") as f:
            f.write(plaintext)
        print(f"[+] File berhasil didekripsi menjadi: {file_dekripsi}")
    except ValueError:
        print("[-] Dekripsi gagal! Password yang dimasukkan salah atau file telah dimodifikasi.")
if __name__ == "__main__":
    print("=== PROGRAM ENKRIPSI FILE AES ===")
    file_input = input("Masukkan nama file TXT yang ingin dienkripsi:")
    pass_enkripsi = input("Buat password untuk mengunci file: ")
    print("\n--- Proses Enkripsi ---")
    file_hasil_enkripsi = encrypt_file(file_input, pass_enkripsi)  
    if file_hasil_enkripsi:
        print("\n--- Proses Dekripsi ---")
        pass_dekripsi = input("Masukkan password: ")
        decrypt_file(file_hasil_enkripsi, file_input, pass_dekripsi)