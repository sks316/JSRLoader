import urllib.request
import requests
import re
import xml.etree.ElementTree as ET
import json
import os
from os import system, name

#--Set app version--#
appver = "JSRLoader v1.2.0 by PrincessLillie"
appverTV = "JSRLoader v1.2.0 by PrincessLillie - JSRLTV downloader"

#--Function for clearing the screen--#
def clearScreen():
  #--Check if OS is Windows--#
  if name == 'nt':
     _ = system('cls')
  else:
     _ = system('clear')

def classicDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/classic/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Classic")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "classic";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Classic/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/classic/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Classic"):
              os.makedirs("Downloaded music/Classic")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Classic/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Classic")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def futureDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/future/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Future")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "future";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Future/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/future/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Future"):
              os.makedirs("Downloaded music/Future")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Future/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Future")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()


def ggsDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/ggs/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: GG's")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "ggs";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/GG's/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/ggs/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/GG's"):
              os.makedirs("Downloaded music/GG's")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/GG's/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: GG's")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def bumpsDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/bumps/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Bumps")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("bumpsArray[bumpsArray.length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Bumps/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/bumps/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Bumps"):
              os.makedirs("Downloaded music/Bumps")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Bumps/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Bumps")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def poisonJamDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/poisonjam/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Poison Jam")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "poisonjam";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Poison Jam/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/poisonjam/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Poison Jam"):
              os.makedirs("Downloaded music/Poison Jam")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Poison Jam/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Poison Jam")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def noiseTanksDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/noisetanks/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Noise Tanks")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "noisetanks";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Noise Tanks/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/noisetanks/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Noise Tanks"):
              os.makedirs("Downloaded music/Noise Tanks")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Noise Tanks/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Noise Tanks")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def loveShockersDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/loveshockers/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Love Shockers")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "loveshockers";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Love Shockers/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/loveshockers/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Love Shockers"):
              os.makedirs("Downloaded music/Love Shockers")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Love Shockers/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Love Shockers")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def rapid99DL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/rapid99/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Rapid 99")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "rapid99";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Rapid 99/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/rapid99/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Rapid 99"):
              os.makedirs("Downloaded music/Rapid 99")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Rapid 99/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Rapid 99")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def immortalsDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/immortals/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: The Immortals")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "immortals";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/The Immortals/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/immortals/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/The Immortals"):
              os.makedirs("Downloaded music/The Immortals")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/The Immortals/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: The Immortals")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def doomRidersDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/doomriders/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Doom Riders")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "doomriders";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Doom Riders/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/doomriders/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Doom Riders"):
              os.makedirs("Downloaded music/Doom Riders")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Doom Riders/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Doom Riders")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def goldenRhinosDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/goldenrhinos/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Golden Rhinos")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "goldenrhinos";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Golden Rhinos/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/goldenrhinos/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Golden Rhinos"):
              os.makedirs("Downloaded music/Golden Rhinos")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Golden Rhinos/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Golden Rhinos")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def summerDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/summer/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Summer")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace('if(systemMonth == "June" || systemMonth == "July" || systemMonth == "August"){', '')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "summer";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace("}", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Summer/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/summer/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Summer"):
              os.makedirs("Downloaded music/Summer")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Summer/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Summer")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def christmasDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/christmas/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Christmas")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace('if(systemMonth == "December" && systemDay < 27){', '')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "christmas";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace("}", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Christmas/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/christmas/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Christmas"):
              os.makedirs("Downloaded music/Christmas")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Christmas/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Christmas")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def halloweenDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/halloween/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Halloween")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace('if(systemMonth == "October"){', '')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "halloween";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace("}", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Halloween/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/halloween/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Halloween"):
              os.makedirs("Downloaded music/Halloween")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Halloween/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Halloween")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def memoriesOfTokyoToDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradiofuture.live/radio/stations/memoriesoftokyoto/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Memories of Tokyo-To")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by 2 Mello. Please support their music! https://2mellomakes.bandcamp.com/")
  print("This station was removed from JSRL, and is instead being downloaded from a clone server at jetsetradiofuture.live.")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "memoriesoftokyoto";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Memories of Tokyo-To/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradiofuture.live/radio/stations/memoriesoftokyoto/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Memories of Tokyo-To"):
              os.makedirs("Downloaded music/Memories of Tokyo-To")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Memories of Tokyo-To/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Memories of Tokyo-To")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def ultraRemixesDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/ultraremixes/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Ultra Remixes")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "ultraremixes";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Ultra Remixes/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/ultraremixes/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Ultra Remixes"):
              os.makedirs("Downloaded music/Ultra Remixes")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Ultra Remixes/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Ultra Remixes")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def kfadDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradiofuture.live/radio/stations/siivagunner/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: King for Another Day")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by contributors to SiIvaGunner. Please support their music! https://gilvasunner.bandcamp.com/")
  print("This station was removed from JSRL, and is instead being downloaded from a clone server at jetsetradiofuture.live.")
  print("-------------------------------------")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "siivagunner";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/King for Another Day/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradiofuture.live/radio/stations/siivagunner/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/King for Another Day"):
              os.makedirs("Downloaded music/King for Another Day")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/King for Another Day/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: King for Another Day")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def lofiDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/lofi/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Lo-Fi")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "lofi";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Lo-Fi/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/lofi/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Lo-Fi"):
              os.makedirs("Downloaded music/Lo-Fi")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Lo-Fi/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Lo-Fi")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()


def elaquentDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradiofuture.live/radio/stations/elaquent/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Forever Is A Pretty Long Time")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by Elaquent. Please support their music! https://elaquent-mello-catalog.bandcamp.com/")
  print("This station was removed from JSRL, and is instead being downloaded from a clone server at jetsetradiofuture.live.")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "elaquent";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Forever Is A Pretty Long Time/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradiofuture.live/radio/stations/elaquent/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Forever Is A Pretty Long Time"):
              os.makedirs("Downloaded music/Forever Is A Pretty Long Time")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Forever Is A Pretty Long Time/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Forever Is A Pretty Long Time")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()



def olliekingDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/ollieking/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Ollie King")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "ollieking";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Ollie King/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/ollieking/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Ollie King"):
              os.makedirs("Downloaded music/Ollie King")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Ollie King/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Ollie King")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()


def toejamDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/toejamandearl/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Toe Jam & Earl")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station are from the game ToeJam & Earl: Back in the Groove! Please support the original product!")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "toejamandearl";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Toe Jam & Earl/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/toejamandearl/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Toe Jam & Earl"):
              os.makedirs("Downloaded music/Toe Jam & Earl")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Toe Jam & Earl/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Toe Jam & Earl")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def crazyTaxiDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/crazytaxi/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Crazy Taxi")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station are from the game Crazy Taxi. Please support the original product!")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "crazytaxi";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Crazy Taxi/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/crazytaxi/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Crazy Taxi"):
              os.makedirs("Downloaded music/Crazy Taxi")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Crazy Taxi/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Crazy Taxi")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()


def hoverDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/hover/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Hover")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station are from the game Hover. Please support the original product!")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "hover";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Hover/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/hover/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Hover"):
              os.makedirs("Downloaded music/Hover")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Hover/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Hover")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def butterfliesDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/butterflies/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Butterflies")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station are from the fangame Butterflies. Please support the original product! http://bit.ly/2TbMM6e")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "butterflies";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Butterflies/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/butterflies/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Butterflies"):
              os.makedirs("Downloaded music/Butterflies")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Butterflies/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Butterflies")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def revolutionDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/revolution/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Revolution")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "revolution";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Revolution/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/revolution/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Revolution"):
              os.makedirs("Downloaded music/Revolution")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Revolution/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Revolution")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def endOfDaysDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/endofdays/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: End of Days")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "endofdays";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/End of Days/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/endofdays/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/End of Days"):
              os.makedirs("Downloaded music/End of Days")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/End of Days/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: End of Days")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def garageDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/garage/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: The Garage")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "garage";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/The Garage/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/garage/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/The Garage"):
              os.makedirs("Downloaded music/The Garage")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/The Garage/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: The Garage")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def spaceDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/outerspace/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Outer Space")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "outerspace";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Outer Space/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/outerspace/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Outer Space"):
              os.makedirs("Downloaded music/Outer Space")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Outer Space/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Outer Space")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def ganjahDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/ganjah/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Ganjah")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "ganjah";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Ganjah/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/ganjah/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Ganjah"):
              os.makedirs("Downloaded music/Ganjah")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Ganjah/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Ganjah")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def chiptunesDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/chiptunes/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Chiptunes")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "chiptunes";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Chiptunes/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/chiptunes/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Chiptunes"):
              os.makedirs("Downloaded music/Chiptunes")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Chiptunes/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Chiptunes")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def retroRemixDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/retroremix/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Retro Remix")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "retroremix";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Retro Remix/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/retroremix/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Retro Remix"):
              os.makedirs("Downloaded music/Retro Remix")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Retro Remix/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Retro Remix")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def classicalRemixDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/classical/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: Classical Remix")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "classical";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/Classical Remix/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/classical/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/Classical Remix"):
              os.makedirs("Downloaded music/Classical Remix")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/Classical Remix/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: Classical Remix")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def bonafideBloomDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/bonafidebloom/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: BonafideBloom")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by Bonafide Bloom. Please support their music! http://www.bonafidebloom.com/")
  print("-------------------------------------")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "bonafidebloom";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/BonafideBloom/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/bonafidebloom/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/BonafideBloom"):
              os.makedirs("Downloaded music/BonafideBloom")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/BonafideBloom/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: BonafideBloom")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def veraFXDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/verafx/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: VeraFX")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by VeraFX. Please support their music! https://verafx.bandcamp.com/")
  print("-------------------------------------")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "verafx";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/VeraFX/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/verafx/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/VeraFX"):
              os.makedirs("Downloaded music/VeraFX")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/VeraFX/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: VeraFX")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def mashradioDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradiofuture.live/radio/stations/jetmashradio/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: JET MASH RADIO")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("Getting list of songs to download...")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: This station was removed from JSRL, and is instead being downloaded from a clone server at jetsetradiofuture.live.")
  print("-------------------------------------")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "jetmashradio";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/JET MASH RADIO/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradiofuture.live/radio/stations/jetmashradio/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/JET MASH RADIO"):
              os.makedirs("Downloaded music/JET MASH RADIO")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/JET MASH RADIO/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: JET MASH RADIO")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def djchidowDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/radio/stations/djchidow/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: DJ Chidow")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by DJ Chidow. Please support their music! https://chidowhouse-shop.bandcamp.com/")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "djchidow";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/DJ Chidow/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradio.live/radio/stations/djchidow/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/DJ Chidow"):
              os.makedirs("Downloaded music/DJ Chidow")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/DJ Chidow/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: DJ Chidow")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()
    
def futuregenDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradiofuture.live/radio/stations/futuregeneration/~list.js"
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You wanted to download songs from station: FUTURE GENERATION")
  print("This process will download all the songs from the station. This will take some time. Go grab a snack or read a book or something.")
  print("If a download takes longer than a few minutes, please force-close the application and check your connection.")
  print()
  print("-------------------------------------")
  print("/!\ NOTICE: All songs on this station were made by SASHKO NAGANUMA. Please support their music! https://sashkonaganuma.bandcamp.com/")
  print("This station was removed from JSRL, and is instead being downloaded from a clone server at jetsetradiofuture.live.")
  print("-------------------------------------")
  print()
  print("Getting list of songs to download...")
  print()
  with urllib.request.urlopen(url) as file:
    #--Make the file actually usable by JSRLoader--#
    data = file.read().decode('utf-8')
    data = data.replace("//Choose a name for the station", '')
    data = data.replace('stationName = "futuregeneration";', '')
    data = data.replace("//Add it to the array of stations", '')
    data = data.replace("stationsArray[stationsArray.length] = stationName;", '')
    data = data.replace("//Define an array for tracks", '')
    data = data.replace('this[stationName+"_tracks"] = new Array();', '')
    data = data.replace("//TRACKS", '')
    data = data.replace("this[stationName+'_tracks'][this[stationName+'_tracks'].length] = ", '')
    data = data.replace(";", '')
    data = data.replace('"', '')
    #--Save the file as data.txt--#
    with open('data.txt', 'w') as f:
      f.write(data)
  #--Open data.txt--#
  with open('data.txt', 'r') as data:
    for x in list(data):
      #--Make the file usable (again)--#
      song = x.replace("\n", '')
      #--Check if song name is blank--#
      if not song == '':
        #--Check if already downloaded--#
        if not os.path.exists("Downloaded music/FUTURE GENERATION/" + song + ".mp3"):
          #--Download the song--#
          print("Downloading " + song + "... Please be patient.")
          print()
          song = "https://jetsetradiofuture.live/radio/stations/futuregeneration/" + song + ".mp3"
          with requests.get(song) as result:
            song = x.replace("\n", '')
            #--Check if our download directory exists, and if it doesn't, create it--#
            if not os.path.exists("Downloaded music/"):
              os.makedirs("Downloaded music/")
            if not os.path.exists("Downloaded music/FUTURE GENERATION"):
              os.makedirs("Downloaded music/FUTURE GENERATION")
            #--Write the downloaded song to a file--#
            with open("Downloaded music/FUTURE GENERATION/" + song + '.mp3', 'wb') as end:
              end.write(result.content)
          #--Print success message--#
          print("Successfully downloaded " + x)
        #--Code to execute if song exists--#
        else:
          print("Skipped " + song + ": Already downloaded!")
          print()
      else:
        pass
  if os.path.exists("data.txt"):
    os.remove("data.txt")
  #--Print final success message--#
  print("Successfully downloaded all songs from station: FUTURE GENERATION")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  gotoStart()

def about():
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("Welcome to JSRLoader! This is a project by PrincessLillie to allow downloading of songs from the online radio station JetSetRadio.live.")
  print("Most online radio stations would play songs server-side and stream that to you via an M3U playlist file. With JetSetRadio.live, that isn't the case. JSRL serves songs as MP3s, which are then streamed to your browser. It keeps track of these songs by listing them in a JS array. While this does make things simpler on the server side, it also means that we can use the URLs of the MP3 files to download the songs directly from JSRL for free!")
  print()
  print("JSRLoader was made possible by:")
  print("PrincessLillie - Creating the application itself")
  print("JetSetRadio.live - They do provide the music...")
  print("All artists on JSRL - Well, they made the music!")
  print("All GitHub contributors - Adding their own flair to JSRLoader by making it better or fixing bugs")
  print("You, the user - Using this application, it puts a smile on my face :)")
  print()
  print("JSRLoader is open-source at https://github.com/sks316/JSRLoader")
  print("For support, open an issue on the GitHub tracker or contact PrincessLillie#2523 on Discord.")
  print()
  input("Please press ENTER to continue. ")
  gotoStart()

