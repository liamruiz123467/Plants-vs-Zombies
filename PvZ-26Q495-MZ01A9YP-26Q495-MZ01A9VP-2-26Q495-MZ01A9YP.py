from gamelib import *

game = Game(1024,626,"Plants Vs Zombies")
Level1 = Image("./images/L!.WEBP",game)
Level1.resizeTo(game.width, game.height)
Level1.draw()

def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,600)
        y = 300
        objects[i].moveTo(x,-y)
        s = randint(3,6)
        objects[i].setSpeed(s, 180)
        objects[i].Visible=True

def positionObjectsZ( objects ):
    for i in range(len(objects)):
        x = game.width + randint(200,4000)
        y = randint(100,500)
        objects[i].setSpeed(0.5,90)
        objects[i].moveTo(x,y)
game.setMusic("sounds/Intro.mp3")

PIcon=Image("images/PIcon.png",game)
PIcon.moveTo(35,40)

progressbar =Shape("bar", game, 100, 30, red)

lose=Sound("sounds/losemusic.ogg",0)
win=Sound("sounds/winmusic.ogg",1)
collect=Sound("sounds/points.ogg",2)
plant=Sound("sounds/plant.ogg",3)
bite=Sound("sounds/ZombieBite.ogg",4)
arrival=Sound("sounds/ZombiesComing.ogg",5)
splat=Sound("sounds/splat.ogg",6)



introduction = Image("./images/introduction.png",game)
adventureon=Image("./images/adventureon.png",game)
adventure=Image("./images/adventure.png",game)
survivalon=Image("./images/survivalon.png",game)
survival=Image("./images/survival.png",game)
sunicon=Image("./images/SunIcon.png",game)
nuticon=Image("./images/NutIcon.png",game)

surrender=Image("./images/Surrender.webp",game)
surrender.resizeBy(250)

lost=Image("./images/Youlose.png",game)
lost.resizeBy(-10)
conehead = []
for i in range(25):
    coneheadwalk=Animation("./images/coneheadwalk.png",90,game, 865 / 5, 4554 / 18,1)
    coneheadwalk.resizeBy(-35)
    conehead.append(coneheadwalk)
positionObjectsZ(conehead)
coneheadwalk=Animation("./images/coneheadwalk.png",90,game, 865 / 5, 4554 / 18,1)
coneheadeat=Animation("./images/coneheadeat.png",259,game, 1490 / 10, 6448 / 26,1)
coneheadeat.resizeBy(-35)
coneheaddeath=Animation("./images/coneheaddeath.png",55,game, 1015 / 5, 1980 / 11,1)
coneheaddeath.resizeBy(-35)
    
zombie = []

for i in range(50):
    zombiewalk=Animation("./images/zombiewalk.png",90,game, 820 / 5, 3654 / 18,1)
    zombiewalk.collisionBorder = "ci"
    zombiewalk.resizeBy(-35)
    zombie.append(zombiewalk)
positionObjectsZ(zombie)
print(zombie)
zombiewalk=Animation("./images/zombiewalk.png",90,game, 820 / 5, 3654 / 18,1)
zombiewalk.resizeBy(-35)
zombieeat=Animation("./images/zombieeat.png",259,game, 725 / 5, 10660 / 52,1)
zombieeat.resizeBy(-35)
zombiedeath=Animation("./images/zombiedeath.png",55,game,1040 / 5, 1870 / 11,2)  
zombiedeath.resizeBy(-35)
zombiedeath.setSpeed(0,90)

Peaball = []
pball=Animation("./images/PeaBall.png",4,game, 400 / 4 , 100 / 1,2)
pball.setSpeed(2,90)
pball.resizeBy(-55)

Sunflower = []
flower=Animation("./images/sunflower.png",54,game,1000 / 5, 2145 / 11,2)
flower.setSpeed(1,90)
flower.resizeBy(-60)
flower.visible = False

'''
for i in range(100):
    flower=Animation("./images/sunflower.png",54,game,1000 / 5, 2145 / 11,2)
    flower.setSpeed(1,90)
    flower.resizeBy(-60)
    Sunflower.append(flower)
positionObjects(Sunflower)
'''


introduction.resizeTo(game.width, game.height)
sunicon.moveTo(35,110)
nuticon.moveTo(32,185)
adventure.moveTo(735,145)
adventure.resizeBy(51)
adventureon.moveTo(735,140)
adventureon.resizeBy(90)
survival.moveTo(726,253)
survivalon.moveTo(726,253)

splatter=Animation("./images/splat.png",47,game,2510 / 5, 5050 / 10,3 )

