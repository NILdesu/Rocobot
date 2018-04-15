SHOWS_DATA_LOCATION = 'data/shows.json'

import util
from util import io

async def _show_already_added(ctx):
    await ctx.send('That show has already been added')

async def _show_not_added(ctx):
    await ctx.send('That show has not yet been added')

async def _user_not_joined(ctx):
    await ctx.send('This user has not yet joined the show')

async def _user_already_joined(ctx):
    await ctx.send('This user has already joined the show')

def _retrieve_shows_data():
    print('retrieve_shows_data')

    data = util.io.read_json(SHOWS_DATA_LOCATION)

    if (data == None):
        return {}

    return data

def _store_shows_data(data):
    util.io.write_json(SHOWS_DATA_LOCATION, data)

async def _shows_add(shows, ctx, title):
    if title in shows:
        await _show_already_added(ctx)
        return

    shows[title] = {}
    shows[title]['watchers'] = []

    await ctx.send(f'add {title}')

    _store_shows_data(shows)

async def _shows_remove(shows, ctx, title):
    if title not in shows:
        await _show_not_added(ctx)
        return

    del shows[title]

    await ctx.send(f'remove {title}')

    _store_shows_data(shows)

async def _shows_invite(shows, ctx, name, title):
    if title not in shows:
        await _show_not_added(ctx)
        return

    if name in shows[title]['watchers']:
        await _user_already_joined(ctx)
        return

    shows[title]['watchers'].append(name)

    await ctx.send(f'invite {name} {title}')
    _store_shows_data(shows)

async def _shows_join(shows, ctx, title):
    await ctx.send(f'join {title}')

    await _shows_invite(shows, ctx, f'<@{ctx.message.author.id}>', title)

async def _shows_kick(shows, ctx, name, title):
    if title not in shows:
        await _show_not_added(ctx)
        return

    if name not in shows[title]['watchers']:
        await _user_not_joined(ctx)
        return

    shows[title]['watchers'].remove(name)

    await ctx.send(f'kick {name} {title}')

    _store_shows_data(shows)

async def _shows_leave(shows, ctx, title):
    await ctx.send(f'leave {title}')
    await _shows_kick(shows, ctx, f'<@{ctx.message.author.id}>', title)

async def _shows_recommend(shows, ctx):
    await ctx.send(f'recommend')

async def _shows_list(shows, ctx):
    await ctx.send(f'list')

async def handle_command(ctx, args):
    async def invalid_syntax():
        await ctx.send('Invalid syntax')

    if len(args) < 1:
        await invalid_syntax(ctx)
        return

    subcommand = args[0]

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
