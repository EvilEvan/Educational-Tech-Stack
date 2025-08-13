"""
Exercise 3: Text-Based Adventure Game
Module: Programming Fundamentals - Final Project

Description:
Create an interactive text-based adventure game that demonstrates
all the programming concepts learned in Module 1. This is the
capstone project for the Programming Fundamentals module.

Learning Objectives:
- Integrate variables, conditionals, loops, and functions
- Implement game logic and state management
- Practice user input validation and error handling
- Create an engaging user experience
- Apply code organization and documentation principles

Game Requirements:
1. Player has health, inventory, and location tracking
2. Multiple rooms/locations to explore
3. Items to collect and use
4. Challenges or puzzles to solve
5. Win/lose conditions
6. Save/load game functionality (optional)

Extension Ideas:
- Combat system with enemies
- Shop system for buying/selling items
- Character stats and leveling
- Multiple story paths and endings
- ASCII art for locations and items
"""

import random
import json
import os

class AdventureGame:
    """Main game class that manages the adventure game state and logic."""
    
    def __init__(self):
        """Initialize the game with default values."""
        self.player = {
            "name": "",
            "health": 100,
            "max_health": 100,
            "inventory": [],
            "location": "forest_entrance",
            "score": 0
        }
        
        # TODO: Define game locations, items, and story
        self.locations = {
            # Example structure - students should expand this
            "forest_entrance": {
                "name": "Forest Entrance",
                "description": "You stand at the entrance to a mysterious forest...",
                "exits": {"north": "deep_forest", "east": "cave_entrance"},
                "items": ["torch"],
                "visited": False
            }
            # Add more locations here
        }
        
        self.items = {
            # Example structure
            "torch": {
                "name": "Torch",
                "description": "A wooden torch that provides light",
                "usable": True
            }
            # Add more items here
        }
        
        self.game_running = True

    def start_game(self):
        """Start the adventure game."""
        print("=" * 50)
        print("🌟 WELCOME TO THE MYSTICAL FOREST ADVENTURE 🌟")
        print("=" * 50)
        
        # Get player name
        self.player["name"] = input("\nWhat is your name, brave adventurer? ").strip()
        if not self.player["name"]:
            self.player["name"] = "Anonymous Hero"
        
        print(f"\nWelcome, {self.player['name']}!")
        print("Type 'help' at any time to see available commands.")
        print("Your adventure begins...\n")
        
        # Main game loop
        while self.game_running:
            self.display_location()
            self.process_command()

    def display_location(self):
        """Display current location information."""
        current_loc = self.locations[self.player["location"]]
        
        print(f"\n📍 {current_loc['name']}")
        print("-" * len(current_loc['name']))
        print(current_loc['description'])
        
        # Show items in location
        if current_loc.get('items'):
            print(f"\nYou see: {', '.join(current_loc['items'])}")
        
        # Show available exits
        exits = list(current_loc['exits'].keys())
        if exits:
            print(f"Exits: {', '.join(exits)}")

    def process_command(self):
        """Process user input and execute commands."""
        command = input(f"\n[Health: {self.player['health']}] What do you do? ").lower().strip()
        
        if not command:
            print("Please enter a command. Type 'help' for assistance.")
            return
        
        # Parse command
        parts = command.split()
        action = parts[0]
        target = parts[1] if len(parts) > 1 else ""
        
        # TODO: Implement command processing
        if action == "help":
            self.show_help()
        elif action in ["go", "move", "walk"]:
            self.move_player(target)
        elif action in ["take", "get", "pick"]:
            self.take_item(target)
        elif action in ["use"]:
            self.use_item(target)
        elif action in ["inventory", "inv", "i"]:
            self.show_inventory()
        elif action in ["look", "examine"]:
            self.examine(target)
        elif action in ["quit", "exit", "q"]:
            self.quit_game()
        else:
            print("I don't understand that command. Type 'help' for available commands.")

    def show_help(self):
        """Display available commands."""
        print("\n=== AVAILABLE COMMANDS ===")
        print("Movement: go [direction] - move to another location")
        print("Items: take [item] - pick up an item")
        print("      use [item] - use an item from your inventory")
        print("Info: inventory - show your items")
        print("      look [item/location] - examine something")
        print("      help - show this help message")
        print("Game: quit - exit the game")

    def move_player(self, direction):
        """Move player to a new location."""
        # TODO: Implement movement logic
        current_loc = self.locations[self.player["location"]]
        
        if not direction:
            print("Go where? Specify a direction.")
            return
        
        if direction in current_loc.get("exits", {}):
            new_location = current_loc["exits"][direction]
            self.player["location"] = new_location
            print(f"You move {direction}...")
            
            # Mark location as visited
            self.locations[new_location]["visited"] = True
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        """Take an item from the current location."""
        # TODO: Implement item taking logic
        if not item_name:
            print("Take what?")
            return
        
        current_loc = self.locations[self.player["location"]]
        
        if item_name in current_loc.get("items", []):
            # Remove from location, add to inventory
            current_loc["items"].remove(item_name)
            self.player["inventory"].append(item_name)
            
            item_info = self.items.get(item_name, {})
            print(f"You take the {item_info.get('name', item_name)}.")
        else:
            print("There's no such item here.")

    def use_item(self, item_name):
        """Use an item from inventory."""
        # TODO: Implement item usage logic
        if not item_name:
            print("Use what?")
            return
        
        if item_name not in self.player["inventory"]:
            print("You don't have that item.")
            return
        
        # Example item usage
        if item_name == "torch":
            print("The torch illuminates the area, revealing hidden details...")
            # Add special effects based on current location
        else:
            print(f"You can't use the {item_name} right now.")

    def show_inventory(self):
        """Display player's inventory."""
        print(f"\n🎒 {self.player['name']}'s Inventory:")
        if self.player["inventory"]:
            for item in self.player["inventory"]:
                item_info = self.items.get(item, {})
                print(f"  - {item_info.get('name', item)}")
        else:
            print("  Your inventory is empty.")

    def examine(self, target):
        """Examine an item or location."""
        # TODO: Implement examination logic
        if not target:
            # Re-display current location
            self.display_location()
            return
        
        # Check if it's an item in inventory or location
        if target in self.player["inventory"]:
            item_info = self.items.get(target, {})
            print(f"🔍 {item_info.get('description', 'A mysterious object.')}")
        else:
            print("You don't see that here.")

    def quit_game(self):
        """Exit the game."""
        print(f"\nThanks for playing, {self.player['name']}!")
        print(f"Final Score: {self.player['score']}")
        print("Your adventure ends here... for now.")
        self.game_running = False

    def save_game(self):
        """Save game state to a file (optional feature)."""
        # TODO: Implement save functionality
        pass

    def load_game(self):
        """Load game state from a file (optional feature)."""
        # TODO: Implement load functionality
        pass

def main():
    """Main function to start the adventure game."""
    try:
        game = AdventureGame()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("The game will now exit.")

if __name__ == "__main__":
    main()

# TODO: Student Implementation Tasks
"""
1. Expand the locations dictionary with at least 5 interconnected rooms
2. Add more items with different properties and uses
3. Implement a simple combat system (optional)
4. Add puzzles or challenges to solve
5. Create win/lose conditions
6. Add more interactive elements (NPCs, shops, etc.)
7. Implement save/load functionality
8. Add ASCII art for enhanced visual appeal
9. Create multiple story paths and endings
10. Add comprehensive error handling and input validation

Example Extended Features:
- Health system with healing items
- Key/door mechanics
- Hidden locations that require specific items
- Random events and encounters
- Character progression and stats
- Multiple difficulty levels
"""
