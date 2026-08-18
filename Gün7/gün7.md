# Gün 7: Ağ Katmanları ve Protokoller

Bugün, ağ iletişiminin temellerini oluşturan katmanlı mimarileri ve protokolleri derinlemesine inceliyoruz.

## 1. Ağ Modelleri: Katmanlı Düşünmek

Veri iletim sürecini anlamak için iki ana modeli bilmek kritik öneme sahiptir:

### OSI Modeli (7 Katman)
1. **Fiziksel (Physical):** Verinin elektriksel veya ışık sinyallerine dönüştürüldüğü katman.
2. **Veri Bağı (Data Link):** MAC adresleme ve çerçeveleme (framing).
3. **Ağ (Network):** IP adresleme ve yönlendirme.
4. **Taşıma (Transport):** Veri iletim kontrolü (TCP/UDP).
5. **Oturum (Session):** Bağlantı yönetimi.
6. **Sunum (Presentation):** Veri formatlama ve şifreleme.
7. **Uygulama (Application):** Kullanıcı arayüzü ve protokoller (HTTP, FTP).

### TCP/IP Modeli (4 Katman)
Pratikte daha yaygın kullanılan modeldir:
1. **Ağ Erişimi (Network Access)**
2. **İnternet (Internet)**
3. **Taşıma (Transport)**
4. **Uygulama (Application)**

> **Temel Soru:** Bir veri paketi bilgisayarımdan çıkıp karşıdaki sunucuya varana kadar hangi aşamalardan geçiyor?
> **Cevap:** Veri, uygulama katmanından başlayarak aşağıya doğru inerken her katman kendi kontrol bilgilerini (header) ekler. Bu işleme **Kapsülleme (Encapsulation)** denir.

## 2. Taşıma Katmanı Protokolleri

Verinin uçtan uca nasıl iletileceğine karar veren protokoller:

*   **TCP (Transmission Control Protocol):** Güvenilir, bağlantı odaklı, hata denetimli iletişim.
*   **UDP (User Datagram Protocol):** Hızlı, bağlantısız, hata denetimi yapmayan (streaming veya oyunlar için).

### Üçlü El Sıkışma (Three-Way Handshake)
TCP'nin güvenli bağlantı kurma süreci:
1. **SYN:** İstemci, sunucuya bağlantı isteği gönderir.
2. **SYN-ACK:** Sunucu, isteği aldığını ve bağlantıya hazır olduğunu onaylar.
3. **ACK:** İstemci, sunucunun onayını aldığını belirterek bağlantıyı tamamlar.

Bu süreci, Gün 9'da **Wireshark** üzerinde gerçek ağ trafiğinde gözlemleyeceğiz.

## 3. Protokoller ve Portlar

Portlar, bir işletim sisteminde çalışan farklı uygulamaların ağ trafiğini birbirinden ayırmasını sağlayan mantıksal giriş noktalarıdır. Bir sunucuda hangi hizmetlerin çalıştığını portlar üzerinden anlarız.

### Yaygın Protokoller ve Port Eşleşmeleri

Bir analist olarak aşağıdaki portları ve işlevlerini ezbere bilmelisin:

| Protokol | Port | İşlevi | Şüpheli Durum |
| :--- | :--- | :--- | :--- |
| **FTP** | 21 | Dosya transferi | Güvensizdir (şifreler düz metin gider). |
| **SSH** | 22 | Uzak terminal erişimi | İnternete açık olması kaba kuvvet saldırılarına davetiyedir. |
| **SMTP** | 25 | E-posta gönderimi | SPAM veya zararlı e-posta gönderimi için kullanılabilir. |
| **DNS** | 53 | Alan adı çözümleme | DNS tünelleme veya veri sızdırma için suistimal edilebilir. |
| **HTTP** | 80 | Web trafiği (şifresiz) | Veriler şifrelenmediği için dinlenebilir (MITM saldırısı). |
| **HTTPS** | 443 | Web trafiği (şifreli) | Şifreli olduğu için daha güvenlidir. |
| **RDP** | 3389 | Uzak masaüstü bağlantısı | Fidye yazılımı saldırılarında en çok hedef alınan porttur. |

### Analitik Bakış Açısı
"Bu portun beklenmedik bir yerde açık olması neden şüphelidir?" sorusunu sormak, bir güvenlik analistinin en önemli yeteneğidir. 
*   **Örnek:** Bir yazıcıda SSH (22) veya RDP (3389) portunun açık olması, cihazın ele geçirilmiş olabileceğini veya yanlış yapılandırıldığını gösterir. 
*   **Log Okuma:** İleride tarama loglarını incelerken, bu standart dışı açık portlar, bir saldırganın sistemde kendine bir arka kapı (backdoor) açtığının göstergesi olabilir.

