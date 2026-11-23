# Kalkan - Etiketleme Kılavuzu

**Sürüm:** v0.1 (taslak) · **İlgili dosyalar:** [categories.md](categories.md), [examples.md](examples.md)

## 1. Amaç ve kapsam

Bu kılavuz, Kalkan için hazırlanan Türkçe veri setindeki içeriklerin **aynı kurallarla, tutarlı biçimde** etiketlenmesini sağlar. Etiketlenen veri, yapay zeka ekibinin metin sınıflandırma modelini eğitmek ve değerlendirmek için kullanılır. Bu yüzden amaç "doğru tahmin etmek" değil, **kılavuzdaki kuralları herkesle aynı şekilde uygulamaktır**.

Her içerik üç sınıftan birine ayrılır: **güvenli**, **şüpheli**, **dolandırıcılık**. Dolandırıcılık olarak etiketlenen içeriklere ayrıca bir **kategori** verilir (bkz. [categories.md](categories.md)).

## 2. Etiketlenen içerik türleri

| Tür | Not |
| --- | --- |
| SMS / mesajlaşma metni | Ana veri türü. |
| E-posta | Konu satırı + gövde metni birlikte değerlendirilir. |
| Tek başına URL | Yalnızca alan adına bakılır (bkz. 6.3). |
| Ekran görüntüsünden çıkarılan (OCR) metin | Metin bozuksa bkz. 9. |
| Dosya ve eklerden çıkarılan metin | Dosya adı, uzantısı ve içinden çıkarılan metin birlikte değerlendirilir. Dosya açılmaz veya çalıştırılmaz. Dosya/uygulama kurdurma isteği G5 kapsamındadır. |

## 3. Etiket alanları

Her kayıt için doldurulacak alanlar:

| Alan | Değerler | Zorunlu mu? |
| --- | --- | --- |
| `sinif` | `guvenli`, `supheli`, `dolandiricilik` | Evet |
| `kategori` | `kimlik_avi`, `sahte_odeme`, `hesap_ele_gecirme`, `kimlik_bilgisi`, `sahte_alisveris`, `odul_kampanya`, `diger` | Yalnızca `dolandiricilik` ise. Diğer sınıflarda boş bırakılır. |
| `ikincil_kategori` | `kategori` ile aynı değerler | Hayır. En fazla 1 tane. Yalnızca `kategori` doluysa verilir ve `kategori`'den farklı olmalıdır. |
| `gozden_gecir` | `true` / `false` | Evet (varsayılan `false`) |
| `not` | Tek cümle serbest metin | Hayır. `kategori = diger` ise zorunlu. Kişisel veri yazılmaz. |

### 3.1 İngilizce karşılıklar

Kod, API ve model tarafında kullanılabilmesi için tüm alan adlarının ve değerlerin İngilizce karşılığı:

| Türkçe (bu kılavuz) | İngilizce |
| --- | --- |
| `sinif` | `label` |
| `guvenli` | `safe` |
| `supheli` | `suspicious` |
| `dolandiricilik` | `fraud` |
| `kategori` | `category` |
| `kimlik_avi` | `phishing` |
| `sahte_odeme` | `fake_payment` |
| `hesap_ele_gecirme` | `account_takeover` |
| `kimlik_bilgisi` | `identity_theft` |
| `sahte_alisveris` | `fake_shopping` |
| `odul_kampanya` | `prize_scam` |
| `diger` | `other` |
| `ikincil_kategori` | `secondary_category` |
| `gozden_gecir` | `needs_review` |
| `not` | `note` |

Kılavuzda okunabilirlik için Türkçe adlar kullanılır. Veri setinde ve kodda İngilizce adlar kullanılacaksa bu tablo bire bir eşleme olarak esas alınır.

## 4. Üç sınıfın tanımı

### 4.1 Güvenli

İçerikte **güçlü veya orta düzey hiçbir risk işareti yoktur** (bkz. 5). Kullanıcıdan şifre, kod veya kart bilgisi istemez; resmi olmayan bir kanala para gönderilmesini istemez; kullanıcıyı korkutmaz veya baskı altında bırakmaz. Resmi alan adlı bir fatura/ödeme hatırlatması, tehdit içermedikçe güvenlidir.

