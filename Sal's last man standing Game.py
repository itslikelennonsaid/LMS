import random, shelve, os, pprint
from placesfile import places
from weaponsfile import weapons
from clothingfile import clothing
from vehiclesfile import vehicles
from materialsfile import materials

def returnRandomItemFromList(list):
    '''Returns random item from a list'''
    rNum = random.randint(0,len(list)-1)
    print(rNum)
    print(len(list))
    return list[rNum]

def createNewPlayer(player):
    '''create new player file with all categories'''
    playerFile = shelve.open(str(player) + 'data')
    global playerStats
    playerStats = {'aim': 1,  'health': 110,
                   'attack': 5,  'speed': 3,
                   'knowledge': 1, 'xp': 1}

    #items: money and food 
    global playerItems
    playerItems = {'money':0, 'food':0, 'ammo':0, 'medkit':0, 'gas':0}
    #Weapons used for battl only
    global playerWeapons
    playerWeapons = {}
    #clothing used to add health only
    global playerClothing
    playerClothing = {}
    #vehicles carry people and add life
    global playerVehicles
    playerVehicles = {}
    #materials crafting and upgrading
    global playerMaterials
    playerMaterials = {}

    playerFile['playerStats'] = playerStats
    playerFile['playerWeapons'] = playerWeapons
    playerFile['playerClothing'] = playerClothing
    playerFile['playerVehicles'] = playerVehicles
    playerFile['playerMaterials'] = playerMaterials
    

createNewPlayer('Sal')









def ItemsWithCategories(itemName, itemDict, playerItemDict):
    if item == itemName:
        subItem = returnRandomItemFromList(list(itemDict.keys()))
        print('Upon closer examination you got a {0}!'.format(subItem))
        try:
            playerItemDict[subItem] = int(playerItemDict[subItem]) + 1
        except KeyError:
            playerItemDict[subItem] = 1
        print(itemName +': '+ str(playerItemDict))
        

def setGameState(state):
    stateList = ['Choose a Place', 'Battle', 'Repair']
    gameState = stateList[state]
    return gameState

def counter(x):
    x=x+1
    
while True:
    setGameState(0)
    place = None
    item = None
    #choose a place

    def chooseAPlace():
        place  = returnRandomItemFromList(list(places.keys()))
        print('You stumble to the {0}.'.format(place))
        return place

    place = chooseAPlace()

    def grabAnItem():
        item = returnRandomItemFromList(list(places[place]))
        print('You blindly grab a {0}.'.format(item))

        return item

    item = grabAnItem()

    '''if item.lower() in playerStats:
        print('poop')'''

    if item in list(playerItems.keys()):
        if item == 'money':
            itemQuant = random.randint(1,20)
            print('Turns out you grabbed {0} of em!'.format(itemQuant))
            playerItems[item.lower()] = playerItems[str(item.lower())] + itemQuant
            print('You\'ve now got {1} {0}.'.format(item, playerItems[item.lower()]))
            print(itemQuant)
            print(playerItems)
        else:
            itemQuant = random.randint(1,10)
            print('Turns out you grabbed {0} of em!'.format(itemQuant))
            playerItems[item.lower()] = playerItems[str(item.lower())] + itemQuant
            print('You\'ve now got {1} {0}.'.format(item, playerItems[item.lower()]))
            print(itemQuant)
            pprint.pprint(playerItems)

    elif item == 'clothing':
        ItemsWithCategories('clothing', clothing, playerClothing)
    elif item == 'vehicle':
        ItemsWithCategories('vehicle', vehicles, playerVehicles)
    elif item == 'weapon':
        ItemsWithCategories('weapon', weapons, playerWeapons)
    elif item == 'material':
        ItemsWithCategories('material', materials, playerMaterials)
    
    

    
            

            
            
   
    
    

    


    
    
    
    

