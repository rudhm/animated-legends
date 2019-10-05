import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

frames = [
    """
       \o/
        |
       / \\
    Legendary!
    """,
    """
        o/
       /|
       / \\
    Legendary!
    """,
    """
       \o
        |\\
       / \\
    Legendary!
    """
]

try:
    clear_screen()
    print("Summoning the legend... (Press Ctrl+C to stop)")
    time.sleep(1)
    
    while True:
        for frame in frames:
            clear_screen()
            print(frame)
            time.sleep(0.4)
except KeyboardInterrupt:
    clear_screen()
    print("\nLegend gone to sleep. Goodbye!\n")
