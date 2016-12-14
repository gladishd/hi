import pygame
import math
surface = pygame.display.set_mode([800,800])
class Fractal:
    angle = 0
    def __init__(self, angle):
        pygame.init()
        self.angle = angle
class TreeFractal(Fractal):
    def __init__(self):
        Fractal.__init__(self, 20)
    def loop(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                self.angle += 0.1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.angle -= 0.1
            surface.fill((0, 0, 0))
            self.draw(6, 800*0.9, (800//2, 800-50), -math.pi/2, (255,255,255))
            pygame.display.flip()
    def draw(self, order, size, pos, heading, color, depth=0):
        trunkratio = 0.3  
        trunk = size * trunkratio 
        deltax = trunk * math.cos(heading)
        deltay = trunk * math.sin(heading)
        (u, v) = pos
        newpos = (u + deltax, v + deltay)
        pygame.draw.line(surface, color, pos, newpos)
        if order > 0: 
            self.draw(order-1, size*(1 - trunkratio), newpos, heading-self.angle, (255,0,0), depth+1)
            self.draw(order-1, size*(1 - trunkratio), newpos, heading+self.angle, color, depth+1)
class RandomFractal(Fractal):
    def __init__(self):
        Fractal.__init__(self, math.pi/2)
    def loop(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                self.angle += 0.1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                self.angle -= 0.1
            surface.fill((255, 255, 255))
            self.draw(800, 800*0.2, (400, 400), math.pi, (0,0,0))
            pygame.display.flip()
    def draw(self, order, size, pos, heading, color, depth=0):
        deltax = 50*math.cos(heading)
        deltay = 50*math.sin(heading)
        u = 400
        v = 400
        (u, v) = pos
        c1 = 50 * math.cos(heading+math.pi/9)
        c2 = 50 * math.sin(heading+math.pi/9)
        c3 = 50 * math.cos(heading+2*math.pi/9)
        c4 = 50 * math.sin(heading+2*math.pi/9)
        c5 = 50 * math.cos(heading-math.pi/9)
        c6 = 50 * math.sin(heading-math.pi/9)
        c7 = 50 * math.cos(heading-2*math.pi/9)
        c8 = 50 * math.sin(heading-2*math.pi/9)
        if order > 0:
            if order & 1 == 0:
                c1 = 50 * math.cos(heading-math.pi/9)
                c2 = 50 * math.sin(heading-math.pi/9)
                c3 = 50 * math.cos(heading-2*math.pi/9)
                c4 = 50 * math.sin(heading-2*math.pi/9)
            else:
                c1 = 50 * math.cos(heading+math.pi/9)
                c2 = 50 * math.sin(heading+math.pi/9)
                c3 = 50 * math.cos(heading+2*math.pi/9)
                c4 = 50 * math.sin(heading+2*math.pi/9)
        newpos = (u + deltax, v + deltay)
        newpos2 = (newpos[0] + c1, newpos[1] + c2)
        newpos3 = (newpos2[0] + c3, newpos2[1] + c4)
        pygame.draw.line(surface, color, pos, newpos)
        pygame.draw.line(surface, color, newpos, newpos2)
        pygame.draw.line(surface, color, newpos2, newpos3)
        if order > 0:
                self.draw(order-1, size, newpos, heading-self.angle, color, depth+1)
def sierpinski(order, angle, size, pos, heading, color, depth=0):
   deltax = 50*math.cos(heading)
   deltay = 50*math.sin(heading)
   u = 400
   v = 400
   (u, v) = pos
   c1 = 50 * math.cos(heading+math.pi/3)
   c2 = 50 * math.sin(heading+math.pi/3)
   c3 = 50 * math.cos(heading+2*math.pi/3)
   c4 = 50 * math.sin(heading+2*math.pi/3)
   if order > 0:
      if order & 1 == 0:
            c1 = 50 * math.cos(heading-math.pi/3)
            c2 = 50 * math.sin(heading-math.pi/3)
            c3 = 50 * math.cos(heading-2*math.pi/3)
            c4 = 50 * math.sin(heading-2*math.pi/3)
      else:
            c1 = 50 * math.cos(heading+math.pi/3)
            c2 = 50 * math.sin(heading+math.pi/3)
            c3 = 50 * math.cos(heading+2*math.pi/3)
            c4 = 50 * math.sin(heading+2*math.pi/3)
   newpos = (u + deltax, v + deltay)
   newpos2 = (newpos[0] + c1, newpos[1] + c2)
   newpos3 = (newpos2[0] + c3, newpos2[1] + c4)
   pygame.draw.line(surface, color, pos, newpos)
   pygame.draw.line(surface, color, newpos, newpos2)
   pygame.draw.line(surface, color, newpos2, newpos3)
   if order > 0:
        sierpinski(order-1, angle, size, newpos3, heading-angle, color, depth+1)
def draw_sierpinski():
    pygame.init()  
    angle = math.pi/1
    while True:
        angle += 1
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: 
            angle += 0.1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            angle -= 0.1
        surface.fill((255, 255, 255))
        sierpinski(5, angle, 800*0.2, (400, 400), math.pi, (0,0,0))
        pygame.display.flip()
def dragon(order, angle, size, pos, heading, color, depth=0):
   u = 400
   v = 400
   (u, v) = pos
   s = 10  
   newpos = (u - s, v + s)
   newpos2 = (newpos[0] - s, newpos[1] - s)
   if order == 3 or order == 7 or order == 11 or order == 15 or order == 19:
       newpos3 = (newpos2[0] + s, newpos2[1] - s)
       newpos4 = (newpos3[0] - s, newpos3[1] - s)
       newpos5 = (newpos4[0] + s, newpos4[1] - s)
       newpos6 = (newpos5[0] + s, newpos5[1] + s)
       newpos7 = (newpos6[0] + s, newpos6[1] - s)
       newpos8 = (newpos7[0] - s, newpos7[1] - s)
       newpos9 = (newpos8[0] + s, newpos8[1] - s)
       newpos10 = (newpos9[0] + s, newpos9[1] + s)
       newpos11 = (newpos10[0] - s, newpos10[1] + s)
       newpos12 = (newpos11[0] + s, newpos11[1] + s)
       newpos13 = (newpos12[0] + s, newpos12[1] - s)
       newpos14 = (newpos13[0] + s, newpos13[1] + s)
       newpos15 = (newpos14[0] + s, newpos14[1] - s)
       newpos16 = (newpos15[0] - s, newpos15[1] - s)
       newpos17 = (newpos16[0] - s, newpos16[1] + s)
       newpos18 = (newpos17[0] - s, newpos17[1] - s)
       newpos19 = (newpos18[0] + s, newpos18[1] - s)
       newpos20 = (newpos19[0] - s, newpos19[1] - s)
       newpos21 = (newpos20[0] + s, newpos20[1] - s)
       newpos22 = (newpos21[0] + s, newpos21[1] + s)
       newpos23 = (newpos22[0] + s, newpos22[1] - s)
       newpos24 = (newpos23[0] - s, newpos23[1] - s)
       newpos25 = (newpos24[0] - s, newpos24[1] + s)
       newpos26 = (newpos25[0] - s, newpos25[1] - s)
       newpos27 = (newpos26[0] + s, newpos26[1] - s)
       newpos28 = (newpos27[0] - s, newpos27[1] - s)
       newpos29 = (newpos28[0] - s, newpos28[1] + s)
       newpos30 = (newpos29[0] - s, newpos29[1] - s)
       newpos31 = (newpos30[0] - s, newpos30[1] + s)
       newpos32 = (newpos31[0] + s, newpos31[1] + s)
   if order == 2 or order == 6 or order == 10 or order == 14 or order == 18:
       newpos3 = (newpos2[0] + s, newpos2[1] + s)
       newpos4 = (newpos3[0] + s, newpos3[1] - s)
       newpos5 = (newpos4[0] + s, newpos4[1] + s)
       newpos6 = (newpos5[0] - s, newpos5[1] + s)
       newpos7 = (newpos6[0] + s, newpos6[1] + s)
       newpos8 = (newpos7[0] + s, newpos7[1] - s)
       newpos9 = (newpos8[0] + s, newpos8[1] + s)
       newpos10 = (newpos9[0] - s, newpos9[1] + s)
       newpos11 = (newpos10[0] - s, newpos10[1] - s)
       newpos12 = (newpos11[0] - s, newpos11[1] + s)
       newpos13 = (newpos12[0] + s, newpos12[1] + s)
       newpos14 = (newpos13[0] - s, newpos13[1] + s)
       newpos15 = (newpos14[0] + s, newpos14[1] + s)
       newpos16 = (newpos15[0] + s, newpos15[1] - s)
       newpos17 = (newpos16[0] - s, newpos16[1] - s)
       newpos18 = (newpos17[0] + s, newpos17[1] - s)
       newpos19 = (newpos18[0] + s, newpos18[1] + s)
       newpos20 = (newpos19[0] + s, newpos19[1] - s)
       newpos21 = (newpos20[0] + s, newpos20[1] + s)
       newpos22 = (newpos21[0] - s, newpos21[1] + s)
       newpos23 = (newpos22[0] + s, newpos22[1] + s)
       newpos24 = (newpos23[0] + s, newpos23[1] - s)
       newpos25 = (newpos24[0] - s, newpos24[1] - s)
       newpos26 = (newpos25[0] + s, newpos25[1] - s)
       newpos27 = (newpos26[0] + s, newpos26[1] + s)
       newpos28 = (newpos27[0] + s, newpos27[1] - s)
       newpos29 = (newpos28[0] - s, newpos28[1] - s)
       newpos30 = (newpos29[0] + s, newpos29[1] - s)
       newpos31 = (newpos30[0] - s, newpos30[1] - s)
       newpos32 = (newpos31[0] - s, newpos31[1] + s)
   if order == 1 or order == 5 or order == 9 or order == 13 or order == 17:
       newpos3 = (newpos2[0] - s, newpos2[1] + s)
       newpos4 = (newpos3[0] + s, newpos3[1] + s)
       newpos5 = (newpos4[0] - s, newpos4[1] + s)
       newpos6 = (newpos5[0] - s, newpos5[1] - s)
       newpos7 = (newpos6[0] - s, newpos6[1] + s)
       newpos8 = (newpos7[0] + s, newpos7[1] + s)
       newpos9 = (newpos8[0] - s, newpos8[1] + s)
       newpos10 = (newpos9[0] - s, newpos9[1] - s)
       newpos11 = (newpos10[0] + s, newpos10[1] - s)
       newpos12 = (newpos11[0] - s, newpos11[1] - s)
       newpos13 = (newpos12[0] - s, newpos12[1] + s)
       newpos14 = (newpos13[0] - s, newpos13[1] - s)
       newpos15 = (newpos14[0] - s, newpos14[1] + s)
       newpos16 = (newpos15[0] + s, newpos15[1] + s)
       newpos17 = (newpos16[0] + s, newpos16[1] - s)
       newpos18 = (newpos17[0] + s, newpos17[1] + s)
       newpos19 = (newpos18[0] - s, newpos18[1] + s)
       newpos20 = (newpos19[0] + s, newpos19[1] + s)
       newpos21 = (newpos20[0] - s, newpos20[1] + s)
       newpos22 = (newpos21[0] - s, newpos21[1] - s)
       newpos23 = (newpos22[0] - s, newpos22[1] + s)
       newpos24 = (newpos23[0] + s, newpos23[1] + s)
       newpos25 = (newpos24[0] + s, newpos24[1] - s)
       newpos26 = (newpos25[0] + s, newpos25[1] + s)
       newpos27 = (newpos26[0] - s, newpos26[1] + s)
       newpos28 = (newpos27[0] + s, newpos27[1] + s)
       newpos29 = (newpos28[0] + s, newpos28[1] - s)
       newpos30 = (newpos29[0] + s, newpos29[1] + s)
       newpos31 = (newpos30[0] + s, newpos30[1] - s)
       newpos32 = (newpos31[0] - s, newpos31[1] - s)
   if order == 0 or order == 4 or order == 8 or order == 12 or order == 16:
       newpos3 = (newpos2[0] - s, newpos2[1] - s)
       newpos4 = (newpos3[0] - s, newpos3[1] + s)
       newpos5 = (newpos4[0] - s, newpos4[1] - s)
       newpos6 = (newpos5[0] + s, newpos5[1] - s)
       newpos7 = (newpos6[0] - s, newpos6[1] - s)
       newpos8 = (newpos7[0] - s, newpos7[1] + s)
       newpos9 = (newpos8[0] - s, newpos8[1] - s)
       newpos10 = (newpos9[0] + s, newpos9[1] - s)
       newpos11 = (newpos10[0] + s, newpos10[1] + s)
       newpos12 = (newpos11[0] + s, newpos11[1] - s)
       newpos13 = (newpos12[0] - s, newpos12[1] - s)
       newpos14 = (newpos13[0] + s, newpos13[1] - s)
       newpos15 = (newpos14[0] - s, newpos14[1] - s)
       newpos16 = (newpos15[0] - s, newpos15[1] + s)
       newpos17 = (newpos16[0] + s, newpos16[1] + s)
       newpos18 = (newpos17[0] - s, newpos17[1] + s)
       newpos19 = (newpos18[0] - s, newpos18[1] - s)
       newpos20 = (newpos19[0] - s, newpos19[1] + s)
       newpos21 = (newpos20[0] - s, newpos20[1] - s)
       newpos22 = (newpos21[0] + s, newpos21[1] - s)
       newpos23 = (newpos22[0] - s, newpos22[1] - s)
       newpos24 = (newpos23[0] - s, newpos23[1] + s)
       newpos25 = (newpos24[0] + s, newpos24[1] + s)
       newpos26 = (newpos25[0] - s, newpos25[1] + s)
       newpos27 = (newpos26[0] - s, newpos26[1] - s)
       newpos28 = (newpos27[0] - s, newpos27[1] + s)
       newpos29 = (newpos28[0] + s, newpos28[1] + s)
       newpos30 = (newpos29[0] - s, newpos29[1] + s)
       newpos31 = (newpos30[0] + s, newpos30[1] + s)
       newpos32 = (newpos31[0] + s, newpos31[1] - s)
   lst = {1: pos, 2: newpos, 3: newpos2, 4: newpos3, 5: newpos4, 6: newpos5, 7: newpos6, 8: newpos7, 9: newpos8, 10: newpos9, 11: newpos10, 12: newpos11, 13: newpos12, 14: newpos13, 15: newpos14, 16: newpos15, 17: newpos16, 18: newpos17, 19: newpos18, 20: newpos19, 21: newpos20, 22: newpos21, 23: newpos22, 24: newpos23, 25: newpos24, 26: newpos25, 27: newpos26, 28: newpos27, 29: newpos28, 30: newpos29, 31: newpos30, 32: newpos31, 33: newpos32}
   for i in range(2, 34):
      pygame.draw.line(surface, color, lst[i-1], lst[i])
   if order > 0:
        dragon(order-1, angle, size, newpos31, heading-math.pi/3, color, depth+1)
def draw_dragon():
    pygame.init() 
    angle = math.pi/1
    order = 2
    bg = (255, 255, 255)
    color = (0,0,0)
    s = 10
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and order >= 0 and order <= 18:
            order += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and order >= 1 and order <= 19:
            order -= 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = (255, 255, 255)
            if event.key == pygame.K_2:
                color = (0, 0, 0)
            if event.key == pygame.K_3:
                color = (255, 0, 0)
            if event.key == pygame.K_4:
                color = (0, 255, 0)
            if event.key == pygame.K_5:
                color = (0, 0, 255)
            if event.key == pygame.K_6:
                color = (0, 255, 255)
            if event.key == pygame.K_7:
                color = (255, 0, 255)
            if event.key == pygame.K_8:
                color = (255, 255, 0)
            if event.key == pygame.K_9:
                bg = (0, 0, 0)
            if event.key == pygame.K_0:
                bg = (255, 255, 255)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                s += 0.1
            elif event.button == 5:
                s -= 0.1
        surface.fill(bg)
        dragon(order, angle, 800*0.2, (400, 400), math.pi, color)
        pygame.display.flip()
fractal = input('Choose: Tree, Dragon, ???, Sierpinski')
if fractal == 'Tree':
    treefractal = TreeFractal()
    treefractal.loop()
elif fractal == 'Dragon':
    draw_dragon()
elif fractal == '???':
    randomfractal = RandomFractal()
    randomfractal.loop()
elif fractal == 'Sierpinski':
    draw_sierpinski()