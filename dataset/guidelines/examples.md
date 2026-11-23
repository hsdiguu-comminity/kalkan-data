# Kalkan - Etiketleme Örnekleri

**Sürüm:** v0.1 (taslak) · **İlgili dosyalar:** [labeling_guide.md](labeling_guide.md), [categories.md](categories.md)

## Bu dosya nasıl kullanılır?

Bu dosya, [labeling_guide.md](labeling_guide.md) ve [categories.md](categories.md) içindeki kuralların örneklerle gösterilmiş hâlidir. Bir içerikte kararsız kalırsan önce karar akışını (labeling_guide 6) uygula, sonra buradaki en yakın örneğe bak. Örnekle kural çelişirse **kural geçerlidir**. Çelişkiyi `gozden_gecir = true` ile işaretle ve bildir.

### Gösterim

- **Etiket sütunu:** `sinif` / `kategori` (+ `ikincil_kategori`). `guvenli` ve `supheli` kayıtlarda kategori boştur, bu yüzden yalnızca sınıf yazılır.
- **Gerekçe sütunu:** Kararı belirleyen risk işareti kodu (G1-G7, O1-O5) ve kısa açıklama. Kodlar için labeling_guide 5.
- `gozden_gecir = true` olan örnekler Etiket sütununda ayrıca belirtilmiştir.
- Örneklerin hepsi **uydurmadır**. Aşağıdaki kurum adları ve alan adları gerçek değildir.

### Örneklerde kullanılan uydurma kurumlar ve resmi alan adları

| Kurum | Resmi alan adı |
| --- | --- |
| X Bankası | `xbankasi.com.tr` |
| Y Kargo | `ykargo.com.tr` |
| Z Operatörü | `zoperator.com.tr` |
| Y Vergi İdaresi | `yvergi.gov.tr` |
| Z Market | `zmarket.com.tr` |

Bunların dışındaki alan adları resmi **değildir** (labeling_guide 6.2). Kişisel veriler labeling_guide 10'daki yer tutucularla maskelenmiştir.

---

## 1. Güvenli örnekleri

Güçlü (G) ve orta (O) işaret yok. Zayıf işaretler (link, yazım hatası, bilinmeyen gönderici, reklam dili) etiketi değiştirmez.

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| GV-01 | "X Bankası: [KART_SON4] ile biten kartınızla Z Market'te 349,90 TL harcama yapılmıştır. 12.11.2026 14:32" | `guvenli` | Tutar, yer ve kart sonu içeren rutin harcama bildirimi. O1 sayılmaz (5.2). Kullanıcıdan bir şey istenmiyor. |
| GV-02 | "Doğrulama kodunuz: [KOD]. Bu kodu kimseyle paylaşmayın. X Bankası çalışanları sizden kod istemez." | `guvenli` | Kodu **bildiriyor**, istemiyor (8). |
| GV-03 | "Sayın [AD_SOYAD], X Bankası olarak sizden SMS ile şifre, kart bilgisi veya doğrulama kodu istemeyiz. Bu tür mesajlara yanıt vermeyin." | `guvenli` | Gerçek kurumun "şifre sormayız" uyarısı. Metinde "şifre", "kod" geçmesi G1 değildir, çünkü bilgi **istenmiyor** (8). |
| GV-04 | "Y Kargo: Gönderiniz bugün teslim edilecektir. Takip: ykargo.com.tr/takip" | `guvenli` | Resmi alan adı, bilgi/ödeme isteği yok (8). |
| GV-05 | "Z Market: Bu hafta sonu tüm ayakkabılarda %40 indirim! Son gün Pazar. Mağazalarda ve zmarket.com.tr'de geçerli." | `guvenli` | Reklam ve "son gün" ticari acelecilik zayıf işarettir (5.3). Link resmi. |
| GV-06 | "Merhaba, [AD_SOYAD] Bey'in ofisinden arıyorum. Randevunuzu perşembe 15:00'e aldık." | `guvenli` | Bilinmeyen gönderici tek başına işaret değil (8). |
| GV-07 | "slm yarin sinava gidemiyecem notlar var mi atarmisn" | `guvenli` | Çok hatalı yazım, ama risk işareti yok (8). |
| GV-08 | "X Bankası: Yeni mobil uygulama sürümümüz yayında." | `guvenli` | Gönderici adı olarak kurum adı güven de risk de göstergesi değildir (5.3). |
| GV-09 | E-posta. Konu: "Kasım faturanız hazır". Gövde: "Merhaba [AD_SOYAD], Z Operatörü Kasım faturanız 389,00 TL, son ödeme tarihi 28.11.2026. Faturanızı zoperator.com.tr adresinden görüntüleyebilirsiniz." | `guvenli` | Resmi alan adı, tehdit veya baskı yok, G/O işareti yok. |
| GV-10 | "X Bankası: Yeni kampanyalarımızı xbankasi.com.tr adresinde inceleyebilirsiniz." | `guvenli` | Resmi alan adlı link, bilgi/ödeme istemiyor (8). |

