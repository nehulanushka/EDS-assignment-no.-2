pratical=1
Qno.1.1.1
mass=float(input())
velocity=float(input())
momentum=mass*velocity
print(f"{momentum:.2f}kgm/s")

Qno.1.1.2
import math
n=int(input())
if 0<n<10:
	print(n**2)
elif 10<=n<100:
	print(f"{math.sqrt(n):.2f}")
elif 100<=n<1000:
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")

Qno.1.1.3
from datetime import date 
from datetime import datetime

date1 = input().strip()
date2 = input().strip()

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")
difference = (d2 - d1).days
print(difference)

Qno.1.1.4
num=int(input())
text=str(num)
reversed_num=text[::-1]
print(reversed_num)

Qno.1.1.5
n=int(input())
for i in range(1,11):
	print(f"{n} x {i} = {n*i}")
