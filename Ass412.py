from capstone import Cs, CS_ARCH_X86, CS_MODE_32, CS_MODE_64

# Dizionario dei comandi e delle relative spiegazioni
command_explanations = {
    "mov": "Muove dati da una posizione all'altra",
    "push": "Inserisce un valore nello stack.",
    "pop": "Estrae un valore dallo stack.",
    "add": "Aggiunge o sottrae due operandi.",
    "sub": "Aggiunge o sottrae due operandi.",
    "inc": "Incrementa o decrementa il valore di un operando.",
    "dec": "Incrementa o decrementa il valore di un operando.",
    "mul": "Moltiplica o divide due operandi.",
    "div": "Moltiplica o divide due operandi.",
    "and": "Operazioni logiche AND, OR, XOR bit a bit.",
    "or": "Operazioni logiche AND, OR, XOR bit a bit.",
    "xor": "Operazioni logiche AND, OR, XOR bit a bit.",
    "jmp": "Salta a un'istruzione specificata.",
    "cmp": "Confronta due operandi.",
    "jz": "Salta se zero.",
    "jnz": "Salta se non zero.",
    "je": "Salta se uguale.",
    "jne": "Salta se non uguale.",
    "jg": "Salta se maggiore.",
    "jge": "Salta se maggiore o uguale.",
    "jl": "Salta se minore.",
    "jle": "Salta se minore o uguale.",
    "movsb": "Copia un byte da una memoria all'altra.",
    "movsw": "Copia una parola da una memoria all'altra.",
    "movsd": "Copia una doppia parola da una memoria all'altra.",
    "lodsb": "Carica un byte in un registro da una memoria.",
    "lodsw": "Carica una parola in un registro da una memoria.",
    "lodsd": "Carica una doppia parola in un registro da una memoria.",
    "stosb": "Salva un byte in una memoria.",
    "stosw": "Salva una parola in una memoria.",
    "stosd": "Salva una doppia parola in una memoria.",
    "call": "Chiama una subroutine o una funzione.",
    "ret": "Ritorna da una subroutine.",
    "pusha": "Salva e ripristina tutti i registri sullo stack.",
    "popa": "Salva e ripristina tutti i registri sullo stack.",
    "lea": "Calcola l'indirizzo effettivo di un operando.",
    "movzx": "Muove dati da una posizione all'altra estendendo la dimensione.",
    "movsx": "Muove dati da una posizione all'altra riducendo la dimensione.",
    "xchg": "Scambia il contenuto di due operandi.",
    "adc": "Aggiunge due operandi, includendo il flag di carry.",
    "outsd": "Invia una stringa di doppie parole (DWORD) dalla memoria a una porta di output.",
    "test": "Esegue un'operazione di AND tra due operandi, ma il risultato non viene memorizzato.",
}

def analyze_assembly(assembly_code):
    # Inizializza Capstone per l'architettura e la modalità specificate
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    # o md = Cs(CS_ARCH_X86, CS_MODE_64) se si utilizza l'architettura a 64 bit

    try:
        # Rimuovi gli spazi dal codice assembly
        assembly_code = assembly_code.replace(" ", "")

        # Verifica che il codice assembly non contenga caratteri non validi
        if len(assembly_code) % 2 != 0 or not all(c in "0123456789ABCDEFabcdef" for c in assembly_code):
            raise ValueError()

        # Converti il codice assembly in un array di byte
        code = bytes.fromhex(assembly_code)

        # Analizza il codice assembly
        for instruction in md.disasm(code, 0x1000):
            mnemonic = instruction.mnemonic.lower()
            op_str = instruction.op_str

            # Ottieni la spiegazione del comando se presente nel dizionario
            explanation = command_explanations.get(mnemonic, "Spiegazione non disponibile")

            # Stampa l'istruzione e la spiegazione
            print("Istruzione: %s, Operandi: %s, Spiegazione: %s" % (mnemonic, op_str, explanation))
    except ValueError:
        print("Errore: Il codice assembly fornito non è nel formato esadecimale corretto.")

# Esempio di utilizzo
assembly_code = input("Inserisci il codice assembly in formato esadecimale: ")
analyze_assembly(assembly_code)
