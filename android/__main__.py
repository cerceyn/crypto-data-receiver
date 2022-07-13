# -*- coding: utf-8 -*-

import asyncio
loop = asyncio.get_event_loop()
from android import *
"""except ImportError:
    try:
        import os;os.system("python -m android")
    except KeyboardInterrupt:
        console.print("\n")
        loop.run_until_complete(disconn())
        hata("Güle güle!")
"""
from .events import register as clabtetikleyici
from telethon.errors import PeerIdInvalidError
try:
    from apscheduler.schedulers.background import BackgroundScheduler
except:
    pip_("apscheduler")
finally:
    from apscheduler.schedulers.background import BackgroundScheduler
try:
    from notifypy import Notify
except:
    pip_("notify-py")
finally:
    from notifypy import Notify

from time import sleep
import asyncio,base64
from os import remove

def log(text,renk=None):
    if renk:
        console.log(f"[{renk}]{text}[/{renk}]")
    else:
        console.log(f"{text}")






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

@clabtetikleyici(bot=bot,incoming=True, pattern="^.settext",patterncorrect=False,disable_edited=True)
async def settt(m):
    string = m.pattern_match.group(1)
    if not string:
        return await m.reply("<i>Lütfen bir değer ayarlayın..\nÖr: /settext Btc ayarlanan değere ulaştı</i>")
    from_user = await m.get_sender()
    if from_user.id not in [1210782223,1687646994]:
        return await m.reply("<i>Sadece izin verilen kişiler değiştirebilir. Ör chapolen</i>")
    try:
        with open("textt.txt","w", encoding="utf-8") as f:
            f.write(string)
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




async def main ():
    global bot,maing
    statusz=None
    if os.name!="nt": os.system("clear")
    else: os.system("cls")
    logo(True)
    internet()
    if statusz:
        passed(statusz);statusz=None
    bot = await botaqgir()
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
    
    scheduler = BackgroundScheduler()
    #scheduler.add_executor('processpool')
    #scheduler.add_job(gunluk, 'interval', seconds=600)
    scheduler.add_job(run_forever, 'interval', seconds=10)
    bilgi("Reminder started..")
    scheduler.start()

    try:
        await bot.run_until_disconnected()
    except KeyboardInterrupt:
        pass #raise KeyboardInterrupt("Çıkış!")
    await disconn ()
    updater.stop()

        
if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        n()
        loop.run_until_complete(disconn())
        updater.stop()
        hata("Güle güle!")






