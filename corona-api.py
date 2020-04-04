#author : VM4K4R0V
import discord
from discord.ext import commands
import requests
import json

BOT = commands.Bot(command_prefix = '/')

@BOT.command()
async def corona(ctx):
    #----- GET Request from corona API
    
    req = requests.get("https://coronavirus-19-api.herokuapp.com/countries/morocco")
    json_object = req.json()

    dawla = json_object["country"]
    hadnhar = json_object["todayCases"]
    lmot = json_object["deaths"]
    k7l_ras = json_object["cases"]
    naj = json_object['recovered']
    ac = json_object['active']
    TD = json_object['todayDeaths']
    cr = json_object['critical']
    #------- EMBED

    embed = discord.Embed(
        title = 'CORONA',
        colour = discord.Colour.red(), 
        )
    
    embed.set_footer(text='dkhlo t9awdo ldyorkom brbi tatnakt.')
    embed.set_author(name='VM4K4R0V', icon_url='https://vignette.wikia.nocookie.net/the-great-fandom-wars/images/1/1f/Makarov2.jpg/revision/latest?cb=20180701165901')
    embed.add_field(name = 'Country', value=dawla, inline= False)
    embed.add_field(name = 'Cases', value=k7l_ras, inline= False)
    embed.add_field(name = 'Deaths', value=lmot, inline= False)
    embed.add_field(name = 'Today Cases', value=hadnhar, inline= False)
    embed.add_field(name = 'Critical', value=cr, inline= False)
    embed.add_field(name = 'Active', value=ac, inline= False)
    embed.add_field(name = 'Recovered', value=naj, inline= False)
    embed.add_field(name = 'Today Deaths', value=TD, inline= False)

    await ctx.send(embed=embed)

#------------------------------- STAY HOME , STAY SAFE -------------------------------#