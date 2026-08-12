import base64
import urllib.parse
import hashlib
import os

def base64_islem(metin):
    print("\n--- Base64 Deneyleri ---")
    bayt_hali = metin.encode('utf-8')
    b64_encoded = base64.b64encode(bayt_hali).decode('utf-8')
    print(f"Orijinal Girdi : {metin}")
    print(f"Base64 Çıktısı : {b64_encoded}")
    b64_decoded = base64.b64decode(b64_encoded).decode('utf-8')
    print(f"Geri Çözülmüş  : {b64_decoded}")

def url_islem(metin):
    print("\n--- URL Encoding Deneyleri ---")
    url_encoded = urllib.parse.quote(metin)
    print(f"Orijinal Girdi : {metin}")
    print(f"URL Encoding   : {url_encoded}")
    url_decoded = urllib.parse.unquote(url_encoded)
    print(f"Geri Çözülmüş  : {url_decoded}")

def hashing_ve_cig_etkisi_islem(metin):
    print(f"\n--- Hashing ve Çığ Etkisi Deneyleri ---")
    md5_hash = hashlib.md5(metin.encode('utf-8')).hexdigest()
    sha1_hash = hashlib.sha1(metin.encode('utf-8')).hexdigest()
    sha256_hash = hashlib.sha256(metin.encode('utf-8')).hexdigest()
    
    print(f"Orijinal Girdi : {metin}")
    print(f"MD5    ({len(md5_hash)*4} bit) : {md5_hash}")
    print(f"SHA-1  ({len(sha1_hash)*4} bit): {sha1_hash}")
    print(f"SHA-256({len(sha256_hash)*4} bit): {sha256_hash}")

# GÜN 3: Dosya Bütünlüğü Deneyi İçin Fonksiyon
def dosya_butunlugu_deneyi():
    print("\n--- Dosya Bütünlüğü (Data Integrity) Deneyi ---")
    dosya_adi = "test_butunluk.txt"
    
    # 1. Aşama: Orijinal dosya oluştur ve hash hesapla
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write("Staj dosya butunlugu testi.")
    
    with open(dosya_adi, "rb") as f:
        orijinal_icerik = f.read()
        orijinal_hash = hashlib.sha256(orijinal_icerik).hexdigest()
    
    print(f"1. Durum (Orijinal Dosya) SHA-256 : {orijinal_hash}")
    
    # 2. Aşama: Dosyada tek bir karakter değiştir (Sonuna nokta ekle)
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write("Staj dosya butunlugu testi..") # Tek bir karakter değiştirildi
        
    with open(dosya_adi, "rb") as f:
        degismis_icerik = f.read()
        degismis_hash = hashlib.sha256(degismis_icerik).hexdigest()
        
    print(f"2. Durum (Değişmiş Dosya)  SHA-256 : {degismis_hash}")
    print("[!] Gözlem: Dosya içeriğindeki tek karakterlik değişim hash değerini tamamen değiştirdi!")

if __name__ == "__main__":
    print("=== GÜN 2 ve GÜN 3: Kodlama ve Hashing Araç Testleri ===")
    
    # 1. Standart Metin Deneyi (Gün 2)
    base64_islem("erdemarr")
    
    # 2. Türkçe Karakter Deneyi (Gün 2)
    print("\n[!] Türkçe Karakter Deneyi Başlıyor...")
    turkce_metin = "Şifreli arama & test"
    base64_islem(turkce_metin)
    url_islem(turkce_metin)
    
    # 3. Parola Base64 Deneyi (Gün 2)
    print("\n[!] Parola Base64 Güvenlik Testi...")
    parola = "GizliSifre123!"
    base64_islem(parola)
    
    # 4. Hashing ve Çığ Etkisi Deneyleri (Gün 3)
    print("\n[!] Gün 3 Hashing ve Çığ Etkisi Testleri Başlıyor...")
    hashing_ve_cig_etkisi_islem("StajGunUclusu")
    hashing_ve_cig_etkisi_islem("stajGunUclusu")
    
    # 5. Dosya Bütünlüğü Deneyi (Gün 3)
    dosya_butunlugu_deneyi()