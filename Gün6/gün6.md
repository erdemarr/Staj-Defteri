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
*   **Yapılandırma Notları:** RAM: 4096 MB, İşlemci: 1, Disk: 25 GB, Ağ: NAT (Varsayılan ayarlarda bırakılmıştır). Bu değerlerin optimizasyonu ilerleyen günlerde tekrar değerlendirilecektir.

### Güvenlik Kararı ve Risk Analizi
VirtualBox kurulumu sırasında sanallaştırma sürecinde yapılan değişiklik aşağıda gerekçelendirilmiştir:

*   **Karşılaşılan Sorun:** VirtualBox üzerinde Ubuntu sanal makinesini başlatmaya çalıştığımda "VT-x/AMD-V is not available (VERR_VMX_NO_VMX)" hatasını aldım. Sanal makine bu donanım desteği olmadan başlatılamadı.
*   **Yapılan Değişiklik:** Bilgisayarın BIOS/UEFI menüsüne girerek CPU yapılandırması altındaki "Intel Virtualization Technology" (veya AMD sistemlerde SVM Mode) ayarını "Disabled" durumundan "Enabled" durumuna getirdim.
*   **Özelliğin İşlevi:** Bu özellik, işlemcinin fiziksel çekirdeklerini sanal makinelere doğrudan paylaştırmasını sağlayan donanım tabanlı bir sanallaştırma desteğidir. İşletim sisteminin ve sanallaştırma yazılımının CPU komut setlerine donanım seviyesinde erişmesine olanak tanır.
*   **Güvenlik Riski ve Karar:** Sanallaştırma teknolojisinin aktif edilmesi, teorik olarak bir saldırganın sanal makineyi kullanarak ana işletim sistemine (Hypervisor Breakout) sızma ihtimalini doğurabilir. Ancak, lab ortamında izole bir Ubuntu üzerinde çalışacağım ve bu makineyi ağ güvenliği analizleri için kullanacağım göz önüne alındığında, bu risk kabul edilebilir seviyededir. Güvenliği sağlamak adına, sanal makine içerisinde gereksiz servisleri kapatmayı ve ağ yapılandırmasını kısıtlamayı bir "güvenlik katmanı" olarak ekliyorum. Bir güvenlik uzmanı olarak, altyapıyı kullanılamaz hale getirecek kadar kısıtlayıcı olmak yerine, riskin farkında olarak kontrollü bir çalışma ortamı oluşturmayı tercih ediyorum.