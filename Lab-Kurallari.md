# Lab Kuralları
 
Bu belge, staj boyunca kurulacak test ortamında neyin serbest, neyin yasak olduğunu tanımlar. Kuralların bir kısmı öğrenme düzenini korumak için, bir kısmı ise hukuki sorumlulukla ilgilidir. İkisinin de aynı ciddiyetle ele alınması beklenir.
 
Güvenlik araçlarının çoğu, kimin elinde olduğuna göre anlam değiştirir. Aynı tarama aracı, izinli bir sistemde denetim; izinsiz bir sistemde suçtur. Bu mesleği diğerlerinden ayıran şey, teknik bilgi değil bu sınırın nerede olduğunu bilmektir.
 
## Ağ Kuralları
 
Tüm keşif ve test araçları yalnızca izole lab ağında, stajyere ait sanal makinelere karşı çalıştırılır.
 
Şirket ağına yönelik hiçbir tarama, sorgulama veya test yapılmaz. Şirket ağına bağlı durumdayken lab araçları çalıştırılmadan önce hedefin doğruluğundan emin olunmalıdır.
 
İnternet üzerindeki hiçbir sisteme (web sitesi, sunucu, IP aralığı) tarama veya test yapılmaz. Kişiye ait olmayan ve yazılı izni alınmamış hiçbir sistem hedef değildir.
 
Merak edilen bir tekniğin denenmesi gerektiğinde, hedef kendi lab ortamında oluşturulur. Bu mesleğin standart yöntemi budur.
 
## Zafiyetli Uygulamalar
 
Eğitim amaçlı zafiyetli uygulamalar (DVWA, OWASP Juice Shop ve benzerleri) kasıtlı olarak güvensiz bırakılmış sistemlerdir. Kurulmaları durumunda üç kural mutlaktır:
 
Yalnızca izole lab ağında çalıştırılırlar. Bridged veya dışarıya açık bir ağ moduna asla alınmazlar. Çalışma bittiğinde kapatılırlar, arka planda açık bırakılmazlar.
 
Bu kuralların sebebi basittir: kasıtlı olarak zafiyetli bir sistemi erişilebilir bırakmak, kendi bilgisayarına açık bir kapı bırakmak demektir.
 
## Araçların Yeri
 
Güvenlik araçları sanal makinelere kurulur, ana işletim sistemine değil. Ana sistemin temiz kalması hem kişisel güvenlik hem de bir sorun çıktığında sanal makinenin silinip yeniden kurulabilmesi için gereklidir.
 
## Veri Kuralları
 
Lab ortamına gerçek veri sokulmaz. Şirkete ait dosyalar, gerçek kullanıcı bilgileri ve gerçek log kayıtları test ortamında kullanılmaz.
 
Çalışmalarda kullanılacak veriler ya kişinin kendi ürettiği trafik ya da eğitim amacıyla yayınlanmış açık veri setleridir.
 
Kurumsal verilerin yapay zeka araçlarına girilmemesi kuralı için `AI-Kullanim-Kurallari.md` dosyasına bakılmalıdır.
 
## Şüphede Kalınan Durumlar
 
Bir şeyin bu kuralların kapsamında olup olmadığından emin olunmadığında, işlem yapılmaz ve sorulur. Bir aksiyonu ertelemenin maliyeti düşüktür; yanlış hedefe yönelmiş bir taramanın maliyeti değildir.
 
## Kural İhlalinin Fark Edilmesi
 
Farkında olmadan bu kurallardan biri ihlal edilirse durumun derhal bildirilmesi gerekir. Yanlış hedefe gitmiş bir tarama, açık bırakılmış bir zafiyetli uygulama, dışarıya açılmış bir sanal makine; ne olduysa gizlenmez.
 
Bu madde özellikle yazılmıştır, çünkü güvenlik kültüründe en kritik davranış budur. Saatler içinde bildirilen bir hata yönetilebilir bir olaydır, gizlenen bir hata gerçek bir sorundur. Bu meslekte insanlar hata yaptıkları için değil, hatayı sakladıkları için sorun yaşarlar.
 
Bildirmek olumsuz bir durum değil, doğru davranıştır.
 
## Kabul
 
Bu belge okunduktan sonra kendi gün notuna okunduğuna ve anlaşıldığına dair bir satırın tarihiyle birlikte eklenmesi beklenir. Kurumlarda güvenlik politikası kabulü bu şekilde kayıt altına alınır.