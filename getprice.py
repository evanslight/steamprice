import steamy
import requests

steamap = steamy.SteamAPI('4D0E1F0AA3D33E94FF26Cxxxxx')

# this 570 means game name. 570 stands for Dota2
steam = steamap.market('570')

offer = steam.get_item_price_history('Rockshell Scout')

print(offer)
