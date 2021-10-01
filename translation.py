import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>Aku Bot Auto Forward, 
Aku dapat Meneruskan Pesan yang Kamu Kirim ke Channel Tertentu
Bantuan? Ketik /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Ikuti Langkah-langkah Berikut!!</b>
<b>• Isi Kolom <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>dan lainnya</b> pada Heroku Config Vars</b>
<b>• Kemudian Beri Izin Admin pada Bot di Telegram Channel</b>
<b>• Kirim pesan Apapun di Telegram Channel mu</b>
<b>• dan Gunakan /run untuk Memulai Proses Forward</b>

<b><u>Daftar Perintah</b></u>

* /start - <b>Bot Alive</b>
* /help - <b>Bantuan</b>
* /run - <b>Mulai Proses</b>
* /about - <b>Tentang Bot</b>"""
  ABOUT_TXT = """<b><u>Informasi Tentang Bot</b></u>

<b>Name :</b> <code>FBC - FORWARD BOT</code>
<b>Credit :</b> <code>Kevin Arifandi</code>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b><code>V1.5</code>"""
