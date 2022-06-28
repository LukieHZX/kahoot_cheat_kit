from kahoot import client

x = input('Names to spam (e.g.: TEST will do: 1. TEST, 2. TESTTEST, 3. TESTTESTTEST, ...)\n> ')
id_game = input('ID of Kahoot-Lobby\n> ')
c = input('How often do you want to have your bots in the Kahoot-Lobby? (Type a high number for full lobby)\n> ')
for counter, i in enumarate(range(c)):
    try:
        client().join(int(id_game), x*counter+1)
    except:
        pass
