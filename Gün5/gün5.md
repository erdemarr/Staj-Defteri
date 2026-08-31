# Gün 5: Bilgi Güvenliği, İnsan Faktörü ve Kurumsal Çerçeve

## Bilgi Güvenliği ile Siber Güvenlik Arasındaki İlişki

Bilgi güvenliği, formatına ve ortamına bakılmaksızın (kâğıt evrak, sözlü iletişim, zihinsel bilgi ve dijital veri dahil) her türlü bilginin korunmasını kapsayan geniş üst kümedir. Siber güvenlik ise bilgi güvenliğinin yalnızca dijital ortamlardaki verileri, ağları ve sistemleri hedef alan alt kümesidir. Yani her siber güvenlik çalışması bilgi güvenliğinin bir parçasıdır, ancak bilgi güvenliği dijital alanın çok ötesinde fiziki ve sözel alanları da kapsar.

## CIA Üçlüsü ve İhlal Örnekleri

* **Gizlilik (Confidentiality):** Verinin yalnızca yetkili kişiler tarafından okunabilmesini ve gizli kalmasını ifade eder. 
  * *İhlal Örneği:* Yetkisiz bir çalışanın hassas müşteri veri tabanına erişerek kişisel bilgileri sızdırması.
* **Bütünlük (Integrity):** Verinin yetkisiz kişilerce değiştirilememesini, doğru, güvenilir ve eksiksiz kalmasını sağlar. 
  * *İhlal Örneği:* Bir saldırganın e-ticaret sitesindeki ödeme bilgilerini veya IBAN numarasını manipüle ederek para akışını kendi hesabına yönlendirmesi.
* **Erişilebilirlik (Availability):** Verinin ve sistemlerin ihtiyaç duyulduğu anda yetkili kişiler tarafından kullanılabilir durumda olmasıdır. 
  * *İhlal Örneği:* Dağıtık hizmet engelleme (DDoS) saldırısı nedeniyle bir kurumun web servislerinin çökmesi ve kullanıcıların sisteme erişememesi.

---

## Haftanın Dönüşümleri ile CIA Eşleştirmesi (Kapanış Cümlesi)

Bu hafta öğrendiğimiz dönüşüm mekanizmalarının her biri CIA üçlüsünün farklı bir ayağına hizmet etmektedir: Şifreleme gizliliği, özetleme (hashing) ise bütünlüğü sağlar; kodlama (encoding) ise herhangi bir güvenlik amacı taşımadığı için bu üçlüden hiçbirine hizmet etmez. Erişilebilirlik ise bu hafta ele almadığımız operasyonel bir alandır.

## Kullanıcı Odaklı Tehditler ve Oltalama (Phishing) Türleri

Teknik önlemlerin çoğunu devre dışı bırakan en yaygın saldırı türü sosyal mühendisliktir. Bu tehditlerin başında gelen oltalama (phishing) türleri ve dikkat edilmesi gereken hususlar şunlardır:

* **Klasik Oltalama (Phishing):** Geniş kitlelere rastgele gönderilen, genellikle banka, e-posta sağlayıcısı veya kurumsal kimlik taklidi yapan genel dolandırıcılık e-postalarıdır.
  * *Çalışanı Neye Dikkat Etmeli?:* Genel hitaplar (örneğin "Sayın Müşterimiz"), resmi olmayan ve kurumla eşleşmeyen gönderen adresleri, panik yaratmaya çalışan aciliyet dili.
* **Hedefli Oltalama (Spear Phishing):** Belirli bir kişi veya çalışan hakkında önceden açık kaynaklardan (sosyal medya vb.) bilgi toplanarak kişiselleştirilmiş, ikna kabiliyeti yüksek saldırılardır.
  * *Çalışan Neye Dikkat Etmeli?:* E-postanın içeriğinde kişinin projeleri, unvanı veya günlük işleriyle ilgili nokta atışı detayların yer alması, beklenmeyen dosya talepleri veya yönlendirmeler.
