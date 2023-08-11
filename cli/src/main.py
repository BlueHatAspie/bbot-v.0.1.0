from command_processors import text_command_processor
from mCookingPy import mCookingPy__onload
from time import sleep


def main():
    print("Hello, I am B-bot, your personal virtual assistant. How may I help you today?")
    while True:
        user_input = input("Enter a command: ")
        text_command_processor(user_input)


if __name__ == "__main__":
    mCookingPy__onload() # Automatically sends the dinner list if it has not already been sent
    
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram Terminated. Goodbye.\n")
        sleep(2)