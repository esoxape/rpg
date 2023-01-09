import curses
import time
import random
import math
from curses import panel
yourTarget=-1
submenuWeapons=[]
submenuRangedWeapon=[]
submenuArmor=[]
main_menu=[]
class Menu(object):
    def __init__(self, items, stdscreen,check):
        self.window = stdscreen.subwin(0, 0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.check=check
        self.items.append(("exit", "exit"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = "%d. %s" % (index, item[0])
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

class StoreKnight(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        main_menu_items = [
            ("Chain Mail (5 damage absorbtion)- 1000 gp", lambda:CanBuy(self.screen,1000,"Chain Mail")),
            ("Full Plate (8 damage absorbtion) - 10000 gp", lambda:CanBuy(self.screen,10000,"Full Plate")),
            ("Steel Two Handed Sword - 1000 gp", lambda:CanBuy(self.screen,1000,"Steel Two Handed Sword")),
            ("Magic Two Handed Sword - 10000 gp", lambda:CanBuy(self.screen,10000,"Magic Two Handed Sword")),
            ("Steel Throwing Dagger - 1000 gp", lambda:CanBuy(self.screen,1000,"Steel Throwing Dagger")),          
        ]
        main_menu = Menu(main_menu_items, self.screen, 0)
        main_menu.display()

class StoreHunter(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        main_menu_items = [
            ("Chain Mail (5 damage absorbtion)- 1000 gp", lambda:CanBuy(self.screen,1000,"Chain Mail")),
            ("Full Plate (8 damage absorbtion)- 10000 gp", lambda:CanBuy(self.screen,10000,"Full Plate")),
            ("Composite Bow- 1000 gp", lambda:CanBuy(self.screen,1000,"Composite Bow")),
            ("Long Bow - 10000 gp", lambda:CanBuy(self.screen,10000,"Long Bow")),
            ("Steel Daggers - 1000 gp", lambda:CanBuy(self.screen,1000,"Steel Daggers")),
            ("Magic Daggers - 10000 gp", lambda:CanBuy(self.screen,10000,"Magic Daggers")),           
        ]
        main_menu = Menu(main_menu_items, self.screen,0)
        main_menu.display()

class StoreMage(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        main_menu_items = [
            ("Apprentice Robe (3 damage absorbtion) - 1000 gp", lambda:CanBuy(self.screen,1000,"Apprentice Robe")),
            ("Master Robe (5 damage absorbtion)- 10000 gp", lambda:CanBuy(self.screen,10000,"Master Robe")),
            ("Ice Twister Spell - 1000 gp", lambda:CanBuy(self.screen,1000,"Ice Twister Spell")),
            ("Yew Quarterstaff - 10000 gp", lambda:CanBuy(self.screen,10000,"Yew Quarterstaff")),
            ("Quarterstaff - 1000 gp", lambda:CanBuy(self.screen,1000,"Quarterstaff")),
            ("Meteor Spell - 10000 gp", lambda:CanBuy(self.screen,10000,"Meteor Spell")),          
        ]
        main_menu = Menu(main_menu_items, self.screen,0)
        main_menu.display()    
class Inventory(object):
    def __init__(self, stdscreen):
        submenu1=[]
        submenu2=[]
        submenu3=[]
        global submenuWeapons
        global submenuRangedWeapon
        global submenuArmor
        global main_menu
        submenuWeapons=[]
        submenuRangedWeapon=[]
        submenuArmor=[]
        main_menu=[]
        self.screen = stdscreen
        curses.curs_set(0)
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Weapon":
                submenu1.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Ranged Weapon":
                submenu2.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))  
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Armor":
                submenu3.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))
        submenuWeapons=Menu(submenu1, self.screen, 0)
        submenuRangedWeapon=Menu(submenu2, self.screen, 0)
        submenuArmor=Menu(submenu3, self.screen, 0)
        main_menu_items = [
            ("Weapon - "+p1.weapon.name, submenuWeapons.display),
            ("Ranged Weapon - "+p1.rangedWeapon.name, submenuRangedWeapon.display),
            ("Armor - "+p1.armor.name, submenuArmor.display),
        ]
        main_menu = Menu(main_menu_items, self.screen,1)
        main_menu.display() 
    def Equip(self,index):
        submenu1=[]
        submenu2=[]
        submenu3=[]       
        if p1.inventory[index].type=="Weapon":        
            p1.weapon=item(p1.inventory[index].name)        
        if p1.inventory[index].type=="Ranged Weapon":        
            p1.rangedWeapon=item(p1.inventory[index].name)              
        if p1.inventory[index].type=="Armor":        
            p1.armor=item(p1.inventory[index].name)      
        self.screen.addstr(0, 0, "Equipped "+p1.inventory[index].name)
        self.screen.refresh()
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Weapon":
                submenu1.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Ranged Weapon":
                submenu2.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))  
        for i in range(len(p1.inventory)):
            if p1.inventory[i].type=="Armor":
                submenu3.append((p1.inventory[i].name, lambda x=i:Inventory.Equip(self,x)))
        submenuWeapons.items=submenu1
        submenuRangedWeapon.items=submenu2
        submenuArmor.items=submenu3
        submenuWeapons.items.append(("exit", "exit"))
        submenuRangedWeapon.items.append(("exit", "exit"))
        submenuArmor.items.append(("exit", "exit"))
        main_menu.items=[
            ("Weapon - "+p1.weapon.name, submenuWeapons.display),
            ("Ranged Weapon - "+p1.rangedWeapon.name, submenuRangedWeapon.display),
            ("Armor - "+p1.armor.name, submenuArmor.display),
            ("exit", "exit"),
        ]
def CanBuy(screen,price,index):
    if price<p1.gold:
        p1.inventory.append(item(index))
        p1.gold=p1.gold-price
        screen.addstr(0, 0, "Bought "+index)
        screen.refresh()
    else: 
        screen.addstr(0, 0, "Not Enough Gold ")
        screen.refresh()    

