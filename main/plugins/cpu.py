from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/cpu"))
async def storage(event):
    cpu = psutil.cpu_percent(interval=1)
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage1 = (load1/os.cpu_count()) * 100
    cpu_usage5 = (load5/os.cpu_count()) * 100
    cpu_usage15 = (load15/os.cpu_count()) * 100
    cpu_total = psutil.cpu_count()
    cpu_physical = psutil.cpu_count(logical=False)
    cpu_usable = len(psutil.Process().cpu_affinity())
    freq = psutil.cpu_freq()
    cpu_cur = freq.current
    cpu_max = freq.max
    cpu_min = freq.min
    await event.reply(f"**OS: {platform.system()}**\n**Version: {platform.release()}**\n**Architecture: {platform.architecture()}**\n-----------------------------------------------------------------\nTotal CPU Cores: {cpu_total}\nUsable CPU Cores: {cpu_usable}\nPhysical CPU Cores: {cpu_physical}\n-----------------------------------------------------------------\nCPU Frequency :-\nCurrent: {cpu_cur}\nMAX: {cpu_max}\nMIN: {cpu_min}\n-----------------------------------------------------------------\nCPU Utilization: {cpu}%\nLoad Past 1 Min: {cpu_usage1}\nLoad Past 5 Min: {cpu_usage5}\nLoad Past 15 Min: {cpu_usage15}\n")
    return