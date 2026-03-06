''' create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up'''
Hindi_to_english_words = {
    'namaste':'Hello',
    'naam':'name',
    'kaise ho':'howare ypu',
    'kya kar rahe ho':'what are you doing',

}
Hindi_to_english_word=input('enter hindi word get its english translation: ')
print(Hindi_to_english_words[Hindi_to_english_word])