#--Start menu--#
def gotoStart():
  #--Print introduction--#
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("You can download from the following stations:")
  print("1: Classic")
  print("2: Future")
  print("3: GG's")
  print("4: Poison Jam")
  print("5: Noise Tanks")
  print("6: Love Shockers")
  print("7: Rapid 99")
  print("8: The Immortals")
  print("9: Doom Riders")
  print("10: Golden Rhinos")
  print("11: Summer")
  print("12: Christmas")
  print("13: Halloween")
  print("14: Bumps")
  print("15: Memories of Tokyo-To")
  print("M: More stations")
  print()
  print("T: JSRLTV Downloader")
  print("A: About JSRLoader")
  print("E: Exit JSRLoader")
  print()
  print()
  #--Ask the user to select a station to download--#
  selection = input("Please enter the number that corresponds with your selection and press ENTER: ")
  if selection == '1':
    classicDL()
  elif selection == '2':
    futureDL()
  elif selection == '3':
    ggsDL()
  elif selection == '4':
    poisonJamDL()
  elif selection == '5':
    noiseTanksDL()
  elif selection == '6':
    loveShockersDL()
  elif selection == '7':
    rapid99DL()
  elif selection == '8':
    immortalsDL()
  elif selection == '9':
    doomRidersDL()
  elif selection == '10':
    goldenRhinosDL()
  elif selection == '11':
    summerDL()
  elif selection == '12':
    christmasDL()
  elif selection == '13':
    halloweenDL()
  elif selection == '14':
    bumpsDL()
  elif selection == '15':
    memoriesOfTokyoToDL()
  elif selection == 'm':
    moreStations()
  elif selection == 'M':
    moreStations()
  elif selection == 't':
    JSRLTV()
  elif selection == 'T':
    JSRLTV()
  elif selection == 'a':
    about()
  elif selection == 'A':
    about()
  elif selection == 'e':
    exit()
  elif selection == 'E':
    exit()
  else:
    gotoStart()

def moreStations():
  #--Print introduction--#
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("More stations:")
  print("1: Ultra Remixes")
  print("2: King for Another Day")
  print("3: Lo-Fi")
  print("4: Forever Is A Pretty Long Time")
  print("5: Ollie King")
  print("6: Toe Jam & Earl")
  print("7: Crazy Taxi")
  print("8: Hover")
  print("9: Butterflies")
  print("10: Revolution")
  print("11: End of Days")
  print("12: JET MASH RADIO")
  print("13: DJ Chidow")
  print("14: FUTURE GENERATION")
  print("15: Outer Space")
  print("M: Even more stations")
  print("B: Go back")
  print()
  print("A: About JSRLoader")
  print("E: Exit JSRLoader")
  print()
  print()
  #--Ask the user to select a station to download--#
  selection = input("Please enter the number that corresponds with your selection and press ENTER: ")
  if selection == '1':
    ultraRemixesDL()
  elif selection == '2':
    kfadDL()
  elif selection == '3':
    lofiDL()
  elif selection == '4':
    elaquentDL()
  elif selection == '5':
    olliekingDL()
  elif selection == '6':
    toejamDL()
  elif selection == '7':
    crazyTaxiDL()
  elif selection == '8':
    hoverDL()
  elif selection == '9':
    butterfliesDL()
  elif selection == '10':
    revolutionDL()
  elif selection == '11':
    endOfDaysDL()
  elif selection == '12':
    mashradioDL()
  elif selection == '13':
    djchidowDL()
  elif selection == '14':
    futuregenDL()
  elif selection == '15':
    spaceDL()
  elif selection == 'm':
    evenMoreStations()
  elif selection == 'M':
    evenMoreStations()
  elif selection == 'b':
    gotoStart()
  elif selection == 'B':
    gotoStart()
  elif selection == 'a':
    about()
  elif selection == 'A':
    about()
  elif selection == 'e':
    exit()
  elif selection == 'E':
    exit()
  else:
    moreStations()

