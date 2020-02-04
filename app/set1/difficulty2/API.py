import requests


class API:
    def __init__(self):
        #self.url = 'https://www.reddit.com/r/all/top/.json'
        self.url = 'https://api.kodesonen.no/?task=hangman'


    def get_word(self):
        response = requests.get(url=self.url)
        data = response.json()
        
        if data['status'] != 'success':
            print('API connection unsuccessful')
            return False
        
        word = data['random-word']
        length = data['characters']

        if len(word) != length:
            print('Error in word length')
            print('Word in question\t', word)
            print('Stated length\t', length)
            print('Actual length\t', len(word))
            #return False

        return word