Pnormal= []
Pnorm = Animation("./images/PeashooterIdle.png",25,game, 3775 / 5, 3775 / 5,3 )
Pnorm.visible = False
Pnorm.resizeBy(-90)
'''
for i in range(100):
    Pnorm = Animation("./images/PeashooterIdle.png",25,game, 3775 / 5, 3775 / 5, )
    Pnorm.resizeBy(-90)
    Pnorm.setSpeed(1,90)
    Pnormal.append(Pnorm)
positionObjects(Pnormal)
'''

Nut = []
NutStarter = Animation("./images/Wallnut.png",44,game,320 / 5, 648 / 9,3)
NutStarter.visible = False
'''
for i in range (100):
    wallnut=Animation("./images/Wallnut.png",44,game,320 / 5, 648 / 9,3)
    wallnut.setSpeed(1,90)
    Nut.append(wallnut)
positionObjects(Nut)
'''
SunFlowerSun=[]
'''
for i in range(50):
    flowersun=Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
    flowersun.visible = False
    SunFlowerSun.append(flowersun)
'''
'''
for i in range(50):
  flowersun = Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
  flowersun.resizeBy(-50)
  SunFlowerSun.append(flowersun)
positionObjects(flowersun)
'''

Suns = []
for i in range(50):
  Sun = Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
  Sun.resizeBy(-50)
  Suns.append(Sun)
positionObjects(Suns)

SunsF = []
for i in range(50):
  SunF = Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
  SunF.resizeBy(-50)
  SunsF.append(SunF)
positionObjects(SunsF)

SunDec = Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
SunDec.moveTo(100,20)
SunDec.resizeBy(-50)

F = Font(red,30,orange,"Comic Sans MS")

progressbar =Shape("bar", game, 100, 20, red)
progressbar.moveTo( 10,10)
progressbar.width = game.score


ry  = randint(250,600)
t=0
Sun_energy = 0
PeaDrag = False
NutDrag = False
SunDrag = False
play = True
game.playMusic()

while not game.over:
    game.processInput()
    introduction.draw()
    adventure.draw()
    adventureon.draw()
    survival.draw()
    survivalon.draw()
    survivalon.visible=False
    adventureon.visible = False
    if mouse.collidedWith(survival):
        survivalon.visible = True

    else:
        survivalon.visible = False
        
    if mouse.collidedWith(adventure):
        adventureon.visible = True
        
    else:
       adventureon.visible = False

    if mouse.collidedWith(adventureon) and mouse.LeftClick:
       game.over=True
        
    game.update(30)

game.over = False

game.stopMusic()

game.setMusic("sounds/level3.mp3")

game.playMusic()

SunF.visible = False


Sun_energy  = 100

pball.t=0

