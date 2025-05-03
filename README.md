# Discord Rich Presence in Python

A simple Python script to display custom Discord Rich Presence (RPC) using the `pypresence` library. This allows you to showcase your activity on Discord with custom details, images, and buttons.

---

## Features
- **Customizable Presence**: Set your own state, details, and images.
- **Interactive Buttons**: Add up to two buttons with custom labels and URLs.
- **Persistent Configuration**: Save your settings in `config.json` for future use.
- **User-Friendly**: Input prompts guide you through setup.

---

## Prerequisites
- Python 3.6 or higher
- A Discord application (to get the `CLIENT_ID`)

---

## Installation
1. Clone this repository.
2. Install the required dependency:
   ```bash
   pip install pypresence
   ```

---

## Usage
1. **First Run**:
   - Execute the script:
     ```bash
     python customrpc.py
     ```
   - Follow the prompts to enter your Discord Rich Presence details. These will be saved in `config.json`.

2. **Subsequent Runs**:
   - The script will automatically load your saved configuration from `config.json`.
   - To modify your settings, delete `config.json` and run the script again.

3. **Stopping the Script**:
   - Press `Ctrl+C` in the terminal to stop the Rich Presence.

---

## Configuration
The `config.json` file stores your settings. Here's an example:
```json
{
    "CLIENT_ID": "Your_Client_ID",
    "STATE": "Your_State",
    "DETAILS": "Your_Details",
    "LARGE_IMAGE_NAME": "large_image_name",
    "LARGE_IMAGE_TEXT": "large_image_text",
    "SMALL_IMAGE_NAME": "small_image_name",
    "SMALL_IMAGE_TEXT": "small_image_text",
    "BUTTONS": [
        {
            "label": "Button_1",
            "url": "https://example1.com"
        },
        {
            "label": "Button_2",
            "url": "https://example2.com"
        }
    ]
}
```

### Notes:
- **`CLIENT_ID`**: Obtain this from the [Discord Developer Portal](https://discord.com/developers/applications).
- **Images**: Upload your images in the "Rich Presence" tab of your Discord application and use their names here.

---

## Troubleshooting
- **Invalid ID Error**: Ensure your `CLIENT_ID` is correct and your Discord app is properly configured.
- **Connection Issues**: Make sure Discord is running and you're logged in.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Support
For issues or feature requests, please [open an issue](https://github.com/your-repo/issues).