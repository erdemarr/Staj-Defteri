# Case 2 - IOC (Indicator of Compromise) Listesi

**Ticket:** INC-2026-0914-07 · **Tarih:** 14 Eylül 2026 (olay), 10-11 Eylül 2026 (inceleme)

Bu liste, bu olaya ait tüm tehdit göstergelerini içerir. Tam olarak tamamlanmamıştır, taslak halindedir. Her satır Splunk'ta bir sorguyla doğrulanmıştır. Amaç: bir sonraki analistin bu göstergeleri kendi ortamında (diğer uç noktalar, e-posta gateway'leri, güvenlik duvarı logları) doğrudan arayabilmesi.

---

## IP Adresleri

| Değer | Rol | Kaynak | Not |
|---|---|---|---|
| `45.137.21.88` | C2 sunucusu | mail-gateway2, dns_query2, firewall2, sysmon2 | Hem kimlik avı e-postasının gönderildiği bağlantı adresi hem de beacon/C2 hedefi. Aynı IP iki farklı aşamada görülüyor |
| `185.220.101.44` | Veri sızdırma hedefi | firewall2 | Bilinen bir Tor çıkış düğümü |

## Alan Adları

| Değer | Rol | Kaynak | Not |
|---|---|---|---|
| `static-cdn-analytics.com` | C2 domaini | dns_query2, sysmon2 | Hem HTTPS beacon hem DNS TXT tünel bu domain üzerinden; 45.137.21.88'e çözülüyor |
| `acme-invoices.com` | Kimlik avı gönderen domaini | mail-gateway2 | `billing@acme-invoices.com` adresinden gönderim, SPF fail / DKIM none |

## Dosya Adları ve Hash'leri

| Dosya Adı | SHA256 | Rol | Kaynak |
|---|---|---|---|
| `Fatura_2026_4471.docm` | `dd50d653c274434bcd62fbde66b49e144ac0658f844ea0528b3cc035dc3a2540` | Kimlik avı eki (ilk bulaşma) | mail-gateway2 |
| `svchost_update.exe` | `746f10f315b4beb6823d1b47539e6c44079434d00e0efa4baa2b30be6b1f3d2b` | İkincil yük (C2 aracısı) - meşru "svchost" adını taklit ediyor | sysmon2 |
| `m.exe` | `97ef7e9ffbcecb476ee47b94fe86b5fc57b30a41f6933cffc3dc8b4ae6f2854e` | Kimlik bilgisi çalma aracı (Mimikatz benzeri) | sysmon2 |
| `u.hta` | Hash yok, sadece URL gözlemlendi | mshta.exe ile çağrılan uzak betik | sysmon2 (`http://static-cdn-analytics.com/u.hta`) |

## Ele Geçirilmiş / Kötüye Kullanılmış Hesaplar

| Hesap | Sistem | Nasıl Kullanıldı | Kaynak |
|---|---|---|---|
| `b.kaya` (COMPANY\b.kaya) | FIN-WS03 | İlk bulaşma noktası. Kimlik avı ekini açan kullanıcı | sysmon2, winsecurity2 |
| `svc-backup` | app-db01 | Çalınan kimlik bilgisiyle yanal harekette kullanıldı (normalde publickey/192.168.30.10, burada password/192.168.20.45) | linux_secure (Case2-auth.log) |

## Kalıcılık Artefaktları

| Değer | Rol | Kaynak |
|---|---|---|
| `\SystemTelemetrySync` | Meşru görünümlü, saldırgan tarafından oluşturulan zamanlanmış görev adı | winsecurity2 (EventCode 4698) |

## Davranışsal Gösterge (TTP düzeyinde, Pyramid of Pain'in üst katmanı)

| Desen | Açıklama |
|---|---|
| ~1 dakikalık düzenli HTTPS beacon | Küçük, tutarlı bayt boyutlu (500-700 bayt giden) bağlantılar. Otomatik C2 check-in deseni |
| ~5 dakikalık rastgele alt-alan-adlı DNS TXT sorguları | Her sorguda farklı, rastgele karakterli alt alan adı, hepsi NXDOMAIN. Olası DNS tünelleme/komut kanalı |
| `sekurlsa::logonpasswords` komut kalıbı | Mimikatz'ın imza niteliğindeki komutu. LSASS bellek erişimiyle birlikte görülürse yüksek güvenilirlikte tespit sağlar |

---

## Kullanım Notu

- IP ve domain göstergeleri (Pyramid of Pain'in alt katmanları) hızlı ama kısa ömürlü. Saldırgan bunları değiştirebilir. Güvenlik duvarında/DNS sinkhole'da **acil engelleme** için kullanılmalı.
- Dosya hash'leri, EDR/antivirüs tarafında imza olarak taranmalı; aynı hash başka uç noktalarda görülürse aynı durumun parçasıdır.
- Davranışsal desenler (beacon aralığı, `sekurlsa::logonpasswords` gibi komut kalıpları) daha kalıcı tespit kuralları için kullanılmalı. Saldırgan altyapısını değiştirse bile bu davranışları büyük olasılıkla tekrarlayacaktır.