while not game.over:
  game.processInput()
  Level1.draw()
  Sun.move()
  #flowersun.move()
  SunF.draw()
  PIcon.draw()
  SunDec.draw()
  sunicon.draw()
  nuticon.draw()
  progressbar.draw()
  progressbar.width = game.score
  progressbar.moveTo(10,600)
  if play:
      arrival.play()
      play = False

  pball.setSpeed(14,270)



  for i in range(len(Nut)):
      Nut[i].draw()
 
  for i in range(len(Pnormal)):
      Pnormal[i].draw()


      
      '''
      if Pnormal[i].health<0:
          Pnormal[i].visible=False

      if Pnormal[i].visible == False:
          z.images = zombiewalk.images
      '''



             
  for i in range(len(Sunflower)):
      Sunflower[i].draw()

  for i in range (len(SunFlowerSun)):
      SunFlowerSun[i].t += 1
      if SunFlowerSun[i].t > 350:
          SunFlowerSun[i].draw()
          SunFlowerSun[i].visible = True
          

      if mouse.collidedWith(SunFlowerSun[i]) and mouse.LeftClick:
          SunFlowerSun[i].visible = False
          SunFlowerSun[i].t = 0
          Sun_energy+=50
          collect.play()

  for i in range(len(zombie)):
      if zombie[i].health < 0:
          zombie[i].draw(False)

      else:
          zombie[i].move()



  for pball in Peaball:
      print(pball.t)
      if pball.t < 25:
            pball.visible = False
            pball.t+=1
            pball.moveTo(pball.sx,pball.sy)
      else:
          if pball.x > game.width:
              pball.Visible = False
              pball.t = 0
              pball.moveTo(pball.sx,pball.sy)

          elif pball.health > 0:
              pball.visible = True
              pball.move()

  for z in zombie:              
      for c in conehead:
          for i in range(len(Pnormal)):
              p = Pnormal[i]
      for i in range(len(Pnormal)):
            p = Pnormal[i]
            if z.collidedWith(p):
                z.images = zombieeat.images
                z.setSpeed(0)
                z.collisonBorder="circle"
                p.health-= 1
                
                bite.play()
                    #print(p.health)


            if p.health<=0:
                    p.visible = False
                    Peaball[i].visible = False
                    Peaball[i].health = 0
                    z.images = zombiewalk.images
                    c.images = coneheadwalk.images
                    c.setSpeed(0.5,90)
                    z.setSpeed(0.5,90)
                    
            for pball in Peaball:
                if pball.collidedWith(z):
                    pball.moveTo(pball.sx,pball.sy)
                    pball.t=0
                    z.health-=10
                    game.score+=1
                    splat.play()


            
                if z.health<=0:
                    z.images = zombiedeath.images


   



  for z in zombie:
      for n in Nut:
          if z.collidedWith(n):
              z.images = zombieeat.images
              z.setSpeed(0)
              z.collisonBorder="circle"
              n.health-= 0.30
              bite.play()
              #print(n.health)


          if n.health<=0:
              #Sprint("Dead")
              n.visible = False
              z.images = zombiewalk.images
              z.setSpeed(0.5,90)

           

  for z in zombie:
      for s in Sunflower:
          if z.collidedWith(s):
              z.images = zombieeat.images
              z.setSpeed(0)
              z.collisonBorder="circle"
              s.health-= 1
              bite.play()
              #print(s.health)


          if s.health<=0:
              #Sprint("Dead")
              s.visible = False
              z.images = zombiewalk.images
              z.setSpeed(0.5,90)

        

      
  if PeaDrag:
      Pnorm.moveTo(mouse.x,mouse.y)
           
  if mouse.collidedWith(PIcon)and mouse.LeftClick and Sun_energy>=100:
    PeaDrag = True
    Pnorm.visible = True

  elif mouse.LeftClick and PeaDrag:
      PeaDrag = False
      P = Animation("./images/PeashooterIdle.png",25,game, 3775 / 5, 3775 / 5,1)
      P.resizeBy(-90)
      P.moveTo(mouse.x,mouse.y)
      Pnormal.append(P)

      Sun_energy-=100
      pball=Animation("./images/PeaBall.png",4,game, 400 / 4 , 100 / 1,2)
      pball.setSpeed(1,90)
      pball.resizeBy(-55)
      pball.moveTo(P.x,P.y)
      pball.sx = P.x
      pball.sy = P.y
      pball.t=200
      Peaball.append(pball)
      plant.play()
         
      #pball.visble = True
      #pball.moveTo(P.x,P.y)
             

  if NutDrag:
      NutStarter.moveTo(mouse.x,mouse.y)
      

  if mouse.collidedWith(nuticon) and mouse.LeftClick and Sun_energy>=50:
      NutDrag = True
      NutStarter.visible = True

  elif mouse.LeftClick and NutDrag:
      NutDrag = False
      wallnut=Animation("./images/Wallnut.png",44,game,320 / 5, 648 / 9,3)
      wallnut.moveTo(mouse.x,mouse.y)
      Nut.append(wallnut)
      plant.play()
      Sun_energy-=50
  
  if SunDrag:
      flower.moveTo(mouse.x,mouse.y)
      
  if mouse.collidedWith(sunicon)and mouse.LeftClick and Sun_energy>=50:
      SunDrag = True
      flower.visible = True
      

  elif mouse.LeftClick and SunDrag:
      SunDrag = False
      fstarter=Animation("./images/sunflower.png",54,game,1000 / 5, 2145 / 11,2)
      fstarter.resizeBy(-60)
      fstarter.moveTo(mouse.x,mouse.y)
      Sunflower.append(fstarter)
      Sun_energy-=50
      flowersun = Animation("./images/sun_sprites.png",30,game, 600 / 5, 720 / 6, 0.5)
      flowersun.resizeBy(-50)
      flowersun.moveTo(mouse.x,mouse.y)
      flowersun.visible = False
      plant.play()
      flowersun.t = 0
      SunFlowerSun.append(flowersun)
  
      

      
  
  if Sun.y >= ry:
      Sun.setSpeed(0,180)

  if t >= 300 :
      ry  = randint(250,600)
      Sun.moveTo(ry,-100)
      t = 0
      Sun.setSpeed(4,180)
      Sun.visible = True


  if mouse.collidedWith (Sun) and mouse.LeftClick:                
      Sun.visible = False
      Sun_energy+=50
      collect.play()
      
      
  game.drawText(".:"+str(Sun_energy),110,7,F)
  t+=1

  for z in zombie:
      if z.x<=60:
          lost.draw()
          game.stopMusic()
          lose.play()
          game.drawText("PRESS SPACE TO QUIT",10,550,F)
          if keys.Pressed[K_SPACE]:
              game.over = True

  if game.score>=300:
      game.over = True

  game.update(30)

game.over = False

game.stopMusic()

while not game.over:
    game.processInput()


    surrender.draw()
    win.play()
    play = False
    game.drawText("PRESS SPACE TO QUIT",10,550,F)
    if keys.Pressed[K_SPACE]:
        game.over = True
    
    game.update(30)
game.quit()
































