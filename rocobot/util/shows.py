SHOWS_DATA_LOCATION = 'data/shows.json'

import util
from util import io

def _retrieve_shows_data():
    print('retrieve_shows_data')
    return {}

def _store_shows_data(data):
    print('store_shows_data')

async def _shows_help(ctx):
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

async def _shows_add(shows, ctx, title):
    await ctx.send(f'add {title}')

async def _shows_remove(shows, ctx, title):
    await ctx.send(f'remove {title}')

async def _shows_join(shows, ctx, title):
    await ctx.send(f'join {title}')

async def _shows_leave(shows, ctx, title):
    await ctx.send(f'leave {title}')

async def _shows_invite(shows, ctx, user, title):
    await ctx.send(f'invite {user} {title}')

async def _shows_kick(shows, ctx, user, title):
    await ctx.send(f'kick {user} {title}')

async def _shows_recommend(shows, ctx):
    await ctx.send(f'recommend')

async def _shows_list(shows, ctx):
    await ctx.send(f'list')

async def handle_command(ctx, args):
    async def invalid_syntax():
        await ctx.send('Invalid syntax')

    if len(args) < 1:
        await invalid_syntax()
        return

    subcommand = args[0]


    if subcommand == 'help':
        await _shows_help(ctx)
        return

    shows = _retrieve_shows_data()

    if subcommand == 'add':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await _shows_add(shows, ctx, title)
    elif subcommand == 'remove':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await _shows_remove(shows, ctx, title)
    elif subcommand == 'join':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await _shows_join(shows, ctx, title)
    elif subcommand == 'leave':
        if len(args) < 2:
            await invalid_syntax()
            return
        title = args[1]
        await _shows_leave(shows, ctx, title)
    elif subcommand == 'invite':
        if len(args) < 3:
            await invalid_syntax()
            return
        user = args[1]
        title = args[2]
        await _shows_invite(shows, ctx, user, title)
    elif subcommand == 'kick':
        if len(args) < 3:
            await invalid_syntax()
            return
        user = args[1]
        title = args[2]
        await _shows_kick(shows, ctx, user, title)
    elif subcommand == 'recommend':
        await _shows_recommend(shows, ctx)
    elif subcommand == 'list':
        await _shows_list(shows, ctx)