- Yazım hatası, link bulunması veya bilinmeyen/doğrulanamayan gönderici (zayıf işaretler) tek başına içeriği şüpheli yapmaz.
- Reklam ve kampanya mesajları, risk işareti taşımadıkça güvenlidir.

### 4.2 Şüpheli

İçerikte **en az bir orta düzey risk işareti** vardır, ama dolandırıcılığı kanıtlayan güçlü bir işaret yoktur. Yani içerik kötü niyetli olabilir, ancak eldeki bilgiyle bunu söylemek için yeterli neden yoktur.

### 4.3 Dolandırıcılık

İçerikte **en az bir güçlü risk işareti** vardır: kullanıcıyı kandırarak para, şifre, doğrulama kodu, kart veya kimlik bilgisi almayı ya da zararlı bir dosyayı/uygulamayı kurdurmayı amaçlayan açık bir kalıp.

> Dolandırıcılık etiketi için "kesin kanıt" aranmaz; 5.1'deki kalıplardan birinin metinde **görünmesi** yeterlidir.

## 5. Risk işaretleri

### 5.1 Güçlü işaretler (en az biri varsa: `dolandiricilik`)

| Kod | İşaret |
| --- | --- |
| G1 | Şifre, SMS/tek kullanımlık doğrulama kodu, kart bilgisi (numara, CVV, son kullanma tarihi) veya internet bankacılığı bilgisi isteniyor. |
| G2 | Bir kurum/marka adına yazılıyor, **link resmi alan adına ait değil** ve kullanıcıdan işlem/ödeme/bilgi girişi isteniyor. |
| G3 | Beklenmedik bir **ödül, çekiliş, hediye veya iade vaadi** var ve kullanıcıdan bir eylem isteniyor (link, bilgi, ücret). |
| G4 | **Para/ödeme talebi** var (borç, ceza, harç, ücret, doğrulanamayan satış için peşin havale/IBAN) ve baskı, tehdit, acelecilik veya aşırı iyi bir fırsat eşlik ediyor. |
| G5 | Kullanıcıdan **dosya veya uygulama kurması** (APK, uzak erişim uygulaması vb.) ya da bilinmeyen bir ek açması isteniyor. |
| G6 | Mesajla/link ile **kimlik bilgisi** isteniyor (TC kimlik no, doğum tarihi, adres, anne kızlık soyadı vb.). |
| G7 | Tanıdık biri gibi davranılıp klasik bir kalıpla acil para veya kod isteniyor (örn. "numaram değişti, acil para lazım", "yanlışlıkla sana kod gitti, iletir misin"). |

**G2 notu:** "İşlem/ödeme/bilgi girişi isteniyor" ifadesi, "güncelleyin", "doğrulayın", "giriş yapın", "ödeyin" gibi açık bir istek anlamına gelir. Yalnızca bilgi vermek için konmuş bir link ("takip için", "detaylar için") işlem isteği sayılmaz. Link resmi değilse bu durumda O2'ye bak.

### 5.2 Orta işaretler (güçlü işaret yoksa ve en az biri varsa: `supheli`)

| Kod | İşaret |
| --- | --- |
| O1 | Olumsuz sonuç tehdidi veya korkutma: hesap kapanacak/kısıtlanacak, ceza, "olağan dışı işlem tespit edildi" gibi belirsiz uyarılar. (Reklamdaki "son gün!" gibi acelecilik ve tutar/yer/kart sonu içeren rutin harcama bildirimleri bu gruba girmez.) |
| O2 | Doğrulanamayan veya kısaltılmış link (bit.ly vb.), ya da alan adının resmi olup olmadığı belirlenemiyor. |
| O3 | Beklenmedik ödül, iade veya borç iddiası var, ancak kullanıcıdan eylem istenmiyor. |
| O4 | Doğrulanamayan bir geri arama kanalına yönlendirme (bilinmeyen telefon, WhatsApp hattı vb.). |
| O5 | Para isteği var, ancak G4/G7 kalıbı tamamlanmıyor (baskı, tehdit, acelecilik, IBAN/link, numara değişikliği gibi unsurlar yok). Örn. kısa bir "2.000 TL atabilir misin?" mesajı. Doğrulama kodu isteği O5 değildir, her zaman G1'dir. |

