import curses
import time
import random
class monster:
    def __init__(self, name):
        self.name=name
        if(name=="bat"):
            self.hp=20
            self.damage="1d4"
            self.weapon="bites"
class item:
    def __init__(self, name):
        self.name=name
        if name=="Short Bow":
            self.gfxN="\U00002191"     
            self.gfxE="\U00002192" 
            self.gfxS="\U00002193"
            self.gfxW="\U00002190"
            self.speed=2
            self.range=120
            self.damage="1d6"
            self.pattern="|"
        if name=="Rusty Throwing Dagger":
            self.gfxN="*"     
            self.gfxE="*" 
            self.gfxS="*"
            self.gfxW="*"
            self.speed=3
            self.range=5
            self.damage="1d4"
            self.pattern="W"
        if name=="Iceball Spell":
            self.gfxN="\U00002744"     
            self.gfxE="\U00002744"    
            self.gfxS="\U00002744"   
            self.gfxW="\U00002744"   
            self.speed=8
            self.range=30
            self.damage="1d10"
            self.pattern="|"
        if name=="Rusty Two Handed Sword":
            self.damage="1d8"
            self.attacks=1
        if name=="Rusty Daggers":
            self.damage="1d3"
            self.attacks=2
            self.penetration=1
        if name=="Broken Quarterstaff":
            self.damage="1d4"
            self.attacks=1


class player:
    def __init__(self,name,klass):
        self.name=name
        self.klass=klass
        self.gold=0
        self.inventory=[]
        self.level=1
        self.xp=0
        if klass=="Knight":
            self.hp=60
            self.weapon=item("Rusty Two Handed Sword")
            self.rangedWeapon=item("Rusty Throwing Dagger")
            self.armor=item("Leather Armor")            
        if klass=="Hunter":
            self.hp=50
            self.weapon=item("Rusty Daggers")
            self.rangedWeapon=item("Short Bow")
            self.armor=item("Leather Armor")   
        if klass=="Mage":
            self.hp=40
            self.weapon=item("Quarterstaff")
            self.rangedWeapon=item("Iceball Spell")
            self.armor=item("Novice Robe")

class projectile:        
    def __init__(self, x,y,type, direction, tick):
        self.x=x
        self.y=y
        self.type=type
        self.direction=direction
        self.tick=tick
        self.tickTotal=0
        self.storeMapGfx=" "
    def move(self):
        self.tick += 1        
        if self.tickTotal==p1.rangedWeapon.range:
            map[self.x][self.y]=self.storeMapGfx
            return True
        
        if self.tickTotal==0 and self.tick==1 and p1.rangedWeapon.pattern =="W":
            if self.direction=="N":
                Bullets.append(projectile(self.x,self.y,p1.rangedWeapon,"NW",0))
                Bullets.append(projectile(self.x,self.y,p1.rangedWeapon,"NE",0))
            if self.direction=="E":
                Bullets.append(projectile(self.x,self.y,p1.rangedWeapon,"ENE",0))
                Bullets.append(projectile(self.x,self.y,p1.rangedWeapon,"ESE",0))

        if self.direction == "N" or self.direction=="NW" or self.direction=="NE":    
            if p1.rangedWeapon.speed == self.tick: 
                self.tickTotal+=1                
                if self.tickTotal>1:map[self.x][self.y]=self.storeMapGfx                
                self.tick = 0
                if(map[self.x-1][self.y]=="." and self.direction=="N" or map[self.x-1][self.y]==" " and self.direction=="N"):
                    self.x = self.x - 1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxN
                elif map[self.x-1][self.y-1]=="." and self.direction=="NW" or map[self.x-1][self.y-1]==" " and self.direction=="NW":
                    self.x = self.x - 1
                    self.y-=1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxN
                elif map[self.x-1][self.y+1]=="." and self.direction=="NE" or map[self.x-1][self.y+1]==" " and self.direction=="NE":
                    self.x = self.x - 1
                    self.y+=1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxN
                
        if self.direction == "E" or self.direction == "ENE" or self.direction == "ESE":
            if p1.rangedWeapon.speed == self.tick:
                self.tickTotal+=1 
                if self.tickTotal>1:map[self.x][self.y]=self.storeMapGfx   
                self.tick = 0
                if(map[self.x][self.y+1]==". " and self.direction == "E" or map[self.x][self.y+1]=="  " and self.direction == "E"):
                    self.y = self.y + 1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxE
                elif(map[self.x-1][self.y+1]==". " and self.direction == "ENE" or map[self.x-1][self.y+1]=="  " and self.direction == "ENE"):
                    self.y = self.y + 1
                    self.x-=1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxE
                elif(map[self.x+1][self.y+1]==". " and self.direction == "ESE" or map[self.x+1][self.y+1]=="  " and self.direction == "ESE"):
                    self.y = self.y + 1
                    self.x+=1
                    self.storeMapGfx=map[self.x][self.y]
                    map[self.x][self.y] = p1.rangedWeapon.gfxE
                
        if self.direction == "S":     
            if p1.rangedWeapon.speed == self.tick:
                self.tickTotal+=1
                map[self.x][self.y]=self.storeMapGfx 
                self.tick = 0
            if(map[self.x+1][self.y]=="." or map[self.x][self.y]==" "):
                self.x = self.x + 1
                self.storeMapGfx=map[self.x][self.y]
                map[self.x][self.y] = p1.rangedWeapon.gfxS
                
        if self.direction == "W":    
            if p1.rangedWeapon.speed == self.tick:
                self.tickTotal+=1
                map[self.x][self.y]=self.storeMapGfx
                self.tick = 0
            if(map[self.x][self.y-1]=="." or map[self.x][self.y]==" "):
                self.y =self.y - 1
                self.storeMapGfx=map[self.x][self.y]
                map[self.x][self.y] = p1.rangedWeapon.gfxW
        return False
                
