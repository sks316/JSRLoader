import urllib.request
import requests
import re
import os
from os import system, name

#--Function for clearing the screen--#
def clearScreen():
  #--Check if OS is Windows--#
  if name == 'nt':
     _ = system('cls')
  else:
     _ = system('clear')

def classicDL():
  #--Get list of songs from JSRL--#
  url = "https://jetsetradio.live/audioplayer/stations/classic/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("classicArray[classicArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/classic/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/future/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("futureArray[futureArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/future/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/ggs/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("ggsArray[ggsArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/ggs/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/bumps/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
          song = "https://jetsetradio.live/audioplayer/stations/bumps/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/poisonjam/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("poisonJamArray[poisonJamArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/poisonjam/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/noisetanks/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("noiseTanksArray[noiseTanksArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/noisetanks/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/loveshockers/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("loveShockersArray[loveShockersArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/loveshockers/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/rapid99/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("rapid99Array[rapid99Array.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/rapid99/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/immortals/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("immortalsArray[immortalsArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/immortals/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/doomriders/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("doomRidersArray[doomRidersArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/doomriders/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/goldenrhinos/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("goldenRhinosArray[goldenRhinosArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/goldenrhinos/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/summer/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("summerArray[summerArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/summer/" + song + ".mp3"
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
  url = "https://jetsetradio.live/audioplayer/stations/christmas/~list.js"
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
    data = data.replace("christmasArray[christmasArray.length] = ", '')
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
          song = "https://jetsetradio.live/audioplayer/stations/christmas/" + song + ".mp3"
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

def about():
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
  print("-------------------------------------")
  print()
  print("Welcome to JSRLoader! This is a project by sks316 to allow downloading of songs from the online radio station JetSetRadio.live.")
  print("Most online radio stations would play songs server-side and stream that to you via a M3U playlist file. With JetSetRadio.live, that isn't the case. JSRL serves songs as MP3s, which are then streamed to your browser. It keeps track of these songs by listing them in a JS array. While this does make things simpler on the server side, it also means that we can use the URLs of the MP3 files to download the songs from JSRL for free!")
  print()
  print("JSRLoader was made possible by:")
  print("sks316 - Creating the application itself")
  print("JetSetRadio.live - They do provide the music...")
  print("All GitHub contributors - Adding their own flair to JSRLoader by making it better or fixing bugs")
  print("You, the user - Using this application, it puts a smile on my face :)")
  print()
  print("JSRLoader is open-source at https://github.com/sks316/JSRLoader")
  print("For support, open an issue on the GitHub tracker or contact sks316#2523 on Discord.")
  print()
  input("Please press ENTER to continue. ")
  gotoStart()

#--Start menu--#
def gotoStart():
  #--Print introduction--#
  clearScreen()
  print()
  print("JSRLoader v1.0.0 by sks316")
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
  print("13: Bumps")
  print()
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
    bumpsDL()
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

gotoStart()