file = open('GFX.txt')
GFX = file.readlines()
file.close()
GFX = [line.strip('\n') for line in GFX]
class monster:
    monsters=[]
    def __init__(self, name, xx, yy):
        self.name=name
        if(self.name=="Death"):
            self.gold=random.randint(1000,5000)
            self.xp=10000
            self.hp=500
            self.maxhp=500
            self.damage="1d4"
            self.absorb=1
            self.weapon="bites"
            self.gfx="\U0001F432"
            self.speed=14
            self.fireSpeed=100
            self.tick=0
            self.tickWeapon=0            
            self.Range=5
            self.x=xx
            self.y=yy            
            self.previousGFX=map[xx][yy]  
            self.meleeGFX=monster.CreateGFX(self)
            self.rangedWeapon=item("Dragon Breath")
        if(self.name=="Dragon"):
            self.gold=random.randint(1000,5000)
            self.xp=10000
            self.hp=500
            self.maxhp=500
            self.damage="2d20"
            self.absorb=1
            self.weapon="bites"
            self.gfx="\U0001F432"
            self.speed=14
            self.fireSpeed=100
            self.tick=0
            self.tickWeapon=0            
            self.Range=5
            self.x=xx
            self.y=yy            
            self.previousGFX=map[xx][yy]  
            self.meleeGFX=monster.CreateGFX(self)
            self.rangedWeapon=item("Dragon Breath")
        if(self.name=="Bat"):
            self.gold=random.randint(100,500)
            self.xp=500
            self.hp=20
            self.maxhp=20
            self.damage="1d4"
            self.absorb=1
            self.weapon="bites"
            self.gfx="\U0001F987"
            self.speed=3
            self.fireSpeed=10
            self.tick=0
            self.tickWeapon=0            
            self.Range=-1
            self.x=xx
            self.y=yy            
            self.previousGFX=map[xx][yy]  
            self.meleeGFX=monster.CreateGFX(self)
            self.rangedWeapon=item("None")
        if(self.name=="Elf"):
            self.gold=random.randint(250,1000)
            self.xp=2500
            self.hp=50
            self.maxhp=50
            self.damage="1d6"
            self.absorb=2
            self.weapon="slashes"
            self.gfx="\U0001F9DD"
            self.speed=14
            self.fireSpeed=80
            self.tick=0
            self.tickWeapon=0            
            self.Range=random.randint(15,20)
            self.x=xx
            self.y=yy            
            self.previousGFX=map[xx][yy]  
            self.rangedWeapon=item("Elf Bow")
            self.meleeGFX=monster.CreateGFX(self)
    def Fire(self):
        dirx=diry=0
        self.tickWeapon+=1
        if self.tickWeapon==self.fireSpeed:
            self.tickWeapon=0
            if abs(playerposx-self.x)>abs(playerposy-self.y):dirx=playerposx-self.x                
            else:diry=playerposy-self.y
            if dirx>0:Bullets.append(projectile(self.x,self.y,self.rangedWeapon,"S",0,self.name))
            if dirx<0:Bullets.append(projectile(self.x,self.y,self.rangedWeapon,"N",0,self.name))
            if diry>0:Bullets.append(projectile(self.x,self.y,self.rangedWeapon,"E",0,self.name))
            if diry<0:Bullets.append(projectile(self.x,self.y,self.rangedWeapon,"W",0,self.name))

    def CreateGFX(self):
        result=[["" for x in range(1)] for y in range(42)]
        if self.name=="Bat":
            start=1
            end=11
        if self.name=="Elf":
            start=48
            end=78
        if self.name=="Dragon":
            start=80
            end=104
        if self.name=="Death":
            start=109
            end=139
        fromTop=math.floor((42-(end-start+1))/2)
        length=0
        for i in range(start, end+1):
            if len(GFX[i])>length:length=len(GFX[i])
        whitespace=math.floor((238-length)/2)
        for i in range(len(result)):
            for j in range(whitespace):
                result[i][0]=result[i][0]+" "
        for i in range(start, end+1):                                
            result[fromTop][0]=result[fromTop][0]+GFX[i]
            fromTop+=1            
        i=0
        while(len(result[41][0])<238):
            while(len(result[i][0])<238):               
                result[i][0]=result[i][0]+" "
            i=i+1
        return result
    def Move(self):
        self.tick+=1
        if self.speed<self.tick:         
            self.tick=0  
        # Determine target destination
            target_x, target_y = playerposx, playerposy
        # Create a list of possible moves
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Choose the move that maximizes distance to target and stays at the same x or y coordinate
            max_distance = float("-inf")
            best_move = None
            for dx, dy in moves:
                x, y = self.x + dx, self.y + dy
                distance = ((x - target_x) ** 2 + (y - target_y) ** 2) ** 0.5
                if distance > max_distance and (x == self.x or y == self.y) and (map[x][y]=="  " or map[x][y]==". "):
                    max_distance = distance
                    best_move = (dx, dy)
        # If the distance between the monster and the player is greater than the desired distance, move towards the player
            if distance > self.Range:
                min_distance = float("inf")
                best_move = None
                for dx, dy in moves:
                    x, y = self.x + dx, self.y + dy
                    distance = ((x - target_x) ** 2 + (y - target_y) ** 2) ** 0.5
                    if distance < min_distance and map[x][y]=="  " or distance < min_distance and map[x][y]==". ":
                        min_distance = distance
                        best_move = (dx, dy)
        # Update position and return new position
            map[self.x][self.y]=self.previousGFX
            if best_move is None:
                best_move = (0, 0)
            self.x += best_move[0]
            self.y += best_move[1]
            if self.x==playerposx and self.y==playerposy:return True
            if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":self.previousGFX=map[self.x][self.y]
            map[self.x][self.y]=self.gfx            
            return False     
