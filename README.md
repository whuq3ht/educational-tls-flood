# 🔒 ATCKLabs TLS Flood Tester

Bu proje, yalnızca **eğitim ve laboratuvar ortamında kullanılmak üzere** geliştirilmiş basit bir **TLS Flood test aracıdır**. Python kullanılarak yazılmıştır ve manuel olarak IP, port ve süre girilerek çalışır.

> ⚠️ Uyarı: Bu araç yalnızca **izinli sunucular üzerinde** test amacıyla kullanılmalıdır. İzinsiz kullanımı yasa dışıdır ve etik dışıdır. Kullanıcı tüm sorumluluğu kabul eder.

---

## 🎯 Özellikler

- TLS (443) üzerinden çoklu bağlantı oluşturarak test trafiği gönderir  
- Eğitim amaçlı özel HTTP header’lar içerir  
- Manuel olarak IP, port ve süre girme desteği  
- 100 eş zamanlı thread ile çalışır  
- Ctrl+C (KeyboardInterrupt) desteğiyle anında durdurulabilir  
- Ek paket gerektirmez

---

## 💻 Kurulum ve Kullanım

### 1. Python 3.x gereklidir

```bash
python --version

2. Projeyi indir

git clone https://github.com/whuq3ht/tls-flooder.git
cd tls-flooder

4. Girişleri yap

Hedef IP veya domain: 127.0.0.1
Port (örnek: 443): 443
Saldırı süresi (saniye): 10

🧪 Örnek Header'lar
Aşağıdaki gibi özel HTTP başlıkları kullanılır:

User-Agent: ATCKLabs Testing DDoS Script/1.0 (Educational Only)
X-Test-Notice: This traffic is part of an authorized stress test by ATCKLabs.
X-Purpose: Educational Testing Only - Not Malicious

📁 Dosya Yapısı

tls-flooder/
├── tls_flood.py      # Ana script
└── README.md         # Açıklama dosyası

📌 Notlar
Saldırı süresi dolunca tüm thread’ler otomatik olarak kapanır.

Script, tüm test yükünü tek bir hedef IP'ye yönlendirir.

Geliştirme ortamları: Linux, macOS, Windows desteklidir.

⚖️ Lisans & Etik Kullanım
Bu proje MIT Lisansı ile lisanslanmıştır.
Kötüye kullanım kullanıcının sorumluluğundadır.

👨‍💻 Geliştirici
ATCKLabs tarafından geliştirilmiştir.
🧠 atcklabs.eu
🐍 GitHub: @whuq3ht
📷 Instagram: @haktan0zturk