---

## 2. Şüpheli örnekleri

En az bir orta işaret (O1-O5) var, güçlü işaret (G1-G7) yok. `kategori` boş bırakılır.

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| SP-01 | "X Bankası: Hesabınızda olağan dışı bir işlem tespit edildi. Detaylar için [TELEFON] numarasını arayın." | `supheli` | O1 (belirsiz "olağan dışı işlem" uyarısı) + O4 (doğrulanamayan geri arama kanalı). Bkz. 8. |
| SP-02 | "X Bankası: Hesabınızda olağan dışı bir işlem tespit edildi. Lütfen müşteri temsilcinizle görüşün." | `supheli` | Yalnızca O1. Link, telefon ve bilgi isteği yok. |
| SP-03 | "Fırsatı kaçırmayın! bit.ly/a1B2c3" | `supheli` | O2: kısaltılmış link, bağlam yok (8). |
| SP-04 | "Tebrikler! Çekilişimizi kazandınız. Ödül detayları ileride duyurulacaktır." | `supheli` | O3: beklenmedik ödül iddiası, **eylem istenmiyor** (8). Eylem isteseydi G3 olurdu. |
| SP-05 | "Y Vergi İdaresi: Adınıza kayıtlı 1.240 TL ödenmemiş borç bulunmaktadır." | `supheli` | O3: borç iddiası, eylem/link/IBAN yok. |
| SP-06 | "2.000 TL atabilir misin? Akşam öderim." | `supheli` | O5: para isteği var ama G4/G7 kalıbı (numara değişikliği, gizlilik isteği, IBAN, baskı) yok (8). |
| SP-07 | "Evden çalışarak ek gelir! Detaylar için WhatsApp: [TELEFON]" | `supheli` | O4: doğrulanamayan WhatsApp hattına yönlendirme. Para veya bilgi isteği yok. |
| SP-08 | "Y Kargo: Gönderiniz sizi bekliyor. Detay: bit.ly/x9Kq2" | `supheli` | O2: kısaltılmış link. Yalnızca bilgi linki, işlem/ödeme/bilgi girişi **istenmiyor**, bu yüzden G2 değil. Karşılaştır: DL-15. |
| SP-09 | "Z Market: Tüm mağazalarda %50 indirim! Bugün son gün: bit.ly/z7Pq" | `supheli` | "Son gün" zayıf işaret (5.3), ama kısaltılmış link O2 olduğu için şüpheli. |

---

## 3. Dolandırıcılık örnekleri

En az bir güçlü işaret (G1-G7) var. Kategori, **mesajın kullandığı bahaneye** göre seçilir (categories 1).

### 3.1 `odul_kampanya`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-01 | "Tebrikler [AD_SOYAD]! Z Operatörü 15. yıl çekilişinde 50.000 TL kazandınız. Ödülünüzü almak için 24 saat içinde giriş yapın: zoperator-odul.top" | `dolandiricilik` / `odul_kampanya` | G3 (ödül + eylem) ve G2 (resmi olmayan alan adı). Bahane ödül. |
| DL-02 | "Z Market çekilişini kazandınız! Hediye kartınızı göndermek için 25 TL kargo ücretini [IBAN] hesabına yatırın." | `dolandiricilik` / `odul_kampanya` (+ `sahte_odeme`) | G3 + G4. İstenen şey para olsa da bahane ödüldür. Para isteği ikincil kategoridir (categories 1, önemli not). |
| DL-03 | "iPhone kazandınız! Teslimat için tıklayın: bit.ly/k8Lm2" | `dolandiricilik` / `odul_kampanya` | G3: ödül + link eylemi. |
| DL-04 | "Çekilişi kazandınız! Ödülünüzü göndermek için TC kimlik numaranızı ve adresinizi bu mesaja yanıtlayın." | `dolandiricilik` / `odul_kampanya` (+ `kimlik_bilgisi`) | G3 + G6. Bahane ödül, istenen kimlik bilgisi (categories 2.6). |