##copy data from world map to display grid
def MapToGrid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==20 and j==59 and p1.klass=="Knight":grid[i][j]="\U0001F468"
            elif i==20 and j==59 and p1.klass=="Hunter":grid[i][j]="\U0001F9DB"
            elif i==20 and j==59 and p1.klass=="Mage":grid[i][j]="\U0001F9D9"
            elif i==20 and j==60:grid[i][j]=""
            else: grid[i][j]=map[x+i][y+j]
        
#Create the overworld map
map = [[" " for x in range(1200)] for y in range(400)]
for i in range(len(map)):
    for j in range(len(map[0])):
        if i<60 and j%2==0 :map[i][j] ="\U0001F332"
        elif i<60 and j%2==1 : map[i][j]=""
        elif i>340 and j%2==0:map[i][j]="\U0001F332"
        elif i>340 and j%2==1: map[i][j]=""
        elif j<60 and j%2==0:map[i][j]="\U0001F332"
        elif j<60 and j%2==1: map[i][j]=""
        elif j>1140 and j%2==0:map[i][j]="\U0001F332"
        elif j>1140 and j%2==1: map[i][j]=""
        elif j%10==0:map[i][j]=". "
        else: map[i][j]="  "

# Create a grid of characters to represent the screen
grid = [[" " for x in range(119)] for y in range(42)]
x = 50
y = 60
start_time=0
counter=0
CanMove=True
CanFire=True
Bullets=[]
Bullets.append(projectile(555,555,"Q",-1,0))
Direction="S"
BulletDelete=[]
p1="zxzxae"
while(p1=="zxzxae"):
    print("Welcome to this awesome RPG, please make sure to maximise your window to not cause crashes")
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
while True:  
    counter+=1    
    stdscr.clear()
    MapToGrid()
    ##Move bullets and add to list if out of bounds
    for i in range(len(Bullets)):
        result=Bullets[i].move()
        if (result==True):
            BulletDelete.append(i)
    ##delete bullets on list
    for i in range(len(BulletDelete) - 1, -1, -1):        
        del Bullets[BulletDelete[i]]
        del BulletDelete[i] 
    ##Paint displayed grid
    for row in grid:
        try:        
            stdscr.addstr("".join(row) + "\n")
        except curses.error:
            pass  
    try: 
        stdscr.addstr("x "+str(x)+" y "+str(y)) 
    except curses.error:
        pass  
    key = stdscr.getch()
    elapsed_time = time.time() - start_time

    if CanMove==True:
        if key == curses.KEY_UP:  
            if grid[19][59]=="." or grid[19][59]==" ":          
                x =  x - 1           
            Direction='N'
            if elapsed_time>0.5:
                start_time = time.time()
                CanMove=False
        elif key == curses.KEY_DOWN:  
            if grid[21][59]=="." or grid[21][59]==" ":           
                x =  x + 1           
            Direction='S'
            if elapsed_time>0.5:
                start_time = time.time()
                CanMove=False
        elif key == curses.KEY_LEFT:
            if grid[20][58]=="." or grid[20][58]==" ":           
                y =  y - 1           
            Direction='W'
            if elapsed_time>0.5:
                start_time = time.time()
                CanMove=False
        elif key == curses.KEY_RIGHT:
            if grid[20][61]=="." or grid[20][61]==" ":            
                y =  y + 1            
            Direction='E'
            if elapsed_time>0.5:
                start_time = time.time()
                CanMove=False
    if CanFire==True and key ==ord(' '):
        CanFire=False        
        if Direction=="N":Bullets.append(projectile(x+20,y+60,p1.rangedWeapon,Direction,0))   
        if Direction=="E":Bullets.append(projectile(x+20,y+60,p1.rangedWeapon,Direction,0)) 
        if Direction=="S":Bullets.append(projectile(x+20,y+60,p1.rangedWeapon,Direction,0)) 
        if Direction=="W":Bullets.append(projectile(x+20,y+60,p1.rangedWeapon,Direction,0)) 
    time.sleep(0.005)
    if counter==10:
        CanMove=True
        CanFire=True
        counter=0
        

