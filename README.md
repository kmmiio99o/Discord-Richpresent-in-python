# 🎮 Discord Rich Presence in Python

A simple and customizable Python script to display your own **Discord Rich Presence (RPC)** using the `pypresence` library. Show off your activity with custom details, images, and interactive buttons!

---

## ✨ Features
- **🎨 Customizable Presence**: Set your own `state`, `details`, and images.
- **🔘 Interactive Buttons**: Add up to two buttons with custom labels and URLs.
- **💾 Persistent Configuration**: Save your settings in `config.json` for future use.
- **👤 User-Friendly**: Guided input prompts make setup a breeze.

---

## 📋 Prerequisites
Before you begin, ensure you have the following:

- **🐍 Python 3.6 or higher**:
  - **Windows**: Download from [Python's official site](https://www.python.org/downloads/windows/).
  - **macOS**: Install via [Homebrew](https://brew.sh/) (`brew install python`) or [python.org](https://www.python.org/downloads/macos/).
  - **Linux**:
    - Debian/Ubuntu: `sudo apt update && sudo apt install python3`
    - Arch Linux: `sudo pacman -S python`
    - Fedora: `sudo dnf install python3`
- **📱 Discord Application**: Create an app in the [Discord Developer Portal](https://discord.com/developers/applications) and copy the `CLIENT_ID`.
- **🖥️ Discord Desktop**: Make sure Discord is running on your computer.

---

## 🛠️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/Discord-RichPresence-in-python.git
   cd Discord-RichPresence-in-python
   ```

2. **Install dependencies**:
   - Required library: `pypresence`.
   - **Windows/macOS/Linux**:
     ```bash
     pip install pypresence
     ```
   - **Linux (alternative)**:
     - If `pip` is not installed:
       ```bash
       sudo apt install python3-pip  # Debian/Ubuntu
       sudo dnf install python3-pip  # Fedora
       sudo pacman -S python-pip     # Arch Linux
       ```
     - Upgrade `pip`:
       ```bash
       pip install --upgrade pip
       ```

3. **Run the script**:
   ```bash
   python customrpc.py
   ```

---

## 🚀 Usage
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

## ⚙️ Configuration
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

### 📌 Notes:
- **There is error in terminal that I can't repair, but you don't need to care about it.**
- **`CLIENT_ID`**: Obtain this from the [Discord Developer Portal](https://discord.com/developers/applications).
- **Images**: Upload your images in the "Rich Presence" tab of your Discord application and use their names here.

---

## 🔧 Troubleshooting
- **❌ Invalid ID Error**: Ensure your `CLIENT_ID` is correct and your Discord app is properly configured.
- **🔌 Connection Issues**: Make sure Discord is running and you're logged in.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 💬 Support
For issues or feature requests, please [open an issue](https://github.com/your-repo/issues).  
Feel free to contribute or suggest improvements! 🚀