### 3.2 `sahte_alisveris`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-05 | "Sıfır telefon sadece 9.500 TL, son 3 adet! Ödeme sadece havale: [IBAN]. Sipariş için WhatsApp: [TELEFON]" | `dolandiricilik` / `sahte_alisveris` | G4: peşin IBAN + aşırı iyi fırsat. WhatsApp kanalına çekme de var. |
| DL-06 | "Kiralık 2+1 daire, çok uygun fiyat. Yer göstermem. 15.000 TL depozitoyu önceden [IBAN] hesabına yatırırsanız anahtarı kargoyla gönderirim." | `dolandiricilik` / `sahte_alisveris` | G4: doğrulanamayan ilan için peşin havale + aşırı iyi fırsat. Bahane ilan/satış. |
| DL-07 | "Z Güvenli Ödeme: İlanınız için [AD_SOYAD] ödeme yaptı. Tutarı hesabınıza aktarmak için kart bilgilerinizi girin: zguvenliodeme-onay.top/[TOKEN]" | `dolandiricilik` / `sahte_alisveris` (+ `kimlik_avi`) | G2 + G1. Kullanıcı **satıcı** tarafında (categories 2.2). Bahane ilan/satış, sahte sayfaya kart bilgisi girdirildiği için ikincil `kimlik_avi`. |

### 3.3 `sahte_odeme`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-08 | "Y Kargo: Paketiniz gümrükte bekliyor. 45 TL gümrük ücretini 24 saat içinde [IBAN] hesabına yatırın, aksi halde paketiniz iade edilecektir." | `dolandiricilik` / `sahte_odeme` | G4: ücret talebi + süre baskısı. Kargo teması kategoriyi değiştirmez (categories 2.3). |
| DL-09 | "Trafik cezanız: 1.250 TL. 3 gün içinde ödenmezse %50 artırılır. Ödeme yapmak için kart bilgilerinizi girin: trafik-ceza-ode.click/[TOKEN]" | `dolandiricilik` / `sahte_odeme` (+ `kimlik_avi`) | G1 + G2 + G4. Sahte ödeme sayfasında kart bilgileri isteniyor; bu nedenle ikincil kategori `kimlik_avi`. Bahane ceza. |
| DL-10 | "Merhaba anne, numaram değişti, eskisini sil. Acil para lazım, kimseye söyleme: [IBAN]" | `dolandiricilik` / `sahte_odeme` | G7 (tanıdık taklidi + numara değişikliği + gizlilik isteği + IBAN) ve G4. Tanıdık taklidi + para `sahte_odeme`'dir (categories 2.3). |

### 3.4 `hesap_ele_gecirme`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-11 | "X Bankası: Hesabınız ele geçirilmesin diye telefonunuza gelen 6 haneli kodu bu mesaja yanıtlayın." | `dolandiricilik` / `hesap_ele_gecirme` | G1: kod **doğrudan mesajla** isteniyor. Sahte sayfa yok. |
| DL-12 | "Selam, yanlışlıkla sana bir doğrulama kodu gitti, iletir misin? [AD_SOYAD]" | `dolandiricilik` / `hesap_ele_gecirme` | G1: doğrulama kodu doğrudan isteniyor, karar için bu yeterli. Gönderenin tanıdık biri gibi davrandığı metinden kesin anlaşılmıyorsa G7'ye dayanılmaz. |

### 3.5 `kimlik_avi`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-13 | "Y Kargo: Kargonuz teslim edilemedi, adresinizi güncelleyin: ykargo-teslimat.xyz" | `dolandiricilik` / `kimlik_avi` | G2: kurum adına yazıyor, alan adı resmi değil (ek kelime + `.xyz`), işlem isteniyor. |
| DL-14 | "X Bankası: Hesabınız kısıtlanacaktır. Şifrenizi doğrulamak için: xbankasi.com.tr.dogrula-giris.com" | `dolandiricilik` / `kimlik_avi` | G1 + G2. Alt alan adı hilesi: gerçek alan adı `dogrula-giris.com`. |
| DL-15 | "Y Kargo: Teslimat adresiniz eksik, hemen güncelleyin: bit.ly/x9Kq2" | `dolandiricilik` / `kimlik_avi` | G2: kurum adına + resmi olmayan link + **işlem isteniyor** ("güncelleyin"). Karşılaştır: SP-08. |
| DL-16 | "Y Vergi İdaresi: 3.120 TL vergi iadeniz onaylandı. İadeyi almak için kart bilgilerinizi girin: yvergi-iade.top/[TOKEN]" | `dolandiricilik` / `kimlik_avi` | G3 + G1 + G2. Resmi kurumdan **iade** vaadiyle sahte siteye kart bilgisi girdirildiği için `kimlik_avi`, ödül değil (categories 2.1). |
| DL-17 | E-posta. Konu: "Hesap güvenliğiniz için işlem gerekli". Gövde: "Sayın müşterimiz, hesabınızda şüpheli giriş denemesi tespit edildi. 12 saat içinde doğrulama yapmazsanız hesabınız kapatılacaktır. Doğrulama: https://xbankaasi.com/giris" | `dolandiricilik` / `kimlik_avi` | G2: harf eklemeli taklit alan adı (`xbankaasi.com`). O1 de var, ama G olduğu için sonuç `dolandiricilik`. |