noGo=["\U0001F525","\U00002191 ","\U00002192 ","\U00002193 ","\U00002190 ","\U00002744 ","* ","O ", " O","\U0001F4A5","OO"]
class item:
    def __init__(self, name):
        self.name=name
        if name=="Dragon Breath":
            self.gfxN="\U0001F525"     
            self.gfxE="\U0001F525" 
            self.gfxS="\U0001F525"
            self.gfxW="\U0001F525"
            self.speed=3
            self.range=8
            self.damage="1d12"
            self.pattern="V"
            self.type="Ranged Weapon"
        if name=="Long Bow":
            self.gfxN="\U00002191 "     
            self.gfxE="\U00002192 " 
            self.gfxS="\U00002193 "
            self.gfxW="\U00002190 "
            self.speed=3
            self.range=80
            self.damage="1d20"
            self.pattern="|||"
            self.type="Ranged Weapon"
        if name=="Elf Bow":
            self.gfxN="\U00002191 "     
            self.gfxE="\U00002192 " 
            self.gfxS="\U00002193 "
            self.gfxW="\U00002190 "
            self.speed=4
            self.range=80
            self.damage="1d8"
            self.pattern="|||"
            self.type="Ranged Weapon"
        if name=="None":
            self.gfxN="  "     
            self.gfxE="  " 
            self.gfxS="  "
            self.gfxW="  "
            self.speed=2
            self.range=0
            self.damage="1d6"
            self.pattern="|"
            self.type="Ranged Weapon"
        if name=="Short Bow":
            self.gfxN="\U00002191 "     
            self.gfxE="\U00002192 " 
            self.gfxS="\U00002193 "
            self.gfxW="\U00002190 "
            self.speed=2
            self.range=80
            self.damage="1d8"
            self.pattern="|||"
            self.type="Ranged Weapon"
        if name=="Composite Bow":
            self.gfxN="\U00002191 "     
            self.gfxE="\U00002192 " 
            self.gfxS="\U00002193 "
            self.gfxW="\U00002190 "
            self.speed=2
            self.range=80
            self.damage="1d12"
            self.pattern="|||"
            self.type="Ranged Weapon"
        if name=="Rusty Throwing Dagger":
            self.gfxN="* "     
            self.gfxE="* " 
            self.gfxS="* "
            self.gfxW="* "
            self.speed=3
            self.range=5
            self.damage="1d4"
            self.pattern="W"
            self.type="Ranged Weapon"
        if name=="Steel Throwing Dagger":
            self.gfxN="* "     
            self.gfxE="* " 
            self.gfxS="* "
            self.gfxW="* "
            self.speed=3
            self.range=5
            self.damage="1d8"
            self.pattern="WW"
            self.type="Ranged Weapon"
        if name=="Iceball Spell":
            self.gfxN="\U00002744 "     
            self.gfxE="\U00002744 "    
            self.gfxS="\U00002744 "   
            self.gfxW="\U00002744 "   
            self.speed=8
            self.range=30
            self.damage="1d12"
            self.pattern="|"
            self.type="Ranged Weapon"
        if name=="Meteor Spell":
            self.gfxN="OO"     
            self.gfxE="OO"    
            self.gfxS="OO"   
            self.gfxW="OO"   
            self.speed=4
            self.range=3000
            self.damage="2d12"
            self.pattern="O"
            self.type="Ranged Weapon"
        if name=="Ice Twister Spell":
            self.gfxN="\U00002744 "     
            self.gfxE="\U00002744 "    
            self.gfxS="\U00002744 "   
            self.gfxW="\U00002744 "   
            self.speed=10
            self.range=30
            self.damage="1d12"
            self.pattern="*|*"
            self.type="Ranged Weapon"
        if name=="Ice Twister SpellGFX":
            self.gfxN="\U00002744 "     
            self.gfxE="\U00002744 "    
            self.gfxS="\U00002744 "   
            self.gfxW="\U00002744 "   
            self.speed=1
            self.range=1
            self.damage="1d12"
            self.pattern="*|*"
            self.type="Ranged Weapon"
        if name=="Meteor SpellGFX":
            self.gfxN="\U0001F4A5"     
            self.gfxE="\U0001F4A5"    
            self.gfxS="\U0001F4A5"   
            self.gfxW="\U0001F4A5"   
            self.speed=1
            self.range=1
            self.damage="1d12"
            self.pattern="*|*"
            self.type="Ranged Weapon"
        if name=="Rusty Two Handed Sword":
            self.damage="1d8"
            self.attacks=1
            self.type="Weapon"
        if name=="Steel Two Handed Sword":
            self.damage="1d12"
            self.attacks=1
            self.type="Weapon"
        if name=="Magic Two Handed Sword":
            self.damage="1d12"
            self.attacks=2
            self.type="Weapon"
        if name=="Rusty Daggers":
            self.damage="1d4"
            self.attacks=2
            self.penetration=1
            self.type="Weapon"
        if name=="Steel Daggers":
            self.damage="1d6"
            self.attacks=2
            self.penetration=1
            self.type="Weapon"
        if name=="Magic Daggers":
            self.damage="1d10"
            self.attacks=2
            self.penetration=1
            self.type="Weapon"
        if name=="Broken Quarterstaff":
            self.damage="1d4"
            self.attacks=1
            self.type="Weapon"
        if name=="Quarterstaff":
            self.damage="1d8"
            self.attacks=1
            self.type="Weapon"
        if name=="Yew Quarterstaff":
            self.damage="1d12"
            self.attacks=1
            self.type="Weapon"
        if name=="Leather Armor":
            self.absorb=2
            self.type="Armor"
        if name=="Chain Mail":
            self.absorb=5
            self.type="Armor"
        if name=="Full Plate":
            self.absorb=8
            self.type="Armor"
        if name=="Novice Robe":
            self.absorb=1
            self.type="Armor"
        if name=="Apprentice Robe":
            self.absorb=3
            self.type="Armor"
        if name=="Master Robe":
            self.absorb=5
            self.type="Armor"
class player:
    def __init__(self,name,klass):
        self.name=name
        self.klass=klass
        self.gold=0
        self.inventory=[]
        self.level=1
        self.xp=0
        self.regen=1
        self.attacks=1
        self.levelUp=500
        if klass=="Knight":
            self.hp=60
            self.maxHP=60
            self.weapon=item("Rusty Two Handed Sword")
            self.rangedWeapon=item("Rusty Throwing Dagger")
            self.armor=item("Leather Armor")
            self.inventory.append(item("Rusty Two Handed Sword"))
            self.inventory.append(item("Rusty Throwing Dagger"))
            self.inventory.append(item("Leather Armor"))            
        if klass=="Hunter":
            self.hp=50
            self.maxHP=50
            self.weapon=item("Rusty Daggers")
            self.rangedWeapon=item("Short Bow")
            self.armor=item("Leather Armor")
            self.inventory.append(item("Rusty Daggers"))
            self.inventory.append(item("Short Bow"))
            self.inventory.append(item("Leather Armor"))      
        if klass=="Mage":
            self.hp=40
            self.maxHP=40
            self.weapon=item("Broken Quarterstaff")
            self.rangedWeapon=item("Iceball Spell")
            self.armor=item("Novice Robe")
            self.inventory.append(item("Broken Quarterstaff"))
            self.inventory.append(item("Iceball Spell"))
            self.inventory.append(item("Novice Robe"))   

