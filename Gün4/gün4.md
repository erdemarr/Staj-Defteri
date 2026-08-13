# Gün 4: Şifreleme, Anahtar Yönetimi ve Dijital İmza

## 1. Temel Kriptografik Kavramlar
* **Düz Metin (Plaintext):** Herhangi bir şifreleme işlemine tabi tutulmamış, üzerinde oynama yapılmamış okunabilir orijinal veridir.
* **Anahtar (Key):** Şifreleme ve çözme algoritmalarını yönlendiren, gizli tutulması gereken veri dizisidir. Modern kriptografinin temel prensibi olan Kerckhoffs Prensibi gereği; şifreleme algoritması herkese açık ve biliniyor olabilir, ancak sistemi güvenli kılan tek unsur anahtarın gizliliğidir.
* **Şifreli Metin (Ciphertext):** Düz metnin, anahtar ve algoritma yardımıyla yetkisiz kişilerin okuyamayacağı karmaşık ve anlamsız bir formata dönüştürülmüş halidir.

---

## 2. Simetrik Şifreleme ve Algoritmalar (DES, 3DES, AES)
Simetrik şifreleme, veriyi şifrelemek ve çökmek için aynı anahtarın kullanıldığı yöntemdir. İşlem hızı oldukça yüksektir ancak en büyük açmazı anahtarın karşı tarafa güvenli bir şekilde nasıl iletileceğidir (Anahtar Dağıtım Problemi).

* **DES (Data Encryption Standard):** 
  * *Özellikleri:* 56-bit anahtar uzunluğu kullanır. 
  * *Güvenlik Durumu:* Günümüz bilgisayarlarının işlem gücü karşısında çok kısa sürede kaba kuvvet (brute-force) saldırılarıyla kırılabildiği için artık kesinlikle güvensizdir.
* **3DES (Triple DES):** 
  * *Özellikleri:* DES'in yetersiz kalmasıyla geçiş dönemi çözümü olarak üretilmiştir. Aynı veriyi DES algoritmasından üç kez farklı anahtarlarla geçirir.
  * *Güvenlik ve Performans:* DES'e göre güvenliği artırsa da blok boyutu küçüktür ve donanım/yazılım üzerinde oldukça yavaştır, günümüzde terk edilmektedir.
* **AES (Advanced Encryption Standard):** 
  * *Özellikleri:* 128, 192 ve 256-bit anahtar uzunluklarını destekler. 
  * *Neden Standart Oldu?:* Hem matematiksel olarak kırılması imkansıza yakındır hem de hem donanım hem de yazılım tabanlı sistemlerde son derece yüksek performans ve hız sunar. Günümüzün küresel şifreleme standardıdır.

---

## 3. Adobe (2013) Sızıntısı ve ECB Modu Zafiyeti
* **Olayın Özeti:** 2013 yılında Adobe sistemlerine düzenlenen saldırıda milyonlarca kullanıcının parolası çalınmıştır. Parolalar düz metin olarak saklanmasa da simetrik şifrelemenin yanlış bir modu kullanıldığı için saldırganlar anahtara ihtiyaç duymadan parolaların büyük kısmını çözebilmiştir.
* **ECB (Electronic Codebook) Modu Nedir?:** Blok şifreleme algoritmalarında verinin eşit boyutlu bloklara bölünerek her bloğun aynı anahtarla birbirinden bağımsız ve aynı şekilde şifrelenmesidir.
* **Neden Zafiyet Yaratır?:** ECB modunda aynı düz metin bloğu (örneğin sık kullanılan kısa parolalar, boşluk karakterleri veya yaygın kelimeler), her şifrelendiğinde birebir aynı şifreli metin (ciphertext) bloğunu üretir. Saldırganlar anahtara sahip olmasalar bile şifreli metinler arasındaki bu kalıpları ve tekrarları analiz ederek parolaları kolaylıkla deşifre edebilmişlerdir. Bu durum, şifrelemede doğru algoritma kadar doğru çalışma modunun (CBC, GCM vb.) seçilmesinin de hayati olduğunu kanıtlamaktadır.