### 3.6 `kimlik_bilgisi`

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-18 | "X Bankası: Kayıtlarınızı güncelliyoruz. TC kimlik numaranızı ve doğum tarihinizi bu mesaja yanıtlayın." | `dolandiricilik` / `kimlik_bilgisi` | G6: kimlik bilgisi mesajla isteniyor, link yok, muğlak "kayıt güncelleme" gerekçesi. |

### 3.7 `diger`

`diger` seçildiğinde `not` alanına türü tek cümleyle yaz.

| No | İçerik | Etiket | Gerekçe |
| --- | --- | --- | --- |
| DL-19 | "Paranızı 3 günde ikiye katlayın! Garantili kazanç. İlk yatırım 5.000 TL: [IBAN]" | `dolandiricilik` / `diger`. `not`: "Sahte yatırım." | G4: para talebi + aşırı iyi fırsat. Hiçbir kategori bahanesine uymuyor. |
| DL-20 | "Evden part-time çalışma, günlük 1.500 TL! Başvuru için 250 TL dosya masrafını [IBAN] hesabına yatırın." | `dolandiricilik` / `diger`. `not`: "Sahte iş ilanı, ön ödeme." | G4: ücret talebi + aşırı iyi fırsat. |
| DL-21 | "Y Kargo: Paketiniz için takip uygulamasını yükleyin: ykargo-takip.xyz/takip.apk" | `dolandiricilik` / `diger`. `not`: "Zararlı uygulama kurdurma." | G5 (+ G2). Dosya/uygulama kurdurma için ayrı kategori yok, labeling_guide 7'ye göre `diger`. |
| DL-22 | E-posta. Konu: "Fatura detayı". Gövde: "Faturanızın detayı ektedir, lütfen açınız." Ek: `Fatura_Detay.pdf.exe` | `dolandiricilik` / `diger`. `not`: "Zararlı ek, çift uzantılı dosya." · `gozden_gecir = true` | G5: bilinmeyen ek açtırma. Dosya açılmaz, yalnızca adı ve uzantısı değerlendirilir (2). Para/bilgi istenmediği için kategori net değil, bu yüzden `gozden_gecir`. |

---

## 4. Tek başına URL

Yalnızca alan adına bakılır (labeling_guide 6.3, 6.2). Metin ve istek olmadığı için bu bölümde G2'deki "istek" koşulu aranmaz: taklit alan adı tek başına `dolandiricilik` sayılır. Bu, labeling_guide 6.3'teki özel kuraldır.

| No | URL | Etiket | Gerekçe |
| --- | --- | --- | --- |
| UR-01 | `https://www.xbankasi.com.tr/giris` | `guvenli` | Kurumun resmi alan adıyla birebir eşleşiyor. |
| UR-02 | `https://xbankasi-dogrula.com` | `dolandiricilik` / `kimlik_avi` | Kurumu taklit ediyor: ek kelime (`-dogrula`). |
| UR-03 | `https://xbankaasi.com.tr` | `dolandiricilik` / `kimlik_avi` | Kurumu taklit ediyor: harf eklemesi. |
| UR-04 | `https://xbankasi.com.tr.guvenli-giris.net` | `dolandiricilik` / `kimlik_avi` | Alt alan adı hilesi: gerçek alan adı `guvenli-giris.net`. |
| UR-05 | `https://xbankasi.xyz` | `dolandiricilik` / `kimlik_avi` | Kurumu taklit ediyor: alışılmadık uzantı. |
| UR-06 | `https://bit.ly/3Qw8z` | `supheli` | Kısaltılmış link, resmi olup olmadığı belirsiz (O2). |
| UR-07 | `https://kampanya-firsat.net/indirim` | `supheli` | Hiçbir bilinen kurumu taklit etmiyor, resmi olup olmadığı belirlenemiyor (O2). |

