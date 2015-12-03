class Item:
    itemtable = { 'GEM' : 
                [ 
                    { 'HP' : 
                        [ 'Pride', 'Joy']
                        },
                    { 'MP' :
                        [ 'Pride', 'Joy']
                        }
                    ]
                    }

    positiontable = { 'HP' : (10,20),
                    'MP' : (20,30),
                    'Pride' : (30,40),
                    'Joy' : (40,50),
                    'GEM' : (50,60)
                    }

    def __init__(self, name, qty=1):
        self.name  = name
        self.qty = qty

    def buy_item(self):
        print ("clicking", self.name, "at", self.positiontable[self.name])

    def buy_prereq(self):
        for x in range(self.qty):
            for y in self.itemtable[self.name]:
                for a,b in y.items():
                    for c in b:
                        subitemtwo = Item(c, self.positiontable[c])
                        subitemtwo.buy_item()
                    subitemone = Item(a, self.positiontable[a])
                    subitemone.buy_item()

gemone = Item("GEM")

print ("Buying", gemone.name)

gemone.buy_prereq()
gemone.buy_item()