def evenMoreStations():
  #--Print introduction--#
  clearScreen()
  print()
  print(appver)
  print("-------------------------------------")
  print()
  print("Even more stations:")
  print("1: The Garage")
  print("2: Ganjah")
  print("3: Chiptunes")
  print("4: Retro Remix")
  print("5: Classical Remix")
  print("6: BonafideBloom")
  print("7: VeraFX")
  print("8: Snow-fi")
  print("B: Go back")
  print()
  print("A: About JSRLoader")
  print("E: Exit JSRLoader")
  print()
  print()
  #--Ask the user to select a station to download--#
  selection = input("Please enter the number that corresponds with your selection and press ENTER: ")
  if selection == '1':
    garageDL()
  elif selection == '2':
    ganjahDL()
  elif selection == '3':
    chiptunesDL()
  elif selection == '4':
    retroRemixDL()
  elif selection == '5':
    classicalRemixDL()
  elif selection == '6':
    bonafideBloomDL()
  elif selection == '7':
    veraFXDL()
  elif selection == '8':
    snowfiDL()
  elif selection == 'b':
    moreStations()
  elif selection == 'B':
    moreStations()
  elif selection == 'a':
    about()
  elif selection == 'A':
    about()
  elif selection == 'e':
    exit()
  elif selection == 'E':
    exit()
  else:
    moreStations()

