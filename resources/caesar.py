
def encrypt(text: str, shift: int):
    encrypted = ""
    if isinstance(shift, int):
        for i in text:
            encrypted += chr(ord(i) + shift)
        return encrypted
    raise TypeError("shift must be an integer.")


def decrypt(text: str,shift: int):
    decrypted = ""
    for char in text:
        decrypted += chr(ord(char) - shift)
    return decrypted
