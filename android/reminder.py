import logging
from android import bilgi, pip_,VeriCek_,onemli,hata,gunluk

from .main import dispatcher
try:
    from apscheduler.schedulers.background import BackgroundScheduler
except:
    pip_("apscheduler")
finally:
    from apscheduler.schedulers.background import BackgroundScheduler
import logging

LOGUKAPAT = logging.getLogger('apscheduler.executors.default')
LOGUKAPAT.setLevel(logging.ERROR)


async def run_forever():
    onemli("CLab Forever Started...")

    if True:
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

            dispatcher.bot.sendMessage(maing,textt)

scheduler = BackgroundScheduler()
scheduler.add_executor('processpool')
scheduler.add_job(gunluk, 'interval', seconds=600)
scheduler.add_job(run_forever, 'interval', seconds=10)
bilgi("Reminder started..")
scheduler.start()
