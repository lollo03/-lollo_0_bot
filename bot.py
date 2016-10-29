import botogram
bot = botogram.create("EHVOLEVI")
 
@bot.command("start")
def start_command(chat, message, args):
    chat.send("ATTENZIONE, BOT IN IPER-BETA, PU0' ESSERE INSTABILE E FASTIDIOSO... VI HO AVVERTITO! Fai /help per vedere cosa fa questo artificio")
 
@bot.command("help")
def help_command(chat, message, args):
    chat.send("Lista comandi che questo artificio può fare: \n /start = fai partire il bot \n /credits = crediti \n /guide = le utili (o non) guide di lollo&co!\n /collaboratori = lista collaboratori ")
 
@bot.command("guide")
def guide_command(chat, message, args):
    chat.send("Ecco qualcosa di utile: \n-Guide sul mondo linux: /guidelinux \n-Guida su come fare un bot in python! (by lollo) /botpy\n-Guida sul PHP fatta da @ImAndrehh /guidaphp\n-Guida su SQLite fatta da @ImAndrehh /guidasqlite")
    chat.send("Per diventare un collaboratore fai questo comando: /divcollaboratore")
 
@bot.command("guidelinux")
def guidelinux_command(chat, message, args):
    chat.send("Ecco tutte le guide riguardati il mondo linux:\n Come installare qualsiasi cosa su VPS ubuntu /installah")
 
@bot.command("credits")
def credits_command(chat, message, args):
    chat.send("Creatore: @lollo_0 \n Per i limitati: @lollo_0limitati_bot \n Canale: https://telegram.me/stickermaster", syntax="plain")
   
@bot.command("installah")
def installah_command(chat, message, args):
    chat.send("1: apt-get update\n 2: apt-get upgrade \n 3: reboot \n 4: apt-get install (pacchetto desiderato)")
 
@bot.command("divcollaboratore")
def divcollaboratore_command(chat, message, args):
    chat.send("Per diventare collaboratore basta entrare in questo gruppo: https://telegram.me/lollo_0_bot_collaboratori", syntax="plain")
    print("comando /divcollaboratore eseguito!")
 
@bot.command("botpy")
def botpy_command(chat, message, args):
    chat.send("Sezione in costruzione, disponibile prossiamente")
 
