import os
import random
from typing import Dict, List


CIPHER_DICT = {
    'a': ['lo', 'eØ', 'Łqπ'],
    'b': ['aπL', 'mi', '™'],
    'c': ['πLq', 'em', 'Tn'],
    'd': ['Leπ', 'k', 'im', 'πX'],
    'e': ['fRµ', 'a'],
    'f': ['πLr', '@am', '€oπ'],
    'g': ['fam', 'Ł:o', 'πge'],
    'h': ['µaπ', 'Joc'],
    'i': ['al', 'o', 'teO'],
    'j': ['kl', 'πL'],
    'k': ['oπm', 'O', 'Łio'],
    'l': ['Re', 'Øom', 'k$'],
    'm': ['#Rg', 'Łeo', 'ton'],
    'n': ['fR†', 'Ła', 'πe'],
    'o': ['K', 'ŁmRe', 'ceØ'],
    'p': ['fR@', 'Łet', 'πRo'],
    'q': ['fat', 'moπL'],
    'r': ['faT', 'Łeco', 'πLo'],
    's': ['faµR', 'Łomn', 'πRe'],
    't': ['faµRø', 'Øceπ'],
    'u': ['eπ', 'Łoc', 'teJ'],
    'v': ['foπL', 'Łß'],
    'w': ['Łom', 'πReØ'],
    'x': ['faπR', 'Łem'],
    'y': ['L', 'Łem†', 'co'],  
    'z': ['₩e', 'Łeom']
}

