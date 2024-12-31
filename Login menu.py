def loading_screen(duration=5):
    print("Loading **", end="")
    for _ in range(duration):  # Multiply by 10 for finer control
        for _ in range(100000000):    # Simple delay without libraries
            pass
        print("***", end="")
    print("\nDone!")

# Run the loading screen
loading_screen()