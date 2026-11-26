# Kalkan - Dolandırıcılık Kategorileri

**Sürüm:** v0.1 (taslak) · **İlgili dosyalar:** [labeling_guide.md](labeling_guide.md), [examples.md](examples.md)

## Amaç

Bu dosya, `dolandiricilik` olarak etiketlenen içeriklerin hangi kategoriye ayrılacağını tanımlar. Amaç, aynı mesaja farklı kişilerin farklı kategori vermesini önlemek ve yapay zeka modelinin kategori ayrımını tutarlı verilerle öğrenmesini sağlamaktır. Sınıf (güvenli/şüpheli/dolandırıcılık) kararı için [labeling_guide.md](labeling_guide.md) kullanılır.

Kategori **yalnızca `sinif = dolandiricilik`** olan içeriklere verilir. `guvenli` ve `supheli` kayıtlarda `kategori` boş kalır. Değerlerin İngilizce karşılıkları başlıklarda ve 1. bölümdeki tabloda `Türkçe / İngilizce` biçiminde gösterilmiştir; tam liste için [labeling_guide.md](labeling_guide.md) 3.1.

## 1. Kategori nasıl seçilir?

Kategoriyi **mesajın kullandığı bahane (hikâye)** belirler, kullanıcıdan istenen şey ikinci planda kalır. Aşağıdaki tabloyu yukarıdan aşağıya uygula, ilk uyan satır `kategori` olur. Başka bir satır da uyuyorsa onu `ikincil_kategori` olarak yaz (en fazla 1 tane).

| Sıra | Mesajdaki bahane | Kategori |
| --- | --- | --- |
| 1 | Ödül, çekiliş, hediye, kampanya kazancı | `odul_kampanya` / `prize_scam` |
| 2 | Ürün/ilan/satış, aşırı ucuz fırsat, alışveriş | `sahte_alisveris` / `fake_shopping` |
| 3 | Borç, fatura, ceza, harç, kargo/gümrük ücreti, ödeme zorunluluğu; tanıdık/yakın taklidiyle acil para isteği | `sahte_odeme` / `fake_payment` |
| 4 | Hesap güvenliği bahanesiyle **şifre/doğrulama kodunun doğrudan paylaşılması** (yanıt, telefonda söyleme) | `hesap_ele_gecirme` / `account_takeover` |
| 5 | Hesap, iade, güncelleme veya doğrulama bahanesiyle **sahte link/site üzerinden** giriş, kart veya kişisel bilgi girdirme | `kimlik_avi` / `phishing` |
| 6 | Belirgin bir hikâye yok; mesajla/yanıtla **kimlik bilgisi** isteniyor, link yok | `kimlik_bilgisi` / `identity_theft` |
| 7 | Yukarıdakilerin hiçbiri | `diger` / `other` |

> **Önemli:** Kullanıcıdan para isteniyor diye otomatik `sahte_odeme` seçme. Önce bahaneye bak. Ödül kazandın diyip "kargo ücreti" isteyen mesaj `odul_kampanya`'dır (`ikincil_kategori`: `sahte_odeme`).

> **Tanıdık taklidi:** Tanıdık gibi davranıp **para** isteyen mesaj satır 3'tür (`sahte_odeme`). Tanıdık gibi davranıp **kod** isteyen mesaj ("yanlışlıkla sana kod gitti") satır 4'tür (`hesap_ele_gecirme`).

## 2. Kategori tanımları

### 2.1 `odul_kampanya` / `prize_scam` - Ödül ve Kampanya Dolandırıcılığı

- **Tanım:** Gerçek olmayan ödül, çekiliş, hediye veya kampanya kazancı vaadiyle kullanıcıyı kandırmaya çalışan içerik.
- **Tipik talepler:** Linke tıklama, kişisel/kart bilgisi girme, "işlem/kargo ücreti" ödeme.
- **Tipik işaretler:** Katılmadığın bir çekilişi kazanma, "tebrikler", süre sınırı, resmi olmayan alan adı.
- **Ayırt etme:** Vaat edilen şey ödül/hediye ise, istenen şey para veya bilgi olsa bile bu kategoridir. Resmi kurumdan **iade/alacak** vaadiyle sahte bağlantı veya site üzerinden giriş ya da kişisel bilgi isteniyorsa `kimlik_avi` olur.

