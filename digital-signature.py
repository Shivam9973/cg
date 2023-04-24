from Crypto.PublicKey import RSA
from hashlib import sha512

# Generate key pair
keyPair = RSA.generate(bits=1024)

# Print key pair
print(f"\nPublic key: (n = {hex(keyPair.n)}, e = {hex(keyPair.e)})")
print(f"\nPrivate key: (n = {hex(keyPair.n)}, d = {hex(keyPair.d)})")

# Sign message
msg = 'sign'
print(f'\nMessage: {msg}')
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)

# Print signature
print(f'\nSignature: {hex(signature)}')

# Verify signature
msg = 'sign'
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
if hash == hashFromSignature:
    print('\nSignature valid')
else:
    print('\nSignature invalid')

# Tamper with message and verify signature
msg = 'sign12'
print(f'\nMessage(tampered): {msg}')
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
if hash == hashFromSignature:
    print('\nSignature valid')
else:
    print('\nSignature invalid(tampered)')