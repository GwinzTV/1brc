'''
first attempt :)
'''
import time

def process_data(txt_file: str):
    with open(txt_file, "r") as data:
        stats: dict[str, dict[str, float]] = {}
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
        f"{k}={v['min']}/{v['sum']/v['count']:.1f}/{v['max']}"
        for k, v in sorted(stats.items(), key=lambda x: x[0])
    )
    print("{" + formatted + "}")


start = time.time()
print_data(process_data("mock.txt"))
print(f"\ntime taken: {time.time()-start:.5f} seconds\n")