### 5.3 Zayıf işaretler (tek başına etiketi değiştirmez)

- Yazım ve dil bilgisi hataları
- Bilinmeyen/doğrulanamayan gönderici
- Mesajda link veya ek bulunması
- Reklam dili, indirim, "son gün" gibi ticari acelecilik
- Gönderici adı olarak bir kurum adının görünmesi (güven göstergesi sayılmaz, risk göstergesi de sayılmaz)

## 6. Karar akışı

Her içerik için sırayla:

1. **Yalnızca eldeki bilgiye dayan:** metin, görünen gönderici, link/alan adı, ek bilgisi. Linke tıklama, kurumu arama, tahmin yürütme. (İstisna: alan adı kontrolü için bkz. 6.2.)
2. **Güçlü işaret (G1-G7) var mı?** Varsa → `dolandiricilik`, sonra kategori seç.
3. **Yoksa orta işaret (O1-O5) var mı?** Varsa → `supheli`.
4. **İkisi de yoksa** → `guvenli`.
5. Emin olamadığın yer varsa `gozden_gecir = true` yap (bkz. 9). Etiketi yine de ver.

### 6.1 Karışık sinyaller

- Güçlü işaret varsa, içerikteki güven verici unsurlar (kurum adı, düzgün dil, logo, resmi görünen gönderici adı) **kararı değiştirmez**.
- İçerikte hem güçlü hem orta işaret varsa sonuç `dolandiricilik` olur.
- Güven verici unsurlar, hiç risk işareti olmayan bir içeriği `supheli` yapmaz.

### 6.2 Alan adı resmi mi?

Mesajda adı geçen kurumun alan adıyla **birebir** eşleşiyorsa resmidir. Şunlar resmi sayılmaz:

- Harf değişimi veya eklemesi (`banka` yerine `banka-`, `bankaa` vb.)
- Ek kelime (`-guvenlik`, `-dogrula`, `-iade`, `-giris`)
- Alışılmadık uzantı (`.xyz`, `.top`, `.click` vb.)
- Alt alan adı hilesi (`kurum.baska-site.com`)

Emin değilsen alan adını kurumun kendi sitesinden (tarayıcıya elle yazarak) karşılaştırabilirsin. Mesajdaki linke tıklama. Hâlâ emin değilsen O2 (orta işaret) say.

### 6.3 Tek başına URL

- Bilinen bir kurumu taklit eden alan adı → `dolandiricilik` (kategori: `kimlik_avi`)
- Resmi olup olmadığı belirsiz veya kısaltılmış → `supheli`
- Bilinen resmi alan adı → `guvenli`

Bu bölüm yalnızca tek başına URL için geçerli özel bir kuraldır. Metin olmadığı için G2'deki "istek" koşulu aranmaz.

## 7. Kategori seçimi (özet)

Yalnızca `dolandiricilik` etiketli içeriklere verilir. Kategoriyi **mesajın kullandığı bahane (hikâye)** belirler. Ayrıntı ve karar tablosu: [categories.md](categories.md).

- Birden fazla kategori uyuyorsa asıl bahaneye göre `kategori`, ikinci en uygun olanı `ikincil_kategori` olarak seç.
- Hiçbiri uymuyorsa `diger` seç ve `not` alanına tek cümleyle yaz.
- Dosya/uygulama kurdurma (G5) için ayrı bir kategori yoktur: bahane başka bir kategoriye uymuyorsa `diger` seç ve `not` alanına yaz.

## 8. Sınır durumları (özet kurallar)

Ayrıntılı örnekler [examples.md](examples.md) dosyasındadır.

