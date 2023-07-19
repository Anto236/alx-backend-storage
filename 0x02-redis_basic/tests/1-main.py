#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)

    # Without fn option
    result_no_fn = cache.get(key)
    print(f"Key: {key}, Value: {value}, Result (No fn): {result_no_fn}")

    # With fn option
    result_with_fn = cache.get(key, fn=fn)
    print(f"Key: {key}, Value: {value}, Result (With fn): {result_with_fn}")

    assert result_with_fn == value
