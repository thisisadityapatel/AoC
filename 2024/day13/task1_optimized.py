import re
import time

start_time = time.time()


total = 0
tolerance = 0.0001
for machine in open("data.txt").read().split("\n\n"):
    ax, ay, bx, by, x, y = map(int, re.findall(r"(\d+)", machine))
    A = (bx * y - by * x) / (bx * ay - by * ax)
    B = (x - ax * A) / bx
    if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
        total += 3 * A + B

print(int(total))
end_time = time.time()
print(f"execution time: {(end_time - start_time):.6f} seconds")
