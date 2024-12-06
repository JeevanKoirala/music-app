
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
            decrypted += reverse_map[]
            temp = ""
    
    return decrypted


if __name__ == "__main__":
    original_password = input("Enter the password to make it secret: ")
    encrypted = password_encrypt(original_password)
    print("The secret password:", encrypted)
    
    decrypted = decrypt_password(encrypted)
    print("The opened password:", decrypted)

    if decrypted == original_password:
        print("Successfully opened the password")
    else:
        print("Oops! Unknown error occurred")


    
