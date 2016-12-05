import Prova
print("parto...")
import botogram.objects.base
class CallbackQuery(botogram.objects.base.BaseObject):
    required = {
        "id": str,
        "from": botogram.User,
        "data": str,
    }
    optional = {
        "inline_message_id": str,
        "message": botogram.Message,
    }
    replace_keys = {
        "from": "sender"
    }
botogram.Update.optional["callback_query"] = CallbackQuery


import botogram

bot = botogram.create("TOKEN")
print("bot creato")



@bot.command("start")
def start(chat, message, args):
    print("Comando /start ricevuto!")
    testo = ("<b>Benvenuto</b> su @lollo_0_bot !\n"
             "Clicca sui pulsani per cominciare!"
    )
    bot.api.call("sendMessage",{
        "chat_id":chat.id, "text":testo, "parse_mode":"HTML", "reply_markup":
            '{"inline_keyboard": [[{"text":"Guide ðŸ“±", "callback_data":"guide"}, {"text":"Credits ðŸŒš", "callback_data":"credits"}],'+
            '[{"text":"Collaboratori ðŸ‘¬", "callback_data":"1"}],'
            '[{"text":"Dona ðŸ¤‘", "callback_data":"2"}]'+
        ']}'
        
})

def process_callback(bot, chains, update):
    '''Process callback'''
    Prova.process(bot, chains, update)
bot.register_update_processor("callback_query", process_callback)

@bot.command("help")
def help_command(chat, message, args):
    chat.send("Lista dei comandi che questo artificio puo' fare: \n /start = fai partire il bot \n /guide = le utili (o non) guide di lollo e co! \n /collaboratori = lista collaboratori \n /guidebtc Guide sulla famosa cryptomoneta! \n  /crediti = crediti", syntax="plain")

@bot.command("guidelinux")
def guidelinux_command(chat, message, args):
    chat.send("Ecco tutte le guide riguardati il mondo linux:\n Come installare qualsiasi cosa su VPS ubuntu /installah") 

    
@bot.command("installah")
def installah_command(chat, message, args):
    chat.send("1: apt-get update\n 2: apt-get upgrade \n 3: reboot \n 4: apt-get install (pacchetto desiderato)")

@bot.command("divcollaboratore")
def divcollaboratore_command(chat, message, args):
    chat.send("Per diventare collaboratore basta entrare in questo gruppo: https://telegram.me/lollo_0_bot_collaboratori", syntax="plain")
    print("comando /divcollaboratore eseguito!")

@bot.command("botpy")
def botpy_command(chat, message, args):
    chat.send("1) Installa python3 \n 2) Installa botogram attarverso pip \n  3)Scrivi questo codice: http://pastebin.com/khC0xAh3 \n 4) Esegui lo script ed avrai creato il tuo primo bot. (Guide in continuo aggiornamento) ")



@bot.command("collaboratori")
def collaboratori_command(chat, message, args):
    chat.send("Ecco i collaboratori: \n 1) @ImAndrehh il primo1 \n 2) @pietroos")

@bot.command("guidebtc")
def guidebtc_command(chat, message, args):
    chat.send("Guide ed altro sul BTC \n Il miglior miner gratuito https://upmcoins.com/?ref=53580 (se utilizzate il ref mi fate un piacere)", syntax="plain")

@bot.command("guidaphp")
def guidaphp_command(chat, message, args):
    chat.send("Qusta guida e' molto lunga e di qualita', la trovi a questo indirizzo:\n http://telegra.ph/Guida-sul-php-11-26 \n Scritta da: @ImAndrehh", syntax="plain")

@bot.command("guideserver")
def guideserver_command(chat, message, args):
    chat.send("Guide sui server & co: \n /guidaserver1 Come collegare un dominio cloudfare ad un server fatta da @pietroos")

@bot.command("guidaserver1")
def guidaserver1_command(chat, message, args):
    chat.send("Guida su come collegare un dominio cloudfare ad un server di @pietroos. Su sito esterno: https://goo.gl/xf96QK", syntax="plain")
    
if __name__ == "__main__":
    bot.run()
print(":/")
