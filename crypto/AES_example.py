import json
from base64 import b64encode
from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
# https://docs.python-guide.org/scenarios/crypto/

def r_pad(payload, block_size=16):
    length = block_size - (len(payload) % block_size)
    return payload + chr(length)*length

key = 'password123'

key = get_random_bytes(16)
IV = get_random_bytes(16)

# Encryption
cipher = AES.new(key , AES.MODE_CBC, IV )
message = "Happy New Year's in 2019"

print(len(message))
cipher_text = cipher.encrypt(r_pad(message, AES.block_size))
iv = b64encode(IV).decode('utf-8')
ct = b64encode(cipher_text).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)

# Decryption

plain_text = cipher.decrypt(cipher_text)
print(str(plain_text))

# try this too
# json_input = result
# try:
#     b64 = json.loads(json_input)
#     iv = b64decode(b64['iv'])
#     ct = b64decode(b64['ciphertext'])
#     cipher = AES.new(key , AES.MODE_CBC, iv)
#     pt = unpad(cipher.decrypt(ct), AES.block_size)
#     print("The message was: ", pt)
# except :
#     print("Incorrect decryption")

# second method
# data = b"Here is my private message"
# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_CBC, IV)
# ct_bytes = cipher.encrypt(r_pad(data, AES.block_size))
# iv = b64encode(cipher.iv).decode('utf-8')
# ct = b64encode(ct_bytes).decode('utf-8')
# result = json.dumps({'iv':iv, 'ciphertext':ct})
# print(result)
# '{"iv": "bWRHdzkzVDFJbWNBY0EwSmQ1UXFuQT09", "ciphertext": "VDdxQVo3TFFCbXIzcGpYa1lJbFFZQT09"}'
