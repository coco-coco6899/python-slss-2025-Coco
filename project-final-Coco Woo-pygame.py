# Author : Coco Woo
# Title : Pygame project
# Date : Jan 14, 2026

import random
from turtle import window_width

import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (242, 43, 43)
GREEN = (35, 196, 17)
BLUE = (76, 224, 253)
GREY = (128, 128, 128)
ORANGE = (252, 162, 27)
YELLOW = (252, 252, 27)
PURPLE = (211, 182, 255)


class BlueBlock(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        """A block of any colour"""
        super().__init__()

        # Visual representation of our image
        self.image = pygame.Surface((width, height))
        # change the colour of self.image
        self.image.fill(BLUE)

        # A Rect tells you two things:
        #   - how big the hitbox is (width, height)
        #   - where it is (x, y)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 100

        self.point_value = 1

    def level_up(self, val: int):
        """Incr point value"""
        self.point_value *= val


class PurpleBlock(pygame.sprite.Sprite):
    def __init__(self, colour: pygame.Color, width: int, height: int):
        """A block of any colour"""
        super().__init__()

        # Visual representation of our image
        self.image = pygame.Surface((width, height))
        # change the colour of self.image
        self.image.fill(PURPLE)

        # A Rect tells you two things:
        #   - how big the hitbox is (width, height)
        #   - where it is (x, y)
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.centery = 50

        self.point_value = 5

    def level_up(self, val: int):
        """Incr point value"""
        self.point_value *= val


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """The player"""
        super().__init__()

        # Right version of Mario and Left version
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.previous_x = 0  # help with direction
        self.health = 500
        self.points = 0

    def calc_damage(self, amt: int) -> int:
        """Decrease player health by amt
        Returns:
            Remaining health"""
        self.health -= amt
        return self.health

    def calc_heal(self, amt: int) -> int:
        """Increase player health by amt
        Returns:
            Remaining health"""
        self.health += amt
        return self.health

    def incr_score(self, amt: int) -> int:
        """Increases player score by amt
        Returns:
            Score"""
        self.points += amt
        return self.points

    def get_damage_percentage(self) -> float:
        return self.health / 100

    def update(self):
        """Update Mario's location based on the mouse pos
        Update Mario's image based on where he's going"""
        self.rect.center = pygame.mouse.get_pos()

        # If Mario's previous x less than current x
        #   Then Mario is facing Right
        # If Mario's previous x is greater than current x
        #   Then Mario is facing Left
        if self.previous_x < self.rect.x:
            self.image = self.image_right
        elif self.previous_x > self.rect.x:
            self.image = self.image_left

        self.previous_x = self.rect.x


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

        self.damage = 1

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 2


class Turtleshell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/turtleshell-nes.png")
        self.image = pygame.transform.scale_by(self.image, 0.05)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

        self.damage = 3

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 2


class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Mushroom.png")
        self.image = pygame.transform.scale_by(self.image, 0.01)
        self.rect = self.image.get_rect()

        self.vel_x = 0
        self.vel_y = 0

        self.heal = 3

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def level_up(self):
        # increase damage
        self.damage *= 2


class HealthBar(pygame.Surface):
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        super().__init__((width, height))

        self.fill(RED)

    def update_info(self, percentage: float):
        """Updates the healthbar with the given percentage"""
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, percentage * self._width, self._height))


