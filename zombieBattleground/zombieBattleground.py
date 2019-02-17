import urllib.request, json

# Constants
API_V1 = 'v1/'
BASE_URL_V1 = 'https://api.loom.games/zb/'

## Filter parameters accepted
# Deck list
getDeckList = ['id', 'user_id', 'deck_id', 'name', 'hero_id', 'primary_skill_id', 'secondary_skill_id', 'version']
# Get Deck by ID
getDeckbyID = []
# Get Match List
getMatchList = ['id', 'player1_id', 'player1_id', 'status', 'version', 'winner_id' ]
# Get Match by Id
getMatchByID = []
# Get card list
getCardList = ['id', 'mould_id', 'version', 'kind', 'set', 'name', 'rank', 'type', 'rarity', 'damage', 'heath', 'cost']
# Get card
getCard = []




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
   return ''
  for param in filterObjects:
    stringFilter += str(param) + '=' + str(filterObjects[param]) + '&'
  return stringFilter[:-1]

class ZombieBattleground:
    def __init__(self, apiVersion):
      self.apiVersion = apiVersion

    def getDeckList(self, filters = {}):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'decks/' + filters
      data = getHttpResp(getUrl)
      return data

    def getDeckByID(self, id):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'deck/' + str(id)
      data = getHttpResp(getUrl)
      return data

    def getMatchList(self, filters = {}):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'matches/' + filters
      data = getHttpResp(getUrl)
      return data

    def getMatchByID(self, id):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'match/' + str(id)
      data = getHttpResp(getUrl)
      return data

    def getCardList(self, filters = {}):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'cards/' + filters
      data = getHttpResp(getUrl)
      return data

    def getCard(self, mould_id, version):
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'card/' + str(mould_id) + str(version) 
      data = getHttpResp(getUrl)
      return data