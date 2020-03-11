import requests

class coinbaseAPI():
    def __init__(self):
        super().__init__()
    
    def getAllTickers(self):
        url = "https://www.coinbase.com/api/v2/assets/prices?base=INR&filter=listed&resolution=latest"
        payload = {}
        headers= {}
        response = requests.request("GET", url, headers=headers, data = payload)
        return response