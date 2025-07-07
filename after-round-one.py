import os
import time
import random
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_boxes(top_highlight=None, bottom_select=None):
    top = ["[ ]", "[ ]"]
    bottom = ["[ ]", "[ ]"]

    if top_highlight is not None:
        top[top_highlight] = "[■]"

    if bottom_select is not None:
        bottom[bottom_select] = "[■]"

    print("   TOP")
    print("  " + "   ".join(top))
    print("\n  " + "   ".join(bottom))
    print(" BOTTOM")


def flicker_boxes(duration=5):
    message = "AFTER ROUND ONE ORIGINAL PANADOL EXTRA O TUN GBE DE"
    words = message.split()
    start_time = time.time()
    current = 0
    sentence = ""

    word_index = 0
    interval = 0.5  # seconds per word
    total_words = int(duration / interval)

    while time.time() - start_time < duration and word_index < len(words):
        sentence += words[word_index] + " "
        clear_screen()
        draw_boxes(top_highlight=current)
        print("\n\n" + sentence.strip())
        current = 1 - current
        word_index += 1
        time.sleep(interval)

    return random.randint(0, 1)





def get_player_input(timeout=2):
    print("\nPress ← or → to choose the mirrored box!")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if keyboard.is_pressed('left'):
            return 0
        elif keyboard.is_pressed('right'):
            return 1
    return None

def main():
    
    while True:
        clear_screen()
        print("🎮 Mirror Match Game 🎮")
        print("Match the top box with its mirror image below!")
        print("Press any key to start or ESC to quit.")
        if keyboard.read_key() == 'esc':
            break

        # Flicker and settle
        settled = flicker_boxes()
        mirrored = settled

        # Get player input
        player_choice = get_player_input()

        clear_screen()
        draw_boxes(top_highlight=settled, bottom_select=player_choice)

        # Evaluate result
        if player_choice is None:
            print("\n⏰ Time's up! No input detected.")
        elif player_choice == mirrored:
            print("\n✅ Correct! You matched the mirror image."
                   ) 
        else:
            print("\n❌ Wrong! That wasn't the mirror image.")

        print("\nPress 'r' to play again or any other key to exit.")
        if keyboard.read_key() != 'r':
            break

if __name__ == "__main__":
    main()
