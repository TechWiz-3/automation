# Not my own, copied from a stackoverflow reply, used as a test out of curiosity

import subprocess
import re

# Get process info
ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0].decode()
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode()

# Iterate processes
processLines = ps.split('\n')
sep = re.compile('[\s]+')  # type: ignore
rssTotal = 0 # kB
for row in range(1,len(processLines)):
    rowText = processLines[row].strip()
    rowElements = sep.split(rowText)
    try:
        rss = float(rowElements[0]) * 1024
    except:
        rss = 0 # ignore...
    rssTotal += rss

# Process vm_stat
vmLines = vm.split('\n')
sep = re.compile(':[\s]+')  # type: ignore
vmStats = {}
for row in range(1,len(vmLines)-2):
    rowText = vmLines[row].strip()
    rowElements = sep.split(rowText)
    vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096  # type: ignore

print('Wired Memory:\t\t%d MB' % (vmStats["Pages wired down"]/1024/1024))
print('Active Memory:\t\t%d MB' % (vmStats["Pages active"]/1024/1024))
print('Inactive Memory:\t%d MB' % (vmStats["Pages inactive"]/1024/1024))
print('Free Memory:\t\t%d MB' % (vmStats["Pages free"]/1024/1024))
print('Real Mem Total (ps):\t%.3f MB' % (rssTotal/1024/1024))