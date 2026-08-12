# Hashing, Veri Bütünlüğü ve Kriptografik Özellikler

## 1. Hashing Nedir?
Hashing (Özetleme), değişken boyutlu herhangi bir girdiyi matematiksel bir fonksiyondan (`hash function`) geçirerek sabit uzunlukta ve benzersiz bir değere (`hash digest` / `özet değer`) dönüştürme işlemidir. Hashing'in temel amacı veriyi gizlemek değil, **verinin değişmediğini (bütünlüğünü) kanıtlamaktır**.

---

## 2. Kriptografik Açıdan Güvenli Bir Hash Fonksiyonunun 3 Temel Özelliği

Bir hash algoritmasının kriptografik olarak güvenli kabul edilebilmesi için şu üç temel şartı sağlaması gerekir:

1. **Deterministik Olma (Aynı Girdinin Her Zaman Aynı Çıktıyı Üretmesi):** Aynı girdi verisi, fonksiyon her çalıştırıldığında kesinlikle birebir aynı hash çıktısını üretmelidir.
2. **Tek Yönlülük / Tersine Çevrilemezlik (Pre-image Resistance):** Elde edilen hash özetinden yola çıkarak orijinal girdiye geri dönmek matematiksel olarak imkansız olmalıdır. Hashing bir kodlama (encoding) veya şifreleme (encryption) değildir; geri döndürülemez.
3. **Çakışmaya Direnç (Collision Resistance):** Farklı iki girdinin tamamen aynı hash çıktısını üretmesi (çakışma / collision) ihtimali pratikte sıfıra yakın olmalıdır.
---

## 3. Çığ Etkisi (Avalanche Effect) Nedir?
Çığ etkisi, kaliteli bir hash fonksiyonunun en belirgin özelliğidir. Girdi verisinde yapılan **en ufak bir değişiklik** (örneğin tek bir karakterin büyük/küçük harf yapılması veya sonuna bir boşluk eklenmesi), çıkan hash özetinin **tamamen ve öngörülemez bir şekilde değişmesine** yol açar. Çıktıdaki bitlerin yaklaşık %50'si değişir. Bu etki, saldırganların deneme-yanılma (brute-force) yoluyla girdiyi tahmin etmesini engeller.

---

## 4. Yaygın Hash Algoritmaları ve Güvenlik Durumları

* **MD5 (Message Digest 5):** 
  * **Çıktı Uzunluğu:** 128-bit (16 bayt)
  * **Güvenlik Durumu:** Günümüzde **güvenli değildir**. Ciddi çakışma zafiyetleri barındırmaktadır (örn. Flame saldırısı). Sadece dosya bütünlüğü gibi kritik olmayan kontrol amaçlı eskilerden kalıntı olarak görülür.
* **SHA-1 (Secure Hash Algorithm 1):** 
  * **Çıktı Uzunluğu:** 160-bit (20 bayt)
  * **Güvenlik Durumu:** Güvenliğini yitirmiştir. Pratik çakışma saldırıları (örn. SHAttered projesi) ile kırıldığı için kriptografik amaçlarla kullanımı yasaklanmıştır.
* **SHA-256 (Secure Hash Algorithm 2 ailesi):** 
  * **Çıktı Uzunluğu:** 256-bit (32 bayt)
  * **Güvenlik Durumu:** Günümüzde endüstri standardı olan, güvenli ve yaygın olarak kullanılan güçlü bir algoritmadır.


# Pratik: Çığ Etkisi ve Dosya Bütünlüğü Deney Sonuçları ve Analizi

## 1. Terminal Çalıştırma Çıktısı

Geliştirdiğimiz Python aracı (`hashing_tool.py`) üzerinde gerçekleştirilen hashing, çığ etkisi ve dosya bütünlüğü testlerinin terminal çıktıları aşağıdadır:

