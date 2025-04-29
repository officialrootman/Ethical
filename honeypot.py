import socket
import logging
from flask import Flask
import threading

# Flask uygulaması (Sahte HTTP servisi)
app = Flask(__name__)

@app.route("/")
def index():
    return "Bu bir honeypot sistemidir!"

# Dinleyici Fonksiyonu (TCP)
def tcp_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8081))  # Farklı bir port seçebilirsiniz
    server_socket.listen(5)
    print("TCP Honeypot çalışıyor. Gelen bağlantılar dinleniyor...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Bağlantı algılandı: {address}")
        log_connection(address, "TCP bağlantısı kuruldu")
        client_socket.send(b"Sunucuya hoş geldiniz!\n")
        client_socket.close()

# Veri Kaydı için Fonksiyon
def log_connection(address, data):
    logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(f"Bağlantı adresi: {address}, Veri: {data}")

# Sahte Dosya Yapısı
def simulate_file_structure():
    fake_files = ["passwords.txt", "bank_accounts.xlsx", "server_config.ini"]
    print("Mevcut dosyalar:")
    for file in fake_files:
        print(f"- {file}")

# Ana Program
if __name__ == "__main__":
    # Sahte dosyaları göster
    simulate_file_structure()

    # Flask sunucusunu bir thread'de çalıştır
    flask_thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080, debug=False))
    flask_thread.start()

    # TCP dinleyiciyi başlat
    tcp_listener()
