from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/cpu"))
async def storage(event):
    cpu = str(psutil.cpu_percent(5))
    load1, load5, load10 = psutil.getloadavg()
    cpu_usage = (load10/os.cpu_count()) * 100
    cpu_total = psutil.cpu_count()
    cpu_physical = psutil.cpu_count(physical=True)
    cpu_logical = psutil.cpu_count(logical=True)
    cpu_usable = len(psutil.Process().cpu_affinity())
    await event.reply(f"**OS: {platform.system()}**\n**Version: {platform.release()}**\n**Architecture: platform.architecture()}**\nCPU Utilization: {cpu}%\nCPU Load Past 10 Min: {cpu_usage}\nTotal CPU Cores: {cpu_total}\nUsable CPU Cores: {cpu_usable}\nCPU Logical Cores: {cpu_logical}\nCPU Physical Cores: {cpu_physical}\n")
    return