```text
=== GÜN 2 ve GÜN 3: Kodlama ve Hashing Araç Testleri ===

[!] Gün 3 Hashing ve Çığ Etkisi Testleri Başlıyor...

--- Hashing ve Çığ Etkisi Deneyleri ---
Orijinal Girdi : StajGunUclusu
MD5    (128 bit) : 810b013bf3633e6aa87cc30795d23776
SHA-1  (160 bit): 36dee660f39a231e2006f22103bc02d87950a3c8
SHA-256(256 bit): fc98e8e4da2ddfb5e44eea302d58c7dad0b47da9b83f07a5db47f55124016d0a

--- Hashing ve Çığ Etkisi Deneyleri ---
Orijinal Girdi : stajGunUclusu
MD5    (128 bit) : 516aede44bbbb4269f22f04bfa4261f3
SHA-1  (160 bit): e907a6e96b1aab98cbfa8e5442ab3d39a96a53bf
SHA-256(256 bit): d54ee246dedda7d5fde056cd30aa6c0d3e39b3ae75b34545c818aba3c223af91

--- Dosya Bütünlüğü (Data Integrity) Deneyi ---
1. Durum (Orijinal Dosya) SHA-256 : 1f1d968b68e125e91f606048567f0813c3c65fa34dad2528bcecd99179df55e9
2. Durum (Değişmiş Dosya)  SHA-256 : b10ff9fd23a9bf61822d585698b2c1e3b521bef880d3252c591e7f400d16cedd
[!] Gözlem: Dosya içeriğindeki tek karakterlik değişim hash değerini tamamen değiştirdi!
```

---

## 2. Teknik Analiz ve Değerlendirme

* **Determinizm ve Çığ Etkisi Birlikteliği:** Yapılan testlerde görüldüğü üzere, aynı metin (`StajGunUclusu`) her defasında birebir aynı MD5, SHA-1 ve SHA-256 çıktılarını üretmiştir (Determinizm). Buna karşın, girdide yapılan sadece tek karakterlik ufak bir değişim (`Staj` -> `staj`), çıktıların tamamen farklılaşmasını sağlamıştır (Çığ Etkisi). Bu iki zıt gibi görünen özellik, güvenli hash fonksiyonlarının temel yapı taşını oluşturur.
* **Kriptografik Güvenilirlik Boyutu:** Terminal çıktısında yer alan MD5 ve SHA-1 algoritmalarının, SHA-256'ya kıyasla daha kısa özetler (sırasıyla 32 ve 40 karakter) ürettiği görülmektedir. Ancak modern siber güvenlik standartlarında MD5 ve SHA-1'in çakışma zafiyetleri barındırdığı için güvenli olmadığını ve kritik sistemlerde kesinlikle kullanılmaması gerektiğini bir kez daha teyit etmiş oluyoruz.
* **Veri Bütünlüğü ve Savunma Mekanizması:** Dosya bütünlüğü deneyinde elde edilen hash değişimleri, hash özetlerinin veriyi şifrelemediğini, aksine verinin parmak izini çıkardığını net bir şekilde göstermektedir. Dosya içeriğindeki tek bir baytlık veya karakterlik sapma, özet değerin tamamen değişmesine yol açarak sistemlerin veya kullanıcıların yoldaki bozulmaları ya da yetkisiz müdahaleleri anında tespit etmesini sağlar.

# Parola Saklama ve Güvenlik Analizi

## 1. Parolalar Neden Düz Metin Olarak Saklanmaz?
* **Güvenlik Riski ve Veri Sızıntısı:** Parolaların veritabanında düz metin (plaintext) olarak saklanması, yaşanabilecek olası bir sızıntı (data breach) durumunda kullanıcı hesaplarının doğrudan ele geçirilmesine yol açar. Saldırganlar çalınan veritabanındaki tüm şifreleri anında okuyabilir.
* **Base64 Yanılgısı ile Bağlantısı:** Dün incelediğimiz Base64 bir şifreleme veya hashleme yöntemi değil, yalnızca bir kodlama (encoding) türüdür. Nasıl ki Base64 ile kodlanmış bir metin tek bir komutla anında geri çözülebiliyorsa, parolaları Base64 ile saklamak da düz metin saklamakla eşdeğerdir ve hiçbir güvenlik sağlamaz.

---

