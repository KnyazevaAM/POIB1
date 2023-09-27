import requests
import hashlib

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    resp = requests.get(url)
    if resp.status_code == 200:
        hashes = resp.text.splitlines()
        for h in hashes:
            if suffix in h:
                return True
    return False

def main():
    filename = input("Введите название файла: ")
  
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                username, password = line.split(',')
                password = password.strip()
                if check_password(password):
                    print(f"Обнаружена утечка данных данного пользователя {username} пароля {password}")
                else:
                    print(f"Пароль введенного пользователя {username} безопасен")
    except FileNotFoundError:
        print("Файл не обнаружен")

if name == "main":
    main()
