# Case 2 Sunum İskeleti

## Akış ve Zaman Dağılımı

| # | Bölüm | Süre | Amaç / İçerik notu (yarın doldurulacak) |
|---|---|---|---|
| 1 | **Açılış** | ~1 dk | İlk olarak dinleyici olayın ne olduğunu anlamalı: tek cümlelik özet + ciddiyet ("bir e-posta, iki sistem, muhtemel veri sızıntısı") |
| 2 | **Giriş Noktası** | ~1.5 dk | Kimlik avı e-postası - hızlı geç, sadece SPF/DKIM fail + saldırgan IP'sinin e-posta göndermek için de kullanıldığı detayı |
| 3 | **Zincir (hızlı geçiş)** | ~2.5 dk | mshta -> gizli PowerShell -> dosya indirme -> beacon - aşama aşama ama tek tek kanıt göstermeden, akışı anlat |
| 4 | **Dönüm Noktası / En Kritik An** | ~4 dk | Sunumun ağırlık merkezi. İki en çarpıcı bulgu kanıtıyla gösterilecek: (a) LSASS'tan kimlik bilgisi çalma (m.exe sekurlsa::logonpasswords), (b) svc-backup'ın normal/anomali IP-yöntem karşılaştırması. |
| 5 | **Sonuç (Zincirin Bitişi)** | ~1.5 dk | Veritabanı paketleme + Tor üzerinden 480MB sızdırma - kısa, çarpıcı sayıyla kapat |
| 6 | **Etki** | ~1.5 dk | Net cümlelerle: hangi sistemler, hangi hesaplar, veri riski, "saldırgan hâlâ içeride mi" sorusu |
| 7 | **Öneriler** | ~2 dk | Kök nedene giden 2-3 öneri öne (EDR eksikliği, segmentasyon, servis hesabı politikası); semptom bazlı olanlara tek cümle |
| 8 | **Kapanış** | ~0.5 dk | Tek cümlelik özet + öncelikli aksiyon |

**Toplam: ~15 dk**

---

## Anlatı İskeleti (4 aşama)

1. **Giriş noktası:** Sahte fatura eki - sıradan görünen ama SPF/DKIM'i geçmeyen bir e-posta.
2. **Dönüm noktası:** Kimlik bilgisi çalma anı (LSASS) - buradan sonra saldırı tek makineden kuruma yayılabilir hale geliyor.
3. **En kritik an:** svc-backup'ın anomali girişi - "başarılı görünen bir giriş her zaman masum değildir" dersinin en somut kanıtı.
4. **Sonuç:** Tor üzerinden veri sızdırma - hikâyenin vardığı yer, ve hâlâ kapanmamış sorular (görünürlük boşlukları).

---

## Slayt Başlıkları (taslak, yarın doldurulacak)

1. Başlık - INC-2026-0914-07
2. Olayın Çerçevesi (60 saniyelik özet)
3. Giriş Noktası - Kimlik Avı
4. Zincir - Nasıl İlerledi (tek slaytta hızlı akış diyagramı)
5. Dönüm Noktası - Kimlik Bilgisi Çalma (kanıt)
6. En Kritik An - Yanal Hareket Anomalisi (kanıt)
7. Sonuç - Veri Sızdırma
8. Etki
9. Görünürlük Boşlukları (kısa)
10. Öneriler (kök neden öncelikli)
11. Kapanış

---

## Yarın İçin Not

İçerik (konuşma metni, gerçek ekran görüntüleri, slayt tasarımı) yarın doldurulacak. Bugünün hedefi yalnızca akış ve ana başlıkların net olmasıydı.
