from zombieBattleground import zombieBattleground


zombies = zombieBattleground.ZombieBattleground(zombieBattleground.API_V1)
filters = {
  'user_id':'ZombieSlayer_5699',
  'false_parameter': 'test'
}
data1 = zombies.getDeckList(filters)

data2 = zombies.getDeckList()

a = 5
a = a + 5

