from pypresence import Presence
import time

# ID of your Discord application (you can create in Discord Developer Portal)
CLIENT_ID = 'Your_Client_ID'

# RPC initialization
RPC = Presence(CLIENT_ID)
RPC.connect()

# Data to be displayed in RPC
RPC.update(
    state="STATE",  # Stan
    details="DETAILS",  # Szczegóły
    large_image="LARGE_IMAGE_NAME",  # The name of the large image (registered in Discord Dev Portal)
    large_text="LARGE_IMAGE_TEXT",  # Text after hovering over a large image
    small_image="SMALL_IMAGE_NAME",  # Name of the small image (registered in Discord Dev Portal)
    small_text="SMALL_IMAGE_TEXT",  # Text after hovering over a small image
    start=time.time(),  # Czas rozpoczęcia (from when you started this script)
    buttons=[{"label": "Anything", "url": "YOUR_URL"}, {"label": "Anything", "url": "YOUR_URL"}]  # Buttons
)

print("Custom RPC is working! Click Ctrl+C to stop it.")

try:
    while True:
        time.sleep(15)  # RPC works as long as the program is running
except KeyboardInterrupt:
    print("\nClosing CustomRPC...")
    RPC.close()