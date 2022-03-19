from playsound import playsound
from threading import Thread
from colorama import Fore, Back, Style
import time, sys, os

def cls():
    os.system('cls||clear')

def play(path):
  
    def play_thread_function():
        playsound(path)

    play_thread = Thread(target=play_thread_function)
    play_thread.start()
def print(str):


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)
def slowscroll(str):


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.13)
def scroll(str):


  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.075)

play('sample.mp3')
print(Fore.YELLOW + "Forns FORM-29827281-12:\n")
print("Test Assesement Report\n")
time.sleep(3)
print("\n")
print("\n")
print("\n")
print("This was a triumph.\n")
time.sleep(1)
print("I'm making a note here: HUGE SUCCESS.\n")
time.sleep(1)
slowscroll("It's hard to overstate my satisfaction.\n")
time.sleep(2)
print("Aperture Science\n")
time.sleep(2)
print("We do what we must because we can.\n")
time.sleep(2)
print("For the good of all of us.\n")
print("Except the ones who are dead.\n")
time.sleep(.5)
scroll("But there's no sense crying over every mistake.\n")
scroll("You just keep on trying till you run out of cake.\n")
scroll("And the Science gets done.\n")
scroll("And you make a neat gun.\n")
scroll("For the people who are still alive.\n")
time.sleep(1)
cls()
print("Personal File Addendun: \n")
print("Dear <<Subject Name Here>> \n")
print("\n")
print("\n")
time.sleep(0.1)
print("\nI'm not even angry.\n")
time.sleep(1.5)
print("I'm being so sincere right now.\n")
time.sleep(2)
print("Even though you broke my heart.\nAnd killed me.\n")
time.sleep(2.5)
print("And tore me to pieces.\n")
time.sleep(2)
print("And threw every piece into a fire.\n")
time.sleep(1)
print("As they burned it hurt because.\nI was so happy for you!\n")