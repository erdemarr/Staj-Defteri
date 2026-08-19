# Gün 8: IP Adresleme ve Subnetting Notları

## 1. IPv4 Temel Yapısı ve Adresleme Kavramları

### Public vs. Private IP
*   **Private IP (Özel IP):** Yerel ağlarda (LAN) cihazların birbirini tanıması için kullanılır. İnternete doğrudan çıkamazlar, NAT ile dış dünyaya açılırlar.
    *   **A Aralığı:** 10.0.0.0 – 10.255.255.255
    *   **B Aralığı:** 172.16.0.0 – 172.31.255.255
    *   **C Aralığı:** 192.168.0.0 – 192.168.255.255
*   **Public IP (Genel IP):** İnternet üzerinde benzersizdir. Servis sağlayıcılar tarafından atanır.

### Analist Gözüyle Log Yorumlama
Loglarda `192.168.x.x` görmek, saldırının veya trafiğin **iç ağdan** (kullanıcı makinesi, iç sunucu) kaynaklandığını gösterir. `8.8.8.8` gibi bir Public IP görmek ise trafiğin dış dünyadan geldiğini veya dışa doğru gittiğini gösterir. Bu, bir güvenlik ihlalinin iç tehdit mi yoksa dış saldırı mı olduğunu anlamada ilk adımdır.

