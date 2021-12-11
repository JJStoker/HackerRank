# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = max(0, min(int(input()), 100))
bc = max(0, min(int(input()), 100))

ac = math.sqrt(ab ** 2 + bc ** 2)

print (f'{round(math.degrees(math.acos((bc / 2) / (ac / 2))))}°')
