"""This module instantiates a player's word into a word object and verifies it.

Variables:
    - english_words (set): a set of valid English words

Class:
    - Word: instantiates a valid user input into a word object and verifies it
    """

from os import path

dic_path = path.abspath("src/dic.txt")
with open(dic_path, 'r', encoding='utf-8') as word_file:
    english_words = set(word.strip() for word in word_file)


class Word:
    """Handles word object instantiation and verification.
    
    Methods:
        - __init__(self, word): used to instantiate a word object
        - __repr__(self): used to represent a word object (developer-friendly)
        - __str__(self): used to represent a word object (user-friendly)
        - verify(self, rack): used to verify a word object against the player's rack
        and checks if it is in the dictionary.
    """

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return self.word

    def __str__(self):
        return self.word
    
    def verify(self, rack):
        """This method checks if a word only contains letters from the rack
         AND if it is a valid English word

        Args:
            rack (_list_): the rack where tiles are used from
        
        Returns:
            _bool_: true if the word uses only words from the rack
            AND it is a valid English word.
            False if any of the conditions is false.
        """
        false_letters_invalid = set()
        false_letters_too_many = set()
        rack_letter_count = {self.word[i] : rack.count(self.word[i]) for i in range(len(self.word))}
        print('Game Referee: ', end = '')
        for letter in self.word:
            if letter not in rack:
                false_letters_invalid.add(letter)
            elif rack_letter_count[letter] > 0:
                rack_letter_count[letter] -= 1
            else:
                false_letters_too_many.add(letter)
        if not false_letters_too_many and not false_letters_invalid:
            if self.word.upper() in english_words:
                print(f'{self.word} is an excellent choice.')
                return self.word
            else:
                print(f'{self.word} isn\'t a valid English word.')
                return False
        else:
            if false_letters_invalid:
                print(f'''{false_letters_invalid}
                 {"is" if len(false_letters_invalid) == 1 else "are"} not in your rack!''', end = '')
            elif false_letters_too_many:
                print(f'''{false_letters_too_many}
                 {"is" if len(false_letters_invalid) == 1 else "are"} used too many times!''')
            return False