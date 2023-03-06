from player import Player
from layouts import Layouts
from pygame import mixer
from config import *


class Game(pygame.sprite.Sprite):
    def __init__(self, screen_game):
        super().__init__()
        self.screen = screen_game
        self.gameplay_loop = gameplay_loop
        self.select_char = True
        self.layout = Layouts()
        self.walls = self.layout.get_group()
        self.looping = looping
        self.menu_looping = self.screen
        self.char_looping_1 = char_looping_1
        self.char_looping_2 = char_looping_2
        self.background = start_img_menu
        self.players = []
        self.hit_timer = 0
        self.score_text_1_rect = (screen_width / 4, -15)
        self.score_text_2_rect = (screen_width - screen_width / 4, -15)
        self.menu = True
        self.victory_can_play = True
        self.moving_left = False
        self.moving_right = False
        self.moving_left2 = False
        self.moving_right2 = False
        self.jump = False
        self.jump2 = False
        self.check = False
        pass

    def get_screen(self):
        self.background = start_img_menu

    def game_loop(self):
        self.get_screen()
        while self.looping:
            if self.gameplay_loop is False:
                self.get_menu()
                self.draw_sprites_menu()
            else:
                for player in self.players:
                    self.player_collision(player)
                    for player2 in self.players:
                        if player2 != player:
                            self.shoot_collision(player, player2)
                    for bullet in player.bullet_list:
                        self.bullet_collision(bullet)
                self.check_events_game()
                self.draw_sprites_game()
                self.check_winner(self.players[0], self.players[1])
            pygame.display.update()
            clk.tick(fps)

    def get_menu(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Exit Press Start
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(6):
                    self.menu_looping = False
                    self.char_looping_1 = True

                # Choice P1
                if self.char_looping_1:
                    self.background = char_left_img_menu
                    if pygame.joystick.Joystick(0).get_button(13) or pygame.joystick.Joystick(0).get_button(14):
                        self.select_char = not self.select_char

                    # Confirm P1
                    if pygame.joystick.Joystick(0).get_button(0):
                        self.char_looping_1 = False
                        self.char_looping_2 = True

                        if self.select_char:
                            self.players.append(Player(xp1, yp1, lenin))
                        else:
                            self.players.append(Player(xp1, yp1, stalin))

                # Choice p2
                if self.char_looping_2:
                    self.background = char_right_img_menu
                    if pygame.joystick.Joystick(1).get_button(13) or pygame.joystick.Joystick(1).get_button(14):
                        self.select_char = not self.select_char

                    # Confirm P2
                    if pygame.joystick.Joystick(1).get_button(0):
                        self.char_looping_2 = False
                        self.gameplay_loop = True
                        if self.select_char:
                            self.players.append(Player(xp2, yp2, jfk))
                        else:
                            self.players.append(Player(xp2, yp2, ronald))
                        mixer.music.pause()
                        mixer.init()
                        mixer.music.load('assets/song_game.mp3')
                        mixer.music.set_volume(0.4)
                        mixer.music.play(-1)

    def check_events_game(self):
        if self.victory_can_play:
            # move players
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                for i in range(len(self.players)):
                    self.players[i].move(self.moving_left, self.moving_right, self.jump)
                    if self.players[i].shoot:
                        self.players[i].shoot_()
                        if event.type == pygame.JOYBUTTONDOWN:
                            if pygame.joystick.Joystick(i).get_button(13):
                                self.moving_left = True
                            if pygame.joystick.Joystick(i).get_button(14):
                                self.moving_right = True
                            if pygame.joystick.Joystick(i).get_button(10):
                                self.players[i].shoot = True
                            if pygame.joystick.Joystick(i).get_button(0):
                                self.jump = True
                                jetpack.play()

                        if event.type == pygame.JOYBUTTONUP:
                            if pygame.joystick.Joystick(i).get_button(13):
                                self.moving_left = False
                            if pygame.joystick.Joystick(i).get_button(14):
                                self.moving_right = False
                            if pygame.joystick.Joystick(i).get_button(10):
                                self.players[i].shoot = False
                            if pygame.joystick.Joystick(i).get_button(0):
                                self.jump = False
                                jetpack.stop()

        else:
            for i in range(len(self.players)):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.JOYBUTTONDOWN:
                        if pygame.joystick.Joystick(i).get_button(1):
                            self.looping = False

    def shoot_collision(self, player1, player2):
        for ball in player2.bullet_list:
            if pygame.sprite.collide_mask(ball, player1):
                self.check = True
                player1.bullet_list.clear()
                player2.bullet_list.clear()
                player1.bullet_group.empty()
                player2.bullet_group.empty()
                player1.hit = True
                player2.stop = True
                player2.score += 1
                death_sfx = pygame.mixer.Sound('assets/death.wav')
                death_sfx.play()

    def player_collision(self, player):
        for wall in self.walls:
            if pygame.sprite.collide_mask(player, wall):
                if abs(player.rect.top - wall.rect.bottom) < 100:
                    player.rect.y += speed
                elif abs(wall.rect.top - player.rect.bottom) < 20:
                    player.rect.y -= speed
                elif abs(wall.rect.left - player.rect.right) < 30:
                    player.rect.x -= speed
                elif abs(player.rect.left - wall.rect.right) < 30:
                    player.rect.x += speed

    def bullet_collision(self, bullet):
        for wall in self.walls:
            if pygame.sprite.collide_mask(bullet, wall):
                bullet.kill()

    def draw_sprites_menu(self):
        self.screen.blit(self.background, (0, 0))

        # draw char picker 1
        if self.char_looping_1:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (255, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1035, 190), 20)

        # draw char picker 2
        elif self.char_looping_2:
            if self.select_char:
                pygame.draw.circle(self.screen, WHITE, (170, 190), 20)
            else:
                pygame.draw.circle(self.screen, WHITE, (1080, 180), 20)

    def draw_sprites_game(self):
        self.background = scenario1
        screen.blit(self.background, (0, 0))
        self.walls.draw(self.screen)
        for player in self.players:
            player.draw()
            # draw and update bullets on screen
            player.bullet_group.update()
            player.bullet_group.draw(self.screen)
            player.update()

    def check_winner(self, player1, player2):
        score_text_1_rect = (screen_width / 4, -15)
        score_text_2_rect = (screen_width - screen_width / 4, -15)
        if player1.score < max_score and player2.score < max_score:
            score_text_1 = score_font.render(str(player1.score), True, RED)
            score_text_2 = score_font.render(str(player2.score), True, BLUE)
            self.screen.blit(score_text_1, score_text_1_rect)
            self.screen.blit(score_text_2, score_text_2_rect)
        else:
            if player2.score < player1.score:
                self.screen.blit(player1_wins, (0, 0))
                if self.victory_can_play:
                    mixer.music.pause()
                    mixer.music.load('assets/soviet_union_1.wav')
                    mixer.music.play(-1)
                self.victory_can_play = False
            else:
                self.screen.blit(player2_wins, (0, 0))
                if self.victory_can_play:
                    mixer.music.pause()
                    mixer.music.load('assets/america_wins.mp3')
                    mixer.music.play(-1)
                self.victory_can_play = False