class projectile:        
    def __init__(self, x,y,type, direction, fireCheck,name,tickTotal=0, storeMapGfx="  "):
        self.x=x
        self.y=y
        self.type=type
        self.direction=direction
        self.tick=0
        self.fireCheck=fireCheck
        self.tickTotal=tickTotal
        self.storeMapGfx=storeMapGfx
        self.name=name
        self.didMove=False
    def Move(self):
        self.tick += 1  
        if self.tickTotal==0 and self.tick==1 and self.type.pattern =="WW" and self.fireCheck==0 or self.tickTotal==5 and self.tick==1 and self.type.pattern =="WW" and self.fireCheck==0:
            if self.direction=="N":
                Bullets.append(projectile(self.x,self.y,self.type,"NW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"NE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"N",1,self.name))
            if self.direction=="E":
                Bullets.append(projectile(self.x,self.y,self.type,"ENE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"ESE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"E",1,self.name))
            if self.direction=="S":
                Bullets.append(projectile(self.x,self.y,self.type,"SE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"SW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"S",1,self.name))
            if self.direction=="W":
                Bullets.append(projectile(self.x,self.y,self.type,"WNW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"WSW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"W",1,self.name))       
        if self.tickTotal==self.type.range+1:
            if self.type.pattern=="O":projectile.Boom(self)            
            return True
        if self.tick==2 and self.type.name=="Ice Twister SpellGFX" or self.tick==2 and self.type.name=="Meteor SpellGFX":
            if self.type.pattern=="O":projectile.Boom(self)
            map[self.x][self.y]=self.storeMapGfx
            return True
        if self.tickTotal==self.type.range:
            if self.type.pattern=="O":projectile.Boom(self)
            if self.type.gfxN==map[self.x][self.y]:map[self.x][self.y]=self.storeMapGfx
            elif self.type.gfxE==map[self.x][self.y]:map[self.x][self.y]=self.storeMapGfx
            elif self.type.gfxS==map[self.x][self.y]:map[self.x][self.y]=self.storeMapGfx
            elif self.type.gfxW==map[self.x][self.y]:map[self.x][self.y]=self.storeMapGfx
            return True
        if self.direction=="None":
            map[self.x][self.y] = self.type.gfxN
            if self.tick%2==0:self.tickTotal+=1
        if self.tickTotal==0 and self.tick==1 and self.type.pattern =="W" and self.fireCheck==0:
            if self.direction=="N":
                Bullets.append(projectile(self.x,self.y,self.type,"NW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"NE",1,self.name))
            if self.direction=="E":
                Bullets.append(projectile(self.x,self.y,self.type,"ENE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"ESE",1,self.name))
            if self.direction=="S":
                Bullets.append(projectile(self.x,self.y,self.type,"SE",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"SW",1,self.name))
            if self.direction=="W":
                Bullets.append(projectile(self.x,self.y,self.type,"WNW",1,self.name))
                Bullets.append(projectile(self.x,self.y,self.type,"WSW",1,self.name))

        if self.tickTotal==0 and self.tick==1 and self.type.pattern =="|||" and self.fireCheck==0:
            if self.direction=="N":
                if map[self.x][self.y+1]=="  " or map[self.x][self.y+1]==". ":Bullets.append(projectile(self.x,self.y+1,self.type,"N",1,self.name))
                if map[self.x][self.y-1]=="  " or map[self.x][self.y-1]==". ":Bullets.append(projectile(self.x,self.y-1,self.type,"N",1,self.name))
            if self.direction=="E":
                if map[self.x+1][self.y]=="  " or map[self.x+1][self.y]==". ":Bullets.append(projectile(self.x+1,self.y,self.type,"E",1,self.name))
                if map[self.x-1][self.y]=="  " or map[self.x-1][self.y]==". ":Bullets.append(projectile(self.x-1,self.y,self.type,"E",1,self.name))
            if self.direction=="S":
                if map[self.x][self.y+1]=="  " or map[self.x][self.y+1]==". ":Bullets.append(projectile(self.x,self.y+1,self.type,"S",1,self.name))
                if map[self.x][self.y-1]=="  " or map[self.x][self.y-1]==". ":Bullets.append(projectile(self.x,self.y-1,self.type,"S",1,self.name))
            if self.direction=="W":
                if map[self.x+1][self.y]=="  " or map[self.x+1][self.y]==". ":Bullets.append(projectile(self.x+1,self.y,self.type,"W",1,self.name))
                if map[self.x-1][self.y]=="  " or map[self.x-1][self.y]==". ":Bullets.append(projectile(self.x-1,self.y,self.type,"W",1,self.name))

        if self.didMove==True and self.tick==1 and self.type.pattern =="V" and self.fireCheck<5 and self.tickTotal%2==0:
            if self.direction=="N":
                if map[self.x][self.y+1]=="  " or map[self.x][self.y+1]==". ":Bullets.append(projectile(self.x,self.y+1,self.type,"N",self.fireCheck+1,self.name,self.tickTotal))
                if map[self.x][self.y-1]=="  " or map[self.x][self.y-1]==". ":Bullets.append(projectile(self.x,self.y-1,self.type,"N",self.fireCheck+1,self.name,self.tickTotal))
                self.fireCheck=5
            if self.direction=="E":
                if map[self.x+1][self.y]=="  " or map[self.x+1][self.y]==". ":Bullets.append(projectile(self.x+1,self.y,self.type,"E",self.fireCheck+1,self.name,self.tickTotal))
                if map[self.x-1][self.y]=="  " or map[self.x-1][self.y]==". ":Bullets.append(projectile(self.x-1,self.y,self.type,"E",self.fireCheck+1,self.name,self.tickTotal))
                self.fireCheck=5
            if self.direction=="S":
                if map[self.x][self.y+1]=="  " or map[self.x][self.y+1]==". ":Bullets.append(projectile(self.x,self.y+1,self.type,"S",self.fireCheck+1,self.name,self.tickTotal))
                if map[self.x][self.y-1]=="  " or map[self.x][self.y-1]==". ":Bullets.append(projectile(self.x,self.y-1,self.type,"S",self.fireCheck+1,self.name,self.tickTotal))
                self.fireCheck=5
            if self.direction=="W":
                if map[self.x+1][self.y]=="  " or map[self.x+1][self.y]==". ":Bullets.append(projectile(self.x+1,self.y,self.type,"W",self.fireCheck+1,self.name,self.tickTotal))
                if map[self.x-1][self.y]=="  " or map[self.x-1][self.y]==". ":Bullets.append(projectile(self.x-1,self.y,self.type,"W",self.fireCheck+1,self.name,self.tickTotal))
                self.fireCheck=5

        if self.direction == "N" or self.direction=="NW" or self.direction=="NE":    
            if self.type.speed == self.tick: 
                self.tickTotal+=1 
                self.didMove=True               
                if self.tickTotal>1 and self.type.pattern!="V":map[self.x][self.y]=self.storeMapGfx
                elif self.type.pattern=="V": Bullets.append(projectile(self.x,self.y,self.type,"None",1,self.name,0,self.storeMapGfx))               
                self.tick = 0
                if self.x-1==playerposx and self.y==playerposy and self.direction=="N" or self.x-1==playerposx and self.y-1==playerposy and self.direction=="NW" or self.x-1==playerposx and self.y+1==playerposy and self.direction=="NE":
                    projectile.PlayerDamage(self) 
                elif self.direction=="N":
                    self.x = self.x - 1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxN
                elif self.direction=="NW":
                    self.x = self.x - 1
                    self.y-=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxN
                elif self.direction=="NE":
                    self.x = self.x - 1
                    self.y+=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxN
                                     
                for i in range(len(monster.monsters)):
                    if self.x==monster.monsters[i].x and self.y==monster.monsters[i].y:
                        projectile.MonsterDamage(self,i)
                        break
                if map[self.x][self.y] not in noGo:
                    self.tickTotal=self.type.range+1   
                
        if self.direction == "E" or self.direction == "ENE" or self.direction == "ESE":
            if self.type.speed == self.tick:
                self.tickTotal+=1 
                self.didMove=True  
                if self.tickTotal>1 and self.type.pattern!="V":map[self.x][self.y]=self.storeMapGfx
                elif self.type.pattern=="V": Bullets.append(projectile(self.x,self.y,self.type,"None",1,self.name,0,self.storeMapGfx)) 
                self.tick = 0
                if self.x==playerposx and self.y+1==playerposy and self.direction=="E" or self.x-1==playerposx and self.y+1==playerposy and self.direction=="ENE" or self.x+1==playerposx and self.y+1==playerposy and self.direction=="ESE":
                    projectile.PlayerDamage(self) 
                elif self.direction == "E":
                    self.y = self.y + 1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxE
                elif self.direction == "ENE":
                    self.y = self.y + 1
                    self.x-=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxE
                elif self.direction == "ESE":
                    self.y = self.y + 1
                    self.x+=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxE

                for i in range(len(monster.monsters)):
                    if self.x==monster.monsters[i].x and self.y==monster.monsters[i].y:
                        projectile.MonsterDamage(self,i)
                        break
                if map[self.x][self.y] not in noGo:
                    self.tickTotal=self.type.range+1   
                    
        if self.direction == "S" or self.direction == "SE" or self.direction == "SW":     
            if self.type.speed == self.tick:
                self.tickTotal+=1
                self.didMove=True  
                if self.tickTotal>1 and self.type.pattern!="V":map[self.x][self.y]=self.storeMapGfx
                elif self.type.pattern=="V": Bullets.append(projectile(self.x,self.y,self.type,"None",1,self.name,0,self.storeMapGfx)) 
                self.tick = 0
                if self.x+1==playerposx and self.y==playerposy and self.direction=="S" or self.x+1==playerposx and self.y+1==playerposy and self.direction=="SE" or self.x+1==playerposx and self.y-1==playerposy and self.direction=="SW":
                    projectile.PlayerDamage(self)  
                elif self.direction == "S":
                    self.x = self.x + 1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxS
                elif self.direction == "SE":
                    self.x = self.x + 1
                    self.y+=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxS
                elif self.direction == "SW":
                    self.x = self.x + 1
                    self.y-=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxS

                for i in range(len(monster.monsters)):
                    if self.x==monster.monsters[i].x and self.y==monster.monsters[i].y:
                        projectile.MonsterDamage(self,i)
                        break
                if map[self.x][self.y] not in noGo:
                    self.tickTotal=self.type.range+1   
                
        if self.direction == "W" or self.direction == "WNW" or self.direction == "WSW":    
            if self.type.speed == self.tick:
                self.tickTotal+=1 
                self.didMove=True                 
                if self.tickTotal>1 and self.type.pattern!="V":map[self.x][self.y]=self.storeMapGfx
                elif self.type.pattern=="V": Bullets.append(projectile(self.x,self.y,self.type,"None",1,self.name,0,self.storeMapGfx))
                self.tick = 0
                if self.x==playerposx and self.y-1==playerposy and self.direction=="W" or self.x+1==playerposx and self.y-1==playerposy and self.direction=="WNW" or self.x-1==playerposx and self.y-1==playerposy and self.direction=="WSW":
                    projectile.PlayerDamage(self) 
                elif self.direction == "W":
                    self.y =self.y - 1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxW
                elif self.direction == "WNW":
                    self.y =self.y - 1
                    self.x+=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxW
                elif self.direction == "WSW":
                    self.y =self.y - 1
                    self.x-=1
                    if map[self.x][self.y]=="  " or map[self.x][self.y]==". ":
                        self.storeMapGfx=map[self.x][self.y]
                        map[self.x][self.y] = self.type.gfxW

                for i in range(len(monster.monsters)):
                    if self.x==monster.monsters[i].x and self.y==monster.monsters[i].y:
                        projectile.MonsterDamage(self,i)
                        break
                if map[self.x][self.y] not in noGo:
                    self.tickTotal=self.type.range+1   

        if self.type.pattern =="*|*" and self.tickTotal>0:
            if self.tick==1:
                if map[self.x-1][self.y]==". " or map[self.x-1][self.y]=="  ":                    
                    Bullets.append(projectile(self.x-1,self.y,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x-1][self.y]))
                else:projectile.SpinDamage(self,self.x-1,self.y)
            if self.tick==2:
                if map[self.x+1][self.y]==". " or map[self.x+1][self.y]=="  ":
                    Bullets.append(projectile(self.x+1,self.y,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x+1][self.y])) 
                else:projectile.SpinDamage(self,self.x+1,self.y)
            if self.tick==3:
                if map[self.x-1][self.y+1]==". " or map[self.x-1][self.y+1]=="  ":
                    Bullets.append(projectile(self.x-1,self.y+1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x-1][self.y+1]))
                else:projectile.SpinDamage(self,self.x-1,self.y+1)
            if self.tick==4:
                if map[self.x+1][self.y-1]==". " or map[self.x+1][self.y-1]=="  ":
                    Bullets.append(projectile(self.x+1,self.y-1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x+1][self.y-1])) 
                else:projectile.SpinDamage(self,self.x+1,self.y-1) 
            if self.tick==5:
                if map[self.x][self.y+1]==". " or map[self.x][self.y+1]=="  ":
                    Bullets.append(projectile(self.x,self.y+1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x][self.y+1])) 
                else:projectile.SpinDamage(self,self.x,self.y+1) 
            if self.tick==6:                   
                if map[self.x][self.y-1]==". " or map[self.x][self.y-1]=="  ":
                    Bullets.append(projectile(self.x,self.y-1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x][self.y-1])) 
                else:projectile.SpinDamage(self,self.x,self.y-1)
            if self.tick==7:
                if map[self.x+1][self.y+1]==". " or map[self.x+1][self.y+1]=="  ":
                    Bullets.append(projectile(self.x+1,self.y+1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x+1][self.y+1])) 
                else:projectile.SpinDamage(self,self.x+1,self.y+1)
            if self.tick==8:
                if map[self.x-1][self.y-1]==". " or map[self.x-1][self.y-1]=="  ":
                    Bullets.append(projectile(self.x-1,self.y-1,item("Ice Twister SpellGFX"),"None",1,self.name,0,map[self.x-1][self.y-1])) 
                else:projectile.SpinDamage(self,self.x-1,self.y-1)
        
        if self.type.pattern =="O" and self.tickTotal>0:
            if self.direction=="N" and map[self.x+1][self.y]==". " or self.direction=="N" and map[self.x+1][self.y]=="  ":
                Bullets.append(projectile(self.x+1,self.y,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x+1][self.y]))                
            if self.direction=="E" and map[self.x][self.y-1]==". " or self.direction=="E" and map[self.x][self.y-1]=="  ":
                Bullets.append(projectile(self.x,self.y-1,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x][self.y-1]))                 
            if self.direction=="S" and map[self.x-1][self.y]==". " or self.direction=="S" and map[self.x-1][self.y]=="  ":
                Bullets.append(projectile(self.x-1,self.y,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x-1][self.y]))                 
            if self.direction=="W" and map[self.x][self.y+1]==". " or self.direction=="W" and map[self.x][self.y+1]=="  ": 
                Bullets.append(projectile(self.x,self.y+1,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x][self.y+1]))                 
        
        return False
    def PlayerDamage(self):
        r=Dice(self.type.damage)
        d=r-p1.armor.absorb
        if p1.armor.absorb>r:
            r=p1.armor.absorb-(p1.armor.absorb-r)
        else: r=p1.armor.absorb
        if d<0:
           d=0                
        TextUpdate(self.name+" did "+str(d)+" damage to "+p1.name+" "+str(r)+" damage was absorbed by "+p1.armor.name)        
        p1.hp=p1.hp-d
        if self.type.pattern!="V": self.tickTotal=self.type.range        
    def MonsterDamage(self, whichMonster):
            global yourTarget
            r=Dice(self.type.damage)
            d=r-monster.monsters[whichMonster].absorb
            if monster.monsters[whichMonster].absorb>r:
                r=monster.monsters[whichMonster].absorb-(monster.monsters[whichMonster].absorb-r)
            else: r=monster.monsters[whichMonster].absorb
            if d<0:
                d=0
            if self.name==p1.name:
                yourTarget=whichMonster                
            TextUpdate(self.name+" did "+str(d)+" damage to "+monster.monsters[whichMonster].name+" "+str(r)+" damage was absorbed by armor")
            monster.monsters[whichMonster].hp=monster.monsters[whichMonster].hp-d  
            if monster.monsters[whichMonster].hp<1 and self.name==p1.name:                       
                TextUpdate(monster.monsters[whichMonster].name+" died! You got "+str(monster.monsters[whichMonster].gold)+" gold and "+str(monster.monsters[whichMonster].xp)+" experience")
                p1.gold=p1.gold+monster.monsters[whichMonster].gold
                p1.xp=p1.xp+monster.monsters[whichMonster].xp
                map[monster.monsters[whichMonster].x][monster.monsters[whichMonster].y]=monster.monsters[whichMonster].previousGFX                
                del monster.monsters[whichMonster] 
                if self.name==p1.name:
                      yourTarget=-1
            elif monster.monsters[whichMonster].hp<1 and self.name!=p1.name:                       
                TextUpdate(monster.monsters[whichMonster].name+" died! "+self.name+" killed it!")
                map[monster.monsters[whichMonster].x][monster.monsters[whichMonster].y]=monster.monsters[whichMonster].previousGFX                
                del monster.monsters[whichMonster] 
            if self.type.pattern!="V": self.tickTotal=self.type.range   
    def SpinDamage(self,a,b):
        global yourTarget
        for i in range(len(monster.monsters)):
            if a==monster.monsters[i].x and b==monster.monsters[i].y:                
                r=Dice(self.type.damage)
                d=r-monster.monsters[i].absorb
                if monster.monsters[i].absorb>r:
                    r=monster.monsters[i].absorb-(monster.monsters[i].absorb-r)
                else: r=monster.monsters[i].absorb
                if d<0:
                    d=0                
                TextUpdate(self.name+" did "+str(d)+" damage to "+monster.monsters[i].name+" "+str(r)+" damage was absorbed by armor")
                monster.monsters[i].hp=monster.monsters[i].hp-d
                yourTarget=i  
                if monster.monsters[i].hp<1:                       
                    TextUpdate(monster.monsters[i].name+" died! You got "+str(monster.monsters[i].gold)+" gold and "+str(monster.monsters[i].xp)+" experience")
                    p1.gold=p1.gold+monster.monsters[i].gold
                    p1.xp=p1.xp+monster.monsters[i].xp
                    map[monster.monsters[i].x][monster.monsters[i].y]=monster.monsters[i].previousGFX              
                    del monster.monsters[i] 
                    yourTarget=-1
                    break
    def Boom(self):
         Bullets.append(projectile(self.x,self.y,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x][self.y]))
         Bullets.append(projectile(self.x+1,self.y,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x+1][self.y]))
         Bullets.append(projectile(self.x,self.y-1,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x][self.y-1]))
         Bullets.append(projectile(self.x-1,self.y,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x-1][self.y]))
         Bullets.append(projectile(self.x,self.y+1,item("Meteor SpellGFX"),"None",1,self.name,0,map[self.x][self.y+1])) 
