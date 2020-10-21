@client.command()
async def vcmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)


@client.command()
async def vcunmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:   
        await member.edit(mute=False)