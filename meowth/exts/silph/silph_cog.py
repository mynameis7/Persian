from meowth import Cog, command, bot, checks
from meowth.exts.users import MeowthUser, users_checks

import asyncio
import aiohttp
import time
from datetime import datetime
from dateparser import parse

from . import silph_info
from .objects import SilphTrainer
from .errors import *

class SilphCog(Cog):

    def __init__(self, bot):
        self.bot = bot

    def parse_info_from_silph(self, data):
        verified = True
        raid_lists = self.bot.raid_info.raid_lists
        for level in data:
            if level == 'LEVEL_6':
                new_level = 'EX'
            else:
                new_level = level[-1]
            for boss in data[level]['boss']:
                silphid = boss['id']
                if not boss['available']:
                    continue
                if not boss['verified']:
                    verified = False
                meowthid = silphid.upper().replace('-', '_')
                if meowthid == 'GIRATINA_ALTERED':
                    meowthid = 'GIRATINA'
                forms = ['ALOLA', 'ATTACK', 'DEFENSE', 'SPEED', 'RAINY', 'SNOWY', 'SUNNY', 'ORIGIN']
                for form in forms:
                    if meowthid.endswith(form):
                        meowthid += "_FORM"
                if meowthid not in raid_lists[new_level]:
                    raid_lists[new_level].append(meowthid)
        return verified

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, InvalidAPIKey):
            return await ctx.error("Invalid Silph API Key")
        elif isinstance(error, SilphCardNotFound):
            return await ctx.error("Silph Card Not Found")
        elif isinstance(error, SilphCardPrivate):
            return await ctx.error("Silph Card Private")
        elif isinstance(error, SilphCardAlreadyLinked):
            return await ctx.error("Silph Card Linked to Another Discord")

    @command()
    @users_checks.users_enabled()
    async def silph(self, ctx, silph_id: SilphTrainer):
        """Link your Silph Road account."""

        silph_card = silph_id.card
        linked_discord = silph_card.discord_name
        if not linked_discord == str(ctx.author):
            raise SilphCardAlreadyLinked
        user_table = ctx.bot.dbi.table('users')
        meowthuser = MeowthUser(ctx.bot, ctx.author)
        data = await meowthuser._data.get()
        if len(data) == 0:
            insert = meowthuser._insert
            d = {'id': ctx.author.id, 'silph': silph_id.name}
            insert.row(**d)
            await insert.commit()
        else:
            update = meowthuser._update
            update.values(silph=silph_id.name)
            await update.commit()
        return await ctx.success(f'Silph ID set to {silph_id.name}')
    
    @command()
    async def silphcard(self, ctx, silph_user: SilphTrainer = None):
        """Displays a user's Silph Road Trainer Card."""
        if not silph_user:
            user_id = ctx.author.id
            meowth_user = MeowthUser.from_id(ctx.bot, user_id)
            silph_id = await meowth_user.silph()
            if not silph_id:
                return await ctx.error(f"You haven't setup a silphcard!")
            silph_user = await SilphTrainer.load_trainer_data(silph_id)
        card = silph_user.card
        if card:
            await ctx.send(embed=card.embed())
        else:
            await ctx.error(f'Silph Card for {silph_user} not found.')

    @command()
    @checks.is_co_owner()
    async def shakeup(self, ctx, *, shaketime=None):
        i = 0
        if shaketime:
            newdt = parse(shaketime, settings={'TIMEZONE': 'America/Chicago', 'RETURN_AS_TIMEZONE_AWARE': True})
            stamp = newdt.timestamp()
            sleeptime = time.time() - stamp
        else:
            sleeptime = 0
        await asyncio.sleep(sleeptime)
        url = 'https://api.thesilphroad.com/v0/raids'
        headers = {'Authorization': f'Silph {silph_info.api_key}'}
        while True:
            async with aiohttp.ClientSession() as sess:
                async with sess.get(url, headers=headers) as resp:
                    data = await resp.json()
                    data = data['data']
                    verified = self.parse_info_from_silph(data)
                    if not verified or i < 60:
                        await asyncio.sleep(60)
                        i += 1
                        continue
                    self.bot.raid_info.raid_lists = {
                        '1': [],
                        '2': [],
                        '3': [],
                        '4': [],
                        '5': [],
                        '6': [],
                        'EX': []
                    }
                    self.parse_info_from_silph(data)
                    break
        with open(self.bot.ext_dir + '/raid/raid_info.py', 'a') as f:
            print('\nraid_lists = ' + str(self.bot.raid_info.raid_lists), file=f)
        
    @command()
    @checks.is_co_owner()
    async def replace(self, ctx):
        self.bot.raid_info.raid_lists = {
            '1': [],
            '2': [],
            '3': [],
            '4': [],
            '5': [],
            '6': [],
            'EX': []
        }
        url = 'https://api.thesilphroad.com/v0/raids'
        headers = {'Authorization': f'Silph {silph_info.api_key}'}
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url, headers=headers) as resp:
                data = await resp.json()
                data = data['data']
                self.parse_info_from_silph(data)
        with open(self.bot.ext_dir + '/raid/raid_info.py', 'a') as f:
            print('\nraid_lists = ' + str(self.bot.raid_info.raid_lists), file=f)
