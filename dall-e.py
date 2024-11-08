from openai import OpenAI
from requests import get

from pathlib import Path

OPEN_AI_API_TOKEN = (Path.home() / ".ssh/openai").read_text().strip()

client = OpenAI(api_key=OPEN_AI_API_TOKEN)

query = "A dog on the moon with a taco"


response = client.images.generate(
    model="dall-e-3",
    prompt=query,
    n=1,  # number of images to return
    size="1024x1024",  # larger resolutions,
)

print(response)
print("")
print(response.created)
print("")
print(response.data[0].revised_prompt)
print("")
print(response.data[0].url)

# revised_prompt='An illustrated interpretation of an adventurous scene:
# Imagine a dog, possibly a mixed breed with curly fur and a distinctive
# wagging tail, engaged in a unique excursion. It finds itself on the moon,
# an isolated yet enchanting setting, where every step raises a small
# cloud of dust. In the luminous reflection of the earth seen in the distance,
# the silhouette of the dog can be seen. Surprisingly, our furry
# explorer holds a taco, perhaps a treat from its Earth-bound home,
# nestled gently in its mouth. The simplistic beauty of this surreal
# scene truly blurs the boundaries between ordinary and extraordinary.'


pic_name = f"{query.replace(' ', '_')}_{response.created}.png"  # use timestamp for name

pic = get(response.data[0].url)

with open(pic_name, "wb") as image:
    image.write(pic.content)
