import os
import time
from glob import glob

for job in glob("jobs/*"):
    os.system(f"bsub < {job}")
    time.sleep(5)
