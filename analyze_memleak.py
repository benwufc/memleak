import matplotlib.pyplot as plt
import re
import timeit

#calculate running time
start = timeit.default_timer()
#========== Adjustable parameters ============
log_file_name = 'meminfo_log.txt'
analyze_args = [ 'MemFree', 'MemAvailable', 'Buffers', 'Cached', 'Slab', 'SUnreclaim', 'VmallocUsed', 'AnonPages']
figure_name = 'test_memleak.jpg'
#======== processing data ==========
#read data
file = open(log_file_name,'r') 
content=file.readlines() 

#pick up info from log and create a dictionary
items = analyze_args
items_dic = {}
for row in content:
    try:
        match = re.search(r"\[(?P<times>.+)\] (?P<item>.+)\:\s+(?P<size>\d+) kB", row)
        item_name = match.group('item')
        item_size = int(match.group('size'))
        if match.group('item') in items:
            items_dic.setdefault(item_name, []).append(item_size)
    except: 
        pass

#======== draw figure ==============
for key, value in items_dic.items():
    plt.plot(value, label=key)
plt.grid()
plt.legend(loc='best', fontsize=12)
plt.title('Memory Variable')
plt.ylabel('Memory Items (kB)')
plt.savefig(figure_name)
plt.show()
stop = timeit.default_timer()
print "run ", stop - start, " seconds"

