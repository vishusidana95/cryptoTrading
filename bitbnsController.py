import requests

class bitbnsController():
    def __init__(self):
        super().__init__()

    def getAllTickers(self):
        url = "https://bitbns.com/order/getTickerWithVolume/"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data = payload)
        return response

    def getJSONData(self):
        getRawRates = self.getAllTickers()
        getJsonRates = getRawRates.json()
        return getJsonRates

    def getBuyRates(self,currentList):
        