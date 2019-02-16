import urllib.request, json

API_V1 = 'v1/'
BASE_URL_V1 = 'https://api.loom.games/zb/'

def getHttpResp(url):
  try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})   
    with urllib.request.urlopen(req) as response:
      data = json.loads(response.read().decode())
    return data
  except Exception as error:
    return error

def parseFilters(filterObjects):
  
  filtersArray = []
  stringFilter = ''
  if len(filterObjects) > 0:
    stringFilter += '?'
  else:
   return []

  for param in filterObjects:
    stringFilter += str(param) + '=' + str(filterObjects[param]) + '&'
  return stringFilter[:-1]



class ZombieBattleground:
    def __init__(self, apiVersion):
      self.apiVersion = apiVersion

    def getDecks(self, filters = {}):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'decks/' + filters
      data = getHttpResp(getUrl)
      return data