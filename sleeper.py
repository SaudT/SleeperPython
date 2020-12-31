import requests
import json
from sleeper_wrapper import League, User


blaj = League('602231677183393792')
leag = blaj.get_league()
with open("blaj.json", "w") as write_file:
    json.dump(leag, write_file, indent = 4)

all_positions = {}
total = {}

for pos in leag['roster_positions']:
    if pos in all_positions:
        all_positions[pos] += 1
    else:
        all_positions[pos] = 1



counter = 0  #to count throught the teams
#12 because we have 12 total teams
while (counter < 12):
    total[leag['last_message_attachment']['data']['rosters'][counter]['owner_id']] = (leag['last_message_attachment']['data']['league_users'][counter]['display_name'])
    counter += 1
  
print(total)
