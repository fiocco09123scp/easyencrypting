###########################################################################################################################
###########################################################################################################################
####&         <--------------------------------------------------------------------------------------------->         &####
####&      I    EasyEncrypting is developed by Riccardo Fiocco, Ultimate Developers and Vittorio Morelli       I      &####
####&      I    Modifing the code without the permission of the creators is against the terms of service       I      &####
####&         <--------------------------------------------------------------------------------------------->         &####
###########################################################################################################################
###########################################################################################################################


# -- Imports


import string
import os 


# -- Statics


allowed_character = list(string.printable.replace("-", ""))


# -- Encrypt / Decrypt


def check_key(key: str): 

	if len(key) < 6:
		raise Exception("The key must be at least 6 characters long")

	va = int(len(key)*(1/6)) 
	vb = int(len(key)*(1/3))

	key_a = list( key[:-(len(key)-va)] )
	key_x = list( key[va:-vb] )
	key_b = list( key[len(key)-vb:] )
	return {"key_a":key_a,"key_x":key_x,"key_b":key_b}


def encrypt(key: str, text: str):

	values = check_key(key)

	for ch in allowed_character:
		ascii_code1 = ord(ch)

		for ch_a in values["key_a"]:
			ascii_code2 = ord(ch_a)

		for ch_x in values["key_x"]:
			ascii_code3 = ord(ch_x)

		for ch_b in values["key_b"]:
			ascii_code4 = ord(ch_b)

		ascii_code_all = ascii_code1 * ascii_code2 + ascii_code3 - ascii_code4
		text = text.replace(ch, f"{ascii_code_all}-")

	return text


def decrypt(key: str, text: str):

	values = check_key(key)

	for ch in allowed_character:
		ascii_code1 = ord(ch)

		for ch_a in values["key_a"]:
			ascii_code2 = ord(ch_a)

		for ch_x in values["key_x"]:
			ascii_code3 = ord(ch_x)

		for ch_b in values["key_b"]:
			ascii_code4 = ord(ch_b)

		ascii_code_all = ascii_code1 * ascii_code2 + ascii_code3 - ascii_code4
		text = text.replace(f"{ascii_code_all}-", ch)

	return text


# -- File Encrypt / Decrypt


def file_encrypt(key: str, filename: str):
	if os.path.isfile(filename):

		with open(filename, "r", encoding="utf-8", newline="\n") as file:
			content = file.read()

		content_encrypted = encrypt(key, content)

		with open(filename, "w", encoding="utf-8", newline='\n') as file:
			file.write(content_encrypted)

		return print(f"[LOG] {filename} has been successfully encrypted")
	
	else:

		raise Exception(f"No file found with the name: {filename}")


def file_decrypt(key: str, filename: str):
	if os.path.isfile(filename):

		with open(filename, "r", encoding="utf-8", newline="\n") as file:
			content = file.read()

		content_encrypted = decrypt(key, content)

		with open(filename, "w", encoding="utf-8", newline='\n') as file:
			file.write(content_encrypted)

		return print(f"[LOG] {filename} has been successfully decrypted")
	
	else:
		
		raise Exception(f"No file found with the name: {filename}")


# -- End