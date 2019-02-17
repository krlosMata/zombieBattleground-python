import urllib.request, json

'''
constants definition
'''
API_V1 = 'v1/'
BASE_URL_V1 = 'https://api.loom.games/zb/'

'''
Filters not used since it can be catched by Http error response
'''
## Filter parameters accepted
# Deck list
getDeckList = ['id', 'user_id', 'deck_id', 'name', 'hero_id', 'primary_skill_id', 'secondary_skill_id', 'version']
# Get Deck by ID
getDeckbyID = []
# Get Match List
getMatchList = ['id', 'player1_id', 'player2_id', 'status', 'version', 'winner_id' ]
# Get Match by Id
getMatchByID = []
# Get card list
getCardList = ['id', 'mould_id', 'version', 'kind', 'set', 'name', 'rank', 'type', 'rarity', 'damage', 'heath', 'cost']
# Get card
getCard = []

def getHttpResp(url):
  '''
    Used to query any url
    @{String} url - String url literal
    @{Dictionaries} data response in json format if query in correct, http object response otherwise
  '''
  try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})   
    with urllib.request.urlopen(req) as response:
      data = json.loads(response.read().decode())
    return data
  except Exception as error:
    return error

def parseFilters(filterObjects):
  '''
    Convert bunch of filters into a single string to beadded to url
    @{Dictionaries} filterObjects - filters in key/value format
    @{String} filters to be used as a string into an url address
  '''
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
      '''
        Constructor
        @{String} apiVersion - Specific version of Api to use on Http calls
      '''
      self.apiVersion = apiVersion

    def getDeckList(self, filters = {}):
      '''
        Get all the decks availables. It can be filtered.
        @{Dictionary} filters - It contains all the filters applied to the Http call
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'decks/' + filters
      data = getHttpResp(getUrl)
      return data

    def getDeckByID(self, id):
      '''
        Get deck filtered by Id
        @{String} id - Parameter to filter decks
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      getUrl = BASE_URL_V1 + API_V1 + 'deck/' + str(id)
      data = getHttpResp(getUrl)
      return data

    def getMatchList(self, filters = {}):
      '''
        Get all the matches availables. It can be filtered.
        @{Dictionary} filters - It contains all the filters applied to the Http call
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'matches/' + filters
      data = getHttpResp(getUrl)
      return data

    def getMatchByID(self, id):
      '''
        Get match filtered by Id
        @{String} id - Parameter to filter matches
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      getUrl = BASE_URL_V1 + API_V1 + 'match/' + str(id)
      data = getHttpResp(getUrl)
      return data

    def getCardList(self, filters = {}):
      '''
        Get all the cards availables. It can be filtered.
        @{Dictionary} filters - It contains all the filters applied to the Http call
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      filters = parseFilters(filters)
      getUrl = BASE_URL_V1 + API_V1 + 'cards/' + filters
      data = getHttpResp(getUrl)
      return data

    def getCard(self, mould_id, version):
      '''
        Get card basd on its mould and version
        @{String} mould_id - Parameter to filter matches
        @{String} version - Parameter to filter matches
        @{Dictionary} Http already parsed into json format, Http error response otherwise
      '''
      getUrl = BASE_URL_V1 + API_V1 + 'card/' + str(mould_id) + str(version) 
      data = getHttpResp(getUrl)
      return data