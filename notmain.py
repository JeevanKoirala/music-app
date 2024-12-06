password_lists = {
    'a': "02s", 'b': "eo2", 'c': "7hd", 'd': "93h", 'e': "h1m",
    'f': "ie4", 'g': "@qo0", 'h': "83h", 'i': "$H7", 'j': "1l*",
    'k': "h10", 'l': "29d", 'm': "9sd", 'n': "19s", 'o': "83h",
    'p': "oa2", 'q': "ugh", 'r': "3hv", 's': "5bs", 't': "xz6",
    'u': "8sl", 'v': "1nb", 'w': "4nq", 'x': "$@a", 'y': "6ba",
    'z': "n92ng", '1': "283", '2': "hgb", '3': "7hf", '4': "8dh",
    '5': "usd", '6': "nam", '7': "awr", '8': "82b", '9': "bfn",
    '0': "2n3", '!': "qps", '@': "9ws",
}
def password_encrypt(password: str) -> str:
    encrypted = ''.join(password_lists.get(char.lower(), char) for char in password)
    return encrypted
def decrypt_password(encrypted_password: str) -> str:
    reverse_map = {v: k for k, v in password_lists.items()}
    decrypted = ""
    temp = ""

    for char in encrypted_password:
        temp += char
        if temp in reverse_map:
            decrypted += reverse_map[temp]
            temp = ""
    
    return decrypted
if __name__ == "__main__":
    print("Welcome to the tool where you can make a secretcode from  a normal word")
    print("Select an option:")
    print("1. Make a secret")
    print("2. Open the truth")
    
    choice = input("what do you wanna do(1 or 2): ").strip()

    if choice == "1":
        original_password = input("Enter the password to encrypt: ")
        encrypted = password_encrypt(original_password)
        print("The secret password:", encrypted)
    elif choice == "2":
        encrypted_password = input("Enter the password to decrypt: ")
        decrypted = decrypt_password(encrypted_password)
        print("The opened password:", decrypted)
    else:
        print("I dont think so the option is available choose available one")
    #this is a project that converts a simple word into a encrypted password just like the encryption system of many popular software.
    # you can also use this to type a message in a encrypted form and send your friends and they can decrypt your message using this program.
    #  dont use this for wrong purpose guys:)
