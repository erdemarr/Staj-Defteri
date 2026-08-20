# Gün 9: Trafiği Görmek, Wireshark ve nmap

## 1. Hedef Servisin Kurulumu ve Doğrulanması
* **Amaç:** İzole lab ortamında hem trafik kaynağı hem de hedef olarak kullanılacak bir web sunucusunun ayağa kaldırılması.
* **Uygulanan Adımlar:** 
  * Ubuntu sanal makinesinde paket listesi güncellendi ve `nginx` web sunucusu tek komutla (`sudo apt install nginx -y`) kuruldu.
  * Servisin aktif olarak çalışıp çalışmadığı `sudo systemctl status nginx` komutu ile kontrol edildi.
* **Doğrulama:** Windows makinesinin web tarayıcısı kullanılarak Ubuntu'nun izole ağ arayüzündeki IP adresine (`enp0s8`) HTTP üzerinden istek atıldı ve Nginx "Welcome to nginx!" karşılama sayfasının başarılı bir şekilde yüklendiği doğrulandı.

## 2. Sabah: Wireshark ile Paket Analizi ve Yetki Yönetimi
* **Yetki Yönetimi ve Güvenlik Modeli:** Wireshark arayüzü ilk açıldığında yerel ağ arabirimlerinin listelenmediği ve *"Yerel arabirimlerde yakalama izniniz yok"* uyarısı alındığı görüldü. Bu durumun, paket yakalama işlemlerinin çekirdek (kernel) seviyesinde ayrıcalıklı (root/admin) yetkiler gerektirmesinden kaynaklandığı analiz edildi.
* **Yetki Çözümü:** Kullanıcı, alt düzey ağ yakalama aracı olan `dumpcap` üzerinde yetki sahibi olabilmesi için `wireshark` grubuna eklendi (`sudo usermod -aG wireshark $USER`) ve sistem zorlamalı olarak yeniden başlatıldı (`sudo systemctl reboot -i`).
* **Arayüz Seçimi:** Sanal makinenin sahip olduğu çoklu ağ arayüzleri arasından (`enp0s3` ve `enp0s8`), Windows ile Ubuntu arasındaki izole lab trafiğini barındıran `enp0s8` arayüzü seçildi.

## 3. Filtre Denemeleri ve Ağ Trafiği Analizi
* **Ham Veri Gözlemi:** Filtresiz yakalama başlatıldığında ekranda akan yüzlerce satırlık mDNS, ARP ve arka plan trafik hareketliliği gözlemlendi.
* **`dns` Filtresi:** Arama çubuğuna `dns` filtresi uygulandı. İzole lab içi ağda gerçek bir DNS sunucusu veya internet trafiği bulunmadığı için ekranın boş kaldığı gözlemlendi; bu durum, lab içi haberleşmenin doğrudan IP adresleri üzerinden yürüdüğünü kanıtladı.
* **`tcp` Filtresi:** Trafikteki tüm TCP segmentleri izole edilerek incelendi.

## 4. TCP Üçlü El Sıkışması (3-Way Handshake) Canlı Gözlemi
* **Test Senaryosu:** Windows tarayıcısından Ubuntu'daki Nginx sunucusuna yeniden HTTP isteği atılarak sıfırdan bir TCP bağlantısı tetiklendi.
* **Paket Analizi:** Wireshark üzerinde `tcp` filtresi altındayken şu üç kritik paket ardışık olarak yakalandı ve doğrulandı:
  1. **SYN (Synchronize):** Windows (`192.168.10.20`) tarafından Ubuntu hedefine (`192.168.10.10`) gönderilen ilk bağlantı istek paketi. Paket detaylarında `SYN` bayrağının (flag) aktif olduğu görüldü.
  2. **SYN-ACK (Synchronize-Acknowledgment):** Ubuntu'nun bu isteği kabul ettiğini belirten ve kendi bağlantı parametrelerini içeren cevap paketi (`SYN` ve `ACK` bayrakları set edilmiş durumda).
  3. **ACK (Acknowledgment):** Windows'un bağlantıyı onaylamak için gönderdiği son paket (`ACK` bayrağı aktif).
* **Üst Katman HTTP Trafiği:** TCP tüneli kurulduktan hemen sonra gerçekleşen `HTTP GET` istekleri ve `304 Not Modified` yanıtları canlı trafikte gözlemlendi.

## 6. Şifreli ve Şifresiz Trafik Karşılaştırması (HTTP vs. TLS/HTTPS)

