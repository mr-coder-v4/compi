from .. import Drone
from telethon import events, Button
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/info"))
async def quick_info(event):
    cpu = str(psutil.cpu_percent()) + '%'
    memory = psutil.virtual_memory()
    available = round(memory.available/1024.0/1024.0/1024.0,2)
    total = round(memory.total/1024.0/1024.0/1024.0,2)
    mem_info = str(available) + 'GB' '(' + str(memory.percent) + '%)' '/' + str(total) + 'GB' 
    disk = psutil.disk_usage('/')
    free = round(disk.free/1024.0/1024.0/1024.0,2)
    total = round(disk.total/1024.0/1024.0/1024.0,2)
    disk_info = str(free) + 'GB' '(' + str(disk.percent) + '%)' '/' + str(total) + 'GB' 
    await event.reply(f"CPU: {cpu}\nDisk: {disk_info}\nMemory: {mem_info}")
    return
