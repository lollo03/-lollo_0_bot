import Bot

import botogram



def process(bot, chains, update):
    message = update.callback_query.message
    chat = message.chat
    query = update.callback_query.data
    callback_id = update.callback_query.id
    sender = update.callback_query.sender

    if query == "guide":
        chat.send("Ecco qualcosa di utile: \n-Guide sul mondo linux: /guidelinux \n-Guida su come fare un bot in python! (by lollo) /botpy \n -/guidaphp la magnifica guida sul php di @ImAndrehh. \n Guide sui bitcoin /guidebtc \n Guide sui server & co /guideserver")
    if query == "credits":
        chat.send("Creatore: @lollo_0 \n Per i limitati: @lollo_0limitati_bot \n Canale: https://telegram.me/stickermaster", syntax="plain")
    if query == "1":
        chat.send("Ecco i collaboratori: \n 1) @ImAndrehh il primo1 \n 2) @pietroos\n Diventa anche tu un collaboratore! Fai /divcollaboratore")
    if query == "2":
        chat.send("In costruzione")
