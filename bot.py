#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by: https://github.com/kubab6

import discord
from discord.ext import commands
from config import token
from transliterate import translit

bot = commands.Bot(command_prefix='$')

HELP = """
Translit Discord Bot
syntax: $command text
output: transliterated text
commands: translit/tl/t = russian
 tar = armenian; tgr = greek; tbg = bulgarian; tsr = serbian; tuk = ukrainian
"""

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.remove_command('help')
@bot.command(name='help', help='Bot help')
async def an(ctx, *args):
    await ctx.send(HELP)

# Translit commands
@bot.command(name='translit', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "ru")
    await ctx.send(str)
@bot.command(name='t', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "ru")
    await ctx.send(str)
@bot.command(name='tl', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "ru")
    await ctx.send(str)

@bot.command(name='tar', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "hy")
    await ctx.send(str)

@bot.command(name='tgr', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "el")
    await ctx.send(str)
@bot.command(name='tbg', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "bg")
    await ctx.send(str)
@bot.command(name='tsr', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "sr")
    await ctx.send(str)
@bot.command(name='tuk', help='Translit.')
async def an(ctx, *, args):
    str = translit(args, "uk")
    await ctx.send(str)


if __name__ == '__main__':
    bot.run(token)