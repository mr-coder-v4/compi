from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    total, used, free, disk= disk_usage('/')
    total = round(total/1024.0/1024.0/1024.0,1)
    free = round(free/1024.0/1024.0/1024.0,1)
    memory = virtual_memory()
    mem_p = round(memory.percent)
    mem_t = round(memory.total/1024.0/1024.0/1024.0,1)
    mem_a = round(memory.available/1024.0/1024.0/1024.0,1)
    mem_u = round(memory.used/1024.0/1024.0/1024.0,1)
    await event.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\n**Total Disk Space:** {total} GB\n**Free:** {free} GB\n**Memory Percent:** {mem_p}%\n**Memory Total:** {mem_t} GB\n**Memory Free:** {mem_a} GB\n**Memory Used:** {mem_u} GB\n")
    return
