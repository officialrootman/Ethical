import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def brute_force(target_hash, wordlist):
    for word in wordlist:
        hashed_word = hash_password(word.strip())
        if hashed_word == target_hash:
            print(f"Parola bulundu: {word}")
            return
    print("Parola bulunamadı.")

if __name__ == "__main__":
    target_password = input("Hedef parolayı giriniz: ")
    target_hash = hash_password(target_password)
    print(f"Hedef hash: {target_hash}")

    wordlist = ["123456", "password", "admin", "letmein", "qwerty"]
    brute_force(target_hash, wordlist)
