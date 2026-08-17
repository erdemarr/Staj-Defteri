# Gün 6: Araştırma Kültürü ve Lab'ın Temeli

## Kuralların Kabulü
İki belgeyi de (AI-Kullanim-Kurallari.md ve Lab-Kurallari.md) okudum ve anladım - 17.08.2026

---

## Sabah: Araştırma ve Doğru Soru Sorma (Google Dorking)

Siber güvenlik alanında en kritik becerilerden biri, bilinmeyeni hızlı ve doğru kaynaklardan arayıp bulabilmektir. Bu doğrultuda arama motorlarını standart cümleler yerine özel operatörlerle yönlendirmeyi sağlayan **Google Dorking** teknikleri araştırılmış ve örneklenmiştir.

### Google Dork Operatörleri ve Örnekleri

*   **`site:`**: Belirli bir web sitesi veya alan adı içinde arama yapar.
    *   *Örnek:* `site:github.com login`
*   **`filetype:`**: Belirli uzantılara sahip dosyaları (PDF, docx, txt vb.) filtreler.
    *   *Örnek:* `filetype:pdf siber güvenlik raporu`
*   **`intitle:`**: Aranan kelimenin web sayfasının başlığında (title) geçmesini sağlar.
    *   *Örnek:* `intitle:"index of /backup"`
*   **`inurl:`**: Web adresinde (URL) belirli bir kelimenin veya parametrenin geçmesini arar.
    *   *Örnek:* `inurl:admin/login.php`
*   **`""` (Tam Eşleşme)**: Kelimelerin arama motoru tarafından bölünmeden, birebir sırayla aranmasını sağlar.
    *   *Örnek:* `"bilgi güvenliği politikası"`
*   **`-` (Hariç Tutma)**: Belirli bir kelimeyi veya siteyi arama sonuçlarından çıkarır.
    *   *Örnek:* `python -tutorial`
*   **`OR`**: Belirtilen kelimelerden herhangi birini içeren sonuçları listeler.
    *   *Örnek:* `siem OR soc`

### Google Hacking Database (GHDB) ve Savunma Boyutu (Blue Team)

*   **GHDB İncelemesi:** Exploit-DB üzerinde bulunan Google Hacking Database incelenmiş, bu operatörler aracılığıyla sistemlerin açıkta bırakılmış hassas bileşenlerine (konfigürasyon dosyaları, unutulmuş yönetim panelleri, sızdırılmış belgeler) ne şekilde erişilebildiği gözlemlenmiştir.
*   **Savunma Perspektifi:** Dorking yalnızca bir saldırı tekniği değildir. Mavi takım (Blue Team) perspektifinden bakıldığında kurumların dış dünyaya istemeden ne tür hassas veriler sızdırdığını proaktif olarak tespit etmek ve kapatmak amacıyla kritik bir savunma denetim aracıdır ("Benim kurumum dışarıya ne gösteriyor?").
*   **Etik Sınırlar:** Çalışmalar tamamen kendi test ve öğrenme alanımızla sınırlandırılmış olup, gerçek kurumların açıkta kalmış sistemlerine izinsiz erişim girişimlerinin yasal ve etik dışı olduğu bilinciyle hareket edilmiştir.

---

## Öğleden Sonra: Lab Ortamının Temeli

Çalışmaların izole bir ortamda yürütülmesi ilkesi gereği, sanal makine altyapısı oluşturulmuştur.

### Kurulum Detayları
*   **Platform:** VirtualBox (Sanal Makine Yöneticisi).
*   **İşletim Sistemi:** Ubuntu 24.04.1 LTS.
*   **Yapılandırma Notları:** RAM: 2048 MB, İşlemci: 1, Disk: 25 GB, Ağ: NAT (Varsayılan ayarlarda bırakılmıştır). Bu değerlerin optimizasyonu ilerleyen günlerde tekrar değerlendirilecektir.

---

## Günlük Linux Alıştırması (OverTheWire: Bandit - Seviye 0 → 4)

Linux komut satırı yetkinliklerini geliştirmek amacıyla OverTheWire Bandit wargame platformunda Seviye 0'dan Seviye 4'e kadar olan görevler tamamlanmıştır.

*   **Bandit Level 0 → Level 1:**
    *   **Görev:** Home dizininde yer alan `readme` adlı dosyadan bir sonraki seviyenin şifresini okumak.
    *   **Çözüm / Kullanılan Komutlar:** `ssh` ile sunucuya bağlanılmış, `cat readme` komutu ile dosya içeriğindeki şifre okunmuştur.
*   **Bandit Level 1 → Level 2:**
    *   **Görev:** Home dizininde tire (`-`) adı verilen özel karakterle adlandırılmış dosyadaki şifreyi okumak.
    *   **Çözüm / Kullanılan Komutlar:** Komut satırında `-` işareti parametre başlangıcı olarak algılandığı için dosya yolu belirtilirken göreceli yol kullanılmış, `cat ./-` komutu ile dosya içeriğine erişilmiştir.
*   **Bandit Level 2 → Level 3:**
    *   **Görev:** Dosya adında boşluklar içeren (`--spaces in this filename--`) dosyadaki şifreyi okumak.
    *   **Çözüm / Kullanılan Komutlar:** Boşluk içeren dosya adlarını işlemek için tırnak işareti kullanılmış, `cat "--spaces in this filename--"` komutu ile şifre okunmuştur.
*   **Bandit Level 3 → Level 4:**
    *   **Görev:** `inhere` dizini altında bulunan gizli (hidden) dosyadan şifreyi bulmak.
    *   **Çözüm / Kullanılan Komutlar:** `inhere` dizinine geçilmiş, gizli dosyaları listelemek için `ls -a` komutu kullanılmış ve bulunan gizli dosya `cat ./.hidden` komutu ile okunmuştur.