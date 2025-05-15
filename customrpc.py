from pypresence import Presence, InvalidID
import time
import json
import os

def get_user_input():
    print("Enter Discord Rich Presence details:")
    while True:
        try:
            client_id = input("Discord Application ID (CLIENT_ID): ").strip()
            if client_id:
                break
            print("Application ID cannot be empty!")
        except KeyboardInterrupt:
            print("\nCancelled entry. Closing the program...")
            exit(1)

    state = input("State (STATE): ").strip() or "No state"
    details = input("Details (DETAILS): ").strip() or "No details"
    large_image = input("Large image name (LARGE_IMAGE_NAME): ").strip() or "large_image"
    large_text = input("Large image hover text (LARGE_IMAGE_TEXT): ").strip() or "Large image"
    small_image = input("Small image name (SMALL_IMAGE_NAME): ").strip() or "small_image"
    small_text = input("Small image hover text (SMALL_IMAGE_TEXT): ").strip() or "Small image"
    button1_label = input("First button label (BUTTON1_LABEL): ").strip() or "Button 1"
    button1_url = input("First button URL (BUTTON1_URL): ").strip() or "https://example.com"
    button2_label = input("Second button label (BUTTON2_LABEL): ").strip() or "Button 2"
    button2_url = input("Second button URL (BUTTON2_URL): ").strip() or "https://example.com"

    config = {
        "CLIENT_ID": client_id,
        "STATE": state,
        "DETAILS": details,
        "LARGE_IMAGE_NAME": large_image,
        "LARGE_IMAGE_TEXT": large_text,
        "SMALL_IMAGE_NAME": small_image,
        "SMALL_IMAGE_TEXT": small_text,
        "BUTTONS": [
            {"label": button1_label, "url": button1_url},
            {"label": button2_label, "url": button2_url}
        ]
    }

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    return config

def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return None

def main():
    config = load_config()

    if not config:
        config = get_user_input()

    while True:
        try:
            print(f"Attempting to connect with CLIENT_ID: {config['CLIENT_ID']}")
            RPC = Presence(config["CLIENT_ID"])
            RPC.connect()
            print("Connected to Discord RPC!")
            break
        except InvalidID:
            print("Error: Invalid Discord Application ID. Please check the ID.")
            config = get_user_input()
        except Exception as e:
            print(f"Unexpected error: {e}")
            return

    RPC.update(
        state=config["STATE"],
        details=config["DETAILS"],
        large_image=config["LARGE_IMAGE_NAME"],
        large_text=config["LARGE_IMAGE_TEXT"],
        small_image=config["SMALL_IMAGE_NAME"],
        small_text=config["SMALL_IMAGE_TEXT"],
        start=time.time(),
        buttons=config["BUTTONS"]
    )

    print("Custom RPC is running! Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nClosing CustomRPC...")
        RPC.close()

if __name__ == "__main__":
    main()