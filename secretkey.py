import secrets

secure_key = secrets.token_hex(10)  # Generate a 32-character (16 bytes) hex key
print("Your secure key:", secure_key)

#e4606ee3be951abf20dd