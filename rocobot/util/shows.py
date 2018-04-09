async def help(ctx):
    message = '```'
    message += 'add title\n'
    message += 'remove title\n'
    message += 'join title\n'
    message += 'leave title\n'
    message += 'invite user title\n'
    message += 'kick user title\n'
    message += 'recommend\n'
    message += 'list'
    message += '```'
    await ctx.send(message)

async def add(ctx, title):
    await ctx.send(f'add {title}')

async def remove(ctx, title):
    await ctx.send(f'remove {title}')

async def join(ctx, title):
    await ctx.send(f'join {title}')

async def leave(ctx, title):
    await ctx.send(f'leave {title}')

async def invite(ctx, user, title):
    await ctx.send(f'invite {user} {title}')

async def kick(ctx, user, title):
    await ctx.send(f'kick {user} {title}')

async def recommend(ctx):
    await ctx.send(f'recommend')

async def list(ctx):
    await ctx.send(f'list')

async def handle_command(ctx, args):
    async def invalid_syntax():
        await ctx.send('Invalid syntax')

    if len(args) < 1:
        await invalid_syntax()
        return

    subcommand = args[0]

    if subcommand == 'help':
        await help(ctx)
    elif subcommand == 'add':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await add(ctx, title)
    elif subcommand == 'remove':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await remove(ctx, title)
    elif subcommand == 'join':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await join(ctx, title)
    elif subcommand == 'leave':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await leave(ctx, title)
    elif subcommand == 'invite':
        if len(args) < 3:
            await invalid_syntax()
            return
        user = args[1]
        title = args[2]
        await invite(ctx, user, title)
    elif subcommand == 'kick':
        if len(args) < 3:
            await invalid_syntax()
            return
        user = args[1]
        title = args[2]
        await kick(ctx, user, title)
    elif subcommand == 'recommend':
        await recommend(ctx)
    elif subcommand == 'list':
        await list(ctx)
