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