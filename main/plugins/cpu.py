from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/cpu"))
async def storage(event):
    cpu = psutil.cpu_percent(interval=1)
    cpu_usage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    cpu_total = psutil.cpu_count()
    cpu_logical = psutil.cpu_count(logical=False)
    cpu_physical = psutil.cpu_count(logical=False)
    cpu_usable = len(psutil.Process().cpu_affinity())
    frequency = psutil.cpu_freq()
    await event.reply(f"**OS: {platform.system()}**\n**Version: {platform.release()}**\n**Architecture: {platform.architecture()}**\nCPU Utilization: {cpu}%\nCPU Load Past 1, 5, 15 Min: {cpu_usage}\nTotal CPU Cores: {cpu_total}\nUsable CPU Cores: {cpu_usable}\nLogical CPU Cores: {cpu_logical}\nPhysical CPU Cores: {cpu_physical}\n")
    return