##copy data from world map to display grid
def MapToGrid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==20 and j==59 and p1.klass=="Knight":grid[i][j]="\U0001F468"
            elif i==20 and j==59 and p1.klass=="Hunter":grid[i][j]="\U0001F9DB"
            elif i==20 and j==59 and p1.klass=="Mage":grid[i][j]="\U0001F9D9"            
            else: grid[i][j]=map[x+i][y+j]
        
#Create the overworld map with treeline
map = [[" " for x in range(1200)] for y in range(400)]
for i in range(len(map)):
    for j in range(len(map[0])):
        if i<40 :map[i][j] ="\U0001F332"        
        elif i>360:map[i][j]="\U0001F332"        
        elif j<40:map[i][j]="\U0001F332"        
        elif j>1159:map[i][j]="\U0001F332"
        else: map[i][j]="  "
# randomize location and place objects on world map
def RandomizeOnMap(start, end, amount):
    length=0               
    for i in range(start, end+1):
        if len(GFX[i])%2==1:GFX[i]=GFX[i]+" "
        if len(GFX[i])>length:length=len(GFX[i])    
    while(amount>0):
        go=False
        empty=True
        start2=start-1
        starti=random.randint(38, 360-(end-start))           
        startj=random.randint(50, 1159-length)  
        if map[starti][startj]=="  ":
            for i in range(starti,starti+(end-start)+1): 
                if empty==False:break            
                for j in range(startj,startj+int(length/2)+1):  
                    if map[i][j]!="  ":empty=False
                    if i==starti+(end-start) and j==startj+int(length/2) and empty==True:go=True
        if go==True:
            for i in range(starti,starti+(end-start)+1):
                k=0
                start2+=1
                for j in range(startj,startj+int(len(GFX[start2])/2)):                                
                    map[i][j]=GFX[start2][k]
                    map[i][j]=map[i][j]+GFX[start2][k+1]
                    k=k+2
                    if i==starti+(end-start) and j==startj+int(len(GFX[start2])/2)-1:
                        amount-=1
                        go=False
