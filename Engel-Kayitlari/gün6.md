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
VirtualBox Kullanım Kılavuzu.

Windows 11 Donanım Sanallaştırma Gereksinimleri.

Hata analizi ve çözüm sürecinde yapay zekâ desteği.