import numpy as np
from groupy.client import Client

TOKEN_FN = "./token.txt"

def message_birdbrains(message, token_fn=TOKEN_FN):
    with open(token_fn, 'r') as token_file:
        token = token_file.read()
    token = token.replace("\n", "")
    client = Client.from_token(token)

    bird_brains = [group.name == 'Bird Brains' for group in client.groups.list()]
    bird_brains = client.groups.list()[np.where(bird_brains)[0][0]]

    return bird_brains.post(text=message)
