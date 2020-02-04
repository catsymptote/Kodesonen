class Hangman:
    def __init__(self, api):
        self.API = api

        self.word = None
        self.get_word_from_API()

        self.found_letters = []
        for i in range(len(self.word)):
            self.found_letters.append('_')
        
        self.guessed_words = []
        self.guessed_letters = []

        self.mistakes = 0


    def get_word_from_API(self):
        self.word = self.API.get_word()


    def add_mistake(self, n=1):
        self.mistakes += n


    def guess(self, string):
        string = string.upper()
        if len(string) == 1:
            if not self.guess_letter(string):
                self.add_mistake()
        elif len(string) > 1:
            if not self.guess_word(string):
                self.add_mistake(n=3)
        else:
            print('Got no letters..')


    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print('>', letter, '< already guessed.')
            return True

        self.guessed_letters.append(letter)
        self.add_mistake(n=1)

        if letter not in self.word:
            return False
        
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.found_letters[i] = letter

        self.add_mistake(n=-1)
        return True


    def guess_word(self, word):
        if word in self.guessed_words:
            print('>', word, '< already guessed.')
            return True

        self.guessed_words.append(word)
        self.add_mistake(n=3)

        letters = list(word)
        if len(letters) != len(self.word):
            return False
        
        #if list(word) == self.word:
        for i in range(len(letters)):
            if letters[i] != self.word[i]:
                return False
        
        self.found_letters = self.word
        self.add_mistake(n=-3)
        return True


    def show(self):
        print(self.found_letters)
        return self.found_letters


    def done(self):
        for letter in word:
            if self.word != self.found_letters:
                print('Game over!')
                return False
        return True
