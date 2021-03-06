import pygame 
import sys
import copy
from settings import *
from player import *
from enemy_class import *
import random


pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH//COLS
        self.cell_height = MAZE_HEIGHT//ROWS
        self.walls = []
        self.coins = []
        self.pellet = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.totalscore=0
        self.mazetype = 'default'
        self.mazelocation = 'maze.png'
        self.wallslocation = 'walls.txt'
        self.load()
        self.player = Player(self, vec(self.p_pos))
        self.make_enemies()
        #self.draw_grid()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
                if self.mazetype == 'random':
                    self.randomise()
                    self.load()
                    self.player = Player(self, vec(self.p_pos))
                    self.make_enemies()
            elif self.state == 'playing':



                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'win':
                self.win_events()
                self.win_update()
                self.win_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

############################ HELPER FUNCTIONS ##################################

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load(self.mazelocation)
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        self.walls = []
        self.coins = []
        self.pellet = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.totalscore=0
        
        # Opening walls file
        # Creating walls list with co-ords of walls
        # stored as  a vector
        with open(self.wallslocation, 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                        self.totalscore+=1
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char ==  "6":
                        self.pellet.append(vec(xidx, yidx))
                        
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx*self.cell_width, yidx*self.cell_height,
                                                                  self.cell_width, self.cell_height))

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x*self.cell_width, 0),
                             (x*self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x*self.cell_height),
                             (WIDTH, x*self.cell_height))
        # for coin in self.coins:
        #     pygame.draw.rect(self.background, (167, 179, 34), (coin.x*self.cell_width,
        #                                                        coin.y*self.cell_height, self.cell_width, self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        self.coins = []
        self.pellet = []
        with open(self.wallslocation, 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
                    if char == '6':
                        self.pellet.append(vec(xidx, yidx))
        


########################### Main menu ####################################
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.mazetype = 'random'  
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.mazetype = 'default'  
            

    def start_update(self):
        pass

    def start_draw(self):
        Pacman = pygame.image.load('./Images/pacman-menu.png')
        self.screen.fill(BLACK)

        self.screen.blit(Pacman, [WIDTH//2-100, HEIGHT//2-320])
        self.draw_text('Pacman', self.screen, [
            WIDTH//2, HEIGHT//2-320], START_TEXT_SIZE, (255, 255, 0), START_FONT, centered=True)
        self.draw_text('Space bar to start', self.screen, [
            WIDTH//2, HEIGHT//2-50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('Maze type '+ self.mazetype, self.screen, [
            WIDTH//2, HEIGHT//2+50], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Year:2021 ', self.screen, [
            WIDTH//2, HEIGHT//2+200], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Course Code: 3815ICT and 7805ICT ', self.screen, [
            WIDTH//2, HEIGHT//2+220], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Chun on Chan ', self.screen, [
            WIDTH//2, HEIGHT//2+240], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Guan-Tse Wu ', self.screen, [
            WIDTH//2, HEIGHT//2+260], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Sirawat Thiangthae ', self.screen, [
            WIDTH//2, HEIGHT//2+280], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
        self.draw_text('Yan Li ', self.screen, [
            WIDTH//2, HEIGHT//2+300], START_TEXT_SIZE, (44, 167, 198), START_FONT, centered=True)
                       
        
        

        pygame.display.update()
        

########################### PLAYING FUNCTIONS ##################################
    def randomise(self):
        #randomnum=random.uniform(0, 1)
        randomnum=1
        if randomnum==0:
            pass
        elif randomnum==1:
            self.mazelocation = 'maze2.png'
            self.wallslocation = 'walls2.txt'


    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1, 0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1, 0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0, -1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0, 1))

    def playing_update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if (enemy.grid_pos == self.player.grid_pos) and self.player.power==False :
                self.remove_life()
            if (enemy.grid_pos == self.player.grid_pos) and self.player.power:
                 enemy.grid_pos = vec(enemy.starting_pos)
                 enemy.pix_pos = enemy.get_pix_pos()
                 enemy.direction *= 0


        if self.totalscore == self.player.current_score:
            self.state = "win"


    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
        self.draw_coins()
        self.draw_pellets()
        # self.draw_grid()
        self.draw_text('CURRENT SCORE: {}'.format(self.player.current_score),
                       self.screen, [60, 0], 18, WHITE, START_FONT)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()

    def remove_life(self):
        self.player.lives -= 1
        death=pygame.mixer.Sound('./Sound/Death_Sound_Effect.mp3')
        death.play()
        death.set_volume(0.1)
        if self.player.lives == 0:
            self.reset()
            self.state = "start"
            
        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            pygame.draw.circle(self.screen, (124, 123, 7),
                               (int(coin.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2,
                                int(coin.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2), 3)
    def draw_pellets(self):
         for pellet in self.pellet:
             pygame.draw.circle(self.screen, (200, 7, 136),
                               (int(pellet.x*self.cell_width)+self.cell_width//2+TOP_BOTTOM_BUFFER//2,
                                int(pellet.y*self.cell_height)+self.cell_height//2+TOP_BOTTOM_BUFFER//2), 5)

########################### Win menu FUNCTIONS ################################

    def win_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state='start'
                self.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def win_update(self):
        pass

    def win_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Press SPACE bar to go to the main menu"
        self.draw_text("Congratulations on winning", self.screen, [WIDTH//2, 100],  52, RED, "arial", centered=True)
        self.draw_text(again_text, self.screen, [
                       WIDTH//2, HEIGHT//2],  36, (190, 190, 190), "arial", centered=True)
        self.draw_text(quit_text, self.screen, [
                       WIDTH//2, HEIGHT//1.5],  36, (190, 190, 190), "arial", centered=True)
        pygame.display.update()
