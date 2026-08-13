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

# Dijital İmza ve Yön Analizi

## 1. Dijital İmzanın Amacı
Dijital imza, sanılanın aksine veriyi gizlemek veya başkalarından saklamak için kullanılmaz. Temel amacı şu üç güvenlik unsurunu sağlamaktır:
* **Kimlik Doğrulama (Authentication):** Mesajın gerçekten iddia edilen kişi tarafından gönderildiğini kanıtlar.
* **Veri Bütünlüğü (Data Integrity):** Mesajın iletim sırasında tek bir karakter bile değiştirilmediğini garanti eder.
* **İnkâr Edememe (Non-repudiation):** Gönderenin, mesajı kendisinin göndermediğini sonradan iddia etmesini engeller.

---

## 2. Dijital İmza Adım Adım İşleyiş Akışı
Dijital imza mekanizması, dün incelediğimiz veri bütünlüğü (hashing) akışının üzerine inşa edilir. İşleyiş aşamaları şunlardır:

1. **Özetleme (Hashing):** Gönderen taraf, ileteceği uzun mesajın/dosyanın öncelikle bir hash algoritması (`SHA-256` vb.) ile benzersiz ve sabit uzunluktaki özetini çıkartır.
2. **Özel Anahtar ile İmzalama:** Gönderen, elde ettiği bu hash özetini kendi özel anahtarı (private key) ile şifreler. Ortaya çıkan bu şifreli özet değer "dijital imza" olur.
3. **Gönderim:** Gönderen, orijinal mesajı (düz metin olarak) ve bu oluşturduğu dijital imzayı karşı tarafa iletir.
4. **Alıcının Doğrulaması:**
   * Alıcı gelen orijinal mesajın tekrar hash özetini çıkartır.
   * Aynı zamanda mesajın yanında gelen dijital imzayı, gönderenin açık anahtarı (public key) ile çözer.
   * İki özet değeri yan yana koyup karşılaştırır. Değerler birebir aynıysa imza geçerlidir; mesaj hem orijinaldir hem de doğru kişiden gelmiştir.

> **Önemli İpucu:** Kriptografik işlemler (asimetrik şifreleme) matematiksel olarak yavaş olduğundan, tüm mesajı özel anahtarla şifrelemek yerine yalnızca mesajın kısa hash özetini imzalamak sistemi binlerce kat hızlandırır. Yani dijital imza, hashing mekanizması olmadan çalışamaz.

---

## 3. Soru Cevabı: Yön Neden Ters? (Şifreleme vs. Dijital İmza)

* **Asimetrik Şifrelemede Yön (Açık Anahtar -> Özel Anahtar):**
  * *Amaç:* **Gizliliktir.**
  * *Mantık:* Herkes alıcının açık anahtarıyla veriyi şifreleyebilir; ancak bu veriyi yalnızca o açık anahtara karşılık gelen gizli özel anahtarın sahibi çözebilir. Hedef, mesajı sadece alıcının okuyabilmesini sağlamaktır.

* **Dijital İmzada Yön (Özel Anahtar -> Açık Anahtar):**
  * *Amaç:* Sahiplik, Kimlik Doğrulama ve İnkar Edememedir.
  * *Mantık:* Özel anahtar yalnızca tek bir kişide bulunur. Bu yüzden veriyi (hash özetini) sadece o özel anahtarın sahibi özel anahtarıyla imzalayabilir. Açık anahtar herkese açık olduğu için, işlemi açık anahtarla doğrulayan herkes bu imzanın yalnızca o özel anahtar sahibinden çıkabileceğini matematiksel olarak teyit eder.

Özetle; Gizlilik istediğimizde hedef kişinin açık anahtarını, Aidiyet / Kimlik Kanıtı vermek istediğimizde ise kendi özel anahtarımızı kullanırız. Yönün ters olma nedeni tamamen hedeflenen güvenlik kriterinin farklılığıdır.

# Anahtar Değişimi, TLS ve Perfect Forward Secrecy Notları