* **Balina Avı (Whaling):** Şirket CEO'su, CFO'su veya üst düzey yöneticileri hedef alan, yüksek maliyetli gizli finansal işlemler veya hassas veri transferini amaçlayan özel oltalama türüdür.
  * *Çalışan Neye Dikkat Etmeli?:* Üst yönetim baskısı, gizlilik vurgusu yapılarak standart onay süreçlerinin atlanmasının istenmesi, olağandışı hesaplara acil para transferi talepleri.

---

## Oltalama E-Postası Şüpheli İşaretler Analizi (Örnek İnceleme)

İnternette yayınlanmış veya gelen kutusunda karşılaşılan şüpheli bir oltalama e-postasındaki temel risk göstergeleri şunlardır:

* **Gönderen Adresi:** Kurumsal domain uzantısı yerine küçük harf oyunlarıyla (`@destek-microsoft.com` veya benzeri taklit domainler) oluşturulmuş adresler.
* **Bağlantı Adresi (URL):** Metin içinde görünen güvenli bağlantı metni ile fareyle üzerine gelindiğinde (`hover`) görünen gerçek hedef URL'nin farklı ve şüpheli alan adlarına yönlendirmesi. *(Kural: Asla hiçbir bağlantıya tıklanmaz ve hiçbir ek açılmaz; adresleri görmek için fareyle üzerine gelmek yeterlidir.)*
* **Aciliyet Dili:** "Hesabınız 24 saat içinde kapatılacak", "Derhal şifrenizi güncelleyin" gibi panik ve aciliyet hissi yaratan ifadeler.
* **Dil Bilgisi ve İmla Hataları:** Resmi yazışma kurallarına uymayan, devrik veya bozuk cümle yapısı ile yazım yanlışları.
* **Beklenmedik Ekler:** Güvenlik taramalarından kaçabilecek makro içeren veya çalıştırılabilir uzantıya sahip şüpheli dosya ekleri (`.iso`, `.scr`, `.xlsm`).

## Kurumsal Çerçeve: ISO 27001 ve Bilgi Güvenliği Yönetim Sistemi (BGYS)

Bir kurumun güvenliği yalnızca bireysel çalışanların kişisel dikkatine bırakılamaz; aksine tanımlı süreçler, kurallar ve standartlarla yönetilir. Bu çerçevenin en temel yapı taşlarından biri ISO 27001 standardıdır.

* **ISO 27001 Nedir?:** Bilgi varlıklarını güvence altına almak ve riskleri sistematik bir şekilde yönetmek için uluslararası alanda kabul görmüş temel bilgi güvenliği standardıdır.
* **Bilgi Güvenliği Yönetim Sistemi (BGYS) Kavramı:** Kurumun hassas verilerini korumak amacıyla insan, süreç ve teknoloji unsurlarını bir arada ele alan; risk analizi, güvenlik politikaları ve sürekli iyileştirme döngüsünü içeren yapısal bir yönetim yaklaşımıdır.
* **Kurumlara Kazandırdıkları ve Çalışan Farkındalığı:** Kurumlara yasal uyumluluk, itibari güvence ve siber tehditlere karşı proaktif savunma kazandırır. Çalışan farkındalığı açısından ise güvenliğin sadece BT departmanının sorumluluğu olmadığını, tüm kurum çalışanlarının ortak bir süreç ve kültürün parçası olduğunu benimsetir.

## Çalışma Kuralları: Ofiste ve Ofis Dışında

Kurumsal güvenlik kuralları, masa başında olunan alanlar ile ofis dışındaki çalışma alanlarını kapsayacak şekilde iki ana gruba ayrılır.

### Ofis İçi: Temiz Masa ve Temiz Ekran Politikaları
* **İncelenen Kurum Politikaları:** Üniversite bilgi güvenliği direktifleri (örneğin Orta Doğu Teknik Üniversitesi BGYS politikaları) ve kurumsal teknoloji şirketlerinin açık kaynaklı bilgi güvenliği yönergeleri incelenmiştir.
* **Günlük Çalışma Hayatında Uyulması Gereken Temel Kurallar:**
  * Masada fiziksel olarak hassas müşteri bilgileri, şifrelerin yazılı olduğu kâğıtlar veya gizli evraklar başıboş bırakılmamalıdır.
  * Masadan geçici olarak dahi kalkıldığında ekran mutlaka kilitlenmelidir (`Win + L` tuş kombinasyonu).
  * Mesai bitiminde tüm gizli dökümanlar kilitli dolaplara kaldırılmalı, çıkarılabilir medya (USB bellek vb.) güvenli yerde saklanmalıdır.

