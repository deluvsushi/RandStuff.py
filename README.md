# RandStuff.py
API For https://randstuff.ru

![RandStuffAPI](https://i.postimg.cc/v8hSZRFb/a-OHLI4-V0-FI.jpg)

### Example
```py3
# Generate Random Joke
import randstuff
client = randstuff.Client()
joke = client.generate_random_joke()["joke"]["text"]
print(f"Joke >> {joke}")
