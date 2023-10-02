from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    total, used, free, disk= disk_usage('/')
    total = str(total / 1024.0 ** 3)
    free = str(free / (1024.0 ** 3))
    memory = virtual_memory() / (1024.0 ** 3)
    mem_p = str(memory.percent)
    mem_t = str(memory.total) / (1024.0 ** 3)
    mem_a = str(memory.available) / (1024.0 ** 3)
    mem_u = str(memory.used) / (1024.0 ** 3)
    await event.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\n**Total Disk Space:** {total}\n**Free:** {free}\n**Memory Total:** {mem_t}\n**Memory Free:** {mem_a}\n**Memory Used:** {mem_u}\n")
    return