---

### Ofis Dışı Çalışma Riskleri ve Somut Önlemler
Ofis dışında (uzaktan çalışma, kafe, seyahat vb.) ortaya çıkan temel riskler ve bunlara karşı alınacak somut önlemler şunlardır:

* **Sosyal Mühendislik:** Fiziksel olarak meraklı gözlerin ekranı izlemesi veya manipülasyon riskleri.
  * *Somut Önlem:* Halka açık alanlarda ekran koruyucu kullanmak ve hassas ekran içeriklerini başkalarının görebileceği ortamlarda açmamak.
* **Zayıf ve Tekrar Kullanılan Parolalar:** Parolaların kolay tahmin edilmesi veya sızdırılması.
  * *Somut Önlem:* Güçlü, karmaşık parolalar üretmek ve yönetmek için bir Parola Yöneticisi (Password Manager) kullanmak.
* **Güvensiz Kablosuz Ağlar:** Ortadaki adam (MitM) saldırıları ve sahte Wi-Fi noktaları.
  * *Somut Önlem:* Halka açık veya şifresiz ağlara asla kurumsal VPN olmadan bağlanmamak.
* **Çok Faktörlü Kimlik Doğrulamanın Olmaması (MFA):** Parolaların ele geçirilmesi durumunda hesaba doğrudan erişilebilmesi.
  * *Somut Önlem:* Tüm kurumsal hesaplarda Çok Faktörlü Kimlik Doğrulama (MFA) zorunlu kılınmalıdır. *Not:* MFA, özellikle kimlik avı (phishing) ve parola sızıntısı (credential stuffing) saldırılarını büyük ölçüde etkisiz kılar; çünkü saldırgan parolayı ele geçirse bile ikinci faktörü (telefon bildirimi, SMS, donanımsal token vb.) aşamaz.
* **Kişisel Cihazdan Çalışma (BYOD):** Güvensiz ve denetimsiz kişisel donanım kullanımı.
  * *Somut Önlem:* Kurumsal verilere sadece onaylı sanal masaüstü (VDI) veya kurum tarafından yönetilen güvenli cihazlar üzerinden erişmek.

  ## Kablosuz Ağ Güvenliğinin Evrimi

Güvensiz kablosuz ağlar, uzaktan çalışırken karşılaşılan temel risklerden biridir. Bu haftaki şifreleme bilgimizle kablosuz ağ protokollerinin evrimine ve arkasındaki güvenlik hikâyesine baktığımızda şu başlıkları görürüz:

* **WEP (Wired Equivalent Privacy):** Zayıf ve statik şifreleme anahtarları ile IV (Initialization Vector) tekrarı zafiyeti barındırdığı için çok kısa sürede kırılabildiği ve dinlenebildiği için tamamen terk edilmiştir.
* **WPA2:** Güçlü simetrik şifreleme algoritmaları kullanmasına rağmen, 4 yönlü el sıkışma (4-way handshake) protokolünün tasarımındaki açıklar nedeniyle KRACK (Key Reinstallation Attacks) saldırısından etkilenmiştir. Bu saldırı, oturum anahtarlarının yeniden kullanımına zemin hazırlayarak ağ trafiğinin çözülmesine yol açmıştır.
* **WPA3:** Modern kimlik doğrulama süreçleri ve ileri düzey şifreleme standartları getirerek KRACK benzeri zafiyetleri, kaba kuvvet (brute-force) saldırılarını ve açık ağlardaki dinleme risklerini çözmeyi hedeflemiştir.

**Çıkarılacak Temel Ders:** Zafiyet her zaman kullanılan saf kriptografik algoritmadan kaynaklanmaz; bazen protokolün çalışma mantığından ve tasarım akışından da kaynaklanabilir. Kafe gibi halka açık ortamlardaki bir kablosuz ağa bağlanırken aslında altyapıya, ağ yöneticisine ve protokolün güvenliğine güvendiğini bilmek bu haftanın en pratik çıktılarından biridir.