### 2.2 `sahte_alisveris` / `fake_shopping` - Sahte Alışveriş ve Satış

- **Tanım:** Var olmayan ürün, ilan veya fırsat üzerinden kullanıcıdan peşin ödeme alıp zarara uğratmayı amaçlayan içerik.
- **Tipik talepler:** Peşin havale/IBAN, "ön ödeme", sadece belirli kanaldan satış.
- **Tipik işaretler:** Piyasa fiyatının çok altında fiyat, "son X adet", güvenli ödeme/teslimat seçeneğinin olmaması, farklı kanala (WhatsApp vb.) çekme.
- **Ayırt etme:** Kullanıcı bir ürün **satın almaya** yönlendiriliyorsa bu kategoridir. Kullanıcıdan **borç/ceza/ücret** isteniyorsa `sahte_odeme`'dir. Kullanıcı **satıcı** tarafındaysa da (ilan sahibi) bu kategori geçerlidir: alıcı gibi davranıp "ödeme yaptım, onaylamak için kart bilgilerini gir" diyerek sahte sayfaya yönlendiren mesaj `sahte_alisveris`'tir. Sahte sayfa bilgi girdirdiği için `ikincil_kategori` olarak `kimlik_avi` yazılır.

### 2.3 `sahte_odeme` / `fake_payment` - Sahte Ödeme ve Para Talebi

- **Tanım:** Gerçek olmayan borç, fatura, ceza, harç veya ücret gerekçesiyle para isteyen içerik. Tanıdık taklidi ile acil para isteyen mesajlar da buraya girer.
- **Tipik talepler:** IBAN'a havale, sahte ödeme linki, kartla ödeme.
- **Tipik işaretler:** Gecikme/artış tehdidi, kısa süre sınırı, kurum adıyla ama kurumun olmayan IBAN/link ile ödeme isteği.
- **Ayırt etme:** Bahane bir **yükümlülüktür** (borç, ceza, ücret). Bahane ödül veya satışsa o kategori geçerlidir. Kargo/gümrük ücreti, trafik cezası, vergi veya harç borcu gibi senaryolarda para/ödeme isteniyorsa kurum teması (kargo, kamu, vergi) kategoriyi değiştirmez, bu kategori seçilir. Mesaj ayrıca giriş veya kart bilgisi girdiren sahte bir sayfaya yönlendiriyorsa `ikincil_kategori` olarak `kimlik_avi` yazılır.

### 2.4 `hesap_ele_gecirme` / `account_takeover` - Hesap Ele Geçirme

- **Tanım:** Kullanıcının hesabına erişmek için şifre veya doğrulama kodunu **doğrudan** paylaşmasını isteyen içerik.
- **Tipik talepler:** "Gelen kodu bu numaraya yanıtla", "kodu bana ilet", şifreyi mesajla/telefonda söyletme.
- **Tipik işaretler:** "Hesabın ele geçirilmesin diye", "yanlışlıkla sana kod gitti", gönderenin tanıdık gibi davranması.
- **Ayırt etme:** Bilgi **mesajla veya telefonla iletiliyorsa** bu kategoridir. Bilgi **sahte bir sayfaya girdiriliyorsa** `kimlik_avi`'dir.

### 2.5 `kimlik_avi` / `phishing` - Kimlik Avı (Oltalama)

- **Tanım:** Sahte link, sahte site veya kurum taklidi ile kullanıcıya giriş bilgisi, kart bilgisi veya kişisel bilgi girdiren içerik.
- **Tipik talepler:** "Giriş yap", "bilgilerini doğrula", "iadeyi almak için kart bilgilerini gir".
- **Tipik işaretler:** Kurumu taklit eden alan adı (bkz. labeling_guide 6.2), "hesabınız kısıtlanacak" tehdidi, resmi tonda mesaj.
- **Ayırt etme:** Kullanıcıyı **bir siteye yönlendirip bilgi girdirme** varsa bu kategoridir. Bilgi mesajla paylaştırılıyorsa `hesap_ele_gecirme` veya `kimlik_bilgisi`'dir. Kargo ("adresinizi doğrulayın"), banka ("hesabınız kısıtlanacak") veya vergi dairesi ("iadeniz onaylandı") adına gelip sahte siteye giriş, kart veya kişisel bilgi girdirenler buraya girer. Aynı kurum temasında asıl istek para ödemesiyse `sahte_odeme`'dir.

