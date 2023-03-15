import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents(messages=True, guilds=True)
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)
BOT_INTRO = "Want to connect with other members of the Dat0s community? React here!"
ROLE = "Connecting!"


@bot.command(name='dat0s-connect', help="Initializes Dat0s Connect")
async def dat0s_connect(ctx):
    """
    INPUTS: 
        - ctx: Discord Context Object

    When a user calls /dat0s-connect this function will be called, send an
    intro message in that channel, and react to its own message.
    """
    # TODO: CHECK PERMS TO SEE IF THIS USER CAN EVOKE THIS COMMAND
    sent_message = await ctx.send(BOT_INTRO)
    await sent_message.add_reaction("👥")
    await create_role(ctx)


@bot.event
async def on_reaction_add(reaction, user):
    """
    INPUTS:
        - reaction: Discord Reaction Object
        - user: Discord Member Object

    Object is called when user reacts to any message. If a non-bot user is
    reacting to the Dat0s bot intro message, this bot will add them to the 
    connect role.
    """
    if user.bot:
        print("User is bot")
        return

    if reaction.message.content != BOT_INTRO:
        print("User is not reacting to relevant message")
        return

    if str(reaction.message.author) != "carlos-test-app#2067":
        print("reaction message:", reaction.message.author)
        return

    else:
        # TODO: ADD ROLE TO USER
        print("User", user, "has reacted to your intro message with", reaction, "!")
        await add_role(user)


@bot.event
async def on_reaction_remove(reaction, user):
    """
    INPUTS:
        - reaction: Discord Reaction Object
        - user: Discord Member Object

    Object is called when user deleted reaction to any message. If a non-bot
    user is deleting a reaction to the Dat0s bot intro message, this bot 
    will remove them from the connect role.
    """
    if user.bot:
        print("User is bot")
        return

    if reaction.message.content != BOT_INTRO:
        print("User is not reacting to relevant message")
        return

    if str(reaction.message.author) != "carlos-test-app#2067":
        print("reaction message:", reaction.message.author)
        return

    else:
        print("User", user,
              "has removed their reaction", (reaction), "to your intro message!")
        await remove_role(user)


async def create_role(ctx):
    """
    INPUT:
        - ctx: Discord Context Object
    
    Takes in Discord Context Object when /dat0s-connect is first called, and 
    creates the connecting role if it does not already exists. Otherwise 
    does nothing.
    """
    role = discord.utils.get(ctx.guild.roles, name=ROLE)
    if role is None:
        print('Role', ROLE, "does not exist")
        try:
            print("Creating role")
            await ctx.guild.create_role(name=ROLE)
            print("Created role")
        except Exception as e:
            print("Failed:", e)
    else:
        print("Role", ROLE, "already exists!")


async def add_role(user):
    """
    INPUTS:
        - user: Discord Member Object
    
    Adds the global role ROLE to user who reacted to Dat0s bot intro message.
    """
    role = discord.utils.get(user.guild.roles, name=ROLE)
    await user.add_roles(role)
    print("Added role", ROLE, "to member", user)


async def remove_role(user):
    """
    INPUTS:
        - user: Discord Member Object
    
    Removes the global role ROLE from user who deleted reaction to Dat0s bot intro message.
    """
    role = discord.utils.get(user.guild.roles, name=ROLE)
    await user.remove_roles(role)
    print("Removed role", ROLE, "from member", user)


print("Bot is ready!")
bot.run(TOKEN)
