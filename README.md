# Project1

**Elon** is a Telegram-based bot designed to perform a variety of remote control operations on a computer. The bot provides advanced features such as keylogging, process management, screenshot capturing, camera control, and more.

## Features

- **Keylogger**: Logs keypresses and sends the data via Telegram.
- **Process Management**: Starts, closes, or terminates specific programs (e.g., Telegram, Chrome, or Brave).
- **Screenshot**: Captures screenshots of the computer.
- **Camera Control**: Takes pictures using the webcam.
- **Remote Shutdown**: Shuts down the computer remotely.
- **Integrated Chatbot**: Responds to messages using a natural language processing model.

## Requirements

- **Python Libraries**:
  - `telepot`
  - `psutil`
  - `requests`
  - `cv2` (OpenCV)
  - `pynput`
  - `mss`
  - `transformers`
  - `pyautogui`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ilpoppattuso/project1.git
   ```
2. Install dependencies

3. Configure the bot:
   - Edit the `main.py` file with your Telegram credentials (`Id`, and `Username`).

## Usage

1. Start the bot:
   ```bash
   python main.py
   ```
2. Use Telegram to send commands such as:
   - **`KEY`**: Start the keylogger.
   - **`SCREEN`**: Capture a screenshot.
   - **`CAMERA`**: Take a photo with the webcam.
   - **`U`**: Update the bot's status.
   - **`OFF`**: Shut down the computer.

## Disclaimer

This project is for educational purposes only. Use this project only to manage your own pc. Using this bot for unauthorized or illegal activities is strictly prohibited. The author is not responsible for any damages or violations caused by the use of this software.

## Contributions

Contributions and improvements are welcome. Feel free to open a pull request or report issues via the Issues tab.
