import time
import datetime
import calendar
import pprint

def main():
    
    timeOfDay=input("Time of Day: ")
    creature=input("Type of Animal: ")
    noun=input("Noun: ")
    emotion=input("Emotion: ")
    
    story1=str("One "+timeOfDay+", a sad-looking "+creature+" stumbled upon an ancient city. Soon after, the "+creature+" happened upon a "+noun+" which gave rise to a sense of "+emotion)
    print(story1)
    input()

main()
