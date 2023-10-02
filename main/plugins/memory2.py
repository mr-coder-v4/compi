

async def sysinfo(e):
    if str(e.sender_id) not in OWNER and event.sender_id !=DEV:
        return
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