#randomize and place specifed amount and chars in a spot that is empty in all adjacent squares
def RandomizeOnMapSpecified(specified, amount):                
    while(amount>0):
        go=False
        empty=True        
        starti=random.randint(40, 358)           
        startj=random.randint(50, 1159)  
        if map[starti][startj]=="  ":
            for i in range(starti-1,starti+2): 
                if empty==False:break            
                for j in range(startj-1,startj+2):   
                    if map[i][j]!="  ":empty=False
                    if i==starti+1 and j==startj+1 and empty==True:go=True
        if go==True:
            map[starti][startj]=specified
            amount-=1
#Castles
RandomizeOnMap(13,34,10)
#Shops
RandomizeOnMap(37,45,300)
#Trees
RandomizeOnMapSpecified("\U0001F332",250)
RandomizeOnMapSpecified(". ",1250)
#Damage rolls
def Dice(dice):
    if (dice=="1d3"):return random.randint(1, 3)
    elif (dice=="1d4"):return random.randint(1, 4)
    elif (dice=="1d6"):return random.randint(1, 6)
    elif (dice=="1d8"):return random.randint(1, 8)
    elif (dice=="1d10"):return random.randint(1, 10)
    elif (dice=="1d12"):return random.randint(1, 12)
    elif (dice=="1d20"):return random.randint(1, 20)
    elif (dice=="2d3"):return random.randint(1, 3)+random.randint(1, 3)
    elif (dice=="2d4"):return random.randint(1, 4)+random.randint(1, 4)
    elif (dice=="2d6"):return random.randint(1, 6)+random.randint(1, 6)
    elif (dice=="2d8"):return random.randint(1, 8)+random.randint(1, 8)
    elif (dice=="2d10"):return random.randint(1, 10)+random.randint(1, 10)
    elif (dice=="2d12"):return random.randint(1, 12)+random.randint(1, 12)
    elif (dice=="2d20"):return random.randint(1, 20)+random.randint(1, 20)

