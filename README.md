# zombieBattleground-python
Python wrapper for zombie-battleground API game [https://loom.games/en/]

This module aims to provide easy access to zombie battleground api calls [https://api-docs.loom.games/]

## Basic usage
```python
import zombieBattleground

'''
Initialize class zombieBattleground
'''
zombies = zombieBattleground.ZombieBattleground(zombieBattleground.API_V1)

'''
Get Decks
'''
dataGetDecks = zombies.getDeckList()

'''
Get Decks by any filter
'''
filtersDeckList = {
  'user_id':'ZombieSlayer_5699',
}
dataGetDecksFiltered = zombies.getDeckList(filtersDeckList)

'''
Get Decks by Id
'''
dataGetDecksById = zombies.getDeckByID('3')

'''
Get Matches
'''
dataGetMatches = zombies.getMatchList()

'''
Get Matches by any filter
'''
filtersMatchList = {
  'id':'8',
}
dataGetMatchesFiltered = zombies.getMatchList(filtersMatchList)

'''
Get Match by Id
'''
dataGetMatchesById = zombies.getMatchByID('3')

'''
Get Card List
'''
dataGetCardList = zombies.getCardList()

'''
Get Card List by any filter
'''
filtersCardList = {
  'name':'Whizpar',
}
dataGetCardListFiltered = zombies.getCardList(filtersCardList)

'''
Get Card List by any filter
'''
dataGetCardList = zombies.getCard('1', 'v3')
```
