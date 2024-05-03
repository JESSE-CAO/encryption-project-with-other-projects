from encryption import *

key = None
matrix_str = None
def init(martix):
    global key, matrix_str
    matrix_str = ';'.join(','.join(str(val) for val in row) for row in martix)
    key = get_random_bytes(32)# 生成随机的16字节密钥

def get_key():
    return key

def get_info():
    return encrypt_matrix(key, caesar_cipher_encrypt(matrix_str, 3))

def get_decrypted_info(iv, ciphertext):
    decrypted_matrix_str = caesar_cipher_decrypt(decrypt_matrix(key, iv, ciphertext), 3)
    decrypted_matrix = np.array([list(map(float, row.split(','))) for row in decrypted_matrix_str.split(';')])
    return decrypted_matrix
