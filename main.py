#!/usr/bin/env python
import subprocess
for i in range(1000):
    result = subprocess.call("adb shell input tap 910 518", shell=True)
    if result:
        print(result)
        break