## Güncellenmiş Dönüşüm Karşılaştırma Tablosu

| Dönüşüm / İşlem Türü | Geri Döndürülebilir mi? | Anahtar Gerektiriyor mu? | Çıktı Uzunluğu Girdiden Bağımsız mı? | Aynı Girdide Aynı Çıktıyı Üretir mi? | Gerçek Olay Referansı / Araç Çıktısı Örneği | Hizmet Ettiği CIA Ayağı |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Kodlama (Base64)** | **Evet** (Kolayca çözülür) | **Hayır** | **Hayır** (Girdi uzadıkça uzar) | **Evet** (Deterministiktir) | Araç çıktısı: `"erdemarr"` -> `ZXJkZW1hcnI=` | Güvenlik sağlamaz; veri taşınabilirliği içindir. |
| **Hashing (SHA-256)** | **Hayır** (Tek yönlüdür) | **Hayır** | **Evet** (Sabit 256-bit / 64 karakter) | **Evet** (Deterministiktir) | Araç çıktısı: `fc98e8e...` (Tek karakter değişiminde tamamen değişen çığ etkisi) | **Bütünlük (Integrity)** sağlar (Parmak izi). |
| **Simetrik Şifreleme (AES)** | **Evet** (Anahtar ile çözülür) | **Evet** (Gizli anahtar şarttır) | **Hayır** (Girdi boyutuna göre değişir) | **Hayır** (Rastgele IV nedeniyle değişir) | Araç çıktısı ve `secret.key` anahtar yönetimi uygulaması | **Gizlilik (Confidentiality)** sağlar. |

---

## Harvest Now, Decrypt Later (Şimdi Topla, Sonra Çöz)
Günümüzde güçlü simetrik veya asimetrik algoritmalarla şifrelenerek güvenle iletilen hassas verilerin, kötü niyetli aktörler veya istihbarat birimleri tarafından gelecekte kuantum bilgisayarların işlem gücüyle çözülmek üzere şimdiden depolanması tehdididir. Bu risk karşısında NIST ve güvenlik otoriteleri tarafından kuantuma dayanıklı (post-quantum) kriptografi standartları geliştirilmektedir. Bu durum, güvenliğin statik olmadığını; bugün güvenli olan algoritmaların yarın yetersiz kalabileceğini gösteren mesleğin en temel gerçeklerinden biridir.

---

## Hafta Özeti
Bu hafta veri dönüşümlerinin teknik temellerinden başlayıp şifreleme mekanizmalarına, dijital imzalara, kurumsal süreçlere ve insan faktörüne uzanan bir öğrenme süreci geçirdim. Kodlama, hashing ve simetrik/asimetrik şifreleme arasındaki ince çizgileri, bunların CIA üçlüsüyle olan doğrudan bağlarını ve protokol tasarımlarındaki incelikleri net bir şekilde kavradım. En çok kafama oturan ve pratik yaparak bizzat deneyimlediğim konu, şifrelemenin kodlama tarafının birkaç satırdan ibaret olduğu ancak asıl zorluğun ve kritik eşiğin güvenli anahtar yönetiminde yattığı gerçeğiydi. Python ile kendi aracımı geliştirirken secret.key dosyasının yönetimi ve simetrik şifrelemenin pratik karşılığı bu kavramı zihnimde somutlaştırdı. En çok zorlandığım nokta ise asimetrik şifrelemedeki anahtar yönlerinin (hangi anahtarla şifrelenip hangisiyle çözüldüğü) dijital imza mekanizmasında neden tersine döndüğünü mantıken oturtmak oldu; bunu hashing adımları ve imzalama akışını adım adım inceleyerek, OpenSSL testleriyle pekiştirerek aştım. Güvenliğin yalnızca saf matematiksel algoritmalardan ibaret olmadığını; insan faktörünün, oltalama tehditlerinin ve protokol açıklarının sistemi doğrudan etkilediğini görerek haftayı tamamladım.

