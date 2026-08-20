# Gün 9 - Teknik Engel Kayıtları

## Engel 1: Wireshark Yerel Arabirim Yakalama Yetki Hatası
* **Sorun.** Ubuntu üzerinde Wireshark açılıp yerel ağ arayüzlerinde trafik yakalanmaya çalışıldığında, standart kullanıcı yetkileri nedeniyle çekirdek (kernel) seviyesindeki paket yakalama işlemine izin verilmedi ve hata alındı[cite: 1].
* **Hata mesajı.** `Yerel arabirimlerde yakalama izniniz yok.`[cite: 1]
* **Denenenler.** Arayüzden farklı ağ kartları seçilmeye çalışıldı ancak yetki uyarısı devam etti. Arayüz seçim pencereleri tıklandı fakat yakalama başlatılamadı.
* **Çözüm.** Kullanıcı `wireshark` grubuna eklendi (`sudo usermod -aG wireshark $USER`) ve sistem zorlamalı olarak yeniden başlatıldı (`sudo systemctl reboot -i`). Bu işlem, `dumpcap` ikilisinin alt düzey ağ arayüzlerine erişim yetkisini standart kullanıcıya grup üyeliği aracılığıyla tanımladığı için sorunu çözdü.
* **Kaynak.** Resmi Wireshark Dokümantasyonu ve Linux Grup Yetkilendirme Rehberi.

## Engel 2: Sanal Makine Oturum İnhibitörü Engeli Nedeniyle Yeniden Başlatılamama
* **Sorun.** Yetki değişikliğinin ardından sistemi yeniden başlatmak için standart `sudo reboot` komutu çalıştırıldı ancak aktif kullanıcı oturumu açık olduğu için sistem komutu engelledi.
* **Hata mesajı.** `Operation inhibited by "vboxuser" (PID 2874 "gnome-session-s", user vboxuser), reason is "user session inhibited". Please retry operation after closing inhibitors and logging out other users.`
* **Denenenler.** Normal `reboot` komutu denendi ancak oturum inhibitörü nedeniyle başarısız oldu.
* **Çözüm.** Aktif oturum kısıtlamalarını baypas ederek sistemi hemen yeniden başlatmak için `sudo systemctl reboot -i` komutu çalıştırıldı. `-i` parametresi, sistem kapatma/yeniden başlatma sırasında aktif oturum inhibitörlerini (engellerini) yok sayarak sistemi zorla yeniden başlattığı için işe yaradı.
* **Kaynak.** Systemd ve Systemctl Manuel Sayfaları (`man systemctl`).

## Engel 3: Paylaşılan Klasöre Yazma İzni (Erişim Engellendi) Hatası
* **Sorun.** Wireshark yakalama dosyası (`.pcapng`) doğrudan Windows'taki paylaşılan klasöre (`/media/sf_Gun9`) kopyalanmak istendiğinde yetki reddi hatası alındı.
* **Hata mesajı.** `cp: normal dosya '/media/sf_Gun9/...' oluşturulamadı: Erişim engellendi`
* **Denenenler.** Normal `cp` komutu ile kopyalama denendi, dosya hedef dizine yazılamadı.
* **Çözüm.** Kopyalama komutu root yetkileriyle çalıştırıldı (`sudo cp ...`). Bu komut, dosya sisteminin paylaşılan dizin üzerindeki yazma kısıtlamalarını yönetici haklarıyla aştığı için dosyayı başarıyla hedef dizine aktardı.
* **Kaynak.** Linux Dosya İzinleri ve VirtualBox Paylaşılan Klasör Dokümantasyonu.
