# Olay Raporu

**Sistem:** web01 (Linux sunucu)
**Önem Derecesi:** Yüksek
**Analist:** L1 Analist
**Rapor Tarihi:** 04.09.2026
**İncelenen Veri:** Case1-auth.log (Case1-auth.log kaydı, Splunk'a Add Data > Upload ile yüklendi, sourcetype=linux_secure, 155 event)

---

## 1. Özet ve Kapsam

24 Ağustos 2026 tarihinde, web01 sunucusunun izleme sistemi kısa bir zaman aralığında çok sayıda başarısız SSH kimlik doğrulama denemesi tespit ederek bu ticket'ı (Case1-Ticket) açtı. web01 normal şartlarda yalnızca şirket iç ağından erişilen bir iç uygulama sunucusudur.

İnceleme sonucunda olayın bir tahmin veya yanlış alarm olmadığı, **gerçek ve başarılı bir saldırı** olduğu doğrulanmıştır. Tek bir dış IP adresi (`203.0.113.66`), web01 üzerinde 91 başarısız SSH giriş denemesi yaptıktan sonra `deploy` sistem hesabına ait parolayı doğru tahmin ederek sisteme giriş yapmıştır. Saldırgan, ele geçirdiği bu hesap üzerinden `/etc/shadow` dosyasını okumuş ve kalıcılık sağlamak amacıyla root yetkileriyle yeni bir kullanıcı hesabı (`svc-update`) oluşturmuştur.

Bu rapor, olayın Splunk üzerinde SPL sorgularıyla adım adım incelenmesini, elde edilen kanıtları, kurumsal etkisini, MITRE ATT&CK eşlemesini ve alınması gereken aksiyonları içermektedir.

---

## 2. Zaman Çizelgesi

| Zaman (24 Ağustos 2026) | Olay |
|---|---|
| 08:03:11 | `deploy` kullanıcısı normal (iç ağ) girişi yapıyor — kaynak IP `10.0.0.50` |
| 11:12:44 | `deploy` kullanıcısı yine normal (iç ağ) girişi yapıyor — kaynak IP `10.0.0.50` |
| 14:22:04 | `203.0.113.66` IP'sinden brute-force/parola tahmin saldırısı başlıyor (ilk deneme: `admin` kullanıcı adı) |
| 14:22:04 – 14:25:53 | Saldırgan sırasıyla `admin`, `oracle`, `postgres`, `test`, `root`, `ubuntu`, `deploy` kullanıcı adlarını dener — toplam 91 başarısız deneme |
| **14:25:53** | **Başarılı giriş** — `203.0.113.66` IP'sinden `deploy` hesabıyla oturum açılıyor (hesap ele geçirildi) |
| 14:25:54 | Saldırgan `sudo cat /etc/shadow` komutunu çalıştırıyor (parola hash'lerine erişim) |
| 14:25:58 | Saldırgan `sudo useradd -m -s /bin/bash svc-update` komutunu çalıştırıyor |
| 14:26:01 | Yeni kullanıcı `svc-update` (UID=1003) sistemde oluşturuluyor — kalıcılık (persistence) |

---

## 3. Bulgular ve Kanıtlar

### Soru 1 & 2 — Şüpheli aktivite hangi IP'den geldi ve kaç başarısız deneme yapıldı?

**SPL Sorgusu:**
```spl
index=main source="Case1-auth.log" "Failed password"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by src_ip
| sort -count
```

**Çıktı:**
| src_ip | count |
|---|---|
| 203.0.113.66 | 91 |

**Bulgu:** Tüm başarısız denemeler tek bir dış IP adresinden (`203.0.113.66`) geldi. Bu IP'den toplam **91 başarısız SSH giriş denemesi** yapılmıştır.

---

### Soru 3 — Saldırgan hangi kullanıcı adlarını denedi, hangileri geçersiz (invalid user) hesaptı?

**SPL Sorgusu:**
```spl
index=main source="Case1-auth.log" "203.0.113.66"
| rex "for (?<invalid_flag>invalid user )?(?<user>\S+) from"
| search user=*
| eval user_type=if(isnotnull(invalid_flag), "invalid (sistemde yok)", "gerçek/var olan hesap")
| stats count by user, user_type
| sort -count
```

**Çıktı:**
| user | user_type | count |
|---|---|---|
| deploy | gerçek/var olan hesap | 19 |
| root | gerçek/var olan hesap | 15 |
| admin | invalid (sistemde yok) | 12 |
| oracle | invalid (sistemde yok) | 12 |
| postgres | invalid (sistemde yok) | 12 |
| test | invalid (sistemde yok) | 12 |
| ubuntu | gerçek/var olan hesap | 10 |

**Bulgu:** Saldırgan sistematik bir kullanıcı adı listesi denedi (yaygın sunucu/veritabanı hesap adları: admin, oracle, postgres, test — bunlar web01'de mevcut olmayan hesaplardır). Ayrıca sistemde gerçekten var olan `root`, `ubuntu` ve `deploy` hesaplarına karşı da parola denemesi yaptı. `deploy` hesabı en çok denenen (19 deneme) hesap oldu ve sonunda ele geçirilen hesap da bu oldu.

---

### Soru 4 — Başarısız denemelerden sonra başarılı giriş oldu mu? Hangi hesap, hangi tarih-saat?

**SPL Sorgusu:**
```spl
index=main source="Case1-auth.log" "203.0.113.66" "Accepted password"
| rex "Accepted password for (?<user>\S+) from"
| table _time, user, src_ip
```

**Çıktı:**
| _time | user | src_ip |
|---|---|---|
| 2026-08-24 14:25:53 | deploy | 203.0.113.66 |

**Bulgu:** Evet. 91 başarısız denemenin hemen ardından, **24 Ağustos 2026 saat 14:25:53**'te `203.0.113.66` IP adresinden **`deploy`** hesabıyla başarılı bir SSH girişi gerçekleşti.

---

### Soru 5 — Ele geçirilen hesap normalde hangi IP'den giriş yapıyordu? Karşılaştırma ne söylüyor?

**SPL Sorgusu:**
```spl
index=main source="Case1-auth.log" "Accepted password for deploy"
| rex "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| table _time, src_ip
| sort _time
```

**Çıktı:**
| _time | src_ip |
|---|---|
| 2026-08-24 08:03:11 | 10.0.0.50 |
| 2026-08-24 11:12:44 | 10.0.0.50 |
| 2026-08-24 14:25:53 | **203.0.113.66** |

**Bulgu:** `deploy` hesabı o gün daha önce iki kez giriş yapmış ve her ikisinde de kaynak IP **iç ağ adresi** (`10.0.0.50`) olmuştur. 14:25:53'teki giriş ise **dış/internet IP'sinden** (`203.0.113.66`) gelmiştir. web01'in normalde yalnızca iç ağdan erişilen bir sunucu olduğu göz önüne alındığında, bu net bir davranış anomalisidir ve girişin `deploy` kullanıcısının kendisi tarafından değil, hesabı ele geçiren bir saldırgan tarafından yapıldığını doğrular.

---

### Soru 6 — Saldırgan başarılı girişten sonra hangi işlemleri yaptı?

**SPL Sorgusu:**
```spl
index=main source="Case1-auth.log" "deploy" ("sudo" OR "useradd")
| rex "COMMAND=(?<command>.+)$"
| table _time, command
| sort _time
```

**Çıktı:**
| _time | command |
|---|---|
| 2026-08-24 14:25:54 | /usr/bin/cat /etc/shadow |
| 2026-08-24 14:25:58 | /usr/sbin/useradd -m -s /bin/bash svc-update |

**Bulgu:** Saldırgan, giriş yaptıktan sonraki **8 saniye içinde** iki kritik işlem gerçekleştirdi:
1. `sudo cat /etc/shadow` — sistemdeki tüm kullanıcıların parola hash'lerine erişim denemesi.
2. `sudo useradd -m -s /bin/bash svc-update` — root yetkisiyle, meşru görünümlü isimli (`svc-update`) yeni bir kullanıcı hesabı oluşturma. Bu hesap 14:26:01'de sistemde aktif hale gelmiştir.

---

### Soru 7 — MITRE ATT&CK Eşlemesi

| Teknik | ID | Açıklama / Kanıt |
|---|---|---|
| **Brute Force: Password Guessing** (Birincil Teknik) | T1110.001 | Tek IP'den, sistematik kullanıcı adı listesiyle 91 ardışık parola denemesi (14:22:04–14:25:53 arası, ~3 dk 49 sn) |
| Valid Accounts | T1078 | Ele geçirilen `deploy` hesabı, sisteme meşru görünümlü erişim için kullanıldı |
| OS Credential Dumping: /etc/passwd and /etc/shadow | T1003.008 | `sudo cat /etc/shadow` komutu ile parola hash'lerine erişim denemesi |
| Create Account: Local Account | T1136.001 | `svc-update` adlı yeni root-yetkili hesabın oluşturulması (kalıcılık amaçlı) |

**Değerlendirme:** Olay, klasik bir **brute-force → hesap ele geçirme → keşif/credential access → kalıcılık** saldırı zincirini takip etmektedir. Otomatize bir araç kullanıldığı, deneme hızından (ortalama 2-3 saniyede bir deneme) ve sistematik kullanıcı adı listesinden anlaşılmaktadır.

---

## 4. Etki

Bu olay yalnızca bir "deneme" değil, **gerçekleşmiş bir güvenlik ihlalidir**. Kurum açısından potansiyel sonuçları:

- **Hesap ele geçirme (confirmed):** `deploy` servis hesabı saldırganın kontrolüne geçmiştir. Bu hesabın sahip olduğu tüm sudo yetkileri saldırgan tarafından kullanılabilir hale gelmiştir.
- **Kimlik bilgisi ifşası riski:** `/etc/shadow` dosyasının okunmuş olması, sistemdeki tüm kullanıcı hesaplarının parola hash'lerinin saldırganın eline geçmiş olabileceği anlamına gelir. Zayıf parolalar offline olarak kırılabilir ve bu, diğer hesapların (`root` dahil) da ele geçirilmesine yol açabilir.
- **Kalıcı arka kapı (persistence) riski:** `svc-update` adında, kasıtlı olarak görünen bir hesap oluşturulmuştur. Bu hesap fark edilmezse saldırgan, ilk giriş noktası (deploy hesabı) kapatılsa bile sisteme erişimini sürdürebilir.
- **Yanal hareket (lateral movement) riski:** web01 iç ağa bağlı bir sunucu olduğundan, ele geçirilen bu makine üzerinden iç ağdaki diğer sistemlere sıçrama denemesi yapılmış olabilir (bu rapor kapsamındaki log verisinde bu yönde doğrudan kanıt yoktur, ancak risk olarak değerlendirilmelidir).
- **İtibar ve uyumluluk riski:** Sunucuda hassas veri varsa (müşteri verisi, iç sistem bilgisi vb.), yetkisiz erişim veri ihlali bildirim yükümlülükleri doğurabilir.

Özetle: "91 başarısız giriş denemesi" tek başına bir bulgudur; ancak bunun bir hesabın ele geçirilmesi, kimlik bilgisi erişimi ve kalıcılık girişimiyle sonuçlanmış olması, kurumun bu olayı **düşük öncelikli bir alarm değil, aktif bir ihlal** olarak ele alması gerektiği anlamına gelir.

---

## 5. Öneriler

1. **Acil — deploy hesabını devre dışı bırak / parolasını değiştir:** `deploy` hesabının parolası derhal değiştirilmeli, mümkünse parola tabanlı SSH erişimi yerine anahtar (key-based) kimlik doğrulamaya geçilmelidir.
2. **Acil — svc-update hesabını kaldır:** Saldırgan tarafından oluşturulan `svc-update` hesabı derhal silinmeli veya devre dışı bırakılmalı; sistemde başka yetkisiz hesap/cron job/SSH key eklenip eklenmediği kontrol edilmelidir.
3. **Acil — /etc/shadow bütünlüğünü doğrula:** Tüm sistem hesaplarının parolaları, özellikle zayıf olabilecekler, kırılmaya karşı değerlendirilmeli ve gerekiyorsa toplu parola sıfırlaması yapılmalıdır.
4. **203.0.113.66 IP'sini engelle:** Bu IP güvenlik duvarı/WAF seviyesinde kalıcı olarak engellenmeli ve tehdit istihbaratı (threat intel) kaynaklarıyla eşleştirilmelidir.
5. **SSH erişimini kısıtla:** web01'e SSH erişimi yalnızca iç ağ IP aralıklarıyla (ör. `10.0.0.0/24`) sınırlandırılmalı; dışarıdan gelen bu tür bir bağlantının hiç mümkün olmaması gerekirken mümkün olması, ağ segmentasyonunda bir açık olduğunu göstermektedir — bu açık araştırılmalıdır.
6. **Parola politikasını sıkılaştır ve fail2ban/oran sınırlama uygula:** Ardışık başarısız giriş denemelerinin belirli bir eşiği aşması durumunda IP'yi otomatik engelleyen bir mekanizma (fail2ban, SSH rate limiting) kurulmalıdır.
7. **Çok faktörlü kimlik doğrulama (MFA):** Mümkünse SSH erişimi için MFA veya bastion/jump host üzerinden erişim zorunlu kılınmalıdır.
8. **Alarm eşiğini gözden geçir:** Bu olay otomatik alarmla tespit edildi, bu iyi bir sonuç; ancak alarmdan başarılı girişe kadar geçen süre (91 deneme, ~4 dakika) göz önüne alındığında, gerçek zamanlı otomatik engelleme mekanizmalarının (yalnızca alarm değil, aktif blok) devreye alınması önerilir.
9. **Geniş kapsamlı iz sürme:** Diğer sunucuların log kayıtları da `203.0.113.66` IP'si ve `deploy`/`svc-update` hesap adları için taranmalı; yanal hareket belirtisi olup olmadığı doğrulanmalıdır.

---

## 6. Sonuç

Case1-Ticket ticket'ı kapsamında incelenen web01 Case1-auth.log kaydı, otomatik alarmın gerçek bir saldırıyı doğru tespit ettiğini göstermiştir. `203.0.113.66` IP adresinden gerçekleştirilen sistematik bir brute-force/parola tahmin saldırısı (T1110.001), `deploy` servis hesabının ele geçirilmesiyle (T1078) sonuçlanmış; saldırgan ardından kimlik bilgisi erişimi (T1003.008) ve kalıcılık (T1136.001) girişiminde bulunmuştur. Bulgular Splunk üzerinde SPL sorgularıyla doğrulanmış ve kanıt zinciri bu raporda eksiksiz olarak belgelenmiştir. Olay "Yüksek" önem derecesini hak etmektedir ve yukarıdaki önerilerin öncelik sırasına göre derhal uygulanması gerekmektedir.
