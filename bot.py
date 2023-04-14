import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5708318695:AAEp-9e7MbcFVMO_cAhwDtjb10ik5x2tvpE")

API_ID = int(os.environ.get("API_ID", "29189916"))

API_HASH = os.environ.get("API_HASH", "1b22031190ccfc4c1e3a394267a5526a76912")

STRING = os.environ.get("STRING", "BQCNvT0XFUwp4t_U2r9l25owf2k545sNPX0mI953DxgukomhZ7CnSzdjKMLPEGLOuaZghh45jdKw3OkSlG3SesPWoz_h-QQnFDcB3QzdGsGK8lph5V3zaT_8kBb2t6KYDat0Oy8EnO-2_Nd5AtalcpC50dP9FTfHJlrHCppAkMvN5mp_QLb42YzJjBB6jHNA4OCaV6sk5Xp-uoJmAcOqbf_mz8YNeFkVVuI9KTLUNz9gtcBnfKKEXxCSlNbMiVaJm47p7qOTcyDPTdCQ4KoX9FQx9o9QLdi4WJAlq-o0q2jA5guMvTbIytOhCB6xUdgOjBmvkXcrNQSppzjkYMU5HLI0AAAAAUNpEfQA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
