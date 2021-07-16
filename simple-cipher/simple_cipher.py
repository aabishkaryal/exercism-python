from string import ascii_lowercase as alphabet
from secrets import choice


class Cipher:
    def __init__(self, key: str = "".join([choice(alphabet) for i in range(100)])):
        if (key.isalpha() and key.islower()):
            self.key = key
        else:
            raise ValueError("Key must be lowercase alphabetic string")

    def encode(self, text: str) -> str:
        '''
        Encode the text with the key using substitution cipher
        '''
        return ''.join([self.__encode_letter(i, l) for i, l in enumerate(text)])

    def decode(self, text: str) -> str:
        '''
        Decode the text with the key using substitution cipher
        '''
        return ''.join([self.__decode_letter(i, l) for i, l in enumerate(text)])

    def __encode_letter(self, index: int, letter: str) -> str:
        '''
        Encodes a single letter for the given index.
        '''
        if (letter.isalpha() and letter.islower()):
            # alpha_index = alphabet.index(letter)
            # key_letter = self.key[index % len(self.key)]
            # key_index = alphabet.index(key_letter)
            # cipher_index = (alpha_index + key_index) % len(alphabet)
            # cipher_letter = alphabet[cipher_index]
            return alphabet[(alphabet.index(letter) +
                             alphabet.index(self.key[index % len(self.key)])) % len(alphabet)]
        else:
            return letter

    def __decode_letter(self, index: int, letter: str) -> str:
        '''
        Decodes a single letter for the given index.
        '''
        if (letter.isalpha() and letter.islower()):
            # alpha_index = alphabet.index(letter)
            # key_letter = self.key[index % len(self.key)]
            # key_index = alphabet.index(key_letter)
            # cipher_index = (alpha_index - key_index) % len(alphabet)
            # cipher_letter = alphabet[cipher_index]
            return alphabet[(alphabet.index(letter) -
                             alphabet.index(self.key[index % len(self.key)])) % len(alphabet)]
        else:
            return letter
