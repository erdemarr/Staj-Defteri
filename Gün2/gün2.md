# Kodlama, Şifreleme, Özetleme ve Karartma Karşılaştırma Tablosu

| Kavram | Temel Amacı Nedir? | Anahtar Gerektirir mi? | Geri Döndürülebilir mi? | Güvenlik Sağlar mı? |
| :--- | :--- | :--- | :--- | :--- |
| **Encoding (Kodlama)** | Verinin farklı sistemler arasında veri kaybı olmadan taşınması ve işlenmesi. | Hayır | Evet (Algoritma bilinmesi yeterlidir). | Hayır. Gizlilik veya koruma sağlamaz. |
| **Encryption (Şifreleme)** | Verinin yetkisiz kişilerden gizlenmesi ve gizliliğin (confidentiality) korunması. | Evet (Kriptografik anahtar gereklidir). | Evet (Yalnızca doğru anahtar/parola ile). | Evet. Doğru uygulandığında yüksek güvenlik sağlar. |
| **Hashing (Özetleme)** | Verinin bütünlüğünün doğrulanması ve parolanın güvenli saklanması (özet değer üretme). | Hayır | Hayır (Tek yönlü bir matematiksel fonksiyondur). | Kısmen. Veri bütünlüğü ve parola doğrulamada güvenlik sağlar. |
| **Obfuscation (Karartma)** | Kaynak kodun veya verinin insan tarafından okunmasını ve tersine mühendisliği zorlaştırmak. | Hayır / Kısmen | Evet (Analiz edilerek veya çözücü araçlarla). | Hayır. Yalnızca bir engeldir, gerçek bir güvenlik katmanı değildir. |

---

# Kodlama Türleri ve Özgün Örnekler

## 1. Base64 Encoding
* **Amacı ve Kullanım Alanı:** İkili (binary) verileri (resim, dosya, şifrelenmiş baytlar) sadece metin karakterlerini destekleyen güvenli ortamlarda taşımaktır. A-Z, a-z, 0-9, `+` ve `/` karakterlerini kullanır.
* **Nerelerde Karşılaşılır?:** 
  * **JWT (JSON Web Token):** Token yapısının başlık (header) ve payload kısımları Base64Url formatında kodlanarak taşınır.
  * **E-posta Ekleri (MIME):** MIME protokolü üzerinden dosya ekleri metne dönüştürülerek gönderilir.
  * **API / HTML:** `data:image/png;base64,...` formatıyla küçük görsellerin doğrudan HTML içine gömülmesinde kullanılır.
* **Özgün Örnek:**
  * Girdi (Plaintext): `erdemarr`
  * Base64 Çıktısı: `ZXJkZW1hcnI=`

---

## 2. URL Encoding (Percent-Encoding)
* **Amacı ve Kullanım Alanı:** URL (Uniform Resource Locator) içinde yapısal olarak özel anlam taşıyan veya çakışmaya yol açabilecek karakterlerin (`?`, `=`, `&`, `/`, boşluk vb.) güvenle iletilmesini sağlar. Özel karakterler `%` işareti ve ardından gelen iki haneli Hex değer ile değiştirilir.
* **Türkçe Karakter Durumu:** Türkçe karakterler URL içinde doğrudan gönderilemez; UTF-8 bayt dizilimine dönüştürülüp her bayt percent-encoding formatına çevrilir. Örneğin, `ş` harfi UTF-8'de iki bayttır (`C5` ve `9F`) ve URL içinde `%C5%9F` şeklinde yer alır. Boşluk karakteri ise `+` veya `%20` olur.
* **Özgün Örnek:**
  * Girdi: `arama = erdem arar?şifre=1`
  * URL Encoding Çıktısı: `arama+%3D+erdem+arar%3F%C5%9Fifre%3D1`

---

## 3. Hex Encoding (Base16)
* **Amacı ve Kullanım Alanı:** Her bir baytın (8-bit) iki adet on altılık karakterle (`0-9`, `A-F`) ifade edilmesidir. Verinin ham bayt seviyesinde incelenmesini kolaylaştırır.
* **Nerelerde Karşılaşılır?:** 
  * **Hata Ayıklama (Debugging) & Bellek İncelemesi:** RAM dökümlerinde (memory dump) veya Hex editörlerinde ham veri analizinde.
  * **Kriptografi:** SHA-256 gibi hash özetlerinin okunabilir metin formatında gösterilmesinde (örn: `e3b0c44298fc1c14...`).
