import httpx 

class RandomApiClient():
    def __init__(self, appSettings) -> None:
        self.__choice_endpoint_url = appSettings.random_api_base_url + "/random/default/choice"

    async def getRandomChoice(self, values):
       with httpx.Client() as client:
           return client.get(self.__choice_endpoint_url, params={"value": values}).json()