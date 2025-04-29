import socket
import os

def honeypot():
    # Kullanıcıdan IP adresi ve port bilgisi al
    host = input("Dinlenecek IP adresini girin (ör. 0.0.0.0): ")
    port = int(input("Dinlenecek port numarasını girin (ör. 9999): "))
    
    # Log dosyasını otomatik oluştur
    log_file = "honeypot_log.txt"
    if not os.path.exists(log_file):
        with open(log_file, "w") as log:
            log.write("Honeypot Logları\n")
    print(f"[Honeypot] Log dosyası oluşturuldu: {log_file}")

    # Socket oluştur ve ayarları uygula
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[Honeypot] Dinleniyor: {host}:{port}")

    try:
        while True:
            # Gelen bağlantıyı kabul et
            client, address = server.accept()
            print(f"[Bağlantı] Yeni bağlantı: {address[0]}:{address[1]}")

            # Veri al ve log dosyasına kaydet
            data = client.recv(1024).decode('utf-8')
            print(f"[Veri] Gelen veri: {data}")
            with open(log_file, "a") as log:
                log.write(f"Bağlantı: {address[0]}:{address[1]}, Veri: {data}\n")

            # Yanıt gönder
            client.send("Bağlantınız loglandı!\n".encode('utf-8'))
            client.close()

    except KeyboardInterrupt:
        print("\n[Honeypot] Sonlandırılıyor...")
        server.close()

if __name__ == "__main__":
    honeypot()