## 1. Diffie-Hellman Anahtar Değişimi Protokolü
* **Temel Problem:** Sabah sorduğumuz soruya dayanarak; iki taraf önceden ellerinde hiçbir ortak gizli anahtar bulunmasa bile, aralarındaki güvensiz (dinlenebilir) bir ağ üzerinden güvenli bir şekilde aynı ortak gizli anahtara nasıl ulaşabilir?
* **Çalışma Prensibi:** Diffie-Hellman protokolü, tarafların kendi yerel gizli (private) sayılarını asla karşı tarafa göndermeden, bu gizli sayıları matematiksel işlemlerden (modüler aritmetik) geçirerek ürettikleri açık (public) değerleri birbiriyle değiş tokuş etmesine dayanır.
* **Ortak Anahtara Ulaşma ve Güvenlik:** Taraflar karşı taraftan gelen açık değeri kendi gizli sayılarıyla birleştirdiklerinde matematiksel olarak aynı ortak gizli anahtarı elde ederler. Buradaki en kritik nokta, ortak gizli anahtarın ağ üzerinden asla fiziksel olarak geçmemesidir. Ağı dinleyen (wiretapping yapan) bir üçüncü taraf sadece açık değerleri görebilir; ancak matrisin içerisindeki ayrık logaritma probleminin hesaplama zorluğu sayesinde bu açık değerlerden ortak gizli anahtarı geri hesaplayamaz.

---

## 2. TLS (Transport Layer Security) Mimarisi: İki Dünyanın Birleşimi
TLS protokolü, güvenli ve hızlı bir iletişim kurabilmek için hem simetrik hem de asimetrik şifrelemeyi birlikte kullanır:

* **Asimetrik Şifrelemenin Yeri (El Sıkışma / Handshake Aşaması):** Bağlantının hemen başında kimlik doğrulama yapmak ve güvenli bir şekilde oturum anahtarı oluşturmak (Diffie-Hellman ile) için asimetrik şifreleme kullanılır. Güvenlidir ancak matematiksel olarak yavaştır.
* **Simetrik Şifrelemenin Yeri (Veri Transferi Aşaması):** Taraflar arasında güvenli anahtar alışverişi yapıldıktan sonra (`Handshake` tamamlandığında), iletişimin geri kalanında devasa veri akışını yüksek hızda şifrelemek için simetrik şifreleme (örn. AES) devreye girer.
* **Bunun Sebebi Nedir?:** Asimetrik şifreleme güvenli anahtar değişimi sağlar ancak tüm veri akışında kullanılmayacak kadar yavaştır. Simetrik şifreleme ise inanılmaz hızlıdır ancak tek başına anahtar dağıtım sorununa sahiptir. TLS, asimetrik şifrelemenin güvenliğiyle simetrik şifrelemenin hızını harmanlayarak en ideal çözümü sunar.

---

## 3. Perfect Forward Secrecy (PFS - Kusursuz İleri Gizlilik)
* **Tanımı ve Mantığı:** PFS, her yeni oturum (connection) veya bağlantı için tamamen bağımsız, geçici anahtarların üretilmesini sağlayan bir güvenlik mimarisidir.
* **Geçmiş Trafiğin Korunması:** Sunucunun kalıcı ve uzun süreli özel anahtarı gelecekte herhangi bir sızıntı sonucu ele geçirilse bile, geçmişte kaydedilmiş olan şifreli ağ trafiği çözülemez. Çünkü her oturumun anahtarı o ana özel olarak türetilmiş ve sonradan yok edilmiştir; sunucunun ana anahtarıyla doğrudan matematiksel bir bağı yoktur.

# Öğleden Sonra: Pratik

## RSA Anahtar Çifti

2048 bit RSA anahtar çifti oluşturuldu:

- `private_key.pem` → Özel anahtar
- `public_key.pem` → Açık anahtar

Açık anahtar, özel anahtardan türetildi ve anahtar bilgileri OpenSSL ile incelendi.

## İmzalama ve Doğrulama

`mesaj.txt` dosyası SHA-256 kullanılarak özel anahtar ile imzalandı.

Orijinal dosyanın açık anahtar ile doğrulanması:

```text
Verified OK
```

Dosyada yalnızca bir karakter değiştirildikten sonra aynı imza ile doğrulama tekrarlandı:

```text
Verification failure
```

Bu deney, dosyanın tek bir karakterinin değiştirilmesinin bile dijital imzanın doğrulanmasını bozduğunu ve dijital imzanın **veri bütünlüğünü** sağladığını gösterdi.

## HTTPS Sertifikası İncelemesi

Google'a ait HTTPS sertifikası OpenSSL ile incelendi.

| Alan | İncelenen değer |
|---|---|
| Subject | `CN=*.google.com` |
| Issuer | `Google Trust Services, CN=WE2` |
| Geçerlilik | 20.07.2026 – 12.10.2026 |
| İmza algoritması | `ECDSA with SHA-256` |
| Public Key | EC, P-256, 256 bit |
| Kullanım | TLS Web Server Authentication |
| CA | `FALSE` |

