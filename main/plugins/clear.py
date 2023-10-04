from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal

@Drone.on(events.NewMessage(incoming=True, pattern="/clear"))
async def clear(event):
    try:
        zylern = "rm *.mp4"
        zylern = "rm -rf encodemedia"
        zylern = "rm *.txt"
        fetch = await asyncrunapp(
            zylern,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Install speedtest-cli**")
