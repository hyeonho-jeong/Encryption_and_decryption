import cryptocode
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

password = "hello12345"

file_path = (r"C:\Users\ASUS\Desktop\Encryption_and_decryption\password_list.txt")

with open(file_path, 'r', encoding = 'UTF8') as f:
    read_file = f.read()

encrypted_string = cryptocode.decrypt(read_file, password)

with open(file_path, 'w', encoding ='UTF8') as f:
    f.write(encrypted_string)