### Lab İçi Şifresiz Trafik (HTTP) Analizi
* **Yöntem:** Windows makinesinin tarayıcısından Ubuntu'daki Nginx sunucusuna `enp0s8` arayüzü üzerinden HTTP protokolüyle bağlantı sağlandı. Wireshark üzerinde `http` filtresi uygulandı.
* **Gözlem:** İletişimin tamamen şifresiz (plaintext) olduğu görüldü. `GET` istekleri, sunucu yanıtları (`304 Not Modified`), tarayıcı bilgileri (`User-Agent`) ve hedef adresler açık bir şekilde okunabildi.

### Dış Ağ Şifreli Trafik (TLS / HTTPS) Analizi
* **Yöntem:** Ubuntu'nun NAT arayüzü (`enp0s3`) üzerinden internete çıkılarak TLS kullanan dış servislerle olan trafik yakalandı ve `tls` filtresi uygulandı.
* **Gözlem:** Protokol sütununda `TLSv1.2` ve `Application Data` paketleri gözlemlendi. Verilerin uçtan uca şifrelendiği, paket içeriklerinin okunamadığı doğrulandı.

### Analiz Sorularının Yanıtları
1. **Lab içi trafikte hangi bilgileri okuyabiliyorsun?**
   * HTTP protokolü şifresiz çalıştığı için URL yollarını, tarayıcı türünü (User-Agent), işletim sistemi detaylarını, sunucu başlıklarını ve iletilen tüm verileri açık metin (plaintext) olarak doğrudan okuyabiliyoruz.
2. **Dışarıya giden trafikte neden okuyamıyorsun?**
   * İnternet trafiği TLS/HTTPS ile şifrelendiği için veriler ağda şifreli baytlar halinde taşınır. Ortadaki adam (MitM) veya ağı dinleyen biri sadece şifrelenmiş veri akışını (`Application Data`) ve bağlantı kurulan IP/sunucu adını görür, içeriği çözemez.
3. **Bir saldırgan ağı dinlese bu iki durumda eline ne geçerdi?**
   * Lab içi (şifresiz HTTP) dinlemede saldırgan hassas verileri, parolaları, çerezleri (cookies) ve oturum bilgilerini doğrudan ele geçirebilirdi. Şifreli (TLS) dış trafikte ise saldırgan sadece şifreli bir akış ve metadata (hangi sunucuyla iletişim kurduğu bilgisi) görür; verinin kendisine erişemez.

## 7. nmap ile Port Taraması ve Savunmacının Bakış Açısı

### Deney Düzenleni ve Kurulum
* **Kaynak (Saldırgan):** nmap aracı Windows makinede çalıştırıldı.
* **Hedef (Gözlem Noktası):** Ubuntu makinede Wireshark (`enp0s8` arayüzü) aktif tutuldu.
* **Uygulama:** Windows üzerinden Ubuntu'nun lab IP adresine tüm portları tarayan SYN Stealth taraması gerçekleştirildi (`nmap -sS -p- 192.168.10.10`).

### Savunmacının Gözünden Tarama Sonuçları ve Yanıtlar
1. **Tarama hedefin trafiğinde nasıl görünüyor?**
   * Hedef sistemin gelen arayüzünde çok kısa bir süre içinde yoğun ve ardışık SYN paket akışları oluştu. Normal kullanıcı trafiğinden farklı olarak tek bir IP adresinden binlerce farklı porta ardışık istekler atıldığı gözlemlendi.
2. **Açık ve kapalı portların cevapları arasındaki fark:**
   * **Açık portlar (örn. 80/tcp http):** Hedef sistem bağlantıyı kabul ederek `[SYN, ACK]` paketi döndü ve nmap portu `open` olarak raporladı.
   * **Kapalı portlar:** Hedef sistem binlerce kapalı port için anında `[RST, ACK]` (Reset) paketi gönderdi.
3. **Loglarda tarama deseni tespiti:**
   * Çok kısa milisaniyeler içerisinde tek bir dış IP adresinden yüzlerce farklı porta yapılan ardışık SYN istekleri ve bunlara karşılık gelen RST yanıtları, normal bir web gezintisinden tamamen farklı olan tipik bir port tarama imzasıdır (port scan signature).

## 8. Adli Bilişim ve Kanıtın Saklanması İlkesi
* **Kanıtın Korunması:** Staj disiplini gereği, yapılan her analiz ve yakalamanın doğrulanabilir olması için ham veriler `.pcapng` formatında kayıt altına alındı
* **Depolama:** Tüm kanıt dosyaları paylaşılan klasör yapısı kullanılarak Windows tarafındaki `Staj-Defteri/Gün9/Kanıtlar` dizinine aktarıldı.