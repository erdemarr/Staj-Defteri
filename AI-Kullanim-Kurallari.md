# Yapay Zeka (AI) Kullanım Kuralları
 
Bu staj boyunca AI araçları (ChatGPT, Claude, Gemini vb.) yasak değildir; doğru kullanıldığında en hızlı öğrenme araçlarından biridir. Ancak stajın asıl eğittiği beceriler analiz yapmak, rapor yazmak ve anlatabilmektir. AI bu becerileri kişinin yerine kullanırsa öğrenme gerçekleşmez. Kurallar bu dengeyi korumak içindir.
 
## Serbest Olanlar
 
- Bir kavramı anlamak için AI'ya soru sormak, örnek istemek, konuyu farklı şekillerde anlattırmak.
- Hata mesajlarını ve komut çıktılarını AI'ya yorumlatmak, takınılan noktada ipucu istemek.
- Kişinin kendi yazdığı komutu, sorguyu veya rapor taslağını AI'ya kontrol ettirmek ve geri bildirim almak.
- İngilizce kaynakları anlamak için çeviri ve özet desteği almak.
 
## Yasak Olanlar
 
- Rapor, haftalık özet veya sunum metnini AI'ya yazdırmak. **Teslim edilen her metin kişinin kendi kaleminden çıkar.**
- Case sorularının cevabını doğrudan AI'ya çözdürmek (sorunun yapıştırılıp cevabın rapora geçirilmesi).
- Anlaşılmayan bir komutun veya sorgunun AI'dan alınıp körlemesine çalıştırılması. Çalıştırılan her şeyin ne yaptığının bilinmesi zorunludur.
 
## Veri Gizliliği
 
Bu kural diğerlerinin hepsinden önce gelir ve yalnızca stajda değil, tüm meslek hayatında geçerlidir.
 
Kuruma ait hiçbir veri AI araçlarına girilmez. Log kayıtları, IP adresleri, kullanıcı adları, sunucu isimleri, konfigürasyon dosyaları, ekran görüntüleri, iç yazışmalar ve müşteri bilgileri bunların hepsi buna dahildir. Ticari AI araçlarına yazılan her şey üçüncü bir tarafın sunucusuna gider ve kontrolden çıkar. Bir analistin kariyerini bitiren hata çoğu zaman teknik bir hata değil, böyle bir dikkatsizliktir.
 
Bir şey sorulmak istendiğinde sorunun genelleştirilmesi gerekir. "Şu sunucudaki şu hata ne demek" yerine "şu tipte bir hata mesajı genelde neyi işaret eder" biçiminde sorulmalıdır.
 
## Doğrulama
 
AI kendinden emin bir dille yanlış bilgi üretebilir. Var olmayan komut parametreleri, uydurma CVE numaraları, çalışmayan sorgular; bunların hepsi sık görülür. AI'dan alınan teknik bir bilgi, resmi dokümantasyondan veya güvenilir bir kaynaktan doğrulanmadan rapora yazılmaz. AI bir başlangıç noktasıdır, kaynak değildir.
 
## Altın Kural: Savunabilirlik
 
Rapordaki her cümlenin ve çalıştırılan her komutun, günlük 2-3 dakikalık anlatımda **kaynağa bakılmadan açıklanabiliyor olması** gerekir. "AI öyle söyledi" bir açıklama değildir. Açıklanamayan bir şey teslim edildiyse, o iş yapılmamış sayılır.
 
## Araştırma Protokolü (soru sormadan önce)
 
Bu protokol **kavramsal takılmalar** içindir: anlaşılmayan bir konu, çözülemeyen bir mantık, oturmayan bir kavram.
 
1. Bir engelde **20 dakika** kendi başına uğraşılır.
2. Çözülemezse araştırılır: dokümantasyon, Google (dork operatörleri dahil), AI.
3. Neyin denendiği ve sonucu not alınır.
4. Hâlâ çözülemediyse soru mentore getirilir. Formatı her zaman şudur: **"Şunu yapmaya çalıştım, şunları denedim, şu sonucu aldım."**
 
> Not: Mentore gelen soruların Google veya AI ile 5 dakikada cevaplanabilir olmaması beklenir. Araştırılabilir her şey önce araştırılır; mentor, araştırmayla ulaşılamayan yerler içindir.
 
## Kurulum ve Yapılandırma Sorunları
 
Bu tür sorunlar yukarıdaki 20 dakika kuralının kapsamı dışındadır. Kurulmayan bir program, açılmayan bir sanal makine, çalışmayan bir servis, beklenmedik bir hata mesajı: bunlar için süre sınırı yoktur ve olmamalıdır.
 
Bu engeller görevin dışında bir aksilik değil, görevin kendisidir. Gün içinde üzerinde çalışılır, araştırılır, denenir. Çözülemeden gün biterse engel kaydına yazılır ve ertesi sabahki kısa anlatımda gündeme getirilir. Günlük anlatım ritmi bu iş için yeterli kontrol noktasıdır.
 
Karşılaşılan her engel `Engel-Kayitlari` klasörüne kaydedilir: sorun neydi, hata mesajı tam olarak neydi, neler denendi, nasıl çözüldü, hangi kaynaktan faydalanıldı.