# Easyencrypting:

Is a library created with the idea in mind of simplifying the encryption of sentences or files. This library is very simple to use and uses a complex encryption system that makes the encrypted elements impossible to decrypt.

## Installation:

To install easyencrypting on Windows just use this command on your teminal

```bash
pip install easyencrypting
```
To install easyencrypting on MacOS just use this command on your terminal
```bash
python -m pip install
```

# Documentation

This is the official documentation for Easyencrypting.

## Encrypting a sentence

```python
import easyencrypting

sentence_to_encrypt = "Hello World!"

encrypted_sentence = easyencrypting.encrypt(key="Example", text=sentence_to_encrypt) #The key must be at least 6 character long

print(encrypted_sentence)
```

## Decrypting a sentence

```python
import easyencrypting

sentence_to_decrypt = "4979-6980-7463-7463-7670-2219-6014-7670-7877-7463-6911-2288-"

decrypted_sentence = easyencrypting.decrypt(key="Example", text=sentence_to_decrypt) #The key must be the same as the encrypting key
print(decrypted_sentence)
```

## Encrypting a file

```python
import easyencrypting

file_name = ("Example.txt")

encrypted_file = easyencrypting.file_encrypt(key="Example", filename=file_name) #The key must be at least 6 character long

print("The file was encrypted succesfully")
```

## Decrypting a file

```python
import easyencrypting

file_name = ("Example.txt")

decrypted_file = easyencrypting.file_decrypt(key="Example", filename=file_name) #The key must be at least 6 character long

print("The file was decrypted succesfully")
```