class Crypt32:
    """The class of the crypt32 cipher."""

    def __init__(self, text: str = ""):
        self.text = text
        self.encoded = ""
        self.salted = ""
        self.salty = ""
        self._build_reverse_dict()

    def __str__(self):
        return f"{Crypt32(self.text)}" if not self.encoded else f"{Crypt32(self.encoded)}"

    def __repr__(self):
        return "{Crypt32(self.text)}" if not self.salted else f"{Crypt32(self.salted)}"

    def __getattr__(self, name):
        return f"{Crypt32(self.text)}"

    def _build_reverse_dict(self):
        self.reverse_dict: Dict[str, List[str]] = {}
        for letter, syms in CIPHER_DICT.items():
            for s in syms:
                self.reverse_dict.setdefault(s, []).append(letter)

        self.symbols_sorted = sorted(
            self.reverse_dict.keys(),
            key=lambda x: len(x),
            reverse=True
        )

    @staticmethod
    def gensalt(length=16):
        """Generates a salt text.
        
        length -- an optional argument indicates the length of the salt, defaulted to 16
        
        >>> Crypt32.gensalt() → '4a7d2123276ac43b40ed35c09b776e75'
        
        >>> Crypt32.gensalt(length=10) → 'c39ff407f94faebbe9b1'
        """
        return os.urandom(length).hex()
        
    

    def crypt(self, sep: str = " ") -> str:
        """Encrypts the text, and gives this value to the self.encoded attribute.
        sep -- an optional argument, which is the separator of each word in the text.
        
        >>> eg: Crypt32 = Crypt32("summer")
        eg.crypt() → 'faµReπ#RgtonfRµπLo'
        """
        
        words = self.text.split(" ")
        encoded_words = []

        for word in words:
            encoded_chars = []
            for ch in word:
                low = ch.lower()
                if low in CIPHER_DICT:
                    encoded_chars.append(random.choice(CIPHER_DICT[low]))
                else:
                    encoded_chars.append(ch)
            encoded_words.append("".join(encoded_chars))

        self.encoded = sep.join(encoded_words)
        return self.encoded



    def decrypt(self, sep: str = " ") -> str:
        """Decrypts the script given. The script should be encoded atleast once to work.
        sep -- an optional argument, which is the separator of each word in the text.
        
        >>> example: Crypt32 = Crypt32("summer")
        example.crypt()
        example.decrypt() → 'summer'
        """
        if not self.encoded:
            raise RuntimeError("'Crypt32' object was not encoded to decode, as expected.")

        if sep:
            parts = self.encoded.split(sep)
            decoded_words = []
            for p in parts:
                decoded_words.append(self._decode_greedy(p))
            return " ".join(decoded_words)
        else:
            return self._decode_greedy(self.encoded)
            
            
            
    def _decode_greedy(self, text: str) -> str:
        i = 0
        n = len(text)
        out = []

        while i < n:
            matched = False
            for sym in self.symbols_sorted:
                L = len(sym)
                if i + L <= n and text[i:i+L] == sym:
                    out.append(self.reverse_dict[sym][0])
                    i += L
                    matched = True
                    break
            if not matched:
                out.append(text[i])
                i += 1
        return "".join(out)
        
        
    def salt(self, sep: str = " ") -> str:
        """Generates a salt with encrypting the text
        sep -- an optional argument, which is the separator of each word in the text
        
        >>> eg: Crypt32 = Crypt32("very important message")
        eg.salt(sep="|") → 'SALT:5402b8bae95e80ec4d277322380a73a2:ŁßfRµπLoŁem†|teO#RgŁetceØfaTØceπ|tonfRµπRefaµReØfamfRµ'
        """
        self.salty = self.gensalt()
        self.encoded = self.crypt(sep=sep)
        self.salted = f"SALT:{self.salty}:{self.encoded}"
        return self.salted



    def salt_decode(self, sep: str = " ") -> str:
        """Decodes the text & removes salt.
        sep -- an optional argument, which is the separator of each word in the text.
        
        >>> eg: Crypt32 = Crypt32("Summer")
        eg.salt()
        eg.salt_decode() → 'summer'
        """
        if not self.salted.startswith("SALT:"):
            return self.decode(sep)

        _, salt, enc = self.salted.split(":", 2)
        self.encoded = enc
        return self.decode(sep)

    def __init__(self, text: str = ""):
        self.text = text
        self.encoded = ""
        self.salted = ""
        self._build_reverse_dict()

    def __str__(self):
        return f"{self.text}" if not self.encoded else f"{self.encoded}"

    def __repr__(self):
        return "{self.text}" if not self.salted else f"{self.salted}"

    def __getattr__(self, name):
        return f"{self.text}"

    def _build_reverse_dict(self):
        self.reverse_dict: Dict[str, List[str]] = {}
        for letter, syms in CIPHER_DICT.items():
            for s in syms:
                self.reverse_dict.setdefault(s, []).append(letter)

        self.symbols_sorted = sorted(
            self.reverse_dict.keys(),
            key=lambda x: len(x),
            reverse=True
        )

    @staticmethod
    def gensalt(length=16):
        return os.urandom(length).hex()
        
    

    def crypt(self, sep: str = " ") -> str:
        words = self.text.split(" ")
        encoded_words = []

        for word in words:
            encoded_chars = []
            for ch in word:
                low = ch.lower()
                if low in CIPHER_DICT:
                    encoded_chars.append(random.choice(CIPHER_DICT[low]))
                else:
                    encoded_chars.append(ch)
            encoded_words.append("".join(encoded_chars))

        self.encoded = sep.join(encoded_words)
        return self.encoded



    def decode(self, sep: str = " ") -> str:
        if not self.encoded:
            raise RuntimeError("'Crypt32' object was not encoded to decode, as expected.")

        if sep:
            parts = self.encoded.split(sep)
            decoded_words = []
            for p in parts:
                decoded_words.append(self._decode_greedy(p))
            return " ".join(decoded_words)
        else:
            return self._decode_greedy(self.encoded)

    def _decode_greedy(self, text: str) -> str:
        i = 0
        n = len(text)
        out = []

        while i < n:
            matched = False
            for sym in self.symbols_sorted:
                L = len(sym)
                if i + L <= n and text[i:i+L] == sym:
                    out.append(self.reverse_dict[sym][0])
                    i += L
                    matched = True
                    break
            if not matched:
                out.append(text[i])
                i += 1
        return "".join(out)

    def salt(self, sep: str = " ") -> str:
        salt = self.gensalt()
        encoded = self.crypt(sep=sep)
        self.salted = f"SALT:{salt}:{encoded}"
        return self.salted

    def salt_decode(self, sep: str = " ") -> str:
        if not self.salted.startswith("SALT:"):
            return self.decode(sep)

        _, salt, enc = self.salted.split(":", 2)
        self.encoded = enc
        return self.decode(sep)