- Gerçek bir kurumun "size şifre/kod sormayız" tarzı uyarı mesajı → `guvenli`.
- Doğrulama kodunu **bildiren** ve "kimseyle paylaşmayın" diyen mesaj → `guvenli`. Kodu **isteyen** mesaj → `dolandiricilik` (G1/G7).
- Resmi alan adlı link içeren, kullanıcıdan bilgi/ödeme istemeyen mesaj → `guvenli`.
- Kısaltılmış link + bağlam yok → `supheli`.
- Bilinmeyen göndericiden gelen, risk işareti taşımayan mesaj → `guvenli`.
- Çok hatalı yazılmış ama risk işareti olmayan mesaj → `guvenli`.
- "Çekilişi kazandınız" der ama eylem istemez → `supheli` (O3). Eylem isterse → `dolandiricilik` (G3).
- Kart/hesap hareketi iddiası + bilinmeyen telefona yönlendirme → `supheli` (O4). Mesaj ayrıca "olağan dışı işlem" gibi belirsiz bir uyarı içeriyorsa O1 de eklenir. Tutar/yer/kart sonu içeren rutin harcama bildirimi tek başına O1 sayılmaz.
- Tanıdık numaradan "acil para" mesajı: klasik dolandırıcılık kalıbı varsa (numara değişikliği, gizlilik isteği, hemen IBAN) → `dolandiricilik`; yalnızca kısa bir para isteği varsa → `supheli`.

## 9. Emin olamadığında

- İçerik anlaşılamayacak kadar bozuksa (OCR hatası, kesik metin): işaret bulabildiğin kadarıyla etiketle, bulamıyorsan `guvenli` ver ve `gozden_gecir = true` yap.
- İki sınıf arasında kararsızsan, 6. bölümdeki akışı tekrar uygula. Akış sonucu belirliyorsa o sonucu kullan.
- Akış da belirsizse (kılavuzda karşılığı olmayan yeni bir durum) en yakın sınıfı ver, `gozden_gecir = true` yap ve `not` alanına durumu yaz. Bu vakalar kılavuza eklenmek üzere toplanır.

## 10. Kişisel veriler ve maskeleme

Veri setine **gerçek kişisel veri girmez** (KVKK). Etiketlemeden önce şu alanlar yer tutucuyla değiştirilir:

| Veri | Yer tutucu |
| --- | --- |
| Telefon numarası | `[TELEFON]` |
| TC kimlik numarası | `[TC_NO]` |
| IBAN | `[IBAN]` |
| Kart numarası | `[KART_NO]` (son 4 hane gösteriliyorsa `[KART_SON4]`) |
| Doğrulama/tek kullanımlık kod | `[KOD]` |
| Ad soyad | `[AD_SOYAD]` |
| Adres | `[ADRES]` |
| E-posta adresi | `[E_POSTA]` |
| Link içindeki kişiye özel parametre/token | `[TOKEN]` |

Maskelenmeyenler (model için gerekli): **alan adı**, **tutar**, **tarih**, **kurum adı**.

Örneklerde ve notlarda gerçek bir kişinin bilgisi kullanılmaz. Örnek hazırlarken gerçek kurum adı yerine "X Bankası", "Y Kargo" gibi genel adlar kullanılır.

## 11. Kalite kontrol ve anlaşmazlıklar

- Veri setinin bir kısmı (öneri: yaklaşık %10) iki farklı kişi tarafından bağımsız etiketlenir ve uyum ölçülür.
- İki etiket farklıysa Veri Bilimi alan yöneticisi (atanana kadar etiketleme alt ekibi sorumlusu) veya görevlendirdiği kişi karar verir. Karar, kılavuza yeni bir kural olarak işlenir.
- `gozden_gecir = true` kayıtları düzenli aralıklarla toplanır ve kılavuz güncellemesinde kullanılır.
- Kılavuz değişince eski etiketlerin etkilenip etkilenmediği kontrol edilir ve sürüm geçmişine yazılır.

## 12. Sürüm geçmişi

| Sürüm | Değişiklik |
| --- | --- |
| v0.1 | İlk taslak. |
