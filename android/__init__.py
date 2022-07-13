import asyncio
import base64

from telethon import TelegramClient;loop = asyncio.get_event_loop()
from subprocess import PIPE, Popen
from time import sleep as antripp
from bs4 import BeautifulSoup

import requests
from rich.console import Console
from rich.panel import Panel
import sys,socket, os
import logging
console = Console()


uyarilacakdeger=0
def nn():
    console.print("\n\n")
def onay (text):
    while True:
        cevap=soru(text)
        if cevap.lower() in ["evet","yes","y","he"]:
            return True
        elif cevap in ["hayır","hayir","no","n","yo","yok"]:
            return False
        else:
            noadded("Lütfen sadece evet-yes veya hayır-no diyin!")
def noadded (text):
    nn()
    console.log(f'[red]❎ {text}[/]')  
def basarili (text):
    nn()
    console.log(f'[bold green]✅ {text}[/]')                         
def onemli (text):
    nn()
    console.print(f'[bold cyan]❗ {text}[/]')      
def ads (text,time=5):
    nn()
    console.log(f'[green]🍔 {text}[/]')     
    antripp(time)              
def soru (soru):
    nn()
    console.print(f'[bold thistle1]❔ {soru}[/]')
    try:                 
        return console.input(f"[bold yellow1]>> [/]")
    except KeyboardInterrupt:
        hata("Klavye çıkışı yapıldı!")
def soru_ (soru):
    nn()
    console.print(f'[bold thistle1]❔ {soru}[/]')
    return console.input(f"[bold yellow1]>> [/]")

def logo (satirbırak=False):
    text = "█▀▀ █▀▀ █▀█ █▀▀ █▀▀ █▄█ █▄░█\n█▄▄ ██▄ █▀▄ █▄▄ ██▄ ░█░ █░▀█\n\n█░░ ▄▀█ █▄▄\n█▄▄ █▀█ █▄█"
    if satirbırak:
        for i in range(25):
            console.print("\n")
    console.print(Panel(f'[bold medium_purple]{text}[/]',width=90),justify="center")
def hata (text):
    nn()
    console.log(f'[bold red]❌ {text}[/]') 
    sys.exit()
def pip_(module):
    onemli(f"📥 installing {module} for cerceynlab")
    pip_cmd = ["pip", "install", f"{module}"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
def myscript ():
    return "ZnJvbSByaWNoLmNvbnNvbGUgaW1wb3J0IENvbnNvbGUNCmZyb20gcmljaC5wYW5lbCBpbXBvcnQgUGFuZWwNCg0KaW1wb3J0IHN5cw0KY29uc29sZSA9IENvbnNvbGUoKQ0KZGVmIGJpbGdpICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JsdWVde3RleHR9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgIA0KZGVmIHNvcnUgKHNvcnUpOg0KICAgIGNvbnNvbGUucHJpbnQoUGFuZWwoZidbYm9sZCB5ZWxsb3dde3NvcnV9Wy9dJyx3aWR0aD03MCksanVzdGlmeT0iY2VudGVyIikgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgcmV0dXJuIGNvbnNvbGUuaW5wdXQoZiJbYm9sZCB5ZWxsb3ddPj4gWy9dIikNCmRlZiBoYXRhICh0ZXh0KToNCiAgICBjb25zb2xlLnByaW50KFBhbmVsKGYnW2JvbGQgcmVkXXt0ZXh0fVsvXScsd2lkdGg9NzApLGp1c3RpZnk9ImNlbnRlciIpICAgIA0KICAgIHN5cy5leGl0KCkNCg0KYmlsZ2koIlBhc3N3b3JkIGRlY29kaW5nLi4uIikNCmRvZ3J1cGFzcz0gNjg5Nw0KICAgIA0Kc2lmcmUgPSBzb3J1KCJNZXJoYWJhISDFnmlmcmU6IikNCnRyeToNCiAgICBkb2dydXBhc3M9IGludChkb2dydXBhc3MpDQogICAgaWYgaW50KHNpZnJlKSAhPSBkb2dydXBhc3M6DQogICAgICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgVHlwZUVycm9yOg0KICAgIGhhdGEoIllhbmzEscWfIMWfaWZyZSIpDQpleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgaGF0YSgiSGF0YTogIitzdHIoZSkp"                 
def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    with console.status("[bold blue] İnternet bağlantınız kontrol ediliyor...") as status:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            console.log("[green] Bağlantı var gibi görünüyor! [/green]")
            return True
        except socket.error as ex:
            print(ex)
            console.log("[red] Bağlantı yok gibi gözüküyor ! [/red]")
            return False                        
def bilgi (text):
    nn()
    console.log(f'[blue]ℹ️ {text}[/]')

try:
    import telegram.ext as tg
except:
    pip_("python-telegram-bot")
finally:
    import telegram.ext as tg

try:
    try: os.remove("bots.session")
    except:pass
    bot = TelegramClient('bots',api_id=13312418, api_hash="78d4836b623e06dece52033114bdb21e")
except Exception as e:
    hata(f"Bir sorunla karşılaştık! Bu hatayı geliştiriciye bildirin:\n{str(e)}")
def n():
    console.print("\n")

logo()
Token="NTU1MDM4MzQ2MjpBQUYtSnQ3aUhrd2gtUTVnekFYM05lUzM4dEZUUHV3WFlSdw=="
onayl = onay("Farklı Token ile işlem yapmak ister misiniz?")
if onayl:
    Token = soru("Token: ")
dispatcher = None
updater = None

LOGUKAPAT = logging.getLogger('apscheduler.executors.default')
LOGUKAPAT.setLevel(logging.ERROR)

onemli("Hesjkxecjnvrıcnxe")

async def botaqgir():
    global bot,Token, updater,dispatcher
    data = [1,2,3,4]
    u=""
    n()

    with console.status("[bold blue] Bota girme işlemi sürüyor...") as status:
        while data:
            num = data.pop(0)
            antripp(.5)
            if num==1:
                if Token.endswith("=="):
                    onemli("🔑 Token ayarlanıyor...")
                    aqj4394 = base64.b64decode(Token)
                else:
                    aqj4394=Token
                updater = tg.Updater(aqj4394.decode("utf-8"), workers=8, use_context=True)
            elif num==2:
                console.log("[cyan] 🎟️ Giriş yapılıyor...[/cyan]")
                console.log("[red] 🎟️ Hata alınması en muhtemel yer...[/red]")
                updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True) 
                await bot.start(bot_token=aqj4394)
                bot.parse_mode="html"
            elif num==3:
                try:

                    await updater.dispatcher.bot.sendMessage(-1001173298784,"⌛ Bot başladı!")
                except:
                    noadded('Mesaj gönderilememe hatası!')
            elif num==4:
                global asesw 
                asesw = aqj4394
                console.log(f'[bold][green]✅ Bot girişi yapıldı!')
                #await bot.disconnect()
    return bot, updater

