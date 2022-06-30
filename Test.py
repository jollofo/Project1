import requests
from pyyoutube import Api

api = Api(api_key='AIzaSyBuq7auCohUzcNyt3HorYwpdJRjf_Y2rQk')
channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)
print(channel_by_id.items[0].to_dict())