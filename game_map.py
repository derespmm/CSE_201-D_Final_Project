try:
    import pygame
except ImportError:
    pygame = None
import threading
from typing import Dict, Set, Tuple
from queue import Queue
import time

class GameMap:
    def __init__(self, screen_width: int = 400, screen_height: int = 400):
        """
        Initialize the GameMap instance with the given screen size.

        This function is responsible for setting up the window, initializing the
        PyGame event loop, and setting the initial state of the game map.

        Parameters
        ----------
        screen_width : int, optional
            The width of the window in pixels. The default is 400.
        screen_height : int, optional
            The height of the window in pixels. The default is 400.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True
        self.update_queue = Queue()
        
        # Colors
        self.BACKGROUND = (196, 164, 132)  # Light brown
        self.UNEXPLORED = (100, 100, 100)  # Dark gray
        self.EXPLORED = (200, 200, 200)    # Light gray
        self.PLAYER = (255, 0, 0)          # Red
        self.WALL = (50, 50, 50)           # Very dark gray
        self.ITEM = (255, 215, 0)          # Gold
        
        # Track explored areas and items for each room
        self.explored_areas: Dict[str, Set[Tuple[int, int]]] = {
            "Cabin": set(),
            "Forest": set(),
            "ufoUnlit": set(),
            "ufoLit": set()
        }
        
        self.items_found: Dict[str, Set[Tuple[int, int]]] = {
            "Cabin": set(),
            "Forest": set(),
            "ufoUnlit": set(),
            "ufoLit": set()
        }
        
        # Room dimensions
        self.room_sizes = {
            "Cabin": 3,
            "Forest": 5,
            "ufoUnlit": 3,
            "ufoLit": 3
        }

        # Start the PyGame thread
        self.thread = threading.Thread(target=self._run_pygame_loop)
        self.thread.daemon = True  # This ensures the thread will close when the main program exits
        self.thread.start()

    def _run_pygame_loop(self):
        """
        Run the PyGame event loop in a separate thread.

        This function initializes PyGame, sets up the window, and enters the
        event loop. It also continuously checks for updates from the main
        thread and applies them to the game map.

        The event loop runs until the window is closed.

        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Unearthed Echoes Map")
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                    
            # Check for updates from the main thread
            while not self.update_queue.empty():
                update_func = self.update_queue.get()
                update_func()
                
            pygame.display.flip()
            time.sleep(0.016)  # Approximately 60 FPS
            
        pygame.quit()

    def mark_explored(self, room_name: str, position: Tuple[int, int]):
        """Mark a position as explored in the specified room"""
        if room_name in self.explored_areas:
            self.explored_areas[room_name].add(position)

    def mark_item_found(self, room_name: str, position: Tuple[int, int]):
        """Mark a position as containing a found item"""
        if room_name in self.items_found:
            self.items_found[room_name].add(position)

    def draw_room(self, room_name: str, player_pos: Tuple[int, int], room_layout: Dict[Tuple[int, int], str]):
        """Queue a room drawing update"""
        def update():
            self.screen.fill(self.BACKGROUND)
            
            room_size = self.room_sizes.get(room_name, 3)
            tile_size = min(self.screen_width, self.screen_height) // (room_size + 2)
            offset_x = (self.screen_width - (tile_size * room_size)) // 2
            offset_y = (self.screen_height - (tile_size * room_size)) // 2
            
            # Draw room grid
            for y in range(room_size):
                for x in range(room_size):
                    rect = pygame.Rect(
                        offset_x + (x * tile_size),
                        offset_y + (y * tile_size),
                        tile_size,
                        tile_size
                    )
                    
                    # Draw base tile
                    if (x, y) in room_layout and room_layout[(x, y)] == "X":
                        pygame.draw.rect(self.screen, self.WALL, rect)
                    elif (x, y) in self.explored_areas[room_name]:
                        pygame.draw.rect(self.screen, self.EXPLORED, rect)
                    else:
                        pygame.draw.rect(self.screen, self.UNEXPLORED, rect)
                    
                    # Draw grid lines
                    pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
                    
                    # Draw items
                    if (x, y) in self.items_found[room_name]:
                        item_size = tile_size // 4
                        item_rect = pygame.Rect(
                            offset_x + (x * tile_size) + (tile_size - item_size) // 2,
                            offset_y + (y * tile_size) + (tile_size - item_size) // 2,
                            item_size,
                            item_size
                        )
                        pygame.draw.rect(self.screen, self.ITEM, item_rect)
            
            # Draw player
            player_rect = pygame.Rect(
                offset_x + (player_pos[0] * tile_size) + (tile_size // 4),
                offset_y + (player_pos[1] * tile_size) + (tile_size // 4),
                tile_size // 2,
                tile_size // 2
            )
            pygame.draw.rect(self.screen, self.PLAYER, player_rect)
            
            # Draw room name
            font = pygame.font.Font(None, 36)
            text = font.render(room_name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.screen_width // 2, offset_y - 30))
            self.screen.blit(text, text_rect)

        self.update_queue.put(update)

    def handle_events(self) -> bool:
        """Check if the map window is still running"""
        return self.running

    def close(self):
        """Clean up the PyGame window"""
        self.running = False
        self.thread.join(timeout=1.0)  # Wait for the thread to finish