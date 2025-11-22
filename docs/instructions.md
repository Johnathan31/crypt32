# Instructions for crypt32

Welcome to the **crypt32** instruction guide. This document explains how to use `Crypt32` class, how salt works, and gives clear examples for encryption and decryption.

---

## 1. Prerequisites

- Python 3.9+  
- Install `crypt32` library (or clone the repository)  
- Basic understanding of strings and encoding  

---

## 2. Installation
You can install `crypt32` module with the __pip__ tool in the terminal:
```bash
pip install crypt32
```

 or by cloning it:
```bash
git clone https://gtihub.com/Johnathan31/crypt32.git
cd crypt32
pip install .
```

---

## 3. 🛠️ Usage Instructions

1. Initialization
```python
from crypt32 import Crypt32

ciphered_text = Crypt32("Python")
```
2. Generating salt
```python

salt = Crypt32.gensalt(length=15) # Generates a 15-character long salt

print("Generated salt: ", salt)
```
3. Encryption:
```python
# Encryption with salt(Recommended)

ciphered_text.salt()
print(f"The salt encryption generated for 'Python' is: ", ciphered_text.salted)

# Encryption only(Not recommended for security, but possible)

ciphered_text.crypt()
print("The encryption for 'Python' is:", ciphered_text)

```
4. Decryption
```python
# By using the decrypt() attribute
print(f"The word {ciphered_text} decrypted is: ", ciphered_text.decrypt())

#or by accessing the original text
print(f"the original text of {ciphered_text} is '{ciphered_text.text}'")
```

---
