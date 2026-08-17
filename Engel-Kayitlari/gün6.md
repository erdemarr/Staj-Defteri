# Gün 6 – Engel Kayıtları

## Engel 1 – Sanallaştırma Teknolojisi Hatası (VT-x/AMD-V)

### Sorun

VirtualBox üzerinde ilk sanal makine olan Ubuntu LTS kurulumu başlatılmaya çalışıldı. Ancak, sanallaştırma yazılımı donanım seviyesinde sanallaştırma desteği bulamadığı için sanal makine başlatılamadı.

### Hata mesajı

text
VT-x/AMD-V is not available (VERR_VMX_NO_VMX)
Sanal makine, ana sistemin CPU sanallaştırma özellikleri donanım seviyesinde (BIOS/UEFI) devre dışı olduğu için başlatılamadı.

### Denenenler
Öncelikle VirtualBox ayarları kontrol edildi:

Sistem > Hızlandırma sekmesinde "Paravirtualization Interface" ayarı "Default" olarak gözlemlendi ancak hata devam etti.

Daha sonra sistemin donanım desteği sorgulandı:

Windows Görev Yöneticisi > Performans > CPU sekmesinden "Virtualization: Disabled" olduğu görüldü.

Sorunun yazılımsal değil, donanım yapılandırması kaynaklı olduğu anlaşıldı. Bilgisayar yeniden başlatılarak BIOS/UEFI menüsüne girildi. "CPU Configuration" veya "Advanced CPU Features" sekmesi altında bulunan "Intel Virtualization Technology" (veya AMD işlemcilerde "SVM Mode") seçeneğinin "Disabled" konumunda olduğu teyit edildi ve "Enabled" olarak değiştirildi.

### Çözüm
BIOS/UEFI üzerinden sanallaştırma teknolojisi aktifleştirildi. Sistem Windows 11'e geri döndüğünde, Görev Yöneticisi üzerinden "Virtualization: Enabled" olduğu doğrulandı.

Bunun ardından VirtualBox'ta sanal makine başlatıldı ve Ubuntu kurulum ekranına başarıyla geçildi.

### Güvenlik Kararı
Sanallaştırma teknolojisinin aktif edilmesi, teorik olarak "Hypervisor Breakout" saldırılarına karşı bir zafiyet kapısı aralasa da, staj kapsamındaki laboratuvar çalışmaları için bu donanım desteği zorunludur. Riski yönetmek adına:

Sanal makine ağ ayarları "NAT" olarak sınırlandırıldı.

Makine içerisindeki gereksiz servisler (SSH, vb.) ihtiyaç duyulmadıkça kısıtlandı.
Güvenlik uzmanı olarak, altyapıyı kullanılamaz kılmak yerine, riskin bilincinde olarak kontrollü ve izole bir çalışma ortamı oluşturmak tercih edilmiştir.

### Kaynak
* VirtualBox Kullanım Kılavuzu.

* Windows 11 Donanım Sanallaştırma Gereksinimleri.

* Hata analizi ve çözüm sürecinde yapay zekâ desteği.

---

## Engel 2 - VirtualBox Ubuntu Siyah Ekran / Görüntü Gelmeme Sorunu

**Tarih:** 17.08.2026  
**İlgili Modül / Ortam:** Oracle VM VirtualBox & Ubuntu (64-bit)  

### **Sorun**
Bandit wargame platformunda pratik yapmak ve gerekli araçları kurmak amacıyla VirtualBox üzerinde kurulu olan Ubuntu 64-bit sanal makinesi başlatılmak istendi. Makine ayrı bir pencerede çalışır duruma geçtiği ("Çalışıyor" durumunda olduğu) ve arka planda çalıştığı halde, sanal makine ekranında uzun süre boyunca hiçbir grafik arayüz ya da konsol çıktısı görünmedi; ekran tamamen düz siyah olarak asılı kaldı.

### **Hata Mesajı**
Doğrudan bir pop-up hata kodu veya yazılı sistem uyarısı dönmedi. Sistem durumu:
> `Sanal makine durumu: "Çalışıyor" / Önizleme ve konsol ekranı: Boş siyah ekran (Black Screen of Death / Display Hang)`

### **Denenenler**
1. **Oturumu Kapatıp Yeniden Başlatma (ACPI / Hard Reset):**
   * *Uygulama:* VirtualBox Yöneticisi üzerinden sanal makineye kapatma/gücü kesme komutu verilip tekrar açıldı.
   * *Sonuç:* Makine yeniden açıldığında sorun devam etti, görüntü yine siyah ekranda kaldı.
2. **Grafik Denetleyicisi Değişimi:**
   * *Uygulama:* Sanal makine kapatıldıktan sonra `Ayarlar > Ekran > Grafik Denetleyicisi` ayarı incelendi. Varsayılan olarak seçili olan `VMSVGA` denetleyicisi `VBoxSVGA` olarak değiştirildi ve 3D Hızlandırma ayarları optimize edildi.
   * *Sonuç:* Sanal makine başlatıldığında ekran sinyali başarıyla alındı ve Ubuntu masaüstü/giriş ekranı sorunsuz bir şekilde yüklendi.

### **Çözüm**
VirtualBox üzerindeki sanal makine tamamen kapatıldıktan sonra:
1. `Ayarlar (Settings) > Ekran (Display)` sekmesine gidildi.
2. **Grafik Denetleyicisi (Graphics Controller)** ayarı `VMSVGA` modundan `VBoxSVGA` moduna getirildi.
3. Değişiklikler kaydedilip makine yeniden başlatıldı.

**Neden İşe Yaradı?**  
VirtualBox'un yeni sürümlerinde Linux konuk sistemler için varsayılan olarak gelen `VMSVGA` denetleyicisi, bazı ana makine (Host) GPU sürücüleri ve Xorg/Wayland görüntü sunucuları ile uyuşmazlık yaşayabilmekte ve sanal ekran arabelleğini (framebuffer) doğru render edemeyerek siyah ekranda kilitlenmektedir. Grafik denetleyicisinin `VBoxSVGA` olarak değiştirilmesi, VirtualBox'un kendi yerel sanallaştırılmış ekran bağdaştırıcısını devreye sokarak sürücü çakışmasını ortadan kaldırmış ve video sinyalinin sanal ekrana başarıyla aktarılmasını sağlamıştır.

### **Kaynak**
* Hata analizi ve çözüm sürecinde yapay zekâ desteği
* Oracle VM VirtualBox User Manual - Display Settings & Virtual Graphics Adapters documentation