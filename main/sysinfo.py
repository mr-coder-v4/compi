


async def sysinfo(event):
    try:
        zyl = "neofetch --stdout"
        fetch = await asyncrunapp(
            zyl,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Install neofetch first**")

