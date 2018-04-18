SHOWS_DATA_LOCATION = 'data/shows.json'

import util
from util import io

async def _show_already_added(ctx, title):
    await ctx.send(f'"{title}" has already been added to the list of shows.')

async def _show_not_added(ctx, title):
    await ctx.send(f'"{title}" has not yet been added to the list of shows.')

async def _user_not_joined(ctx, name, title):
    await ctx.send(f'{name} is not watching "{title}."')

async def _user_already_joined(ctx, name, title):
    await ctx.send(f'{name} is already watching "{title}."')

def _retrieve_shows_data():
    data = util.io.read_json(SHOWS_DATA_LOCATION)

    if (data == None):
        return {}

    return data

def _store_shows_data(data):
    util.io.write_json(SHOWS_DATA_LOCATION, data)

async def _shows_add(shows, ctx, title):
    if title in shows:
        await _show_already_added(ctx, title)
        return

    shows[title] = {}
    shows[title]['watchers'] = []

    await ctx.send(f'Added "{title}" to the list of shows.')

    _store_shows_data(shows)

async def _shows_remove(shows, ctx, title):
    if title not in shows:
        await _show_not_added(ctx, title)
        return

    del shows[title]

    await ctx.send(f'Removed "{title}" from the list of shows.')

    _store_shows_data(shows)

async def _shows_invite(shows, ctx, name, title):
    if title not in shows:
        await _show_not_added(ctx, title)
        return

    if name in shows[title]['watchers']:
        await _user_already_joined(ctx, name, title)
        return

    shows[title]['watchers'].append(name)

    await ctx.send(f'{name} is now watching "{title}."')

    _store_shows_data(shows)

async def _shows_join(shows, ctx, title):
    await _shows_invite(shows, ctx, f'<@{ctx.message.author.id}>', title)

async def _shows_kick(shows, ctx, name, title):
    if title not in shows:
        await _show_not_added(ctx, title)
        return

    if name not in shows[title]['watchers']:
        await _user_not_joined(ctx, name, title)
        return

    shows[title]['watchers'].remove(name)

    await ctx.send(f'{name} is no longer watching "{title}."')

    _store_shows_data(shows)

async def _shows_leave(shows, ctx, title):
    await _shows_kick(shows, ctx, f'<@{ctx.message.author.id}>', title)

async def _shows_recommend(shows, ctx):
    cur_channel = None
    cur_voice = ctx.message.author.voice
    if (cur_voice != None):
        cur_channel = cur_voice.channel

    members = []
    if (cur_channel == None):
        members = util.get_online_members(ctx.guild.members)
    else:
        members = cur_channel.members

    if (len(members) == 0):
        await ctx.send('No members in voice chat or online.')
        await _shows_list(shows, ctx)
        return

    points = {}
    cur_title = ''
    max_points = 0
    for title in shows:
        points[title] = 0
        for member in members:
            if f'<@{member.id}>' in shows[title]['watchers']:
                points[title] += 1
        if (points[title] > max_points):
            cur_title = title
            max_points = points[title]

    await ctx.send(f'You should watch: {cur_title}')

async def _shows_list(shows, ctx):
    if (len(shows) == 0):
        await ctx.send("No shows have been added yet. Add some shows!")
        return

    message_parts = []
    i = 0
    for title in shows:
        i += 1
        message_parts.append(f'{i}. "{title}"')

    await ctx.send('\n'.join(message_parts))

async def handle_command(ctx, args):
    async def invalid_syntax():
        await ctx.send('Invalid syntax')

    if len(args) < 1:
        await invalid_syntax()
        return

    subcommand = args[0]

    shows = _retrieve_shows_data()

    if subcommand == 'add' and len(args) == 2:
        title = args[1]
        await _shows_add(shows, ctx, title)
        return
    elif subcommand == 'remove' and len(args) == 2:
        title = args[1]
        await _shows_remove(shows, ctx, title)
        return
    elif subcommand == 'join' and len(args) == 2:
        title = args[1]
        await _shows_join(shows, ctx, title)
        return
    elif subcommand == 'leave' and len(args) == 2:
        title = args[1]
        await _shows_leave(shows, ctx, title)
        return
    elif subcommand == 'invite' and len(args) == 3:
        user = args[1]
        title = args[2]
        await _shows_invite(shows, ctx, user, title)
        return
    elif subcommand == 'kick' and len(args) == 3:
        user = args[1]
        title = args[2]
        await _shows_kick(shows, ctx, user, title)
        return
    elif subcommand == 'recommend' and len(args) == 1:
        await _shows_recommend(shows, ctx)
        return
    elif subcommand == 'list' and len(args) == 1:
        await _shows_list(shows, ctx)
        return
    else:
        await invalid_syntax()