* **Özgün Örnek:**
  * Girdi (Metin): `ET`
  * Bayt Karşılığı (ASCII): `69` (E), `84` (T)
  * Hex Çıktısı: `4554`

---

## 4. Binary Encoding
* **Amacı ve Kullanım Alanı:** Verinin bilgisayarın en temel anlama birimi olan `0` ve `1` (ikili sistem) bit dizileri şeklinde temsil edilmesidir. Donanım seviyesindeki veri iletimi ve mantıksal işlemleri anlamak için kullanılır.
* **Özgün Örnek:**
  * Girdi (Karakter): `A`
  * ASCII Karşılığı: `65`
  * Binary Çıktısı: `01000001`

---

## 5. ASCII ve UTF-8 Karakter Kodlamaları
* **ASCII (American Standard Code for Information Interchange):** 7-bitlik bir standarttır ve toplamda 128 karakteri (İngilizce alfabe, rakamlar ve temel noktalama işaretleri) destekler. Türkçe karakterleri (ç, ğ, ı, ö, ş, ü) desteklemez.
* **UTF-8:** Unicode karakter setini bayt tabanlı olarak kodlayan esnek bir standarttır. 1 ila 4 bayt arasında değişen uzunluklar kullanarak dünyadaki neredeyse tüm dillerin karakterlerini destekler hale gelmiştir.
* **Türkçe Karakter Sorununun Kaynağı:** Eski sistemlerin veya veritabanlarının yalnızca ASCII veya ISO-8859-1 gibi dar kapsamlı karakter setlerini beklediği durumlarda, UTF-8 ile kodlanmış Türkçe karakterler (birden fazla bayt kapladıkları için) doğru yorumlanamaz ve ekranda bozuk karakterler (`Ã§` gibi) olarak görünür.

---

# Obfuscation (Karartma) Analizi ve Sınırları

## 1. Obfuscation Neden Güçlü Bir Güvenlik Kontrolü Sayılmaz?
Obfuscation, bir koruma mekanizmasından ziyade bir **caydırıcılık ve zorlaştırma** (security through obscurity) yöntemidir. Güçlü bir güvenlik kontrolü sayılmamasının temel nedenleri şunlardır:
* **Matematiksel Garanti Yoktur:** Şifreleme (Encryption) veriyi korumak için kırılması zor, kanıtlanmış matematiksel algoritmalar kullanırken; obfuscation yalnızca kodu veya mantığı karmaşıklaştırır (değişken isimlerini değiştirmek, gereksiz döngüler eklemek vb.).
* **Makinenin Çalıştırma Zorunluluğu:** Bilgisayarın veya tarayıcının o kodu anlayıp çalıştırabilmesi için mantığın hâlâ orada olması gerekir. Makine kodu çözebiliyorsa, mantığı tersine mühendislikle inceleyen bir insan veya otomasyon aracı da zamanla çözebilir.
* **Otomatik Araçlar:** Deobfuscation (karartmayı çözme) araçları ve yapay zeka destekli analiz yazılımları, karmaşıklaştırılmış yapıları hızla standart ve okunabilir hâle getirebilir.

---

## 2. Şifreleme (Encryption) ile Obfuscation Arasındaki Farklar

| Özellik | Encryption (Şifreleme) | Obfuscation (Karartma) |
| :--- | :--- | :--- |
| **Temel Amaç** | Verinin gizliliğini ve bütünlüğünü matematiksel olarak korumak. | Kaynak kodun okunabilirliğini azaltarak tersine mühendisliği zorlaştırmak. |
| **Çalışabilirlik** | Şifrelenmiş veri doğrudan çalıştırılamaz; önce **deşifre (decrypt)** edilmesi gerekir. | Karıştırılmış kod **doğrudan makine tarafından çalıştırılmaya devam eder**. |
| **Güvenlik Gücü** | Doğru anahtar uzunluğuyla (örn. AES-256) pratik olarak kırılması imkansızdır. | Zaman ve maliyet engelidir; yeterli kaynakla her zaman çözülebilir. |
| **Kullanım Alanı** | Veritabanları, network trafiği (TLS), hassas dosya saklama. | Mobil uygulama APK'ları, istemci tarafı (client-side) JavaScript kodları, zararlı yazılım analizini geciktirme. |

---

## 3. Çalışabilirlik Kısıtının Yarattığı Sınır
Obfuscation işleminin en büyük kısıtı, **karıştırılan kodun veya verinin bozulmadan, hâlâ hatasız bir şekilde çalışmak zorunda olmasıdır.** 

