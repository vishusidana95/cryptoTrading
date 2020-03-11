import requests

class coinbaseController():
    def __init__(self):
        super().__init__()

    def getAllTickers(self):
        url = "https://www.coinbase.com/api/v2/assets/prices?base=INR&filter=listed&resolution=latest"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data = payload)
        try:
            if(response.status_code == 200):
                return response
            else:
                return None
        except Exception as e:
            raise e
        return None
    
    def getJSONData(self):
        getRawRates = self.getAllTickers()
        if(getRawRates == None): # Add last 10 sec old request
            return None
        getJsonRates = getRawRates.json()
        return getJsonRates['data']
    
    def getRates(self,currencyList):
        lastRates = self.getJSONData()
        returnDictionary = {}
        for currency in currencyList:
            currencyData = None
            buySellList = []
            for i in range(len(lastRates)):
                if lastRates[i]['base'] == currency:
                    currencyData = lastRates[i]
                    break
            currentData = float(currencyData['prices']['latest'])
            currentData = round(currentData,2)
            buySellList.append(currentData)
            buySellList.append(currentData)
            returnDictionary[currency] = buySellList
        return returnDictionary