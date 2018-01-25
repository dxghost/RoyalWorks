#just starting from scratch! )
import PIL
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


class Units:
    '''
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
    '''

    def place_in_deck(self):
        self.deploy_state = 'inDeck'

    def deploy(self):
        self.life_state = 'Aliv   e'
        self.deploy_state = 'Deployed'

    def get_damage(self, value):
        self.hp = self.hitpoint
        self.hp -= value
        if self.hp == 0:
            self.kill()

    def re_assign_hp(self):
        self.hp = self.hitpoint

    def kill(self):
        self.life_state = 'Dead'
        self.deploy_state = 'notinDeck'
        self.re_assign_hp()


class Dragon(Units):
    def attr(self):
        self.movement_type = 'Fly'
        self.shoot_type = 'Both'
        self.target_type = 'Any'
        self.rarity_type = 'Rare'
        self.movement_speed = ['Normal']
        self.elixir_cost = 4
        self.hitpoint = 600
        self.damage = 100
        self.count = 1
        self.attack_type = 'Ranged'


class Goblin(Units):
    def __init__(self):
        # attributes
        self.movement_type = 'Walk'
        self.shoot_type = 'Ground'
        self.target_type = 'Any'
        self.rarity_type = 'Common'
        self.movement_speed = ['Fast']
        self.elixir_cost = 2
        self.hitpoint = 60
        self.damage = 50
        self.count = 3
        self.attack_type = 'Melee'


class Prince(Units):
    def __init__(self):
        # attributes
        self.movement_type = 'Walk'
        self.shoot_type = 'Ground'
        self.target_type = 'Any'
        self.rarity_type = 'Common'
        self.movement_speed = ['Fast']
        self.elixir_cost = 2
        self.hitpoint = 60
        self.damage = 50
        self.count = 3
        self.attack_type = 'Melee'
        # load image

        self.images = []
        self.img = pygame.image.load("Assets\\chr_prince_out\\1_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\2_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\3_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\4_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\5_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\6_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\7_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\8_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\9_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.img = pygame.image.load("Assets\\chr_prince_out\\10_Down.png")
        self.img = pygame.transform.scale(self.img, (90, 90))
        self.images.append(self.img)
        self.prince = AnimatedSprite((200, 100), images)
        up_prince = pygame.sprite.Group(prince)

