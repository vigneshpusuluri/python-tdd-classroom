class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        listvovel = ["a","e","i","o","u"]

        if character.lower() in listvovel:
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longestWord = max(sentence.split(), key=len) 
        return longestWord

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        words = text.split()
        words_Length = []
        for word in words:
            words_Length.append((len(word)))
        return words_Length