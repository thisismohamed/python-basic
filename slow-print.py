import time

def slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()

slow("Hello, World!")
time.sleep(1)
slow("I am mohamed I start learn python at learn-python.org")
time.sleep(1)
slow("Python is awesome , and python programming tech me 💓 love...")
time.sleep(1)
slow("This my favorate print effect")
time.sleep(1)
print("Python is awesome")
