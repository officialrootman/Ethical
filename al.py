import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style

colorama.init()

def check_username(username, websites):
    print(f"{Fore.BLUE}Kontrol edilen kullanıcı adı: {username}{Style.RESET_ALL}")
    for website in websites:
        try:
            url = website.format(username)
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Bulundu: {url}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Yok: {url}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Hata: {url} - {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    username = input("Kullanıcı adını giriniz: ")
    websites = [
        "https://github.com/{}",
        "https://twitter.com/{}",
        "https://www.instagram.com/{}",
        "https://www.facebook.com/{}"
    ]
    check_username(username, websites)
