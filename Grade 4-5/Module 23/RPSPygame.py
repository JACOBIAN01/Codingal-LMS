import pygame
import random

pygame.init()

# Screen settings
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock, Paper, Scissors")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Game loop
running = True
while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            user_choice = ""
            if event.key == pygame.K_r:
                user_choice = "Rock"
            elif event.key == pygame.K_p:
                user_choice = "Paper"
            elif event.key == pygame.K_s:
                user_choice = "Scissors"
            
            if user_choice:
                computer_choice = random.choice(choices)
                result = "It's a Tie!"
                if (user_choice == "Rock" and computer_choice == "Scissors") or \
                   (user_choice == "Paper" and computer_choice == "Rock") or \
                   (user_choice == "Scissors" and computer_choice == "Paper"):
                    result = "You Win!"
                elif user_choice != computer_choice:
                    result = "You Lose!"
                
                # Display result
                screen.fill(white)
                user_text = font.render(f"You: {user_choice}", True, black)
                comp_text = font.render(f"Computer: {computer_choice}", True, black)
                result_text = font.render(result, True, black)
                screen.blit(user_text, (20, 100))
                screen.blit(comp_text, (20, 150))
                screen.blit(result_text, (20, 200))
                pygame.display.flip()
                pygame.time.delay(2000)
    
    pygame.display.update()

pygame.quit()