##Method to update combat text window
def TextUpdate(new):    
    text.append(new)
    if len(text)>42:del text[0]
#melee combat GFX
def MeleeGFX(a):
    i=0 
    stdscr.refresh()
    stdscr.clear()
    upper=BannerUpper()
    lower=BannerLower() 
    stdscr.addstr(upper+"\n") 
    for row in monster.monsters[a].meleeGFX:
        try:        
            stdscr.addstr("".join(row) +" "+ str(text[i])+ "\n")
            i+=1             
        except curses.error:
            pass  
    try: 
        stdscr.addstr("x "+str(playerposx)+" y "+str(playerposy)+" monsters "+str(len(monster.monsters))+" hp "+str(p1.hp)+" gold "+str(p1.gold)+" level "+str(p1.level)+"\n") 
        stdscr.addstr(lower)
    except curses.error:
        pass            
#melee combat logic
def MeleeCombat(a):  
    global yourTarget 
    yourTarget=a
    while(True):             
        MeleeGFX(a)
        #player turn
        for i in range(p1.weapon.attacks*p1.attacks):
            r=Dice(p1.weapon.damage) 
            d=r-monster.monsters[a].absorb
            if monster.monsters[a].absorb>r:
                r=monster.monsters[a].absorb-(monster.monsters[a].absorb-r)
            else: r=monster.monsters[a].absorb
            if d<0:
                d=0                
            TextUpdate(p1.name+" did "+str(d)+" damage to "+monster.monsters[a].name+" "+str(r)+" damage was absorbed by armor")
            monster.monsters[a].hp=monster.monsters[a].hp-d  
            MeleeGFX(a)
            time.sleep(0.2)
        if monster.monsters[a].hp<1:                       
            TextUpdate(monster.monsters[a].name+" died! You got "+str(monster.monsters[a].gold)+" gold and "+str(monster.monsters[a].xp)+" experience")
            yourTarget=-1
            p1.gold=p1.gold+monster.monsters[a].gold
            p1.xp=p1.xp+monster.monsters[a].xp
            MeleeGFX(a)
            map[monster.monsters[a].x][monster.monsters[a].y]=monster.monsters[a].previousGFX 
            del monster.monsters[a]                        
            time.sleep(2) 
            break          
        #monster turn
        r=Dice(monster.monsters[a].damage)
        d=r-p1.armor.absorb
        if p1.armor.absorb>r:
            r=p1.armor.absorb-(p1.armor.absorb-r)
        else: r=p1.armor.absorb
        if d<0:
           d=0                
        TextUpdate(monster.monsters[a].name+" did "+str(d)+" damage to "+p1.name+" "+str(r)+" damage was absorbed by "+p1.armor.name)        
        p1.hp=p1.hp-d
        Death()
        MeleeGFX(a) 
        time.sleep(1)
#Check for meleecombat from player moves              
def PlayerMeeleCombat(a,b):
        for i in range(len(monster.monsters)):        
            if monster.monsters[i].x==playerposx+a and monster.monsters[i].y==playerposy+b:            
                MeleeCombat(i)
                break
##Check if coordinate is store
def IsStore(a,b):
    if grid[20+a][59+b]=="$$":
        if p1.klass=="Knight":curses.wrapper(StoreKnight)
        if p1.klass=="Hunter":curses.wrapper(StoreHunter)
        if p1.klass=="Mage":curses.wrapper(StoreMage)
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.nodelay(True) 
def RandomSpawn():
    rng=random.randint(0,1000)
    if rng<100:rngMonster="Bat"
    elif rng<950:rngMonster="Elf"
    else:rngMonster="Dragon"
    amount=1
    if len(monster.monsters)<10:
            while(amount>0):
                go=False
                empty=True        
                starti=random.randint(playerposx-80, playerposx+80)           
                startj=random.randint(playerposy-80, playerposy+80)  
                if map[starti][startj]=="  ":
                    for i in range(starti-1,starti+2): 
                        if empty==False:break            
                        for j in range(startj-1,startj+2):   
                            if map[i][j]!="  ":empty=False
                            if i==starti+1 and j==startj+1 and empty==True:go=True
                if go==True:
                    monster.monsters.append(monster(rngMonster,starti,startj))
                    amount-=1
# Level up check and formula
def LevelUp():
    if p1.xp>p1.levelUp:  
        p1.levelUp=p1.levelUp+500      
        if p1.klass=="Knight":                            
            p1.maxHP=p1.maxHP+20
            p1.regen=p1.regen+1
            p1.level=p1.level+1
            if p1.level%3==0:
                TextUpdate("You gained a level!! +20 hp, +1 regen and +1 attack")
                p1.attacks=p1.attacks+1
            else: TextUpdate("You gained a level!! +20 hp and +1 regen")
        if p1.klass=="Hunter":    
            TextUpdate("You gained a level!! +15 hp and +1 regen")            
            p1.maxHP=p1.maxHP+15
            p1.regen=p1.regen+1
            p1.level=p1.level+1
            if p1.level%4==0:
                TextUpdate("You gained a level!! +15 hp, +1 regen and +1 attack")
                p1.attacks=p1.attacks+1
            else: TextUpdate("You gained a level!! +15 hp and +1 regen")
        if p1.klass=="Mage":    
            TextUpdate("You gained a level!! +10 hp and +1 regen")            
            p1.maxHP=p1.maxHP+10
            p1.regen=p1.regen+1
            p1.level=p1.level+1
            if p1.level%5==0:
                TextUpdate("You gained a level!! +10 hp, +1 regen and +1 attack")
                p1.attacks=p1.attacks+1
            else: TextUpdate("You gained a level!! +10 hp and +1 regen")
