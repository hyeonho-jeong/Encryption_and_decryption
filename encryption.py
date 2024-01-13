#call library that can do encoded
import cryptocode

txt = "It's what you want to encrypt. It encrypts the string that's written here."
password = "12345"

encoded_string = cryptocode.encrypt(txt, password)
print("Encryption:",encoded_string)

decoded_string = cryptocode.decrypt(encoded_string, "3")
print("Wrong password:",decoded_string)

decoded_string = cryptocode.decrypt(encoded_string, password)
print("Decryption:", decoded_string)