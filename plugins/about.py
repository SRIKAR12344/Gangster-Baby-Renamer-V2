import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5708318695:AAEp-9e7MbcFVMO_cAhwDtjb10ik5x2tvpE')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"𝗠𝗔𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 :- <a href='https://t.me/BOSSHINDIOFFCIAL_DRAMAZ'>𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘</a>\n𝗖𝗥𝗘𝗔𝗧𝗘𝗥 :- <a href='https://t.me/SIRISH_123'>🦋𝗦𝗜𝗥𝗜𝗦𝗛🦋</a>\n𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 :- Python3\nLibrary :- Pyrogram 2.0\n𝗦𝗘𝗥𝗩𝗘𝗥 :- 𝗩𝗣𝗦\n𝗧𝗢𝗧𝗔𝗟 𝗥𝗘𝗡𝗔𝗠𝗘𝗗 𝗙𝗜𝗟𝗘 :- {total_rename}\n𝗧𝗢𝗧𝗔𝗟 𝗦𝗜𝗭𝗘 𝗥𝗘𝗡𝗔𝗠𝗘𝗗 :- {humanbytes(int(total_size))} \n\n 𝗢𝗪𝗡𝗘𝗥 **<a href='https://t.me/SIRISH_123'>𝗦𝗜𝗥𝗜𝗦𝗛</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/SIRISH_123'>**𝗦𝗜𝗥𝗜𝗦𝗛**</a> ❤️",quote=True)
