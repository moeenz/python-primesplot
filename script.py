from PIL import Image
import math, primesieve, sys

try:
    times = int(sys.argv[1])
except:
    raise ValueError('You should have entered an integer as number of times')

primes_iterator = primesieve.Iterator()

screen_w, screen_h = 2000, 2000 # Specify a screen size.
img = Image.new('RGB', (screen_w, screen_h), 'black')
pixels = img.load()

last = 2
for z in range(times):
    n = primes_iterator.next_prime()
    x = screen_w/2 + math.cos(last) * screen_w/2
    y = screen_h/2 + math.sin(n) * screen_h/2
    pixels[x, y] = (128, 128, 1)
    last = n


img.show()