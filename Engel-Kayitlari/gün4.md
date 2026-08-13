# Gün 4 – Engel Kayıtları

## Engel 1 – OpenSSL Kurulumunda 404 Hatası

### Sorun

RSA anahtar çifti ve dijital imza uygulamasında kullanılmak üzere Windows ortamına OpenSSL kurulmaya çalışıldı. İlk olarak `openssl version` komutu çalıştırıldı ancak OpenSSL'in sistemde tanınmadığı görüldü.

Daha sonra `winget` kullanılarak OpenSSL kurulmaya çalışıldı.

### Hata mesajı

```text
openssl : The term 'openssl' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, try again.
At line:1 char:1
+ openssl version
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (openssl:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

`winget` ile ilk kurulum denemesinde ise:

```text
No package found matching input criteria.
```

OpenSSL paketleri arandıktan sonra `ShiningLight.OpenSSL.LTS.Light` paketi bulundu ve kurulmaya çalışıldı. Ancak indirme sırasında:

```text
An unexpected error occurred while executing the command:
Download request status is not success.
0x80190194 : Not found (404).
```

hatası alındı.

### Denenenler

Öncelikle OpenSSL'in sistemde bulunup bulunmadığı kontrol edildi:

```powershell
openssl version
```

Komut tanınmadı.

Ardından:

```powershell
winget install ShiningLight.OpenSSL
```

komutu denendi ancak paket bulunamadı.

Mevcut paketler:

```powershell
winget search openssl
```

komutu ile arandı. Arama sonucunda `ShiningLight.OpenSSL.LTS.Light` paketi bulundu.

Bu paket:

```powershell
winget install ShiningLight.OpenSSL.LTS.Light
```

komutu ile kurulmaya çalışıldı fakat paketin indirme adresi 404 döndürdüğü için kurulum tamamlanamadı.

Bunun üzerine OpenSSL Windows kurulum paketi üreticinin indirme sayfasından temin edilerek kuruldu.

Kurulumdan sonra OpenSSL'in doğrudan çalıştırılabildiği doğrulandı:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" version
```

Çıktı:

```text
OpenSSL 4.0.1 9 Jun 2026 (Library: OpenSSL 4.0.1 9 Jun 2026)
```

### Çözüm

`winget` üzerindeki OpenSSL paketinin indirme bağlantısı 404 verdiği için OpenSSL Windows kurulum paketi alternatif olarak kullanıldı.

OpenSSL başarıyla kuruldu ve:

```text
C:\Program Files\OpenSSL-Win64\bin\openssl.exe
```

konumundan çalıştırılabildi.

Böylece RSA anahtar oluşturma ve dijital imza uygulamasına devam edilebildi.

### Kaynak

- OpenSSL Windows kurulumu için Shining Light Productions.
- Windows `winget` paket yöneticisi.
- Kurulum ve hata analizi sırasında yapay zekâ desteği.

---

# Engel 2 – RSA Dijital İmza Doğrulamasının Başarısız Olması

### Sorun

RSA özel anahtarı ve açık anahtar oluşturulduktan sonra `mesaj.txt` dosyası özel anahtar kullanılarak imzalandı. Oluşturulan imzanın açık anahtar kullanılarak doğrulanması amaçlandı.

İmzalama işlemi başarılı olmasına rağmen doğrulama işlemi başarısız oldu.

### Hata mesajı

İlk doğrulama denemesinde:

```text
Verification failure
483D0000:error:0308010C:digital envelope routines:inner_evp_generic_fetch:unsupported:crypto\evp\evp_fetch.c:376:Global default library context, Algorithm (dgst : 0), Properties (<null>)
483D0000:error:0200008A:rsa routines:RSA_padding_check_PKCS1_type_1:invalid padding:crypto\rsa\rsa_pk1.c:78:
483D0000:error:02000072:rsa routines:rsa_ossl_public_decrypt:padding check failed:crypto\rsa\rsa_ossl.c:779:
483D0000:error:1C880004:Provider routines:rsa_verify_directly:RSA lib:providers\implementations\signature\rsa_sig.c:1065:
```

