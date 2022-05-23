import requests

def get_quote():
    
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    
    response = requests.get(url).json()[0]
    
    quote = response['quote']
    author = response['author']
    
    return quote, author


if __name__=='__main__':
    print(get_quote())
