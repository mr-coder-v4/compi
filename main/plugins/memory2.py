from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal

@Drone.on(events.NewMessage(incoming=True, pattern="/memory2"))
async def sysinfo(event):
    total, used, free, disk= disk_usage('/')
    total = hbs(total)
    free = hbs(free)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = hbs(memory.total)
    mem_a = hbs(memory.available)
    mem_u = hbs(memory.used)
    await e.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\n**Total Disk Space:** {total}\n**Free:** {free}\n**Memory Total:** {mem_t}\n**Memory Free:** {mem_a}\n**Memory Used:** {mem_u}\n")
    return