## 4. Tanılama Araçları

Ağ sorunlarını gidermek ve sistemdeki hareketliliği izlemek için kullanılan temel komut satırı araçlarıdır. Hem Windows hem de Linux ortamında bu araçları kullanabilmek, bir analistin yetkinliğinin göstergesidir.

### Temel Komutlar ve İşlevleri

*   **`ipconfig` (Windows) / `ip a` (Linux):** Ağ arayüzlerinin IP adresini, alt ağ maskesini ve ağ geçidini görüntüler. Cihazın ağdaki kimliğini doğrulamak için kullanılır.
*   **`ping`:** Bir hedefe ICMP yankı paketleri göndererek bağlantının durumunu ve gecikme süresini ölçer. (Hedef canlı mı?)
*   **`tracert` (Windows) / `traceroute` (Linux):** Paketin hedefe ulaşana kadar geçtiği tüm yönlendiricileri (hop) listeler. Ağdaki darboğazları veya rota hatalarını bulmaya yarar.
*   **`nslookup` / `dig`:** Alan adı çözümleme (DNS) sorguları yaparak, bir alan adının hangi IP adresine karşılık geldiğini öğrenmeyi sağlar.
*   **`arp`:** IP adresinden fiziksel MAC adresine eşlemeyi gösterir (ARP tablosunu listeler). Yerel ağdaki cihazları tanımak için önemlidir.
*   **`netstat`:** Aktif ağ bağlantılarını, dinlenen portları ve yönlendirme tablolarını gösterir.

### Analistin Gözünden: `netstat`

Bir analist için en kritik komutlardan biridir. `netstat` çıktısı üzerinden şunları analiz edebilirsin:
1. **Dinlenen Portlar (Listening):** Hangi servisler dışarıdan bağlantı kabul ediyor?
2. **Açık Bağlantılar (Established):** Hangi uzak IP'lerle aktif veri alışverişi var?
3. **Beklenmedik Durumlar:** Tanınmayan bir IP adresine veya şüpheli bir portta (örneğin standart dışı bir yüksek portta) kurulan bağlantılar, zararlı bir yazılımın dışarıya veri sızdırdığının (C2 trafiği) habercisi olabilir.

## 5. Lab: İkinci Makine (Windows Evaluation)

Laboratuvar ortamını genişletmek ve farklı işletim sistemi loglarını analiz etme yeteneği kazanmak adına Windows ortamına geçiş yapıyoruz.

*   **Kurulum:** Microsoft'un sunduğu ücretsiz Windows değerlendirme (evaluation) sürümünü indirip VirtualBox üzerinden kuruldu.
*   **Neden Windows?** Gerçek dünya senaryolarında loglar, Linux ve Windows işletim sistemlerinde farklı biçimlerde üretilir. Bir analist olarak her iki sistemin de çalışma mantığını ve log yapılarını bilmek gerekir.

## 6. Günlük Linux Alıştırması

Bugünkü hedef **Bandit (OverTheWire)** oyununda **Seviye 5-9** aralığını tamamlamak.

*   **Bandit Level 5 → Level 6:**
    *   **Görev:** `inhere` dizini içerisinde, belirli bir boyutta, insan tarafından okunabilir ve çalıştırılabilir olmayan dosyayı bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `find ./inhere -type f -size 1033c ! -executable` komutu kullanılarak ilgili dosya bulunmuş, `cat` ile şifre okunmuştur.
*   **Bandit Level 6 → Level 7:**
    *   **Görev:** Sunucu üzerinde `user=bandit7`, `group=bandit6` ve 33 bytes boyutunda olan dosyayı bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` komutu ile dosya bulunmuş, şifreye ulaşılmıştır.
*   **Bandit Level 7 → Level 8:**
    *   **Görev:** `data.txt` dosyası içerisinde `millionth` kelimesinin yanındaki şifreyi bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `grep "millionth" data.txt` komutu kullanılarak şifre satırı filtrelenmiş ve alınmıştır.
*   **Bandit Level 8 → Level 9:**
    *   **Görev:** `data.txt` içerisinde sadece bir kez tekrarlanan satırı bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `sort data.txt | uniq -u` komutu kullanılarak veriler sıralanmış ve tekrarsız satır (şifre) bulunmuştur.
*   **Bandit Level 9 → Level 10:**
    *   **Görev:** `data.txt` içerisinde en az birkaç `=` işareti ile başlayan insan tarafından okunabilir (human-readable) dizeleri bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `strings data.txt | grep "=="` komutu ile dosya içeriği taranmış, anlamlı dize bulunarak şifreye ulaşılmıştır.