def gunluk():
    import datetime
    zaman = datetime.datetime.now()
    bilgi('Time: '+str(zaman))
def passed (text):
    console.print("\n")
    console.print(Panel(f'[steel_blue1]🚸 {text}[/]',width=70),justify="center")
async def VeriCek(index=5):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/80.0.3987.163 Safari/537.36 "
    }

    request = requests.get("https://www.doviz.com/", headers=header)
    if not str(request.status_code).startswith("2"):
        hata("Site yanıt vermiyor..")
    tumVeriler = BeautifulSoup(request.content, "html.parser")

    tumVeriler = tumVeriler.find("div", {"class": "market-data"}).findAll("div", {"class": "item"})

    bitcoin = tumVeriler[index].find("span", {"class": "value"}).text
    if index==5: # bitcoin
        bitcoin = list(bitcoin)
        bitcoin.pop(0)
        yeniDeger = "".join(bitcoin)
        return yeniDeger
    return bitcoin
def VeriCek_():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/80.0.3987.163 Safari/537.36 "
    }

    request = requests.get("https://www.doviz.com/", headers=header)
    if not str(request.status_code).startswith("2"):
        hata("Site yanıt vermiyor..")
    tumVeriler = BeautifulSoup(request.content, "html.parser")

    tumVeriler = tumVeriler.find("div", {"class": "market-data"}).findAll("div", {"class": "item"})

    bitcoin = tumVeriler[5].find("span", {"class": "value"}).text
    bitcoin = list(bitcoin)
    bitcoin.pop(0)
    yeniDeger = "".join(bitcoin)
    return yeniDeger
asesw=""

def run_forever():
        dgr = None
        btcdeger=str(VeriCek_())
        print(btcdeger)
        try:
            with open("output.txt","r", encoding="utf-8") as f:
                readfile=f.read().strip("\n").split("|")
            uyarilacakdegr = int(readfile[0])
        except:
            uyarilacakdegr = -1
        deger= int(btcdeger.split(".")[0])
        if deger != uyarilacakdegr:
            return
        try:
            with open("output.txt","r", encoding="utf-8") as f:
                dgr=f.read().split("|")
        except FileNotFoundError:
            return
        except Exception: 
            hata("Sistem dosyası hatalı...")
        if dgr[1] == "True":
            with open("output.txt","w", encoding="utf-8") as f:
                f.write(str(dgr[0]) + "|" + "False")
            
            with open("maing.txt","r", encoding="utf-8") as f:
                maing= int(f.read().strip("\n"))

            with open("textt.txt","r", encoding="utf-8") as f:
                textt= f.read().strip("\n")

            updater.dispatcher.bot.sendMessage(maing,textt)


def btcbildir():
    btcdeger=str(VeriCek_())
    print(btcdeger)
    try:
        with open("output.txt","r", encoding="utf-8") as f:
            readfile=f.read().strip("\n").split("|")
        uyarilacakdegr = int(readfile[0])
        uyar=str(readfile[1])
    except:
        uyarilacakdegr = -1
    deger= int(btcdeger.split(".")[0])
    if deger == uyarilacakdegr:
        bilgi("Algılandı::....")
        if uyar=="True":
            onemli("Raporlandı!")
        
    else:
        bilgi(f"Henüz o değere ulaşmadı...,{deger} {uyarilacakdegr}")



async def disconn():
    try:
        await bot.disconnect()
        
        noadded("Bottan çıkış yapıldı!")
    except:
        pass
    finally:
        try: os.remove("bots.session");onemli("Bot dosyası silindi...")
        except:pass
