import requests

def get_quote():
    
    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    
    response = requests.get(url).json()
    
    return response[0]


if __name__=='__main__':
    print(get_quote())
