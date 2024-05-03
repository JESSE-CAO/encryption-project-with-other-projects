## 与Lqy、Zqt同志共同合作的项目之传输加密
### api.init(matrix)
* matrix 矩阵
### api.get_key()
获取密钥（32字节密钥）
### api.get_info()
获取iv，加密后的矩阵
### api.get_decrypted_info(iv, ciphertext)
* iv
* ciphertext：加密后的矩阵
得到解密后的矩阵