## 2. Salt (Tuzlama) Nedir?
* **Tanımı ve Amacı:** Salt, parola hashlenmeden önce parolanın sonuna veya başına eklenen **rastgele ve benzersiz bir veri dizisidir**. 
* **Aynı Parolaların Farklı Hash Üretmesi:** Sistemde iki farklı kullanıcı aynı zayıf parolayı (örneğin `123456`) seçse bile, her kullanıcıya atanan rastgele salt değeri farklı olacağı için veritabanında saklanan hash değerleri tamamen birbirinden farklı olur.
* **Salt Neden Gizli Tutulmaz?:** Salt değerinin gizli kalmasına gerek yoktur; çünkü salt, saldırganın önceden hesaplanmış hazır tablolarla (`Rainbow Table`) saldırmasını engellemek için tasarlanmıştır. Her kullanıcı için benzersiz bir salt kullanıldığında, saldırganın her bir kullanıcı için ayrı ayrı tablo üretmesi gerekir ki bu da hesaplama maliyetini imkansıza yaklaştırır.

---

## 3. Rainbow Table (Gökkuşağı Tablosu) Nedir?
* **Çalışma Mantığı:** Rainbow table, yaygın olarak kullanılan parolaların düz metin halleri ile bunların hash değerlerinin önceden hesaplanıp devasa dosyalar halinde eşleştirildiği önbellek tablolarıdır. 
* **Parola Kırmayı Hızlandırma:** Saldırganlar çalınan hash'leri tek tek deneme-yanılma ile çözmek yerine bu tablolarda aratarak saniyeler içinde orijinal parolaya ulaşırlar.
* **Salt'ın Etkisi:** Sisteme salt eklendiğinde, saldırganların önceden hazırladığı standart rainbow table'lar tamamen işlevsiz hale gelir; çünkü tablodaki hash değerleri salt eklenmiş versiyonlarla eşleşmez.

---

## 4. Hashcat Nedir?
* **Tanımı ve İşlevi:** Hashcat, dünya çapındaki en güçlü ve popüler parola kurtarma ve kırma aracıdır. Çalınmış hash değerlerini kırmak, zayıf parolaları tespit etmek ve brute-force (kaba kuvvet) / sözlük saldırıları yürütmek için kullanılır.
* **Neden Ekran Kartı (GPU) Kullanır?:** Parola hash'lerini denemek aşırı yüksek matematiksel işlem gücü gerektirir. GPU'lar (Grafik İşlem Birimleri), paralel işlem mimarileri sayesinde aynı anda binlerce hesaplamayı CPU'lara göre çok daha hızlı yapabildikleri için Hashcat bu donanımı tercih eder.
* **Savunma Boyutu:** Bu araç yalnızca saldırganlar tarafından değil, güvenlik ekipleri ve yöneticiler tarafından şirket içi kullanıcıların zayıf parola politikalarını denetlemek ve riskleri önceden tespit etmek amacıyla da kullanılır.

# Gerçek Olaylar ve Kriptografik Zafiyet Analizleri

## 1. LinkedIn (2012) Veri Sızıntısı
* **Parolaların Saklanma Yöntemi:** Sızıntı sırasında LinkedIn, milyonlarca kullanıcının parolasını dönemin yaygın ancak yetersiz bir uygulaması olan salt (tuzlama) kullanılmadan ve zayıf bir algoritma ile (düz SHA-1) saklıyordu.
* **Kriptografik Açıdan Asıl Ders ve Eksik:** En temel eksiklik, her kullanıcı için benzersiz bir salt kullanılmamış olması ve gün aşırı rainbow table saldırılarına karşı korumasız bırakılmasıdır. Salt kullanılmadığı için aynı parolayı kullanan milyonlarca hesabın hash değeri sistemde aynı görünmüş ve saldırganlar çalınan hash özetlerini önceden hesaplanmış tablolar veya hızlı kırma araçlarıyla saniyeler içinde çözerek düz metin haline getirebilmiştir.

---

## 2. Flame (2012) Zararlı Yazılımı ve MD5 Çakışması
* **Olayın Özeti:** Flame, son derece gelişmiş bir casus yazılımdır. Saldırganlar, Microsoft'un Update sunucularından gelen güncellemeleri yasal ve güvenli sanmasını sağlamak için MD5 algoritmasındaki çakışma zafiyetini istismar etmişlerdir.
* **Teorik Zayıflığın Pratik Sonucu:** MD5'in çakışmaya direncinin kırılmış olması, saldırganların zararlı bir kod dosyası ile yasal bir sertifikanın aynı MD5 hash değerini üretmesini sağlamasına yol açmıştır. Bu sayede sahte bir kod imzalama sertifikası üretilmiş, işletim sistemi yazılımın güvenilir olduğuna kandırılarak zararlı yazılım resmi bir güncelleme gibi sisteme sızdırılmıştır.