### Diğer Temel Kavramlar
*   **Localhost/Loopback (127.0.0.1):** Makinenin kendi kendine yaptığı çağrılardır. Dış ağa çıkmaz.
*   **CIDR (/24):** Ağın büyüklüğünü gösterir. /24, ilk 24 bitin ağ adresi (subnet) olduğunu, kalan 8 bitin host (cihaz) olduğunu belirtir (254 kullanılabilir cihaz).
*   **Subnet Mask:** Bir IP adresinin hangi kısmının ağ, hangi kısmının host olduğunu belirleyen 32 bitlik maskedir.
*   **Default Gateway (Varsayılan Ağ Geçidi):** Yerel ağ dışına çıkan trafiğin kapısıdır (Genellikle Router IP'si).

## 2. Subnetting Alıştırmaları

### Örnek 1: 192.168.1.0/24 ağı kaç host alabilir?
**Çözüm:** /24 maskede 8 bit hostlar için ayrılmıştır. 2^8 - 2 = 254 cihaz (Network ve Broadcast adresleri çıkarılır).

### Örnek 2: 10.0.0.0/8 ağının subnet maskı nedir?
**Çözüm:** 8 bitlik maske, 255.0.0.0 şeklindedir.

## 3. Ağ Servisleri (Görünmez Motorlar)

| Servis | İşlevi | Güvenlik Önemi |
| :--- | :--- | :--- |
| **DNS** | İsimleri IP'ye çevirir (domain → IP). | DNS Cache Poisoning saldırıları veya C2 (Command & Control) tespiti için kritiktir. |
| **DHCP** | Cihazlara otomatik IP atar. | Rogue DHCP (sahte sunucu) saldırıları ile trafik yönlendirme yapılabilir. |
| **NAT** | İç IP'yi dış IP'ye çevirir. | İç ağdaki makinelerin maskelenmesini sağlar, ancak izlenmesi zordur. |
| **ARP** | IP'yi MAC adresine eşler. | ARP Spoofing/Poisoning (Man-in-the-Middle) saldırıları için temeldir. |

---

## Ağ Cihazları ve Güvenlik Analizi

Ağ cihazlarını anlamak, trafiğin nerede, nasıl manipüle edilebileceğini veya izlenebileceğini anlamaktır.

| Cihaz | Çalıştığı Katman | Karar Mekanizması | Analist İçin Neden Önemli? |
| :--- | :--- | :--- | :--- |
| **Switch** | 2 (Data Link) | MAC Adres Tablosu | İç ağdaki MAC spoofing veya ARP poisoning saldırılarını tespit etmek için kritiktir. |
| **Router** | 3 (Network) | IP Routing Tablosu | Ağlar arası trafiği yönetir. Yanlış yapılandırılmış routing, trafiğin saldırganın kontrolündeki bir cihaza yönlendirilmesine (Man-in-the-Middle) neden olabilir. |
| **Firewall** | 3, 4, (bazen 7) | ACL (Erişim Kontrol Listesi), Durum bilgisi (Stateful) | Ağın "bekçisidir". Engellenen ve izin verilen trafik logları, bir sızıntının ilk belirtilerini (IoC - Indicators of Compromise) burada yakalarız. |

### Detaylı İnceleme

*   **Switch (Anahtar):** 
    *   **Karar:** Gelen çerçevenin (frame) hedef MAC adresine bakar ve hangi porttan iletileceğine karar verir.
    *   **Analist Notu:** "CAM Table" dolumu (MAC Flooding) saldırıları ile switch'in bir hub gibi davranmasını sağlayarak trafiği dinlemek mümkündür.

*   **Router (Yönlendirici):** 
    *   **Karar:** Paketin hedef IP adresine ve yönlendirme tablosuna (Routing Table) bakar.
    *   **Analist Notu:** Ağlar arasındaki geçiş noktasıdır. Dışarıdan içeriye veya içeriden dışarıya sızan trafiğin analiz edildiği en önemli noktalardan biridir.

*   **Firewall (Güvenlik Duvarı):**
    *   **Karar:** Önceden tanımlanmış kurallar (Source/Destination IP, Port, Protokol) üzerinden trafiği filtreler.
    *   **Analist Notu:** Günümüz firewall'ları sadece porta değil, uygulamanın içeriğine (Deep Packet Inspection - DPI) de bakar.

---

## Öğleden Sonra: Lab Ağının Kurulması ve Gözlem

### 1. Lab Ağı Yapılandırması
Makinelerimizin hem internete çıkabilmesi (güncelleme/indirme için) hem de dış dünyaya kapalı, güvenli bir hat üzerinden haberleşebilmesi için **Çift Adaptör Stratejisi** uygulandı.

*   **Adaptör 1 (NAT):** İnternet erişimi için kullanıldı (DHCP).
*   **Adaptör 2 (Internal Network):** Makineler arası izole iletişim için "intNet" adıyla yapılandırıldı.
*   **Sabit IP Yapılandırması:** Log analizinde tutarlılık sağlamak amacıyla, izole ağ arayüzüne (`enp0s8`) statik IP tanımlandı (`192.168.10.10/24`).

### 2. Lab Envanteri
Gerçek kurumlarda varlık envanteri tutmak, bir güvenlik analistinin olay anında kör kalmaması için hayati öneme sahiptir.

| Makine Adı | İşletim Sistemi | Rolü | IP Adresi (Lab) |
| :--- | :--- | :--- | :--- |
| **Ubuntu-Lab** | Ubuntu 22.04 | Analiz & Saldırı | 192.168.10.10 |
| **Win-Lab** | Windows 11 | Hedef & Kurban | 192.168.10.20 |

### 3. Ping Testi ve Gözlemler

Testler, iki yönlü trafiğin farklı sonuçlar verdiğini gösterdi:
*   **Windows -> Ubuntu:** Ping testi başarılı (%0 kayıp).
*   **Ubuntu -> Windows:** Ping testi yanıt vermedi/bekliyor.

**Analist Değerlendirmesi:**
*   **Neden Farklı Sonuç?** Bu bir arıza değil, bir güvenlik tercihi olan **Firewall (Güvenlik Duvarı)** mekanizmasının sonucudur. Windows Defender Firewall, dışarıdan gelen (ICMP/ping) isteklerini varsayılan olarak engellemektedir.
*   **Soru:** Bir sistemin ping'e cevap vermemesi, o sistemin kapalı olduğu anlamına gelir mi?
*   **Cevap:** **Hayır.** Ping'e cevap vermeyen bir sistem; güvenlik duvarı tarafından korunuyor, ICMP paketleri ağ geçidinde engelleniyor veya sistem ping isteklerini yoksayacak şekilde yapılandırılmış olabilir. Bu, yarınki ağ tarama (scanning) çalışmalarında sistemlerin canlılığını doğrulamak için farklı teknikler kullanmamız gerektiğini gösterir.