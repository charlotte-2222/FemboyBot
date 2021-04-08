# import discord
# from discord import Colour, Embed
#
# ERRORICON = ""
# SUCCESSICON = ""
# WARNINGICON = ""
#
#
# class ErrorEmbed(Embed):
#     def __init__(self, message, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.colour = Colour.red()
#         # self.title = "Error!"
#         self.set_author(name="Error!", icon_url=ERRORICON)
#         self.description = message
#
#
# class SuccessEmbed(Embed):
#     def __init__(self, message, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.colour = Colour.magenta()
#         self.description = message
#         self.set_author(icon_url=SUCCESSICON,
#                         name="Success!")
#
#
# class WarningEmbed(Embed):
#     def __init__(self, message, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.colour = Colour.orange()
#         self.description = message
#         self.set_author(icon_url=WARNINGICON,
#                         name="Warning!")
