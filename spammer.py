from kahoot import client

x = input('NAMES TO SPAM (E.G.: TEST will do: 1. TEST, 2. TESTEST, 3. TESTTESTTEST, etc.\n> )')
id_game = input('ID OF KAHOOT GAME\n> ')
for counter, i in enumarate(range(150)):
    try:
        client().join(int(id_game), x + x*counter)
        y += 1
    except:
        pass