def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")

    # Variables
    done = False
    clock = pygame.time.Clock()
    num_enemies = random.choice([1, 2, 3, 4])
    num_allies = 1
    num_blocks = 75
    health_bar = HealthBar(200, 10)
    level = 1

    # Create a Sprite Group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    allies_sprites_group = pygame.sprite.Group()

    # Create Enemies
    for _ in range(num_enemies):
        # Create an enemy
        enemy = Enemy()
        # Randomize movement
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.vel_x, enemy.vel_y = random_x, random_y
        # Start them in the middle
        enemy.rect.center = (WIDTH / 2, HEIGHT / 2)

        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

        enemy = Turtleshell()
        # Randomize movement
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        enemy.vel_x, enemy.vel_y = random_x, random_y
        # Start them in the middle
        enemy.rect.center = (WIDTH / 2, HEIGHT / 2)
        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    # Create 100 blocks
    # Randomly place them throughout the screen
    for _ in range(num_blocks):
        block = BlueBlock(BLUE, 20, 10)
        # Choose a random position for it
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprites_group.add(block)

    for _ in range(num_blocks):
        block = PurpleBlock(PURPLE, 10, 5)
        # Choose a random position for it
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # Create Enemies
    for _ in range(num_allies):
        # Create an enemy
        ally = Mushroom()
        # Randomize movement
        random_x = random.choice([-5, -3, -1, 1, 3, 5])
        random_y = random.choice([-5, -3, -1, 1, 3, 5])
        ally.vel_x, ally.vel_y = random_x, random_y
        # Start them in the middle
        ally.rect.center = (WIDTH / 2, HEIGHT / 2)

        all_sprites_group.add(ally)
        allies_sprites_group.add(ally)

    # Create 100 blocks
    # Randomly place them throughout the screen
    for _ in range(num_blocks):
        block = BlueBlock(BLUE, 20, 10)
        # Choose a random position for it
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)

        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # Create a player
    player = Mario()
    player.rect.center = (WIDTH / 2, HEIGHT / 2)
    # Add the player to the sprite group
    all_sprites_group.add(player)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep enemies in screen
        for enemy in enemy_sprites_group:
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        for ally in allies_sprites_group:
            if ally.rect.left < 0 or ally.rect.right > WIDTH:
                ally.vel_x = -ally.vel_x
            if ally.rect.top < 0 or ally.rect.bottom > HEIGHT:
                ally.vel_y = -ally.vel_y

        # Collision between Player and Blocks
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        # if the blocks_collided list has something in it
        # print Mario has collided with a block!
        for block in blocks_collided:
            if type(block) is BlueBlock:
                print("Player score: ", player.incr_score(block.point_value))
            elif type(block) is PurpleBlock:
                print("Player score: ", player.incr_score(block.point_value))

        # Fill blocks if block list is empty
        # Add more blocks and add one enemy
        if not block_sprites_group:
            level += 1

            for _ in range(num_blocks):
                block = BlueBlock(BLUE, 20, 10)
                # Choose a random position for it
                block.rect.centerx = random.randrange(0, WIDTH)
                block.rect.centery = random.randrange(0, HEIGHT)

                block.level_up(level)

                all_sprites_group.add(block)
                block_sprites_group.add(block)

            for _ in range(num_blocks):
                block = PurpleBlock(PURPLE, 10, 5)
                # Choose a random position for it
                block.rect.centerx = random.randrange(0, WIDTH)
                block.rect.centery = random.randrange(0, HEIGHT)

                block.level_up(level)

                all_sprites_group.add(block)
                block_sprites_group.add(block)

            enemy = Enemy()
            random_x = random.choice([-5, -3, -1, 1, 3, 5])
            random_y = random.choice([-5, -3, -1, 1, 3, 5])
            enemy.vel_x, enemy.vel_y = random_x, random_y
            # Start them in the middle
            enemy.rect.center = (WIDTH / 2, HEIGHT / 2)
            all_sprites_group.add(enemy)
            enemy_sprites_group.add(enemy)

            for enemy in enemy_sprites_group:
                enemy.level_up()

        # Collision between Player and Enemies
        enemies_collided = pygame.sprite.spritecollide(
            player, enemy_sprites_group, False
        )
        for enemy in enemies_collided:
            # decrease mario's life
            player.calc_damage(enemy.damage)

        health_bar.update_info(player.get_damage_percentage())

        allies_collided = pygame.sprite.spritecollide(
            player, allies_sprites_group, False
        )
        for ally in allies_collided:
            # decrease mario's life
            player.calc_heal(ally.heal)

        health_bar.update_info(player.get_damage_percentage())

        # Game ends when Player's health is zero or less
        if player.health <= 0:
            done = True

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        all_sprites_group.draw(screen)
        screen.blit(health_bar, (10, 10))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    # Display final score:
    print("Thanks for playing!")
    print("Final score is:", player.points)

    pygame.quit()


if __name__ == "__main__":
    game()