Alternatif olarak `pkeyutl` ile doğrulama denendiğinde:

```text
Signature Verification Failure
D06B0000:error:0200008A:rsa routines:RSA_padding_check_PKCS1_type_1:invalid padding:crypto\rsa\rsa_pk1.c:78:
D06B0000:error:02000072:rsa routines:rsa_ossl_public_decrypt:padding check failed:crypto\rsa\rsa_ossl.c:779:
D06B0000:error:1C880004:Provider routines:rsa_verify_directly:RSA lib:providers\implementations\signature\rsa_sig.c:1065:
```

### Denenenler

Öncelikle dosya özel anahtar ile imzalandı:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" dgst -sha256 -sign private_key.pem -out signature.bin mesaj.txt
```

Ardından açık anahtar ile doğrulama denendi:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" dgst -sha256 -verify public_key.pem -signature signature.bin mesaj.txt
```

Doğrulama başarısız oldu.

İlk aşamada OpenSSL 4.0.1 ile `dgst` komutunun uyumluluğundan şüphelenildi ve alternatif olarak `pkeyutl` komutu denendi:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" pkeyutl -sign -in mesaj.txt -inkey private_key.pem -out signature.bin -digest sha256
```

Ardından:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" pkeyutl -verify -in mesaj.txt -inkey public_key.pem -pubin -sigfile signature.bin -digest sha256
```

komutu çalıştırıldı.

Ancak bu yöntemde de:

```text
Signature Verification Failure
```

hatası alındı.

Bunun üzerine sorunun komuttan ziyade kullanılan RSA anahtar çiftinden kaynaklanıp kaynaklanmadığı araştırıldı.

Özel anahtardan yeni bir açık anahtar üretildi:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" pkey -in private_key.pem -pubout -out public_check.pem
```

Mevcut `public_key.pem` ile yeni oluşturulan `public_check.pem` dosyalarının SHA-256 hash değerleri karşılaştırıldı:

```powershell
Get-FileHash public_key.pem -Algorithm SHA256
Get-FileHash public_check.pem -Algorithm SHA256
```

Sonuçlar:

```text
public_key.pem
032BE229A35E150DF241635CECADAED5A1552FF20D4B1327DE11624D48DA50E5

public_check.pem
2BCF38F216B30AF2B402FBECF2C28D409A728C86EC4468B5F44EB65CB7424C6E
```

İki hash değerinin farklı olduğu görüldü. Bu durum mevcut `public_key.pem` ile `private_key.pem` dosyalarının aynı anahtar çiftine ait olmadığını gösterdi.

### Çözüm

Özel anahtardan türetilen doğru açık anahtar mevcut `public_key.pem` dosyasının yerine konuldu:

```powershell
Copy-Item public_check.pem public_key.pem -Force
```

Daha sonra daha önce oluşturulmuş imza silindi:

```powershell
Remove-Item signature.bin
```

Dosya, doğru özel anahtar ile yeniden imzalandı:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" dgst -sha256 -sign private_key.pem -out signature.bin mesaj.txt
```

Son olarak doğru açık anahtar kullanılarak doğrulama yapıldı:

```powershell
& "C:\Program Files\OpenSSL-Win64\bin\openssl.exe" dgst -sha256 -verify public_key.pem -signature signature.bin mesaj.txt
```

Sonuç:

```text
Verified OK
```

Böylece sorunun `dgst` veya `pkeyutl` komutlarından kaynaklanmadığı, asıl problemin **özel anahtar ile kullanılan açık anahtarın birbirleriyle eşleşmemesi** olduğu tespit edildi.

Bu deney aynı zamanda açık anahtarın özel anahtardan doğru şekilde türetilmesinin ve imza doğrulamasında doğru anahtar çiftinin kullanılmasının önemini gösterdi.

### Kaynak

- OpenSSL resmi dokümantasyonu – `openssl dgst`
- OpenSSL resmi dokümantasyonu – `openssl pkeyutl`
- OpenSSL resmi dokümantasyonu – `openssl pkey`
- PowerShell `Get-FileHash` komutu
- Hata analizi ve çözüm sürecinde yapay zekâ desteği