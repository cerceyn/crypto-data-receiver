# -*- coding: utf-8 -*-

import asyncio
loop = asyncio.get_event_loop()
try:
    from android import *
except ImportError:
    try:
        import os;os.system("python -m android")
    except KeyboardInterrupt:
        console.print("\n")
        loop.run_until_complete(disconn())
        hata("Güle güle!")
try:
    from apscheduler.schedulers.background import BackgroundScheduler
except:
    pip_("apscheduler")
finally:
    from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .events import register as clabtetikleyici
from telethon.errors import PeerIdInvalidError

try:
    from notifypy import Notify
except:
    pip_("notify-py")
finally:
    from notifypy import Notify

from time import sleep
import asyncio,base64
from os import remove
from android import *


def n():
    console.print("\n")
def log(text,renk=None):
    if renk:
        console.log(f"[{renk}]{text}[/{renk}]")
    else:
        console.log(f"{text}")

Token="NTU1MDM4MzQ2MjpBQUhRc1Z1WmRPUlhIbktlQTRmN0tydV9XOGlmS0NKX3lkSQ=="

async def botagir():
    global bot
    data = [1,2,3,4]
    u=""
    n()
    onayl = onay("Farklı Token ile işlem yapmak ister misiniz?")
    if onayl:
        Token = soru("Token: ")
    with console.status("[bold blue] Bota girme işlemi sürüyor...") as status:
        while data:
            num = data.pop(0)
            sleep(.5)
            if num==1:
                if Token.endswith("=="):
                    log("🔑 Token ayarlanıyor...","cyan")
                    aqj4394 = base64.b64decode(Token)
                else:
                    aqj4394=Token
            elif num==2:
                console.log("[cyan] 🎟️ Giriş yapılıyor...[/cyan]")
                console.log("[red] 🎟️ Hata alınması en muhtemel yer...[/red]")
                await bot.start(bot_token=aqj4394)
                bot.parse_mode="html"
            elif num==3:
                try:
                    await bot.send_message(-1001173298784,"⌛ Bot başladı!")
                except:
                    noadded('Mesaj gönderilememe hatası!')
            elif num==4:
                global asesw 
                asesw = aqj4394
                console.log(f'[bold][green]✅ Bot girişi yapıldı!')
                #await bot.disconnect()
    return bot



sozluk = {"main":"None"}


maing=None

@clabtetikleyici(bot=bot,incoming=True, pattern="^.start",disable_edited=True)
async def strt(m):
    await m.reply("Running...⚡")

@clabtetikleyici(bot=bot,incoming=True, pattern="^.set",patterncorrect=False,disable_edited=True)
async def settt(m):
    global uyarilacakdeger
    string = m.pattern_match.group(1)
    if not string:
        return await m.reply("<i>Lütfen bir değer ayarlayın..\nÖr: /set 22</i>")
    from_user = await m.get_sender()
    if from_user.id not in [1210782223,1687646994]:
        return await m.reply("<i>Sadece izin verilen kişiler değiştirebilir</i>")
    try:
        with open("output.txt","w", encoding="utf-8") as f:
            f.write(string + "|" + "True")
    except:
        return await m.reply("<i>Sanırım bir antivirüs programı bunu engelliyor..</i>")
    await m.reply(f"✅<i>İşlem Tamamlandı..\nAyarlanan Değer: {string}</i>")

@clabtetikleyici(bot=bot,incoming=True, pattern="^.btc",disable_edited=True)
async def btcc(m):
    msg=await m.reply("<i>Değer getiriliyor...</i>")
    btcdeger= await VeriCek()
    await msg.edit("<b>💰 Güncel Bitcoin Değeri 💲</b>\n>> {}".format(btcdeger))

@clabtetikleyici(bot=bot,incoming=True, pattern="^.usd",disable_edited=True)
async def usdd(m):
    msg=await m.reply("<i>Değer getiriliyor...</i>")
    btcdeger= await VeriCek(1)
    await msg.edit("<b>💰 Güncel Dolar Değeri 💲</b>\n>> {}".format(btcdeger))

