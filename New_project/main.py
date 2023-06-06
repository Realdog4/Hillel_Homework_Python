from collections import OrderedDict
import functools
import requests
import memory_profiler


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key][1] += 1
                deco._cache.move_to_end(cache_key, last=True)
                return deco._cache[cache_key][0]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                min_key = min(deco._cache, key=lambda x: deco._cache[x][1])
                deco._cache.pop(min_key)
            deco._cache[cache_key] = [result, 1]
            return result
        deco._cache = OrderedDict()
        return deco
    return internal


def memory_usage(func):
    def wrapper(*args, **kwargs):
        memory_1 = memory_profiler.memory_usage()[0]
        result = func(*args, **kwargs)
        memory_2 = memory_profiler.memory_usage()[0]
        mem_diff = memory_2 - memory_1
        print(f"Memory usage: {mem_diff / 1024} KB")
        return result
    return wrapper


@memory_usage
@cache(max_limit=100)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content
