from unscramble import Unscramble


if __name__ == '__main__':
    
    u = Unscramble()
    text = u.permute_text('noge')
    valid_word = u.search_valid_us_word(text)
    

    print(valid_word)