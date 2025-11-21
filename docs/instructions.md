## Crypt32 class Features 🧰
the available features currently in the class are:
- Encoding text
- Decoding encrypted text
- Generating salt
- Generating salt text with encrypted text

---

## 🛠️ Instructions
1. Instanciate the class like this:
```python
from crypt32 import Crypt32

instance: Crypt32 = Crypt32("Python")
# name it as you want
```

2. encrypt it by doing: `instance.crypt()`

3. Or encrypt it with salt: `instance.salt()`

4. Get original text by decoding it with: `instance.decode()` or access original text by `instance.text`

---

# Examples🔬

Here are 2 examples on the usages of the class:

```python
from crypt32 import Crypt32

s: Crypt32 = Crypt32("Hello world") # created instance

s.crypt() # Encrypting text

print(s.decode()) # 'hello world'
```

---

```python
from crypt32 import Crypt32

example: Crypt32 = Crypt32("Python") # created an instance

example.crypt() # Encrypted the text

print(f"The word '{example.text}' encrypted: {example}.") # 'The word 'Python' encrypted: πRocofaµRøµaπceØπe.'

example.salt() # salting the text with encrypting it

print(repr(example)) # 'SALT:33d739db75ae9f800e47f0ce16a71a42:πRocofaµRøµaπceØπe'

#Generating salt text
print(Crypt32.gensalt(length=10)) # 'd75ae9f80e'

```
