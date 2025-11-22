# Instructions for crypt32

Welcome to the **crypt32** instruction guide. This document explains how to use `Crypt32` class, how salt works, and gives clear examples for encryption and decryption.

---

## 1. Prerequisites

- Python 3.9+  
- Install `crypt32` library (or clone the repository)  
- Basic understanding of strings, encoding & classes

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

### 3.1. Initialization
```python
from crypt32 import Crypt32

ciphered_text = Crypt32("Python")
```
### 3.2. Generating salt
```python

salt = Crypt32.gensalt(length=15) # Generates a 15-character long salt

print("Generated salt: ", salt)
```
### 3.3. Encryption:
```python
# Encryption with salt(Recommended)

ciphered_text.salt()
print(f"The salt encryption generated for 'Python' is: ", ciphered_text.salted)

# Encryption only(Not recommended for security, but possible)

ciphered_text.crypt()
print("The encryption for 'Python' is:", ciphered_text)

```
### 3.4. Decryption
```python
# By using the decrypt() attribute
print(f"The word {ciphered_text} decrypted is: ", ciphered_text.decrypt())

#or by accessing the original text
print(f"the original text of {ciphered_text} is '{ciphered_text.text}'")
```
### 3.5. Accessing other attributes


#### 3.5.1. ciphered_text.text

returns the original text

#### 3.5.2 ciphered_text.encoded 

returns The encoded text of the variable. You should do functions self.crypt() or self.salt() thus it gets the value of the encryption

#### 3.5.3 ciphered_text.salty

the salt generated for the variable.
You should do function self.salt() thus it gets the value

#### 3.5.4 ciphered_text.salted


Returns the salt + the encryption.
You should do the self.salt() fucntion thus it gets the value


---


