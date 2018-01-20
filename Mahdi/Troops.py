#just starting from scratch! )
class Units:
    def __init__(self):
        self.movement_types=['Fly','Walk']
        self.movement_type='X'
        self.shoot_types=['Air','Ground','Both']
        self.shoot_type='X'
        self.target_types=['Building','Any']
        self.target_type=  'X'
        self.rarity_types = ['Common','Rare','Epic','Legendary']
        self.rarity_type = 'X'
        self.movement_speeds = ['Slow','Normal','Fast']
        self.movement_speed = 'X'
        self.elixir_costs = [1,2,3,4,5,6,7,8,9,10]
        self.elixir_cost = 'X'
        self.counts = [i for i in range(1,15)]
        self.count = 'X'
        self.hitpoints = [i for i in range(10,3000)]
        self.hp='X'
        self.damages=[i for i in range(10,1000)]
        self.damage='X'
        self.life_states=['Dead','Alive']
        self.life_state='X'
        self.deploy_states=['Deployed','inDeck','notinDeck']
        self.deploy_state = 'notinDeck'
        self.attack_types = ['Melee','Ranged']
        self.attack_type = 'X'

    def place_in_deck(self):
        self.deploy_state = 'inDeck'
    def deploy(self):
        self.life_state='Aliv   e'
        self.deploy_state = 'Deployed'
    def get_damage(self,value):
        self.hp=self.hitpoint
        self.hp -= value
        if self.hp ==0:
            self.kill()
    def re_assign_hp(self):
        self.hp = self.hitpoint
    def kill(self):
        self.life_state='Dead'
        self.deploy_state='notinDeck'
        self.re_assign_hp()
class Dragon(Units):
    def attr(self):
        self.movement_type='Fly'
        self.shoot_type='Both'
        self.target_type='Any'
        self.rarity_type='Rare'
        self.movement_speed=['Normal']
        self.elixir_cost=4
        self.hitpoint=600
        self.damage=100
        self.count=1
        self.attack_type ='Ranged'
class Goblin(Units):
    def attr(self):
        self.movement_type='Walk'
        self.shoot_type='Ground'
        self.target_type='Any'
        self.rarity_type='Common'
        self.movement_speed=['Fast']
        self.elixir_cost=2
        self.hitpoint=60
        self.damage=50
        self.count=3
        self.attack_type = 'Melee'

class Board:
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 'P', 'P', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'P', 'P', 0, 0, 1]
    [1, 0, 0, 'P', 'P', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'P', 'P', 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0,'B','B', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'B','B', 0, 0, 1]
    [1, 0, 0, 'B', 'B', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'B', 'B', 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    [1, 0, 0, 'P', 'P', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'P', 'P', 0, 0, 1]
    [1, 0, 0, 'P', 'P', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'P', 'P', 0, 0, 1]