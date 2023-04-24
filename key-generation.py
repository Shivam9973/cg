# key-generation
# pip install pycryptodome
import os
import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

# Symmetric Key Generation
symmetric_key = hashlib.sha256(os.urandom(32)).digest()
print("Symmetric Key:", symmetric_key.hex())

# Asymmetric Key Generation
asymmetric_key = RSA.generate(2048)
private_key = asymmetric_key.export_key()
public_key = asymmetric_key.publickey().export_key()
print("Private Key:", private_key.hex())
print("Public Key:", public_key.hex())


# key-generation (b)
import hashlib
from Crypto.Cipher import AES, DES
import rsa, secrets
from tinyec import registry
def aes_key_generation(key):
    print("AES KEY GENERATION")
    aes_block_size = AES.block_size
    aes_key = hashlib.sha256(key.encode()).hexdigest()
    print("\nblocksize: {}\n\naes_key: {}".format(aes_block_size, aes_key))

def des_key_generation(key):
    print("\nDES KEY GENERATION")
    des_block_size = DES.block_size
    des_key = hashlib.md5(key.encode()).hexdigest()
    print("\nblocksize: {}\n\ndes_key: {}".format(des_block_size, des_key))

def RSA():
    print("\nRSA KEY GENERATION")
    (publickey, privatekey) = rsa.newkeys(1024)
    print("\npublic key: {} \nprivate key: {}".format(publickey, privatekey))

def compress_point(point):
    
    return hex(point.x) + hex(point.y % 2)[2:]
def ecc():
    print("\nECC ALGORITHM")
    ecc_curve = registry.get_curve('brainpoolP256r1')
    privKey = secrets.randbelow(ecc_curve.field.n)
    pubKey = privKey * ecc_curve.g
    print("\nprivate key: ", int(hex(privKey), 16))
    print("\npublic key: ", int(compress_point(pubKey), 16))
    
aes_key_generation("secret")
des_key_generation("secret")
RSA()
ecc()