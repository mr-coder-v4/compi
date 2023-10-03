from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    disk= psutil.disk_usage('/')
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    used = round(disk.used/1024.0/1024.0/1024.0,1)
    used_p = round(disk.percent/1024.0/1024.0/1024.0,1)
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    mem_p = memory.percent
    mem_t = round(memory.total/1024.0/1024.0/1024.0,1)
    mem_a = round(memory.available/1024.0/1024.0/1024.0,1)
    mem_f = round(memory.free/1024.0/1024.0/1024.0,1)
    mem_u = round(memory.used/1024.0/1024.0/1024.0,1)
    await event.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\nTotal Disk Space: {total} GB\nUsed Disk Space: {used}\n\nAvailable Disk Space: {free} GB\n--------------------------\nMemory Utilization: {mem_p}%\nTotal RAM: {mem_t} GB\nAvailable RAM: {mem_a} GB\nFree RAM: {mem_f} GB\nRAM Utilized: {mem_u} GB\n")
    return
