from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    disk= psutil.disk_usage('/')
    d_t = round(disk.total/1024.0/1024.0/1024.0,1)
    d_u = round(disk.used/1024.0/1024.0/1024.0,1)
    d_p = disk.percent
    d_f = round(disk.free/1024.0/1024.0/1024.0,1)
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    mem_p = memory.percent
    mem_t = round(memory.total/1024.0/1024.0/1024.0,1)
    mem_a = round(memory.available/1024.0/1024.0/1024.0,1)
    mem_f = round(memory.free/1024.0/1024.0/1024.0,1)
    mem_u = round(memory.used/1024.0/1024.0/1024.0,1)
    await event.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\n--------------------------------------------------\nTotal Disk Space: {d_t} GB\nAvailable Disk Space: {d_f} GB\nUsed Disk Space: {d_u} GB\nUsed Disk Percentage: {d_p}%\n--------------------------------------------------\nTotal RAM: {mem_t} GB\nAvailable RAM: {mem_a} GB\nFree RAM: {mem_f} GB\nRAM Utilized: {mem_u} GB\nRAM Utilized Percentage: {mem_p}%\n")
    return