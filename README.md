# randstuff.py
Web-API For [randstuff](https://randstuff.ru) website for generating random stuff

![](https://i.postimg.cc/v8hSZRFb/a-OHLI4-V0-FI.jpg)

### Example
```py3
import randstuff
randstuff = randstuff.RandStuff()
random_joke = randstuff.generate_random_joke()["joke"]["text"]
print(random_joke)
```
