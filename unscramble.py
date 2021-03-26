from itertools import permutations
import enchant


class Unscramble:
    """ Class for the unscramble bot """

    def _text_length_validator(self, text) -> bool:
        """ validate if text is <= 8 """
        if len(text) <= 8:
            return True
        else:
            return False


    def permute_text(self, text: str) -> list:
        """ return a list of all permutations of the word """
        if(self._text_length_validator(text=text)):
            permuted_text = [''.join(p) for p in permutations(text)]
            return permuted_text

        return []

    def search_valid_us_word(self, arr: list) -> list:
        """ return a valid english word in the list """
        d = enchant.Dict("en_US")
        words_list = []

        for word in arr:
            if d.check(word):
                words_list.append(word)
        
        return words_list



if __name__ == '__main__':
    u = Unscramble()
    text = u.permute_text('noge')
    valid_word = u.search_valid_us_word(text)
    

    print(valid_word)