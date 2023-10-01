from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal

Drone.on(events.NewMessage(incoming=True, pattern="/sysinfo"))
async def sysinfo(event):
    try:
        zyl = "neofetch --stdout"
        fetch = await asyncrunapp(
            zyl,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Install neofetch first**")

