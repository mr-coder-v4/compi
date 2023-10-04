from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/info"))
async def quick_info(event):
    cpu = str(psutil.cpu_percent()) + '%
    memory = psutil.virtual_memory()
    available = round(memory.available/1024.0/1024.0,2)
    total = round(memory.total/1024.0/1024.0,2)
    mem_info = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'
    disk = psutil.disk_usage('/')
    free = round(disk.free/1024.0/1024.0/1024.0,2)
    total = round(disk.total/1024.0/1024.0/1024.0,2)
    disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
    await event.reply(f"CPU Info: {cpu}/nMemory Info: {mem_info}\nDisk Info: {disk_info}")
    return