@bot.command("guidaphp")
def guidaphp_command(chat, message, args):
    chat.send("Hypertext Pre Processor\nPHP nasce nel 1994 la cui funzione era quella di facilitare ai programmatori l'amministrazione delle home page personali: da qui\n trae origine il suo nome, che allora significava appunto Personal Home Page.\n Oggi, con il grande sviluppo della tecnologia PHP può girare su ogni Web Server, da Apache, Nginx ecc..\n Adesso, dalla semplice home page dinamica fino ai grande portale o al sito di e-commerce.\n PHP e HTML\n Il codice php infatti deve essere compreso fra appositi tag di apertura e di chiusura, che sono i seguenti:\n <?php //tag di apertura codice\n?> //tag di chiusura codice\n Tutto ciò che è contenuto fra questi tag deve corrispondere alle regole sintattiche del PHP, ed è codice che sarà eseguito\n dall'interprete e non sarà inviato al browser. Per generare il codice da inviare al browser abbiamo due costrutti del linguaggio,\n che possiamo considerare equivalenti, che sono: print() e echo().\n che possiamo considerare equivalenti, che sono: print() e echo().\n Vediamo  un primo esempio:/ n<HTML>\n <HEAD>\n <TITLE>PaginaTest</TITLE>\n </HEAD>\n </HEAD>\n <BODY>\n <?php\n print('LolloDomina!<br> \n');\n echo('Guida di @ImAndrehh');\n?>\n</BODY>\nQuesto semplice codice produrrà un file HTML il cui contenuto sarà semplicemente:\n <HTML>/ n<HEAD>\n <TITLE>Titolo TEST</TITLE>\n</HEAD>\n<BODY>\nLBot PHP!<br>\nIl BOT Telegram è crato in PHP\n</BODY>\nE quindi l'utente vedrà sul suo browser le due righe 'LBot PHP!' ed 'Il BOT Telegram è crato in PHP'.\nPoco fa abbiamo visto che i comandi print() ed echo() hanno un funzionamento identico. In realtà ci sono alcune\ncose da puntualizzare: intanto, nessuno dei due richiede obbligatoriamente le parentesi intorno alla stringa di output. Avremmo\nquindi potuto scrivere\nprint 'LBot, ex...!<br>\n';\n2\necho 'E' una bellissima giornata';\ne sarebbe stato ugualmente corretto. Inoltre al comando echo possono essere date in input più stringhe, separate da virgole,\ncosì:\necho '1 TITOLO", "<br>\n", "2 TITOLO';\nIl risultato sarebbe stato lo stesso dell'esempio precedente; in questo caso, però, non devono essere usate le parentesi.\nDunque abbiamo visto che print() ed echo() sono le istruzioni che 'creano' il codice della nostra pagina. Nel prosieguo del corso\nuseremo spesso il verbo 'stampare' riferito alle azioni prodotte da questi due comandi: ricordiamoci però che si tratta di una\nconvenzione, perché in questo caso la 'stampa' non avviene su carta, ma sul browser!\nFacciamo caso ad un dettaglio: nelle istruzioni in cui stampavamo '1 TITOLO', abbiamo inserito, dopo il "'br>", il\nsimbolo "\n". Questo simbolo ha una funzione abbastanza importante, anche se non fondamentale, che serve più che altro per\ndare leggibilità al codice html che stiamo producendo. Infatti PHP, quando trova questa combinazione di caratteri fra virgolette, li\ntrasforma in un carattere di ritorno a capo: questo ci permette di controllare l'"impaginazione del nostro codice html. Bisogna\nperò stare molto attenti a non confondere il codice html con il layout della pagina che l'utente visualizzerà sul browser: infatti, sul\nbrowser è solo il tag <br> che forza il testo ad andare a capo. Quando questo tag non c'è, il browser allinea tutto il testo\nproseguendo sulla stessa linea (almeno fino a quando gli altri elementi della pagina e le dimensioni della finestra non gli\n'consigliano' di fare diversamente), anche se il codice html ha un ritorno a capo. Vediamo di chiarire questo concetto con un\npaio di esempi:\n<?php\nprint('prima riga\n');\nprint('seconda riga<br>');\nprint('terza riga');\n?>\nQuesto codice php produrrà il seguente codice html:\nprima riga\nseconda riga<br>terza riga\nmentre l'utente, sul browser, leggerà:\nprima rigasecondariga\nterzariga\nQuesto perché il codice php, mettendo il codice 'newline' dopo il testo 'prima riga', fa sì che il codicehtml venga formato con un\nritorno a capo dopo tale testo. Il file ricevuto dal browser quindi andrà a capo proprio lì. Il browser, però, non trovando un tag\nche gli indichi di andare a capo, affiancherà la frase 'prima riga' alla frase 'seconda riga', limitandosi a mettere uno spazio fra le\ndue. Successivamente accade l'esatto contrario: PHP produce un codice html nel quale il testo 'seconda riga' è seguito dal tag\n<br>, ma non dal codice 'newline'. Per questo, nel file html, 'seconda riga<br>' e 'terza riga' vengono attaccati. Il browser, però,\nquando trova il tag <br> porta il testo a capo.\n")
    chat.send("Avrete forse notato che in fondo ad ogni istruzione php abbiamo messo un punto e virgola; infatti la sintassi del PHP prevede\nche il punto e virgola debba obbligatoriamente chiudere ogni istruzione. Ricordiamoci quindi di metterlo sempre, con qualche\neccezione che vedremo più avanti.\nDa quanto abbiamo detto finora emerge una realtà molto importante: chi vuole avvicinarsi al PHP deve già avere una\nconoscenza approfondita di HTML e di tutto quanto può far parte di una pagina web (JavaScript, CSS eccetera).\n")
 
@bot.command("guidasqlite")
def guidasqlite_command(chat, message, args):
    chat.send("Guida in elaborazione, online tra pochi minuti")
 
@bot.command("collaboratori")
def collaboratori_command(chat, message, args):
    chat.send("Collaboratori:\n@ImAndrehh - Creatore delle guide su php ed sqlite")
 
 
if __name__ == "__main__":
    bot.run()
