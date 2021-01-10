import requests 

class Dictionary:
	BASE_URL = 'https://api.dictionaryapi.dev/api/v2/entries'

	def __init__(self, word, language='en'):
		self.word = word
		self.language = language

	def get_word_meaning(self):
		headers = {
		    'authority': 'api.dictionaryapi.dev',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'sec-fetch-site': 'same-site',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-user': '?1',
		    'sec-fetch-dest': 'document',
		    'referer': 'https://dictionaryapi.dev/',
		    'accept-language': 'en-US,en;q=0.9'
		}
		url = '{}/{}/{}'.format(Dictionary.BASE_URL, self.language, self.word)
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			result = '{}. {}. {}'
			response = response.json()
			for word in response:
				meaning = word['meanings'][0]
				part_of_speech = meaning['partOfSpeech']
				definition = meaning['definitions'][0]['definition']
				result = result.format(word['word'], part_of_speech, definition)
			return 1, result
		else:
			return 0, 'An error has occured'


def main():
	word = input("Word? ")
	status, message = Dictionary(word).get_word_meaning()
	if status == 1:
		print(message)


if __name__ == '__main__':
	main()


