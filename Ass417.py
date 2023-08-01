from capstone import Cs, CS_ARCH_X86, CS_MODE_32

# Dizionario dei comandi e delle relative spiegazioni
command_explanations = {
    # Comandi assembly
    "mov": "Muove dati da una posizione all'altra (registro a registro, registro alla memoria, memoria al registro).",
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
    "insb": "Inserisce un byte da una porta di input nella memoria.",
    "jae": "Salta se sopra o uguale (CF=0, ZF=0).",
    "aaa": "Converte i risultati di una somma binaria BCD in un numero binario BCD corretto.",
    "popal": "Estrae i valori dai registri sullo stack nello stesso ordine in cui sono stati inseriti.",
    "jns": "Salta se il flag di segno è uguale a 0.",
    "js": "Salta se il flag di segno è uguale a 1.",
    "jb": "Salta se inferiore (CF=1).",
    "bound": "Verifica se un indice è all'interno di un array specificato.",
    "arpl": "Verifica e regola i privilegi di accesso di un registro a livello di privilegio.", 
 # Aggiungi gli altri comandi assembly e relative spiegazioni qui
}

# Lista delle traduzioni assembly -> C
assembly_to_c_translations = [
    ("mov", "int main() { /* Traduzione C per l'istruzione mov */ }"),
    ("push", "void myFunction() { /* Traduzione C per l'istruzione push */ }"),
    ("pop", "int foo() { /* Traduzione C per l'istruzione pop */ }"),
    ("add", "void bar() { /* Traduzione C per l'istruzione add */ }"),
    ("sub", "int main() { /* Traduzione C per l'istruzione sub */ }"),
    ("inc", "void myFunction() { /* Traduzione C per l'istruzione inc */ }"),
    ("dec", "int foo() { /* Traduzione C per l'istruzione dec */ }"),
    ("mul", "void bar() { /* Traduzione C per l'istruzione mul */ }"),
    ("div", "int main() { /* Traduzione C per l'istruzione div */ }"),
    ("and", "void myFunction() { /* Traduzione C per l'istruzione and */ }"),
    ("or", "int foo() { /* Traduzione C per l'istruzione or */ }"),
    ("xor", "void bar() { /* Traduzione C per l'istruzione xor */ }"),
    ("jmp", "int main() { /* Traduzione C per l'istruzione jmp */ }"),
    ("cmp", "void myFunction() { /* Traduzione C per l'istruzione cmp */ }"),
    ("jz", "int foo() { /* Traduzione C per l'istruzione jz */ }"),
    ("jnz", "void bar() { /* Traduzione C per l'istruzione jnz */ }"),
    ("je", "int main() { /* Traduzione C per l'istruzione je */ }"),
    ("jne", "void myFunction() { /* Traduzione C per l'istruzione jne */ }"),
    ("jg", "int foo() { /* Traduzione C per l'istruzione jg */ }"),
    ("jge", "void bar() { /* Traduzione C per l'istruzione jge */ }"),
    ("jl", "int main() { /* Traduzione C per l'istruzione jl */ }"),
    ("jle", "void myFunction() { /* Traduzione C per l'istruzione jle */ }"),
    ("movsb", "int foo() { /* Traduzione C per l'istruzione movsb */ }"),
    ("movsw", "void bar() { /* Traduzione C per l'istruzione movsw */ }"),
    ("movsd", "int main() { /* Traduzione C per l'istruzione movsd */ }"),
    ("lodsb", "void myFunction() { /* Traduzione C per l'istruzione lodsb */ }"),
    ("lodsw", "int foo() { /* Traduzione C per l'istruzione lodsw */ }"),
    ("lodsd", "void bar() { /* Traduzione C per l'istruzione lodsd */ }"),
    ("stosb", "int main() { /* Traduzione C per l'istruzione stosb */ }"),
    ("stosw", "void myFunction() { /* Traduzione C per l'istruzione stosw */ }"),
    ("stosd", "int foo() { /* Traduzione C per l'istruzione stosd */ }"),
    ("call", "void bar() { /* Traduzione C per l'istruzione call */ }"),
    ("ret", "int main() { /* Traduzione C per l'istruzione ret */ }"),
    ("pusha", "void myFunction() { /* Traduzione C per l'istruzione pusha */ }"),
    ("popa", "int foo() { /* Traduzione C per l'istruzione popa */ }"),
    ("lea", "void bar() { /* Traduzione C per l'istruzione lea */ }"),
    ("movzx", "int main() { /* Traduzione C per l'istruzione movzx */ }"),
    ("movsx", "void myFunction() { /* Traduzione C per l'istruzione movsx */ }"),
    ("xchg", "int foo() { /* Traduzione C per l'istruzione xchg */ }"),
    ("adc", "void bar() { /* Traduzione C per l'istruzione adc */ }"),
    ("outsd", "int main() { /* Traduzione C per l'istruzione outsd */ }"),
    ("test", "void myFunction() { /* Traduzione C per l'istruzione test */ }"),
    ("insb", "int foo() { /* Traduzione C per l'istruzione insb */ }"),
    ("jae", "void bar() { /* Traduzione C per l'istruzione jae */ }"),
    ("aaa", "int main() { /* Traduzione C per l'istruzione aaa */ }"),
    ("popal", "void myFunction() { /* Traduzione C per l'istruzione popal */ }"),
    ("jns", "int foo() { /* Traduzione C per l'istruzione jns */ }"),
    ("js", "void bar() { /* Traduzione C per l'istruzione js */ }"),
    ("jb", "int main() { /* Traduzione C per l'istruzione jb */ }"),
    ("bound", "void myFunction() { /* Traduzione C per l'istruzione bound */ }"),
    ("arpl", "int foo() { /* Traduzione C per l'istruzione arpl */ }"),
 # Aggiungi gli altri comandi assembly -> C qui
]

def disassemble_to_c(assembly_code):
    md = Cs(CS_ARCH_X86, CS_MODE_32)

    try:
        assembly_code = assembly_code.replace(" ", "")
        if len(assembly_code) % 2 != 0 or not all(c in "0123456789ABCDEFabcdef" for c in assembly_code):
            raise ValueError()

        code = bytes.fromhex(assembly_code)

        c_code = ""  # Stringa per contenere il codice C tradotto

        for instruction in md.disasm(code, 0x1000):
            mnemonic = instruction.mnemonic.lower()
            op_str = instruction.op_str

            # Ottieni la spiegazione del comando se presente nel dizionario
            assembly_explanation = command_explanations.get(mnemonic, "Spiegazione non disponibile")

            # Cerca la traduzione C nell'elenco assembly_to_c_translations
            c_translation = next((c for asm, c in assembly_to_c_translations if asm == mnemonic), None)

            c_code += f"// Istruzione originale: {mnemonic} {op_str}\n"
            c_code += f"// Spiegazione: {assembly_explanation}\n"
            c_code += f"// Traduzione C: {c_translation}\n\n" if c_translation else "// Traduzione C: // Traduzione non disponibile\n\n"

        # Stampa il codice C tradotto
        print("\nCodice C tradotto:")
        print(c_code)
    except ValueError:
        print("Errore: Il codice assembly fornito non è nel formato esadecimale corretto.")

# Esempio di utilizzo
assembly_code = input("Inserisci il codice assembly in formato esadecimale: ")
disassemble_to_c(assembly_code)