---

## 3. SHAttered (2017) Saldırısı ve SHA-1'in Kırılması
* **Olayın Özeti:** CWI Amsterdam ve Google araştırmacılarının ortak çalışmasıyla SHA-1 algoritmasına karşı ilk pratik çakışma (collision) saldırısı gerçekleştirilmiştir.
* **Anlamı ve Önemi:** İki farklı PDF dosyasının birebir aynı SHA-1 hash özetini üretmesi sağlanmıştır. Bu durum, teorik olarak "imkansız" denilen çakışma direncinin SHA-1 için pratikte aşıldığını kanıtlamıştır. Bir saldırganın iyi niyetli bir belgenin içeriğini değiştirip kötü niyetli başka bir belgeyle aynı hash değerine sahip hale getirmesi, imza ve onay mekanizmalarının güvenliğini tamamen ortadan kaldırmaktadır.

---

## 4. Soru Cevabı: Bir Hash Algoritmasının Çakışmaya Direncinin Kırılması Pratikte Neye Yol Açar?
Bir hash algoritmasının çakışmaya direncinin kırılması, aynı hash değerini veren iki farklı veri (dosya, kod veya belge) üretilebilmesi anlamına gelir. Şu büyük riskleri doğurur:
1. **Güven ve İmza Mekanizmalarının Çökmesi:** Dijital imza ve kod imzalama süreçlerinde dosyaların bütünlüğünü kanıtlayan hash değerleri güvenliğini yitirir; saldırganlar zararlı yazılımları güvenilir yazılım gibi göstererek sistemlere entegre edebilir.
2. **Sahtecilik ve Doğrulama Açıkları:** Resmi belgeler, yazılım güncellemeleri veya kaynak kodlar üzerinde yetkisiz değişiklikler yapılmasına rağmen sistemin veya kullanıcıların bunu "değişmemiş" (orijinal) olarak algılamasına ve ağır güvenlik ihlallerine yol açar.

# Günün Kavramsal Kapanışı: Veri Bütünlüğü (Data Integrity) ve Hashing'in Rolü

## 1. Veri Bütünlüğü Nedir ve Nasıl Sağlanır?
Veri bütünlüğü (data integrity), bir verinin iletim (ağ üzerinden aktarım) veya saklama (disk üzerinde depolama) süreçleri boyunca yetkisiz veya kazara hiçbir değişikliğe uğramadığının, bozulmadığının ve eksiksiz olduğunun garanti edilmesidir. Bu güvence, modern kriptografide temel olarak hashing mekanizmaları aracılığıyla sağlanır.

---

## 2. Veri Bütünlüğü Doğrulama Akışı
Gönderen ile alıcı arasında veri bütünlüğünün nasıl korunduğunu ve doğrulandığını şu 4 adımlı akışla özetleyebiliriz:

1. **Özetleme (Hashing):** Gönderen taraf, ileteceği orijinal veriyi (mesajı veya dosyayı) bir hash fonksiyonundan (`SHA-256` vb.) geçirerek sabit uzunlukta benzersiz bir özet değer (`hash digest`) elde eder.
2. **İletim Süreci:** Gönderen hem orijinal veriyi hem de elde ettiği bu hash özetini karşı tarafa (alıcıya) iletir. (Veri yolda şifrelenmemiş olabilir, çünkü buradaki amaç gizlilik değil bütünlüktür).
3. **Alıcı Tarafında Yeniden Hesaplama:** Alıcı veriyi teslim aldığında, elindeki orijinal veriyi aynı hash algoritmasından geçirerek kendi yerel özet değerini hesaplar.
4. **Karşılaştırma (Doğrulama):** Alıcı, hesapladığı yeni hash değerini gönderenin ilettiği hash değeri ile karşılaştırır. 
   * Eğer iki değer birebir aynı çıkarsa, verinin yolda hiçbir manipülasyona veya bozulmaya uğramadığı kesin olarak doğrulanmış olur (Veri Bütünlüğü Sağlanmıştır).
   * Eğer değerler farklı çıkarsa, verinin iletim sırasında değiştirildiği veya bozulduğu anlaşılır.