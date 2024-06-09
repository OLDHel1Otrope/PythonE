import pygame
import random
import sys

from PIL import Image, ImageDraw, ImageFont

def is_black_or_white(img, x, y):
    grayscale_img = img.convert("L")
    pixel_value = grayscale_img.getpixel((x%1900, y%1080))
    if pixel_value == 0:
        return True
    else: return False


def drawImage(text):
    width, height = 1920, 1080
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 544)
    except IOError:
        font = ImageFont.load_default()

    text_width, text_height = 1000,1000
    font1 = ImageFont.truetype("arial.ttf",size=500)
    draw.text((200, 300), text, fill="black", font=font1)
    image_path = "hello_world_image.png"
    image.save(image_path)
    return image


image=drawImage("name")
def checkFlowers(i,j):
    if(is_black_or_white(image,i,j)):
        flowers.append((i,j,True))
    else: flowers.append((i,j,False))

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
pygame.display.set_caption("Flower Shower")

# Colors
black = (0,0,0)
green = (0, 255, 0)
red = (255, 0, 0)

# Flower settings
flower_colors = [(255, 0, 255),(55, 40, 25),(90, 80, 75),(155, 10, 95)]
flower2=(255,255,255)
flower_radius = 10
flowers = []

# Button settings
button_color = green
button_hover_color = (0, 200, 0)
button_rect = pygame.Rect(350, 250, 100, 50)

# Function to draw the button
def draw_button(screen, rect, color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Shower", True, black)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

# Main game loop
running = True
while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Shower flowers
                for _ in range(500):
                    flower_x = random.randint(0, width)
                    flower_y = random.randint(0, height)
                    # flowers.append((flower_x, flower_y))
                    checkFlowers(flower_x, flower_y)

    # Draw flowers
    for flower in flowers:
        pygame.draw.circle(screen, flower2 if flower[2] else random.choice(flower_colors), (flower[0],flower[1]), 15 if flower[2] else 7)

    # Draw button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        draw_button(screen, button_rect, button_hover_color)
    else:
        draw_button(screen, button_rect, button_color)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()
