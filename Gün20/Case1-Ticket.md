# Case 1 — Olay Bildirimi (Ticket)

| Alan | Değer |
|---|---|
| Ticket No | INC-2026-0824-01 |
| Önem | Yüksek |
| Kaynak | Otomatik alarm: "web01 üzerinde çok sayıda başarısız SSH kimlik doğrulama" |
| Etkilenen sistem | web01 (Linux sunucu) |
| Atanan | L1 Analist |
| Veri | `Case1-auth.log` (web01 sunucusunun /var/log/auth.log kaydı) |

## Durum

web01 sunucusunun izleme sistemi, kısa bir zaman aralığında çok sayıda başarısız SSH giriş denemesi tespit etti ve bu ticket'ı açtı. Sunucu bir iç uygulama sunucusudur ve normal şartlarda yalnızca şirket iç ağından erişilir.

Senden bu olayı incelemen, gerçekten bir saldırı olup olmadığını ve olduysa sonucunu ortaya koyman isteniyor.

## Veriyi Yükleme

Sana verilen `Case1-auth.log` dosyasını Splunk'a dün öğrendiğin **Add Data > Upload** yöntemiyle yükle. Bu vaka canlı lab beslemene bağlı değil; tamamen bu dosya üzerinden çalışacaksın. Dosya klasik Linux syslog (auth.log) biçimindedir; yükleme sırasında `linux_secure` sourcetype'ını seçmen ya da otomatik algılamanın doğru ayrıştırdığını doğrulaman alan çıkarımını (kaynak IP, kullanıcı, olay) kolaylaştırır. Yükleme bittiğinde kaynak IP ve kullanıcı gibi alanların düzgün çıktığını kontrol et.

## Cevaplaman Gereken Sorular

Her cevabı bir SPL sorgusu ve çıktısıyla kanıtla. "Şöyle görünüyor" değil, "şu sorguyu çalıştırdım, şu çıktıyı aldım, bu yüzden şu sonuca vardım" şeklinde ilerle.

1. Şüpheli aktivite hangi kaynak IP adresinden geldi?
2. Bu IP adresinden kaç adet başarısız giriş denemesi yapıldı?
3. Saldırgan hangi kullanıcı adlarını denedi? Bunlardan hangileri sistemde var olmayan (invalid user) hesaplardı?
4. Başarısız denemelerden sonra bu IP adresinden başarılı bir giriş oldu mu? Olduysa hangi hesapla ve tam olarak hangi tarih-saatte?
5. Ele geçirildiğinden şüphelendiğin hesap, bu olaydan önce normalde hangi IP adresinden giriş yapıyordu? Bu karşılaştırma sana ne söylüyor?
6. Saldırgan başarılı girişten sonra hangi işlemleri yaptı?
7. Bu saldırı MITRE ATT&CK çerçevesinde hangi tekniğe karşılık gelir? (En az birincil tekniği belirt.)

## Teslim

Bulgularını Gün 20 görev dosyasındaki olay raporu yapısıyla yaz: özet ve kapsam, zaman çizelgesi, bulgular ve kanıtlar, etki, öneriler, sonuç. Etki bölümünde "ne buldum"dan öte "bunun kuruma ne zararı olabilir"i; öneriler bölümünde de bu olaya karşı somut aksiyonları yazman bekleniyor.
