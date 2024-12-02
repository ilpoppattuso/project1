#import
import telepot
import os
import shutil
import psutil
import time
import socket
import cv2
import sys
import pyautogui as p
from telepot.loop import MessageLoop
from pynput import keyboard as k
from telepot.namedtuple import ReplyKeyboardMarkup
from mss import mss

#def
def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'
def Id():
    return 000000000 #change numbers with your id there (write '/getid' to @IDBot)
def Username():
    return "YOURUSERNAME" #insert your username there
def botToken():
    return "5000707454:AAFYraFIigO03ARxqXVu9HgGl-XYIqhB5hI" #do NOT change this id

def notifyTelegramPoint():
    bot.sendMessage(Id(), 'Elon Muschioso is ON')

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
    return False

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
        bot.sendMessage(Id(), "Elon Muschioso is ON " + greenSquare())
    else:
        bot.sendMessage(Id(), "Elon Muschioso is OFF " + redSquare())

def shutdownPc():
    os.system('shutdown -s -t 0')


def handle(msg): #what to do if new message is received
    contentType, chatType, chatId = telepot.glance(msg)
    text = msg['text'].upper()
    if not (chatId == 000000000): #change the numbers with your id
        bot.sendMessage(chatId, "You aren't my boss: I can't feel the force.")
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
    elif (text == '/START'):
        bot.sendMessage(Id(), "Welcome back boss", reply_markup=keyboard)
    elif(text == 'ELON OFF'or text == 'OFF'):
        bot.sendMessage(Id(), "Have a good day")
        shutdownPc()
    else:
        bot.sendMessage(Id(), "I don't understand...", reply_markup=keyboard)

waitForInternetConnection()
bot = telepot.Bot(botToken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['U', 'OFF'], ['KP', 'KA']])
bot.sendMessage(Id(), 'Elon Muschioso is ON', reply_markup=keyboard)
while 1:
    time.sleep(1)