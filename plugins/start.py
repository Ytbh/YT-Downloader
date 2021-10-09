from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Channel", url="https://t.me/xdf54")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/xdf54")]
    ])
    welcomed = f"Hi! <b>{message.from_user.first_name}</b>\n/Halo!."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