@clabtetikleyici(bot=bot,incoming=True, pattern="^.euro",disable_edited=True)
async def eurr(m):
    msg=await m.reply("<i>Değer getiriliyor...</i>")
    btcdeger= await VeriCek(2)
    await msg.edit("<b>💰 Güncel Euro Değeri 💲</b>\n>> {}".format(btcdeger))

"""
@clabtetikleyici(bot=bot,incoming=True,groups_only=True,disable_edited=True)
async def ssss(m):
    bilgi(f"Şuradan bir mesaj algılandım🌀: {m.chat_id}")
"""

def notify_user(text,block=False):
    notification = Notify()
    notification.title = "Bitcoin Değeri"
    notification.message = text + "$"
    #notification.icon = "bitcoin.jpg"
    notification.send(block)
"""
@bot.on(bberc(incoming=True))
async def handler(event):
    await event.reply("b "+ event.text)
"""

async def run_forever():
    onemli("CLab Forever Started...")
    while True:
        dgr = None
        try:
            with open("output.txt","r", encoding="utf-8") as f:
                dgr=f.read().split("|")
        except: 
            hata("Sistem dosyası hatalı...")
        if dgr[1] == "True":
            with open("output.txt","w", encoding="utf-8") as f:
                f.write(str(dgr[0]) + "|" + "False")
            
            with open("maing.txt","r", encoding="utf-8") as f:
                maing= int(f.read().strip("\n"))

            with open("textt.txt","r", encoding="utf-8") as f:
                textt= f.read().strip("\n")

            await bot.send_message(maing,textt)
        await asyncio.sleep(10)




scheduler = AsyncIOScheduler()

async def main ():
    global bot
    statusz="ads"
    global maing
    if os.name!="nt": os.system("clear")
    else: os.system("cls")
    logo(True)
    internet()
    if statusz=="ads":ads("Free trial bitiş süresi: 31 gün"); statusz=None
    elif statusz:
        passed(statusz);statusz=None
    global bot
    bot = await botagir()
    if not os.path.exists("maing.txt"):
        maing = str(soru("Hangi grupla işlem yapılacak? "))
        try:
            with open("maing.txt","w", encoding="utf-8") as f:
                f.write(maing)
        except:
            return hata("<i>Sanırım bir antivirüs programı dosya işlemlerini engelliyor..</i>")
    else:
            with open("maing.txt","r", encoding="utf-8") as f:
                maing=f.read().strip("\n")
    if maing.startswith("-") or maing[0] in ["0","1","2","3","4","5","6","6","7","8","9"]:
            maing=int(maing)
    try:
        maing = (await bot.get_entity(maing)).id
    except Exception as e:
        if "deleted/deactivated" in str(e):
            hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
        hata(e)
    n()
    try:
        with open("textt.txt","r", encoding="utf-8") as f:
            f.read()
    except FileNotFoundError:
        with open("textt.txt","w", encoding="utf-8") as f:
            f.write("Btc ayarlanan değere ulaştı !!")
    log("💨💨 Şimdi botunuz çalışıyor ve ana kanalınızda birşey paylaşmanız bekleniyor...","green")
    statusz="Bottan çıkış yapıldı!"
    scheduler.add_executor('processpool')
    scheduler.add_job(gunluk, 'interval', seconds=600)
    scheduler.add_job(btcbildir, 'interval', seconds=10)
    scheduler.start()
    with console.status("[bold thistle1]⌛ Bot çalışıyor, durdurmak için Ctrl C yapın!") as status:
        try:
            await run_forever()
        except KeyboardInterrupt:
            pass #raise KeyboardInterrupt("Çıkış!")
        await disconn ()
        
if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        n()
        loop.run_until_complete(disconn())
        hata("Güle güle!")






