import qrcode
import json

def save_user(user):
    with open('users.json', 'a') as file:
        json.dump(user, file)
        file.write('\n')

def load_users():
    try:
        with open('users.json', 'r') as file:
            users = [json.loads(line) for line in file]
    except FileNotFoundError:
        users = []
    return users

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_code(user, filename):
    data = json.dumps(user)
    qr = generate_qr_code(data)
    qr.save(filename)

def main():
    users = load_users()

    while True:
        print("1. Aggiungi nuovo utente")
        print("2. Genera QR code per utenti salvati")
        print("3. Esci")

        choice = input("Scelta: ")

        if choice == "1":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            societa = input("Società: ")
            partita_iva = input("Partita IVA: ")

            user = {
                "nome": nome,
                "cognome": cognome,
                "societa": societa,
                "partita_iva": partita_iva
            }
            users.append(user)
            save_user(user)

        elif choice == "2":
            for i, user in enumerate(users):
                filename = f"user_qr_{i+1}.png"
                save_qr_code(user, filename)
                print(f"QR code per utente {i+1} salvato su '{filename}'")

        elif choice == "3":
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
