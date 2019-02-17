import zombieBattleground

'''
Initialize class zombieBattleground
'''
ZombieAPI = zombieBattleground.ZombieBattleground(zombieBattleground.API_V1)

'''
Get Decks
'''
dataGetDecks = ZombieAPI.getDeckList()

'''
Get Decks by any filter
'''
filtersDeckList = {
  'user_id':'ZombieSlayer_5699',
}
dataGetDecksFiltered = ZombieAPI.getDeckList(filtersDeckList)

'''
Get Decks by Id
'''
dataGetDecksById = ZombieAPI.getDeckByID('3')

'''
Get Matches
'''
dataGetMatches = ZombieAPI.getMatchList()

'''
Get Matches by any filter
'''
filtersMatchList = {
  'id':'8',
}
dataGetMatchesFiltered = ZombieAPI.getMatchList(filtersMatchList)

'''
Get Match by Id
'''
dataGetMatchesById = ZombieAPI.getMatchByID('1454')

'''
Get Card List
'''
dataGetCardList = ZombieAPI.getCardList()

'''
Get Card List by any filter
'''
filtersCardList = {
  'name':'Whizpar',
}
dataGetCardListFiltered = ZombieAPI.getCardList(filtersCardList)

'''
Get Card List by any filter
'''
dataGetCardList = ZombieAPI.getCard('1', 'v3')