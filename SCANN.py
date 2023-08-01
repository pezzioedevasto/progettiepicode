import usb.core

# Ottiene la lista dei dispositivi USB collegati al PC
def get_usb_devices(idVendor=None, idProduct=None):
    usb_devices = usb.core.find(find_all=True, idVendor=idVendor, idProduct=idProduct)
    return usb_devices

# Stampa la lista dei dispositivi USB collegati
def print_usb_devices(usb_devices):
    print("Dispositivi USB collegati:")
    for i, device in enumerate(usb_devices):
        print(f"[{i+1}] {device}")

# Esempio di utilizzo
usb_devices = get_usb_devices()
print_usb_devices(usb_devices)