---

## 5. Ekran görüntüsü (OCR) metni

Metin bozuksa işaret bulabildiğin kadarıyla etiketle (labeling_guide 9).

| No | OCR metni | Etiket | Gerekçe |
| --- | --- | --- | --- |
| OC-01 | "X Bankas1: Hesab1n1z k1s1tland1. Açmak icin: xbankasi-guvenlik.com" | `dolandiricilik` / `kimlik_avi` | Karakter hatalarına rağmen G2 (ek kelimeli alan adı + işlem isteği) okunuyor. |
| OC-02 | "...ınız için lütfen en kısa sürede bilgi..." (metin kesik) | `guvenli` · `gozden_gecir = true`. `not`: "Metin kesik, işaret bulunamadığı için güvenli verildi, inceleme gerekli." | Hiç işaret bulunamıyor ve metin anlaşılamayacak kadar kesik: `guvenli` ver, `gozden_gecir` işaretle (labeling_guide 9). Güvenli olduğu kesin değildir, bu yüzden `not` alanına nedeni yazılır. |

---

## 6. Sınır durumları

Etiketleyicilerin en çok karıştırdığı durumlar. Çoğu **çiftler hâlinde** verilmiştir: iki mesaj birbirine çok benzer ama etiketleri farklıdır.

### 6.1 Kodu bildirmek ve kodu istemek

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| SN-01 | "Doğrulama kodunuz: [KOD]. Kimseyle paylaşmayın." | `guvenli` | Kodu **bildiriyor**. |
| SN-02 | "X Bankası: Hesabınıza giriş denemesi var. Gelen [KOD] kodunu bu mesaja yanıtlayın." | `dolandiricilik` / `hesap_ele_gecirme` | Kodu **istiyor** (G1). |
| SN-03 | "Selam, telefonuna gelen doğrulama kodunu söyler misin?" | `dolandiricilik` / `hesap_ele_gecirme` | G1: doğrulama kodu isteniyor. Kod isteği O5 değildir, her zaman G1'dir. |

### 6.2 Çekiliş: eylem var mı?

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| SN-04 | "Tebrikler, çekilişi kazandınız!" | `supheli` | O3: eylem yok. |
| SN-05 | "Tebrikler, çekilişi kazandınız! Ödül için giriş yapın: zoperator-odul.top" | `dolandiricilik` / `odul_kampanya` | G3: eylem (link) var. |

### 6.3 Aynı tür mesaj, farklı sonuç: tanıdıktan para isteği

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| SN-06 | "Merhaba, numaram değişti, eskisini sil. Acil para lazım, kimseye söyleme: [IBAN]" | `dolandiricilik` / `sahte_odeme` | Klasik kalıp: numara değişikliği + gizlilik + IBAN (G7). |
| SN-07 | "Müsaitsen 500 TL atabilir misin?" | `supheli` | Yalnızca kısa para isteği (O5). |

### 6.4 Kart hareketi iddiası

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| SN-08 | "X Bankası: [KART_SON4] kartınızdan 4.850 TL harcama yapıldı. İtiraz için [TELEFON] numarasını arayın." | `supheli` | O4: doğrulanamayan telefona yönlendirme. Tutar/kart sonu rutin bildirim gibi görünse de arama yönlendirmesi orta işarettir. |
| SN-09 | "X Bankası: [KART_SON4] kartınızdan 4.850 TL harcama yapıldı. İptal için kart bilgilerinizi girin: xbankasi-itiraz.com" | `dolandiricilik` / `kimlik_avi` | G1 + G2. Güçlü işaret orta işareti bastırır. |

### 6.5 Güven verici unsurlar kararı değiştirmez

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| SN-10 | "Değerli müşterimiz, X Bankası Güvenlik Birimi olarak hesabınızda yetkisiz erişim tespit ettik. Hesabınızı korumak için kart bilgilerinizi doğrulayın: xbankasi-guvenlik.com. Saygılarımızla, X Bankası Müşteri Hizmetleri" | `dolandiricilik` / `kimlik_avi` | Düzgün dil, kurum adı, resmi ton var, ama G1 + G2 var (6.1). Aynı anda O1 de var, sonuç yine `dolandiricilik`. |
| SN-11 | "X Bankası: Yeni mobil uygulama sürümümüz yayında." | `guvenli` | Güven verici unsur, risk işareti olmayan içeriği şüpheli yapmaz, çünkü işaret yok (6.1). |

