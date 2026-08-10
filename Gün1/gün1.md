Git Nedir?
 Dağıtık bir Versiyon Kontrol Sistemidir. Yazılım projelerinde kod değişikliklerini takip etmeyi, geçmişe dönmeyi ve birden fazla kişinin aynı projede birlikte çalışmasını sağlar.
 Bize Ne Sağlar?:
  1-	Dağıtık Çalışma Yapısı: Geliştiriciler, merkezi bir sunucuya ihtiyaç duymadan yerel ortamlarda çalışabilirler.
  2-	Versiyon Takibi: Yapılan tüm değişiklikler detaylı bir şekilde kaydedilir ve geçmişe dönüş imkanı sağlar
  3-	Branch Yönetimi: Farklı dallar üzerinde paralel geliştirme yapılabilir ve kolayca birleştirilebilir.
  4-	Kolay Paylaşım: Değişiklikler kolayca paylaşılır ve işbirliğini kolaylaştırır.
  5-	Verimlilik ve Hız: Çoğu işlem yerel makinede gerçekleştiği için hızlı ve verimlidir.
Temel Git Komutları Nelerdir ve Nasıl Kullanılır?
 1-	git config: Kullanıcı adı ve e-posta gibi ayarları yapar.
 Kullanım: git config --global user.name "Adınız"
 2-	git init: Bulunduğun klasörde yeni bir Git deposu (repository) başlatır.
 Kullanım: git init
 3-	git status: Çalışma dizinindeki değişikliklerin durumunu gösterir.
 Kullanım: git status
 4-	git add: Değişen dosyaları bir sonraki kayıt için hazırlar.
 Kullanım: git add . (tüm dosyalar için)
 5-	git branch: Mevcut dalları listeler veya yeni dal oluşturur.
 Kullanım: git branch yeni-dal
 6-	git push: Yereldeki kayıtları uzak depoya gönderir.
 Kullanım: git push origin main
 7-	git pull: Uzak depodaki güncellemeleri indirip projeyle birleştirir
 Kullanım: git pull origin main