#updates hp och enemy and self
def BannerUpper():       
    texter="Enemy HP:"+str(yourTarget)
    if yourTarget>-1:
        texter=monster.monsters[yourTarget].name+" HP:"
        for i in range(int(monster.monsters[yourTarget].hp/monster.monsters[yourTarget].maxhp*200)):
            texter=texter+"I"
    return texter
def BannerLower():
    texter="Your HP:"
    for i in range(int(p1.hp/p1.maxHP*200)):
        texter=texter+"I"
    return texter
def Death():
    if p1.hp<1:
        TextUpdate("You died!")
        monster.monsters.append(monster("Death",x,y)) 
        while(True):                           
            MeleeGFX(len(monster.monsters)-1)            
text = [" "]*42
# Create a grid of characters to represent the screen
grid = [[" " for x in range(119)] for y in range(42)]
x = 25
y = -10
playerposx=x+20
playerposy=y+59
start_time=0
counter=0
CanMove=True
CanFire=True
Bullets=[]
Direction="S"
BulletDelete=[]
p1="zxzxae"
regenCounter=0
upper=""
lower=""
while(p1=="zxzxae"):      
    print("Welcome to this awesome RPG, please make sure to maximise your window to not cause crashes 1440p or higher resolution is required")
    print("Use arrow keys to navigate, space to shoot and enter to buy and equip stuff. Melee combat is automatic so just relax while in melee")
    print("Walk onto $$ squares to enter the shop")
    print("Please select your class:")
    print("1 for Knight(strong melee, weak ranged):")
    print("2 for Hunter (Balanced melee and ranged)")      
    print("3 for Mage (weak melee strong ranged)")
    tst=input()
    if(tst=="1"):tst="Knight"
    elif(tst=="2"):tst="Hunter"
    elif(tst=="3"):tst="Mage"
    else:
        print("Incorrect selection, try again:")
    if tst=="Hunter" or tst=="Knight" or tst=="Mage":
        print("Please type in the name of your hero:")
        name=input()
        p1=player(name,tst)    
# Initialize the screen
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
#monster.monsters.append(monster("Dragon",60,60)) 
while True:  
    counter+=1 
    regenCounter+=1   
    stdscr.clear()  
    #Move monsters and engage combat if on same x y coords as player
    for i in range(len(monster.monsters)):
        result=monster.monsters[i].Move()
        if result==True:            
            MeleeCombat(i)
            break   
    #Fire bullets from monsters
    for i in range(len(monster.monsters)):
        monster.monsters[i].Fire()
    ##delete bullets on list
    for i in range(len(BulletDelete) - 1, -1, -1):        
        del Bullets[BulletDelete[i]]
        del BulletDelete[i]
    MapToGrid() 
    ##Move bullets and add to delete list if due for deletion
    for i in range(len(Bullets)):
        result=Bullets[i].Move()
        if result==True:
            BulletDelete.append(i)
    ##Paint displayed grid
    i=0
    upper=BannerUpper()
    lower=BannerLower() 
    stdscr.addstr(upper+"\n")
    for row in grid:
        try:        
            stdscr.addstr("".join(row) +" "+ str(text[i])+ "\n")
            i+=1  
        except curses.error:
            pass  
    try: 
        stdscr.addstr("x "+str(playerposx)+" y "+str(playerposy)+" monsters "+str(len(monster.monsters))+" hp "+str(p1.hp)+" gold "+str(p1.gold)+" level "+str(p1.level)+"\n") 
        stdscr.addstr(lower)
    except curses.error:
        pass  
    key = stdscr.getch() 
    # Check for arrow keys
    if key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
        # Check elapsed time
        elapsed_time = time.time() - start_time
        if elapsed_time > 0.1:
            # Update start time
            start_time = time.time()
            # Process key press            
            if key == curses.KEY_UP:
                PlayerMeeleCombat(-1,0)
                IsStore(-1,0)               
                if grid[19][59]==". " or grid[19][59]=="  ":          
                    x =  x - 1   
                    playerposx-=1        
                Direction='N'
                CanMove=False
            elif key == curses.KEY_DOWN:
                PlayerMeeleCombat(+1,0) 
                IsStore(+1,0)  
                if grid[21][59]==". " or grid[21][59]=="  ":           
                    x =  x + 1  
                    playerposx+=1         
                Direction='S'
                CanMove=False
            elif key == curses.KEY_LEFT:
                PlayerMeeleCombat(0,-1)
                IsStore(0,-1) 
                if grid[20][58]==". " or grid[20][58]=="  ":           
                    y =  y - 1
                    playerposy-=1           
                Direction='W'
                CanMove=False
            elif key == curses.KEY_RIGHT:
                PlayerMeeleCombat(0,+1)
                IsStore(0,+1) 
                if grid[20][60]==". " or grid[20][60]=="  ":            
                    y =  y + 1
                    playerposy+=1          
                Direction='E'              
    for i in range(len(monster.monsters)):        
        if monster.monsters[i].x==playerposx and monster.monsters[i].y==playerposy:            
            MeleeCombat(i)
            break 
    if key ==ord('i'):
        curses.wrapper(Inventory)
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.nodelay(True) 
    if CanFire==True and key ==ord(' '):
        CanFire=False        
        if Direction=="N":Bullets.append(projectile(x+20,y+59,p1.rangedWeapon,Direction,0,p1.name))   
        if Direction=="E":Bullets.append(projectile(x+20,y+59,p1.rangedWeapon,Direction,0,p1.name)) 
        if Direction=="S":Bullets.append(projectile(x+20,y+59,p1.rangedWeapon,Direction,0,p1.name)) 
        if Direction=="W":Bullets.append(projectile(x+20,y+59,p1.rangedWeapon,Direction,0,p1.name)) 
    time.sleep(0.005) 
    Death()   
    if counter==50:        
        CanFire=True
        counter=0
        LevelUp()
    if regenCounter==400:
        RandomSpawn()
        regenCounter=0
        if p1.hp<p1.maxHP:
            p1.hp=p1.hp+p1.regen
            TextUpdate("You regenerate "+str(p1.regen)+" hp")
        if p1.hp>p1.maxHP:p1.hp=p1.maxHP

        

