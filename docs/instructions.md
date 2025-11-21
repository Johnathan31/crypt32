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