**Yorum:** Sertifika, Google alan adının kimliğini doğrulamak için kullanılır. Google Trust Services tarafından imzalanmış olup bir sertifika zinciri üzerinden güven oluşturur. P-256 eliptik eğri ve ECDSA/SHA-256 kullanımı, modern TLS sertifikalarında kullanılan kriptografik yapıların incelenmesini sağladı.

# Haftanın Karşılaştırması ve Dönüşüm Analizi

## 1. Aynı Metin Üzerindeki Üç Dönüşümün Çıktıları
Girdi Metni: `"Erdem"`

* **1. Kodlama (Base64 Encoding):**
  * *Çıktı:* `RXJkZW0=`
  * *Açıklama:* Veriyi sadece okunabilir/taşınabilir başka bir formata dönüştürür.
* **2. Hashing (SHA-256):**
  * *Çıktı:* `3b2b81404c0d0c3547f6cfdd55a1599320e4de3a52bb4a80604b3a4a75367878`
  * *Açıklama:* Verinin sabit uzunlukta benzersiz parmak izini (özetini) çıkarır.
* **3. Simetrik Şifreleme (AES / Fernet):**
  * *Çıktı:* `gAAAAAB... (Rastgele IV ve şifreli bayt dizisi)`
  * *Açıklama:* Veriyi anahtar yardımıyla gizli ve okunamaz bir formata getirir.

---

## 2. Soruların Cevapları ve Analiz Tablosu

| Dönüşüm Türü | 1. Geri Döndürülebilir mi? | 2. Anahtar Gerektiriyor mu? | 3. Çıktı Uzunluğu Girdiden Bağımsız mı? | 4. Aynı Girdide Aynı Çıktıyı Üretir mi? |
| :--- | :--- | :--- | :--- | :--- |
| **Kodlama (Base64)** | **Evet** (Kolayca çözülür) | **Hayır** | **Hayır** (Girdi uzadıkça çıktı da uzar) | **Evet** (Deterministiktir) |
| **Hashing (SHA-256)** | **Hayır** (Tek yönlüdür, çözülemez) | **Hayır** | **Evet** (Girdi boyutu ne olursa olsun çıktı daima 256-bit / 64 karakterdir) | **Evet** (Deterministiktir) |
| **Simetrik Şifreleme (AES)** | **Evet** (Anahtar ile çözülür) | **Evet** (Gizli anahtar şarttır) | **Hayır** (Girdi boyutuna ve padding/IV yapısına göre değişir) | **Hayır** (Çoğu blok/mod yapısında rastgele IV nedeniyle her seferinde farklı ciphertext üretir) |

---

## 3. Genel Özet ve Değerlendirme
* **Kodlama:** Güvenlik amacı taşınmaz, veri taşıma ve uyumluluk içindir.
* **Hashing:** Bütünlük ve parmak izi içindir; geri döndürülemez ve sabittir.
* **Şifreleme:** Gizlilik içindir; anahtar olmadan okunamaz, ancak doğru anahtarla tamamen geri döndürülebilirdir.

# Ek Okuma: Şifreleme Doğru, Uygulama Yanlış - Heartbleed (2014) Örneği

* **Zafiyetin Doğası:** Heartbleed, OpenSSL kütüphanesinin TLS "Heartbeat" (kalp atışı) uzantısında ortaya çıkan kritik bir bellek okuma (`buffer over-read`) hatasıdır; kesinlikle RSA, AES veya SHA gibi şifreleme algoritmalarının matematiğinden kaynaklanan bir zafiyet değildir.
* **Saldırganın Veriyi Alışı:** Sunucuya gönderilen kalp atışı isteklerinde, karşı taraftan geri istenen verinin uzunluğu ile gerçek veri boyutu arasındaki sınır denetimi (`bounds checking`) yazılımsal olarak yapılmamıştır. Saldırgan, gönderdiği istekte verinin boyutunu olduğundan çok daha büyük beyan edip içeriğini küçük tutarak, sunucunun RAM belleğinde o an açık bulunan hassas verileri (özel anahtarlar, kullanıcı parolaları ve oturum çerezleri) dışarı sızdırmasını tetiklemiştir.
* **Ana Ders:** Güçlü ve doğru şifreleme algoritmaları kullansanız dahi, yazılımın uygulama kodundaki en ufak bir girdi işleme veya sınır denetimi hatası tüm sistemi savunmasız bırakabilir.