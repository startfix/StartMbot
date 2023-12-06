import os

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from KyyRobot import telethn as tbot
from KyyRobot import ubot2
from KyyRobot.events import register

@register(pattern="^/tiktok ?(.*)")
async def tiktod(event):
    Kyy = event.pattern_match.group(1)
    if Kyy:
        d_link = Kyy
    elif event.is_reply:
        d_link = await event.get_reply_message()
    else:
        return await event.reply("`Usage /tiktok <link>`")
    xx = await event.reply("`Video Sedang Diproses...`")
    chat = "@thisvidbot"
    async with ubot2.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await ubot2(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await ubot2.send_read_acknowledge(conv.chat_id)
            Kyy = await ubot2.download_media(video.media)
        await tbot.send_file(event.chat_id, Kyy)
        await ubot2.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id, text.id]
        )
        await xx.delete()
        
__mode_name__ = "TikTok"
