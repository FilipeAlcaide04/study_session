""" Simple shooting game for 2 people :)"""
import random as r
import time
import os

class Player:
    """ Creates the player for the mini-game"""

    def __init__(self, name, health=1000, ammo=10):
        """ Class Constructor"""
        self.name = name
        self.health = health
        self.ammo = ammo

    def player_info(self):
        """ Displays the entire player info"""
        print(f"\nPlayer: {self.name}")
        self.display_health()
        self.display_ammo()

    def display_ammo(self):
        """ Displays the ammo available"""
        if self.ammo == 0:
            ammo = "Ammo:   ◌ ◌ ◌ ◌ ◌ ◌ ◌ ◌ ◌ ◌"
        else:
            ammo = "Ammo:  "
            ammo += " ●" * self.ammo
            ammo += " ◌" * (10 - self.ammo)
        print(ammo)

    def display_health(self):
        """Displays the health available."""
        if self.health == 0:
            health = "Health: ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡"
        else:
            health = "Health:"
            health += " ♥" * (self.health // 100)
            health += " ♡" * ((1000 - self.health) // 100)
        print(health)

    def shoot(self, opponent):
        """Shoot at the opponent."""
        if self.ammo <= 0:
            print(f"{self.name} has no ammo left!")
            return

        damage = r.choice([0, 0, 0 ,0 , 0, 0, 100, 100, 100, 100, 100, 200, 300, 400, -1])
        self.ammo -= 1

        if damage == 0:
            print(f"{self.name} missed the shot!")
        elif damage == -1:
            print(f"{self.name}'s gun jammed and did not fire!")
        else:
            opponent.health = max(opponent.health - damage, 0)
            print(f"{self.name} hit {opponent.name} for {damage} damage!")

    def heal(self):
        """Heal the player with random amount, including zero."""
        healing_amount = r.choice([0, 0, 0 ,0 , 0, 0, 100, 100, 100, 100, 100, 200])
        self.health = min(self.health + healing_amount, 1000)  # Health cannot exceed 1000
        if healing_amount == 0:
            print(f"{self.name} tried to heal but gained no health!")
        else:
            print(f"{self.name} healed for {healing_amount} health!")

# Function to clear the screen based on OS
def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # If the OS is Windows
        os.system("cls")
    else:  # If the OS is Linux or macOS
        os.system("clear")

# Create two players
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")

clear_screen()  # Clear the screen initially

player1 = Player(player1_name)
player2 = Player(player2_name)

# Game loop
Turn = 0
while player1.health > 0 and player2.health > 0 and (player1.ammo > 0 or player2.ammo > 0):
    # Always show both players' stats
    print("\n----- CURRENT STATS -----")
    player1.player_info()
    player2.player_info()

    # Player's turn
    if Turn % 2 == 0:
        print(f"\n{player1.name}'s Turn:")
        action = input("Do you want to shoot (1) or heal (0)? ").strip()
        
        if action == "1":
            player1.shoot(player2)
        elif action == "0":
            player1.heal()
        else:
            os.system("Clear")
            print("Invalid choice, please type '1' to shoot or '0' to heal.")
            continue  # Restart the loop for a valid input

    else:
        print(f"\n{player2.name}'s Turn:")
        action = input("Do you want to shoot (1) or heal (0)? ").strip()
        
        if action == "1":
            player2.shoot(player1)
        elif action == "0":
            player2.heal()
        else:
            os.system("Clear")
            print("Invalid choice, please type '1' to shoot or '0' to heal.")
            continue  # Restart the loop for a valid input

    time.sleep(2)  # Pause for 2 seconds before clearing the screen
    clear_screen()  # Clear the screen after every turn
    Turn += 1

# Game Over
print("\n----- GAME OVER -----")
if player1.health <= 0 and player2.health <= 0:
    print("Both players are down! It's a draw!")
elif player1.health <= 0:
    print(f"{player2.name} wins!")
elif player2.health <= 0:
    print(f"{player1.name} wins!")
else:
    # Health is still > 0, but both out of ammo
    if player1.health > player2.health:
        print(f"{player1.name} wins by having more health!")
    elif player2.health > player1.health:
        print(f"{player2.name} wins by having more health!")
    else:
        print("It's a draw based on equal health!")
