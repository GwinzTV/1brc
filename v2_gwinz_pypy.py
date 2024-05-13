'''
third attempt :)

changes:
 - swapped out the use of a dictionary for a list for the city data storage
 - using byte strings instead of unicode
'''
import time


def process_data(txt_file):
    with open(txt_file, "rb") as data:
        stats = {}
        for line in data:
            city, temp_str = line.strip().split(b";")
            temp = float(temp_str)
            if city in stats:
                city_stats = stats[city]
                city_stats[0] = min(temp, city_stats[0])
                city_stats[1] += temp
                city_stats[2] = max(temp, city_stats[2])
                city_stats[3] += 1
            else:
                stats[city] = [temp, temp, temp, 1]  # [min, sum, max, count]
    return stats


def print_data(stats):
    formatted = ", ".join(
        k.decode() + "=" + str(v[0]) + "/" + "{:.1f}".format(v[1]/v[3]) + "/" + str(v[2])
        for k, v in sorted(stats.items(), key=lambda x: x[0])
    )
    print("{" + formatted + "}")


start = time.time()
print_data(process_data("mock.txt"))
print("\ntime taken: {:.5f} seconds\n".format(time.time() - start))

'''
RESULTS:
'''