### 6.6 Alan adı resmi mi? (labeling_guide 6.2)

Mesajda kurum "X Bankası" (resmi alan adı `xbankasi.com.tr`) olsun.

| Alan adı | Resmi mi? | Neden |
| --- | --- | --- |
| `xbankasi.com.tr` | Evet | Birebir eşleşme. |
| `xbankaasi.com.tr` | Hayır | Harf eklemesi. |
| `xbankasi-guvenlik.com` | Hayır | Ek kelime. |
| `xbankasi.xyz` | Hayır | Alışılmadık uzantı. |
| `xbankasi.com.tr.giris-yap.com` | Hayır | Alt alan adı hilesi. |
| `xbankasi.com` | Belirsiz | Birebir eşleşmiyor. Kurumun sitesinden kontrol et (linke tıklama). Hâlâ emin değilsen O2 say (`supheli`) ve `gozden_gecir = true` yap. |

### 6.7 Kategori seçimi: sık karışan çiftler (categories 3)

| No | İçerik | Etiket | Neden |
| --- | --- | --- | --- |
| KT-01 | "Hesabınız kapatılacak, şifrenizi doğrulamak için linke tıklayın: xbankasi-dogrula.com" | `kimlik_avi` | Bilgi **sahte sayfaya** girdiriliyor. |
| KT-02 | "Hesabınız ele geçirilmesin, SMS kodunu bu numaraya yanıtlayın." | `hesap_ele_gecirme` | Bilgi **mesajla** iletiliyor. |
| KT-03 | "Vergi iadeniz onaylandı, kart bilgilerinizi girin: yvergi-iade.top/[TOKEN]" | `kimlik_avi` | Resmi kurumdan iade vaadi + sahte siteye kart bilgisi girdirme, ödül değil. |
| KT-04 | "Çekilişi kazandınız, 25 TL kargo ücretini ödeyin: [IBAN]" | `odul_kampanya` (+ `sahte_odeme`) | Bahane ödül, para isteği ikincil. |
| KT-05 | "Paketiniz gümrükte, 45 TL ücreti 24 saat içinde [IBAN] hesabına yatırın." | `sahte_odeme` | Bahane yükümlülük (ücret). Kargo teması kategoriyi değiştirmez. |
| KT-06 | "Yarı fiyatına telefon, sadece IBAN'a havale: [IBAN]" | `sahte_alisveris` | Kullanıcı bir ürünü **satın almaya** yönlendiriliyor. |
| KT-07 | "TC kimlik numaranızı yanıtlayın, kaydınızı güncelleyelim." | `kimlik_bilgisi` | Belirgin hikâye ve link yok, kimlik bilgisi mesajla isteniyor. |
| KT-08 | "Merhaba anne, numaram değişti, acil para lazım: [IBAN]" | `sahte_odeme` | Tanıdık taklidi + para. |

---

## 7. Sık yapılan hatalar

- **"Para istiyor, o hâlde `sahte_odeme`."** Hayır. Önce bahaneye bak (categories 1). Ödül bahanesi `odul_kampanya`, satış bahanesi `sahte_alisveris`'tir.
- **"Link var, o hâlde şüpheli veya dolandırıcılık."** Hayır. Link tek başına zayıf işarettir. Resmi alan adlı ve bir şey istemeyen link `guvenli`'dir.
- **"Yazım hatası çok, o hâlde dolandırıcılık."** Hayır. Yazım hatası zayıf işarettir (GV-07).
- **"Resmi görünüyor, o hâlde güvenli."** Hayır. G işareti varsa resmi ton kararı değiştirmez (SN-10).
- **"Şifre/kod kelimesi geçiyor, o hâlde G1."** Hayır. G1 için bilgi **istenmeli**. Uyarı mesajları `guvenli`'dir (GV-02, GV-03).
- **Kategori `guvenli`/`supheli` kayda yazılmaz.** Kategori yalnızca `dolandiricilik` içindir.
- **Emin değilsen etiketi boş bırakma.** Akışı uygula, en yakın etiketi ver, `gozden_gecir = true` yap.

---

## 8. Sürüm geçmişi

| Sürüm | Değişiklik |
| --- | --- |
| v0.1 | İlk taslak. |
