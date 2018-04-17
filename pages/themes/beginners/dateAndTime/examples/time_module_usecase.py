import time
import datetime
from functools import reduce

start = time.time()
# do some time intensive stuff:
sum = reduce(lambda x,y:x+y, range(1,1_000_001))
print("The sum of numbers from 1 to 1_000_000 is: ", sum)
end = time.time()

print("[Finished in {:.6f}s]".format(end - start))


print(time.strftime("%H:%M:%S"))