def TVpinned():
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download pinned")
  print("This process will download the pinned video, the one that plays first every time you open JSRLTV. This will take only a few moments.")
  print("If the download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  #--Check if already downloaded--#
  if not os.path.exists("Downloaded videos/Pinned/pinned.mp4"):
    #--download video--#
    print("Downloading pinned... Please be patient.")
    print()
    video = "https://jetsetradio.live/tv/APP/videoplayer/pinned/pinned.mp4"
    #--save video to disk--#
    with requests.get(video) as result:
	 #--Check if our download directory exists, and if it doesn't, create it--#
      if not os.path.exists("Downloaded videos/"):
        os.makedirs("Downloaded videos/")
      if not os.path.exists("Downloaded videos/Pinned"):
        os.makedirs("Downloaded videos/Pinned")
    #--write downloaded video to file--#
    with open("Downloaded videos/Pinned/pinned.mp4", 'wb') as end:
        end.write(result.content)
        #--Print success message--#
        print("Successfully downloaded pinned")
        print()
  #--Code to execute if song exists--#
  else:
    print("Skipped pinned: Already downloaded!")
    print()
  #--Print final success message--#
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch1():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 1")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray1'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 1/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch1/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 1"):
            os.makedirs("Downloaded videos/Channel 1")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 1/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 1")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch2():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 2")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray2'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 2/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch2/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 2"):
            os.makedirs("Downloaded videos/Channel 2")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 2/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 2")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch3():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 3")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray3'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 3/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch3/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 3"):
            os.makedirs("Downloaded videos/Channel 3")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 3/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 3")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch4():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 4")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray4'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 4/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch4/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 4"):
            os.makedirs("Downloaded videos/Channel 4")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 4/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 4")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch5():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 5")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray5'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 5/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch5/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 5"):
            os.makedirs("Downloaded videos/Channel 5")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 5/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 5")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch6():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 6")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray6'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 6/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch6/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 6"):
            os.makedirs("Downloaded videos/Channel 6")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 6/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 6")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch7():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 7")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray7'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 7/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch7/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 7"):
            os.makedirs("Downloaded videos/Channel 7")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 7/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 7")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch8():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 8")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray8'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 8/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch8/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 8"):
            os.makedirs("Downloaded videos/Channel 8")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 8/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 8")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def TVch9():
  #--Get list of videos from JSRLTV--#
  url = "https://jetsetradio.live/tv/APP/preloader/retrieveTotalFilesAndFilesList.php"
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("You chose to download videos from channel 9")
  print("This process will download all the videos from the channel. This will take a while. Go grab a snack or read a book or something.")
  print("If a download takes longer than half an hour, please force-close the application and check your connection.")
  print()
  print("Getting list of videos to download...")
  print()
  #--download list of videos--#
  with urllib.request.urlopen(url) as file:
    #--make the XML usable--#
    data = file.read().decode('utf-8')
	 #--open videos.xml on disk and write downloaded data--#
    with open('videos.xml', 'w') as f:
      f.write(data)
  #--parse XML and convert to JSON--#
  tree = ET.parse('videos.xml')
  root = tree.getroot()
  for item in root.findall('./fileListArray9'):
  #--open file.json on disk--#
    with open('videos.json', 'w') as f:
      #--remove extra characters and backslashes--#
      string = str(item.text.encode('utf8'))[2:-1]
      string = string.replace("/", '')
      string = string.replace("\\", '')
      #--write JSON to videos.json--#
      f.write(string)
  #--parse JSON--#
  with open('videos.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
	 #--get names of videos from JSON--#
    for x in data:
      #--Check if already downloaded--#
      if not os.path.exists("Downloaded videos/Channel 9/" + x + ".mp4"):
	     #--download video--#
        print("Downloading " + x + "... Please be patient.")
        print()
        video = "https://jetsetradio.live/tv/APP/videoplayer/ch9/" + x + ".mp4"
        #--save video to disk--#
        with requests.get(video) as result:
		    #--Check if our download directory exists, and if it doesn't, create it--#
          if not os.path.exists("Downloaded videos/"):
            os.makedirs("Downloaded videos/")
          if not os.path.exists("Downloaded videos/Channel 9"):
            os.makedirs("Downloaded videos/Channel 9")
        #--write downloaded video to file--#
        with open("Downloaded videos/Channel 9/" + x + '.mp4', 'wb') as end:
            end.write(result.content)
            #--Print success message--#
            print("Successfully downloaded " + x)
            print()
      #--Code to execute if song exists--#
      else:
        print("Skipped " + x + ": Already downloaded!")
        print()
  #--once done, remove the JSON and XML file--#
  if os.path.exists("videos.json"):
		 os.remove("videos.json")
  if os.path.exists("videos.xml"):
		 os.remove("videos.xml")
  #--Print final success message--#
  print("Successfully downloaded all videos from channel 9")
  print()
  input("Please press ENTER to continue. ")
  #--Go back to start--#
  JSRLTV()

def JSRLTV():
  #--Print JSRLTV downloader menu--#
  clearScreen()
  print()
  print(appverTV)
  print("-------------------------------------")
  print()
  print("Welcome to the JSRLTV downloader!")
  print("With this, you can download videos from the JSRLTV player at jetsetradio.live.")
  print("Just so you know, this can take a lot of drive space. Please make sure you have at least 70GB if you intend to download all channels.")
  print("Select a channel to download:")
  print()
  print("P: pinned")
  print("1: Channel 1")
  print("2: Channel 2")
  print("3: Channel 3")
  print("4: Channel 4")
  print("5: Channel 5")
  print("6: Channel 6")
  print("7: Channel 7")
  print("8: Channel 8")
  print("9: Channel 9")
  print()
  print("B: Go back")
  print("E: Exit JSRLoader")
  print()
  print()
  #--Ask the user to select a channel to download--#
  selection = input("Please enter the number that corresponds with your selection and press ENTER: ")
  if selection == 'P':
    TVpinned()
  elif selection == 'p':
    TVpinned()
  elif selection == '1':
    TVch1()
  elif selection == '2':
    TVch2()
  elif selection == '3':
    TVch3()
  elif selection == '4':
    TVch4()
  elif selection == '5':
    TVch5()
  elif selection == '6':
    TVch6()
  elif selection == '7':
    TVch7()
  elif selection == '8':
    TVch8()
  elif selection == '9':
    TVch9()
  elif selection == 'b':
    gotoStart()
  elif selection == 'B':
    gotoStart()
  elif selection == 'e':
    exit()
  elif selection == 'E':
    exit()
  else:
    JSRLTV()

gotoStart()