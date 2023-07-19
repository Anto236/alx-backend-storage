#!/usr/bin/env python3
""" Main file """

# Import the Cache class from exercise module using __import__
exercise = __import__('exercise')
Cache = exercise.Cache
replay = exercise.replay

def main():
    # Create an instance of the Cache class
    cache = Cache()

    # Make some method calls to store data
    key1 = cache.store("foo")
    key2 = cache.store("bar")
    key3 = cache.store(42)

    # Display the history of calls using the replay function
    replay(cache.store)

if __name__ == "__main__":
    main()
