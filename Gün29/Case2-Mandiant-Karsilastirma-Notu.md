# Yan Yana Okuma: Mandiant "FIN7 Power Hour" vs. Kendi Case 2 Raporum

**Kaynak:** Abdo, Work, Teaca, McKeague (2022), "FIN7 Power Hour: Adversary Archaeology and the Evolution of FIN7", Mandiant / Google Cloud Blog.
**Karşılaştırılan:** `INC-2026-0914-07-Olay-Raporu-Taslak.md`

---

## 1. Belirsizliğin İfadesi

Mandiant, belirsizliği benim kullandığım 3'lü etiketten (Doğrudan Gözlem / Çıkarım / Bilinmiyor) farklı bir yerde uyguluyor: **teknik gözlemleri düz, hedge'siz cümlelerle** anlatıyorlar ("FIN7 used established RDP access...", "TERMITE is a password-protected shellcode loader...") - çünkü bunlar zaten doğrulanmış bir izinsiz girişin içindeki adımlar. Belirsizlik dilini yalnızca **atıf (attribution)** katmanında kullanıyorlar: bir UNC grubunun gerçekten FIN7 olup olmadığını "suspected... with low confidence" veya "...with high confidence" gibi somut, ikili bir ölçekle etiketliyorlar. En çarpıcı yer: "as of publishing this report, Mandiant has **not** attributed any direct deployment of ransomware to FIN7" - yani sadece belirsiz olanı işaretlemiyorlar, **kesinleştiremediklerini açıkça "hayır" diyerek de belirtiyorlar**.

**Farkımız:** Ben kanıt derecesini her teknik iddiaya (küçük teknik detaylara bile) uyguladım; Mandiant bunu yalnızca "bu kimin işi" sorusuna saklıyor, teknik anlatımı hedge'lemiyor. Ayrıca onlarda gördüğüm ama bende olmayan bir kalıp: **açık bir negatif ifade** ("bunu bulamadık", sadece "bunu bilmiyoruz" değil).

## 2. Yapı ve Sunum

- **IOC tablosu:** Mandiant'ınki çok daha sade - yalnızca `Indicator | Notes` (2 sütun). Benimki 4 sütunlu (Tür, Değer, Kanıt Kaynağı, Değerlendirme). Bunun sebebi tür farkı: onlarınki yıllara yayılan, çok sayıda izinsiz girişi özetleyen bir **kampanya** raporu; benimki **tek bir olayın** adli raporu - kaynak/değerlendirme sütunları tek olay için daha değerli, kampanya raporunda gereksiz detay olurdu.
- **MITRE eşlemesi:** Mandiant, teknikleri **taktik başlıkları altında düz liste** olarak veriyor (ID + isim, başka hiçbir sütun yok); açıklama ve kanıt gövde metninde, kod örnekleriyle ayrı veriliyor. Benimki tabloya "İlgili Bulgu" ve "Güven" sütunlarını gömdü - daha izlenebilir ama tablo daha kalabalık. Mandiant'ın ayrımı (tablo = referans listesi, gövde = kanıt) okunurluk açısından daha temiz.
- **Zaman çizelgesi:** Mandiant'ta **hiç böyle bir tablo yok**. Kampanya genelinde konuya göre (atıf metodolojisi -> PowerShell alışkanlıkları -> savunmadan kaçınma -> modül derinlemesine incelemeler -> fidye yazılımı bağlantısı) ilerliyorlar; tek bir vaka örneğinde (FIN7 From the Trenches) bile kronolojiyi tablo değil, ok işaretli süreç zinciri diyagramıyla (`rdpinit.exe -> notepad++.exe -> cmd.exe -> powershell.exe`) anlatıyorlar. Benim raporum tek bir olayı anlattığı için zaman çizelgesi tablosu daha değerli; onlarınki çok-olaylı bir sentez olduğu için tematik yapı daha mantıklı.

## 3. Teknik Tanıma

Kendi vakamda gördüğüm tekniklerden hangileri bu raporda da geçiyor, karşılaştırdım:

| Bizim Vakada | Mandiant'ta FIN7'ye atfedilmiş mi? |
|---|---|
| Kimlik avı eki (.docm) | **Evet** - doğrudan "GRIFFON DOCM Lure" doğrulama eylemi var, T1566.001 listede |
| Ağır PowerShell kullanımı, gizli/base64 | **Evet, güçlü örtüşme** - raporun kendisi PowerShell'i "FIN7'nin aşk dili" diye tanımlıyor |
| SSH ile yanal hareket | **Evet** - T1021.004 doğrudan listede |
| Obfuscation / gizleme | **Evet ama çok daha gelişmiş** - bizim tek base64 kodlamamıza karşılık, LOADOUT'ta İncil ayetleriyle doldurma, özel şifreleme gibi çok katmanlı teknikler var |
| mshta.exe kullanımı | **Hayır, bu raporda yok** - T1218.010 (Regsvr32) ve T1218.011 (Rundll32) var ama T1218.005 (Mshta) listede değil |
| LSASS'tan Mimikatz tarzı kimlik çalma (T1003.001) | **Hayır, şaşırtıcı şekilde yok** - Credential Access bölümünde T1110.002 (parola kırma), T1555.003 (tarayıcıdan kimlik), T1558.003 (Kerberoasting) var ama LSASS bellek dökümü yok |
| Zamanlanmış görevle kalıcılık (T1053.005) | **Hayır** - raporda hiç Persistence taktik başlığı yok |
| T1078 (Valid Accounts) | **Hayır, listede değil** - ilginç, çünkü vaka çalışmasında çalıntı RDP kimlik bilgisiyle giriş var ama bu teknik açıkça etiketlenmemiş |
| Tor üzerinden veri sızdırma (T1090.003, T1041) | **Kısmen** - genel T1090 (Proxy) var ama alt teknik ya da Exfiltration taktiği hiç yok |
| AMSI bypass (BOATLAUNCH modülü) | Bizim vakada **yok** - gerçek FIN7'de var, bizde karşılığı yok |

**Genel değerlendirme:** Vakamızın iskeleti (kimlik avı -> PowerShell -> yanal hareket) gerçek FIN7 tradecraft'ıyla güçlü örtüşüyor, özellikle PowerShell merkeziliği ve SSH ile yanal hareket. Ama vakamızın en çarpıcı iki tekniği - LSASS/Mimikatz ve zamanlanmış görev kalıcılığı - bu spesifik Mandiant raporunda FIN7'ye atfedilmiyor. Bu, sentetik verinin "genel kötücül davranış kalıbı" ile "bir grubun imzası" arasındaki farkı harmanladığını gösteriyor - gerçekçi ama bire bir kopya değil.

## 4. Tek Somut İyileştirme

**Değişiklik:** Mandiant'ın "bunu bulamadık" tarzı açık negatif ifadesinden esinlenerek, raporuma MITRE eşlemesi bölümünün sonuna şu notu ekledim: *incelenen tekniklerin bilinen bir tehdit grubuna (ör. FIN7) özgü araç/altyapı imzasıyla eşleşip eşleşmediğini kontrol ettim ve böyle bir eşleşme bulunmadığını, bu olayın bağımsız bir vaka olarak değerlendirilmesi gerektiğini açıkça belirttim.* Bu, "atıf yapmadım" ile "atıf yapmayı denedim ve bulamadım" arasındaki farkı gösteriyor - ikincisi çok daha güçlü bir ifade biçimi.

Uygulandı: `INC-2026-0914-07-Olay-Raporu.md`, Bölüm 6 sonu.
