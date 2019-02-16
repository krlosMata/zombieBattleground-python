from zombieBattleground import zombieBattleground

zombies = zombieBattleground.ZombieBattleground('v1')
filters = {
  'user_id':'1',
  'deck_id':'1'
}
data = zombies.getDecks(filters)

