import base64
import urllib.parse

def base64_islem(metin):
    print("\n--- Base64 Deneyleri ---")
    # Metni Base64'e çevirme (Encoding)
    bayt_hali = metin.encode('utf-8')
    b64_encoded = base64.b64encode(bayt_hali).decode('utf-8')
    print(f"Orijinal Girdi : {metin}")
    print(f"Base64 Çıktısı : {b64_encoded}")
    
    # Base64'ü geri çözme (Decoding)
    b64_decoded = base64.b64decode(b64_encoded).decode('utf-8')
    print(f"Geri Çözülmüş  : {b64_decoded}")

def url_islem(metin):
    print("\n--- URL Encoding Deneyleri ---")
    # URL Encoding
    url_encoded = urllib.parse.quote(metin)
    print(f"Orijinal Girdi : {metin}")
    print(f"URL Encoding   : {url_encoded}")
    
    # URL Decoding
    url_decoded = urllib.parse.unquote(url_encoded)
    print(f"Geri Çözülmüş  : {url_decoded}")

if __name__ == "__main__":
    print("=== GÜN 2: Kodlama Aracı Testleri ===")
    
    # 1. Standart Metin Deneyi
    base64_islem("erdemarr")
    
    # 2. Türkçe Karakter Deneyi
    print("\n[!] Türkçe Karakter Deneyi Başlıyor...")
    turkce_metin = "Şifreli arama & test"
    base64_islem(turkce_metin)
    url_islem(turkce_metin)
    
    # 3. Parola Base64 Deneyi
    print("\n[!] Parola Base64 Güvenlik Testi...")
    parola = "GizliSifre123!"
    base64_islem(parola)