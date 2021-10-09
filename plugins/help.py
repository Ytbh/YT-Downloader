from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Kirim link video youtube nya dan kami akan mengunduhnya!."
    await message.reply_text(helptxt)
