import requests

class bitbnsController():
    def __init__(self):
        super().__init__()

    def getAllTickers(self):
        url = "https://bitbns.com/order/getTickerWithVolume/"
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
        return getJsonRates

    def getRates(self,currentList):
        lastRates = self.getJSONData()
        returnDictionary = {}
        for i in currentList: # Apply try catch if currency is not present
            currentInfo = lastRates[i]
            buySellList = []
            buySellList.append(currentInfo['highest_buy_bid'])
            buySellList.append(currentInfo['lowest_sell_bid'])
            returnDictionary[i] = buySellList
        return returnDictionary
        