### 2.6 `kimlik_bilgisi` / `identity_theft` - Kimlik Bilgisi Hırsızlığı

- **Tanım:** Belirgin başka bir bahane olmadan, kimlik bilgilerini (TC kimlik no, doğum tarihi, adres, anne kızlık soyadı) mesaj veya yanıt yoluyla isteyen içerik.
- **Tipik talepler:** "TC kimlik numaranızı ve adresinizi yanıtlayın."
- **Tipik işaretler:** Sebep belirtmeden veya "kayıt güncelleme" gibi muğlak gerekçeyle bilgi isteme, link olmaması.
- **Ayırt etme:** Link/site varsa `kimlik_avi`'dir. Ödül, satış, borç gibi bir hikâye varsa o hikâyenin kategorisi seçilir ve bu kategori `ikincil_kategori` olabilir.

### 2.7 `diger` / `other` - Diğer

- **Tanım:** Güçlü bir dolandırıcılık işareti (G1-G7) taşıyan ama yukarıdaki kategorilere girmeyen içerik. Sahte bahis veya duygusal ilişki gibi türlerde para/ödeme talebi ya da baskı yoksa G işareti oluşmaz. Bu durumda sınıf karar akışına göre belirlenir (genellikle `supheli`) ve kategori verilmez.
- **Tipik talepler:** Yatırım adı altında para, sahte iş ilanı için ön ödeme veya bilgi, duygusal ilişki bahanesiyle para, sahte bahis sitesine yönlendirme, zararlı dosya/uygulama veya uzak erişim uygulaması kurdurma (G5).
- **Tipik işaretler:** "Paranı ikiye katla", garantili kazanç, kısa sürede yüksek getiri, tanışmadığın biriyle hızla yakınlaşma, işe alım için ücret isteme.
- **Ayırt etme:** Önce 2.1-2.6'yı dene. Hiçbirine uymuyorsa `diger` seç ve `not` alanına türü tek cümleyle yaz (örn. "sahte yatırım"). Aynı tür sık görülürse yeni bir kategori olarak kılavuza eklenir.

## 3. Kategoriler arası sık karışan durumlar

| Durum | Karar |
| --- | --- |
| "Hesabınız kapatılacak, şifrenizi doğrulamak için linke tıklayın" | `kimlik_avi` (link var) |
| "Hesabınız ele geçirilmesin, SMS kodunu bu numaraya yanıtlayın" | `hesap_ele_gecirme` (kod doğrudan paylaştırılıyor) |
| "Vergi iadeniz onaylandı, kart bilgilerinizi girin: [link]" | `kimlik_avi` (resmi kurumdan iade; ödül değil) |
| "Çekilişi kazandınız, 25 TL kargo ücretini ödeyin" | `odul_kampanya`, ikincil: `sahte_odeme` |
| "Paketiniz gümrükte, 45 TL ücreti 24 saat içinde [IBAN] hesabına yatırın" | `sahte_odeme` |
| "Yarı fiyatına telefon, sadece IBAN'a havale" | `sahte_alisveris` |
| "TC kimlik numaranızı yanıtlayın, kaydınızı güncelleyelim" | `kimlik_bilgisi` |
| "Merhaba anne numaram değişti, acil para lazım: [IBAN]" | `sahte_odeme` (tanıdık taklidi + para) |
| "Yanlışlıkla sana bir kod gitti, iletir misin?" | `hesap_ele_gecirme` (tanıdık taklidi + kod) |
| "İlanınız için ödeme yapıldı, tutarı almak için kart bilgilerinizi girin: [link]" | `sahte_alisveris`, ikincil: `kimlik_avi` (satıcı tarafı) |
| "Paketiniz için uygulamayı yükleyin: [APK linki]" | `diger` (`not`: "zararlı uygulama kurdurma") |

## 4. Sürüm geçmişi

| Sürüm | Değişiklik |
| --- | --- |
| v0.1 | İlk taslak. |