* **Mantığın Korunması Zorunluluğu:** Bir yazılımı şifrelediğinizde onu çalıştırmazsınız; önce açarsınız. Ancak obfuscation işleminde kod derleyicinin veya yorumlayıcının (interpreter) kurallarına uymak zorundadır. Değişkenlerin yerini değiştirebilir, mantığı dallandırabilir veya simgeleri karmaşıklaştırabilirsiniz ancak yazılımın algoritması çalışmak zorundadır.
* **Analist İçin İpucu:** Kodun çalışabilmesi için belirli kurallara uymak zorunda olması, tersine mühendislik yapan kişiye bir yol haritası sunar. Analist, programın giriş ve çıkış noktalarını (API çağrıları, girdi alanları) takip ederek karartılmış mantığı mantıksal çıkarımlarla çözer.

> **Özetle:** Obfuscation bir kilit değil, sadece karmaşık bir labirenttir. Labirentin içinde doğru yolu bulmak zaman alır, ancak çıkış kapısı her zaman mevcuttur.

---

# Parolalar Neden Base64 ile Saklanmaz?

## 1. Veritabanı Ele Geçirildiğinde Base64 Saldırganın İşini Ne Kadar Zorlaştırır?
Hiç zorlaştırmaz. Base64 bir şifreleme veya özetleme (hashing) algoritması değil, yalnızca bir **kodlama (encoding)** biçimidir. Kodlama, verinin bütünlüğünü bozmadan başka bir formata çevrilmesi işlemidir ve tersine çevrilebilir (reversible) bir yapısı vardır. 

Saldırgan ele geçirdiği veritabanında `ZXJkZW1hcnI=` gibi Base64 ile kodlanmış metinler gördüğünde, herhangi bir anahtar veya parola çözme (brute-force) maliyetine katlanmaksızın, saniyeler içinde standart yazılımlar veya komut satırı araçları (`base64 -d`) vasıtasıyla orijinal parolalara ulaşabilir. Güvenlik katmanı olarak hiçbir bariyer oluşturmaz.

---

## 2. Bu Yöntem Parolaları Hiç Korumadan (Düz Metin/Plaintext) Saklamaktan Farklı mıdır?
Pratikte **hiçbir farkı yoktur**. 
* Düz metin saklandığında insan gözü parolayı doğrudan okuyabilir (`erdemarar`).
* Base64 ile saklandığında ise insan gözü anında okuyamaz, ancak işlem tersine çevrilebilir olduğu için bilgisayar veya herhangi bir kod bloğu anında orijinal haline getirebilir. 

Güvenlik açısından bakıldığında, kilitlenmemiş kapının üzerine sadece "Girmeyiniz" yazılı bir perde asmakla aynı şeydir; yetkisiz erişimi engellemez, sadece ilk bakışta görünürlüğü gizler.

---

## 3. Base64'ün Deterministik Olması (Her Zaman Aynı Girdiye Aynı Çıktıyı Üretmesi) Saldırgana Ne Kazandırır?
Base64, salt (seed) veya rastgele veri (salt) kullanmayan **deterministik** bir kodlama şemasıdır. Aynı parola her kodlandığında kesinlikle birebir aynı çıktıyı üretir. Bu durum saldırgana büyük avantajlar sağlar:
* **Hızlı Analiz ve Eşleme:** Saldırgan, veritabanındaki şüpheli alanların şifrelenmiş mi yoksa sadece kodlanmış mı olduğunu doğrudan anlar.
* **Rainbow Table ve Ön Hesaplama Kolaylığı:** Aynı girdinin her seferinde aynı çıktıyı vermesi, saldırganın yaygın parolaları önceden Base64 formatına çevirip veritabanındaki değerlerle saniyeler içinde eşleştirmesini (lookup) sağlar.

> **Sonuç:** Parolaların güvenli bir şekilde saklanabilmesi için geri döndürülebilir (reversible) yöntemlere değil; yarın detaylıca incelenecek olan, tek yönlü çalışan, tuzlama (salting) ve hashing mekanizmalarına ihtiyaç vardır.

---

# Kodlama Hatalarının Zafiyete Dönüşmesi: Endpoint Bozulması ve Apache CVE'leri

## 1. Endpoint Kavramı ve Kodlanmamış Özel Karakterlerin Etkisi
Bir **endpoint**, bir web uygulamasının veya API'nin dış dünyayla iletişim kurduğu, istekleri (`HTTP Request`) kabul ettiği URL tabanlı uç noktadır (örn. `/api/v1/user?name=erdem`). 

