# Use decorators to factor-out separate logic
# example for caching webpages :
from functools import wraps
from urllib.request import urlopen

# This entangles the lookup with the caching logic.
# Caching should be reusable.
from subprocess import call


def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urlopen(url).read()
    saved[url] = page
    return page

local_cache = {}
google = web_lookup("http://www.google.com", local_cache)
youtube = web_lookup("http://www.youtube.com", local_cache)
google2 = web_lookup("http://www.google.com", local_cache)
print(google2 is google)
print("cache size", len(local_cache))
print(local_cache)


# Caching decorator
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

# Achieve clean separation and untanglement by use of decarators.
# Only pure functions should be cacheable.
@cache
def pure_web_lookup(url):
    return urlopen(url).read()

google = pure_web_lookup("http://www.google.com")
youtube = pure_web_lookup("http://www.youtube.com")
google2 = pure_web_lookup("http://www.google.com")
print(google2 is google)
