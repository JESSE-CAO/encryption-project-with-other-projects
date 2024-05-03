from api import  *

init(np.array([[1,1,4],[5,1,4]]))
print(f'key:{get_key()}')
iv,ct=get_info()
print(f'iv,ct:{(iv,ct)}')
print(f'decrypted info:{get_decrypted_info(iv,ct)}')