Kullanıcıdan veya istemciden gelen girdiler (`input`) doğru şekilde kodlanmadığında (URL encoding atlandığında veya hatalı yapıldığında), URL'in yapısı bozulur ve sunucu girdiyi komutun veya yolun bir parçası olarak yorumlar. 

* **Yapının Bozulması:** Örneğin, bir arama endpoint'ine `q=test&debug=true` verisi gönderilmek istendiğinde, arada geçen `&` veya `=` karakterleri URL encoding işleminden geçmezse, sunucu bunu iki ayrı parametre (`q=test` ve `debug=true`) olarak algılar. Eğer saldırgan bu alanlara özel karakterler (`?`, `#`, `/`) enjekte ederse, endpoint'in yönü tamamen değişebilir veya istek yanlış rotaya (`routing`) düşerek yetkilendirme bypass'larına yol açabilir.

---

## 2. Apache HTTP Server Zafiyetleri: CVE-2021-41773 ve CVE-2021-42013
Bu iki zafiyet, web sunucularının gelen URL girdilerini normalize etme (path normalization) ve kod çözme (`url-decoding`) işlemlerini **yanlış sırada** gerçekleştirmesinden kaynaklanan klasik birer girdi işleme hatasıdır.

### A. CVE-2021-41773 (Ağustos 2021)
* **Zafiyetin Doğuşu:** Apache HTTP Server 2.4.49 sürümünde, dosya yolu kısıtlamalarını (`Require all denied` gibi yönergelerle korunan dizinleri) aşmak için bir path traversal zafiyeti keşfedildi. 
* **Hatalı Sıralama:** Sunucu, gelen URL isteğini önce harici olarak kontrol ediyor, ancak URL içindeki URL-encoded karakterleri (örneğin nokta işaretinin hex karşılığı olan `%2e` veya `%2E`) erken ya da yanlış aşamada çözüyordu. Saldırganlar `%2e%2e/` (yani `../`) dizilimini URL-encoded olarak gönderdiklerinde, sunucu ilk güvenlik kontrolünde bu karakterleri düz metin olarak görüp engellemeyi atlıyor, ancak dosyayı sunarken bu kodlamayı çözerek kök dizinin dışına (`/var/www/html` sınırlarının dışına) çıkabiliyor ve hassas sistem dosyalarına (`/etc/passwd` gibi) erişebiliyordu.
* **RCE Boyutu:** Eğer sunucuda CGI betikleri (`mod_cgi`) aktifse, saldırganlar bu dizin dışına çıkma yetkisini kullanarak sunucuda uzaktan kod çalıştırma (`Remote Code Execution - RCE`) hakkı elde edebiliyordu.

### B. CVE-2021-42013 (Ekim 2021 - İlk Düzeltmenin Eksik Kalması)
* **Düzeltmenin Neden Eksik Kaldığı:** Apache geliştiricileri CVE-2021-41773 için bir yama yayınladılar. Ancak bu yama yalnızca `%2e%2e/` (veya büyük/küçük harf varyasyonlarını) engelleyecek şekilde, yani sorunun sadece görünen yüzüne odaklanan eksik bir filtreleme (blacklist) mantığıyla hazırlandı. Sunucunun URL-decoding mekanizmasının tüm katmanlarını kapsayan kök neden (`root cause`) düzeltilmedi.
* **İkincisinin Ortaya Çıkışı:** Saldırganlar, kodlamanın iki kez (double-url-encoding) yapılabileceğini fark ettiler. Nokta karakteri `%2e` yerine çift kodlanarak `%252e%252e/` şeklinde gönderildiğinde, Apache sunucusu bu girdiyi ilk aşamada filtreden geçirirken çözmedi; ancak işleme sırasındaki ikinci decode aşamasında karakterler `../` haline gelerek güvenlik mekanizmasını tamamen bypass etti. Bu durum, CVE-2021-41773 zafiyetinin aynen devam etmesine yol açtı.

---

## 3. Günün Özeti ve Temel Ders

> **Kodlama bir güvenlik katmanı değildir, ama kodlamanın yanlış işlenmesi başlı başına kritik bir güvenlik açığıdır.**

Yukarıdaki Apache örneklerinde görüldüğü gibi, yazılımların girdileri hangi sırada doğruladığı (`validation`), hangi sırada kodunu çözdüğü (`decoding`) ve bu süreçlerin mantıksal sıralaması hayati önem taşır. Güvenlik kontrolleri, girdinin ham hali üzerinde değil; tüm kodlama katmanları çözüldükten sonraki normalize edilmiş hali üzerinde yapılmalıdır.