# Asimetrik Şifreleme, RSA, ECC ve PGP/GPG Notları

## 1. Asimetrik Şifrelemenin Temelleri
Asimetrik şifrelemede (açık anahtarlı kriptografi), simetrik şifrelemeden farklı olarak **iki farklı anahtar** kullanılır:
* **Açık Anahtar (Public Key):** Herkesle güvenle paylaşılabilen, mesajları şifrelemek veya imzaları doğrulamak için kullanılan anahtar.
* **Özel Anahtar (Private Key):** Yalnızca veri sahibinin bilgisayarında veya güvenli donanımında saklanan, şifre çözmek veya dijital imza atmak için kullanılan gizli anahtar.

---

## 2. RSA ve ECC Algoritmaları
* **RSA:** Güvenliğini, büyük iki asal sayının çarpımının orijinal asal çarpanlarına ayrılmasının matematiksel olarak çok zor olmasından (çarpanlara ayırma problemi) alır. Güvenli bir iletişim için anahtar uzunluklarının (örn. 2048-bit, 4096-bit) oldukça büyük olması gerekir.
* **ECC (Elliptic Curve Cryptography):** Eliptik eğriler üzerindeki cebirsel yapılara dayanır. 
  * **ECC Neden Daha Kısa Anahtarla Yetinebilir?:** ECC, RSA'ya kıyasla çok daha karmaşık ve dik bir matematiksel problem (eliptik eğri ayrık logaritma problemi) üzerine kuruludur. Bu sayede RSA ile aynı kriptografik güvenlik seviyesini (örneğin 3072-bit RSA güvenliğini) çok daha küçük anahtar boyutlarıyla (örneğin 256-bit ECC) sağlayabilir.
  * **Mobil Cihazlar İçin Önemi:** Daha kısa anahtar uzunluğu; işlemci gücünü, bellek alanını, depolama kapasitesini ve özellikle **batarya tüketimini** minimumda tuttuğu için akıllı telefonlar, tabletler ve IoT (Nesnelerin İnterneti) gibi kısıtlı kaynaklara sahip mobil cihazlar için hayati önem taşır.

---

## 3. Simetrik vs. Asimetrik (RSA / ECC) Karşılaştırma Tablosu

| Özellik | Simetrik Şifreleme (Örn. AES) | Asimetrik Şifreleme (RSA / ECC) |
| :--- | :--- | :--- |
| **Kaç Anahtar Kullanılıyor?** | Tek bir ortak anahtar (paylaşılan gizli anahtar) | İki anahtar (Açık anahtar ve Özel anahtar) |
| **Anahtar Nasıl Paylaşılıyor?** | Taraflar arasında güvenli bir kanal üzerinden önceden paylaşılmalı | Açık anahtar herkesle açıkça paylaşılabilir, özel anahtar paylaşılmaz |
| **Hız** | Çok hızlıdır (Büyük veri bloklarını şifrelemek için idealdir) | Yavaştır (Yoğun matematiksel ve cebirsel işlemler gerektirir) |
| **Tipik Kullanım Alanı** | Toplu veri şifreleme, disk şifreleme, TLS veri akışı | Anahtar değişimi (Key exchange), dijital imza, kimlik doğrulama |
| **Temel Sorunu Ne?** | Güvenli anahtar dağıtımı (Key distribution problem) | İşlem maliyeti yüksek ve yavaştır |

---

## 4. PGP ve GPG Kavramları
* **PGP (Pretty Good Privacy):** E-postaları, dosyaları ve hassas verileri şifrelemek, şifresini çözmek ve imzalamak için geliştirilmiş popüler bir kriptografik programdır.
* **GPG (GNU Privacy Guard):** PGP standardının (`OpenPGP`) tamamen açık kaynak kodlu ve özgür bir yazılım olan güncel implementasyonudur. Günümüzde özellikle geliştiriciler arasında kod imzalamada ve güvenli e-posta iletişiminde yaygın olarak kullanılır.