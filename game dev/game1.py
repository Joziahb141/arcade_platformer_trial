import arcade
import random

WIDTH = 1200
HEIGHT = 800
TITTLE = "Sprites"


class Mouse():
  def __init__(self,x,y,vel_x,vel_y,color_1,color_2,color_3,color_4):
      self.x = x
      self.y = y
      self.vel_x = vel_x
      self.vel_y = vel_y
      self.color_1 = color_1
      self.color_2 = color_2
      self.color_3 = color_3
      self.color_4 = color_4
  
  def update(self):
      if self.x > WIDTH - 199:
          self.vel_x = - abs(self.vel_x)
      if self.y > HEIGHT - 249:
          self.vel_y = - abs(self.vel_y)
      if self.x < 199:
          self.vel_x = abs(self.vel_x)
      if self.y < 185:
          self.vel_y = abs(self.vel_y)
      self.x += self.vel_x
      self.y += self.vel_y


  def draw_mouse(self):
      arcade.draw_circle_filled( self.x ,   self.y , 60, self.color_1)
      arcade.draw_circle_filled( self.x - 50,  self.y + 70, 30, self.color_1)
      arcade.draw_circle_filled( self.x + 50,  self.y + 70, 30, self.color_1)
      arcade.draw_circle_outline( self.x - 40,  self.y - 30, 18, self.color_1, 4)
      arcade.draw_circle_outline( self.x + 40 ,  self.y - 30, 18, self.color_1, 4)
      arcade.draw_triangle_outline(self.x - 12, self.y - 64, self.x - 24, self.y -48, self.x, self.y - 56, self.color_1, 4)
      arcade.draw_triangle_outline(self.x + 12, self.y - 64, self.x + 24, self.y -48, self.x, self.y - 56, self.color_1, 4)
      arcade.draw_ellipse_outline( self.x, self.y - 32, 110, 52, self.color_1, 2)
      arcade.draw_parabola_outline( self.x - 14 ,  self.y - 34, self.x + 14, - 24, self.color_1, 4)
      arcade.draw_triangle_filled(self.x - 12, self.y - 64, self.x - 24, self.y -48, self.x, self.y - 56, self.color_2)
      arcade.draw_triangle_filled(self.x + 12, self.y - 64, self.x + 24, self.y -48, self.x, self.y - 56, self.color_2)
      arcade.draw_circle_filled( self.x - 40,  self.y - 30, 16, self.color_2)
      arcade.draw_circle_filled( self.x + 40,  self.y - 30, 16, self.color_2)
      arcade.draw_parabola_filled( self.x - 14 ,  self.y - 34, self.x + 14, - 24,self.color_2)
      arcade.draw_parabola_filled( self.x - 36,  self.y - 142, self.x + 10, 128, self.color_2, 8)
      arcade.draw_parabola_filled( self.x - 10,  self.y - 142, self.x + 36, 128, self.color_2, 352)      
      arcade.draw_ellipse_filled( self.x, self.y - 32, 106, 48, self.color_2)
      arcade.draw_parabola_filled( self.x - 22,  self.y - 102, self.x - 2, 86, self.color_1, 2)
      arcade.draw_parabola_filled( self.x + 2,  self.y - 102, self.x + 22, 86, self.color_1, 358)
      arcade.draw_parabola_filled( self.x - 20,  self.y - 96, self.x - 4, 80, self.color_3, 2)
      arcade.draw_parabola_filled( self.x + 4 ,  self.y- 96, self.x + 20, 80, self.color_3, 358)
      arcade.draw_parabola_filled( self.x - 14, self.y - 48, self.x - 6, 32, self.color_1, 3)
      arcade.draw_parabola_filled( self.x + 6, self.y - 48, self.x + 14, 32, self.color_1, 357)
      arcade.draw_arc_outline( self.x, self.y - 20, 52, 10, self.color_1, 0, 180, 4)
      arcade.draw_ellipse_filled( self.x, self.y - 28, 30, 20, self.color_1)
      arcade.draw_parabola_outline( self.x - 40, self.y + 4, self.x + 40, - 32, self.color_1, 10)
      arcade.draw_parabola_filled(self.x - 16, self.y -4, self.x + 16, -40, self.color_1)
      arcade.draw_triangle_filled(self.x - 12, self.y - 56, self.x - 24, self.y -40, self.x, self.y - 48, self.color_1)
      arcade.draw_triangle_filled(self.x + 12, self.y - 56, self.x + 24, self.y -40, self.x, self.y - 48, self.color_1)
      arcade.draw_arc_filled(self.x + 40, self.y - 28, 12, 4, self.color_1, 0, 180, 330)
      arcade.draw_arc_filled(self.x - 40, self.y - 28, 12, 4, self.color_1, 0, 180, 30)
      arcade.draw_parabola_filled(self.x - 14, self.y -20, self.x + 14, -28, self.color_4)
      points_list = ((self.x - 10, self.y - 58),
                      (self.x + 10, self.y -58),
                      (self.x + 20, self.y - 44),
                      (self.x - 20, self.y - 44))
      arcade.draw_polygon_filled(points_list, self.color_1)
      arcade.draw_parabola_filled(self.x - 9, self.y - 68, self.x, 8, self.color_4)
      arcade.draw_parabola_filled(self.x, self.y - 68, self.x + 9, 8, self.color_4)
      arcade.draw_parabola_outline(self.x - 10, self.y - 68, self.x + 1, 9, self.color_1, 6)

def get_color() ->  list:
    colors_list = ()
    for i in range 3:
        colors_list.append(random.randint(0,255))

mouse1 = Mouse(400, 400, 3, 1.5, arcade.color.BLACK, arcade.color.SUNRAY, arcade.color.WHITE, arcade.color.RED)
mouse2 = Mouse( 200, 200, 1, 2, arcade.color.CYAN, arcade.color.WHITE, arcade.color.RED, arcade.color.BLUE)
mouse3 = Mouse( 400, 400, 7, 4.5, arcade.color.OLD_GOLD, arcade.color.NEW_CAR, arcade.color.BLACK, arcade.color.BRONZE)
mouse4 = Mouse(600 ,600 ,1.5, 2.5, arcade.color.NAVY_BLUE, arcade.color.BABY_POWDER, arcade.color.NEON_GREEN, arcade.color.SILVER)
mouse5 = Mouse(350, 350, 3.5, 3.5, arcade.color.ORANGE_RED, arcade.color.NEW_YORK_PINK, arcade.color.BRONZE_YELLOW, arcade.color.ORANGE)

def on_draw(delta_time):
    mouse1.update()
    mouse2.update()
    mouse3.update()
    mouse4.update()
    mouse5.update()
    arcade.start_render()
    mouse2.draw_mouse()
    mouse3.draw_mouse()
    mouse4.draw_mouse()
    mouse5.draw_mouse()
    mouse1.draw_mouse()
    arcade.finish_render()

window = arcade.open_window(WIDTH, HEIGHT, TITTLE)
arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)

arcade.schedule(on_draw, 1/60)

arcade.run()