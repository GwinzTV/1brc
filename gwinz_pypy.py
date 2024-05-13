'''
second attempt :)

changes:
using "pypy" interpreter instead of "cpython"
'''
import time

def process_data(txt_file):
    with open(txt_file, "r") as data:
        stats = {}
        for line in data:
            city, temp_str = line.strip().split(";")
            temp = float(temp_str)
            if city in stats:
                city_stats = stats[city]
                city_stats["min"] = min(temp, city_stats["min"])
                city_stats["sum"] += temp
                city_stats["max"] = max(temp, city_stats["max"])
                city_stats["count"] += 1
            else:
                stats[city] = {"min":temp, "sum":temp, "max":temp, "count":1}
    return stats

def print_data(stats):
    formatted = ", ".join(
        k + "=" + str(v['min']) + "/" + "{:.1f}".format(v['sum']/v['count']) + "/" + str(v['max'])
        for k, v in sorted(stats.items(), key=lambda x: x[0])
    )
    print("{" + formatted + "}")


start = time.time()
print_data(process_data("mock.txt"))
print("\ntime taken: {:.5f} seconds\n".format(time.time() - start))





'''
RESULTS: 

The first major issue, I run into is that the official input txt file is 10GB
and my MacBook only has 8GB of RAM, so I won't be able to load the entire file into
memory while I am processing the data.

I will have to utilise some memory management techniques to overcome this...
'''