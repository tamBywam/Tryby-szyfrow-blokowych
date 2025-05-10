# Jakub Opólski

import hashlib
import numpy as np

KEY = "kluczyk123"

def read_bmp(path, size=64):
    with open(path, 'rb') as f:
        data = f.read()
    header = data[:54]
    pdata = data[54:]
    
    parray = np.frombuffer(pdata, dtype=np.uint8)
    
    padding_check = (size - (len(parray) % size)) % size
    
    if padding_check > 0:
        padded = np.concatenate([parray, np.zeros(padding_check, dtype=np.uint8)])
    else:
        padded = parray
    
    return header, padded

def write_bmp(path, header, pdata, org_length=None):
    if org_length is not None:
        pdata = pdata[:org_length]
    
    with open(path, 'wb') as f:
        f.write(header)
        f.write(pdata.tobytes())

def hash_block(block):
    block_bytes = block.tobytes() + KEY.encode()
    return hashlib.sha1(block_bytes).digest()

def ecb_encrypt(pdata, size):
    encrypted = np.zeros_like(pdata)
    for i in range(0, len(pdata), size):
        block = pdata[i:i+size]
        hashed = hash_block(block)
        repeat = (size // len(hashed)) + 1
        mask = (hashed * repeat)[:size]
        encrypted[i:i+size] = np.frombuffer(mask, dtype=np.uint8)
    return encrypted

def cbc_encrypt(pdata, size):
    encrypted = np.zeros_like(pdata)
    previous = np.zeros(size, dtype=np.uint8)
    for i in range(0, len(pdata), size):
        block = pdata[i:i+size]
        block = block ^ previous[:len(block)]
        hashed = hash_block(block)
        repeat = (size // len(hashed)) + 1
        mask = (hashed * repeat)[:size]
        encrypted[i:i+size] = np.frombuffer(mask, dtype=np.uint8)
        previous = encrypted[i:i+size]
    return encrypted

def main():
    size = 8 * 8
    input_image = "plain.bmp"
    ecb_crypto = "ecb_crypto.bmp"
    cbc_crypto = "cbc_crypto.bmp"

    header, pdata = read_bmp(input_image, size)
    org_length = len(pdata)

    ecb_encrypted = ecb_encrypt(pdata, size)
    cbc_encrypted = cbc_encrypt(pdata, size)

    write_bmp(ecb_crypto, header, ecb_encrypted, org_length)
    write_bmp(cbc_crypto, header, cbc_encrypted, org_length)

if __name__ == "__main__":
    main()