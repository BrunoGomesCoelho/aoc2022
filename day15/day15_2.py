from sys import stdin

def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

#  x = 10
x = 2_000_000
extra_beacons = set()


sensors = [] # (A, B, raio)
for line in stdin:
    sensor_text, beacon_text = line.split(":")

    s_y = int(sensor_text[sensor_text.find("=")+1:sensor_text.find(",")])
    s_x = int(sensor_text[sensor_text.find("y")+2:])

    b_y = int(beacon_text[beacon_text.find("=")+1:beacon_text.find(",")])
    b_x = int(beacon_text[beacon_text.find("y")+2:])

    if b_x == x:
        extra_beacons.add((b_x, b_y))

    radius = manhattan_dist((s_x, s_y), (b_x, b_y))
    sensors.append((s_x, s_y, radius))


def is_not_beacon(sensor, point):
    s_x, s_y, radius = sensor
    dist = manhattan_dist((s_x, s_y), point)

    # < ?
    return dist <= radius


#  print(extra_beacons)
#  for y in range(-100, 100):
print(sensors, extra_beacons)
total = 0


for x in range(0, 4_000_000):
    for y in range(0, 4_000_000):
        for sensor in sensors:
            if is_not_beacon(sensor, (x, y)):
                total += 1
                break

print(total - len(extra_beacons))


print(3*3585462)
