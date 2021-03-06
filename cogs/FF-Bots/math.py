from discord.ext.commands import Cog, command


#######################################################################################################################
#                                           ---  'Math' cog  ---                                                      #
#                              Cog containing commands for mathematical functions                                     #
#######################################################################################################################
class Math(Cog):
    def __init__(self, client):
        self.client = client

    # Give the value of a squared number.
    # Use with '!square X' to get X squared.
    @command()
    # lock it
    async def square(self, context, number):
        squared_value = int(number) * int(number)
        await context.channel.send(str(number) + " squared is " + str(squared_value))


def setup(client):
    client.add_cog(Math(client))
